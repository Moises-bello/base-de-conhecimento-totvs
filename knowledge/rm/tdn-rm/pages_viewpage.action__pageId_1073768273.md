---
content_hash: 5a89a32d440e7973e50dfd5287226bdb03fdc1cc3f8ba31288c3e1de6e5ce1a7
fetched_at: '2026-06-29T00:05:54.044116+00:00'
page_id: '1073768273'
product: rm
source: tdn-rm
title: Como aumentar a segurança de sua aplicação - Moderno
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1073768273
version: 8
---

## **Índice**

---

Índice

## **Introdução à Nova Arquitetura**

---

Este produto foi desenvolvido utilizando tecnologias modernas (ASP.NET Core), que operam sob o conceito de alta performance e processamento assíncrono.   
Diferente das aplicações legadas, os serviços modernos separam as responsabilidades de **processamento de negócio** e **segurança de borda**.   
Este documento estabelece as diretrizes de configuração exigidas para garantir que a aplicação opere de forma segura, seja em redes internas (Intranet) ou exposta à Internet.

## **Topologia Obrigatória: Proxy Reverso e Kestrel**

---

A aplicação utiliza um servidor web embutido de altíssima performance (Kestrel).   
No entanto, para ambientes produtivos, **não é recomendada a exposição direta do Kestrel à internet pública**.

* **Acesso Interno (Intranet):** Pode operar diretamente em IPs locais.
* **Acesso Externo (Internet/DMZ):** É **obrigatória** a utilização de um *Reverse Proxy* (Proxy Reverso) ou *API Gateway* (ex: IIS, Nginx, Apache, F5) à frente da aplicação.   
  O proxy reverso será o responsável por absorver o tráfego externo, realizar o balanceamento de carga e filtrar conexões maliciosas antes que atinjam o servidor da aplicação.

## **Criptografia e Segurança de Transporte (TLS/SSL e HSTS)**

---

* **Terminação SSL/TLS:** A instalação dos certificados digitais HTTPS deve ser feita no **Proxy Reverso** (borda da rede).   
  O tráfego da internet até o proxy deve ser rigorosamente criptografado (TLS 1.2 ou superior).   
  A comunicação entre o proxy e o servidor da aplicação na rede interna pode ocorrer via HTTP puro para maximizar a performance (conhecido como *SSL Offloading*).
* **HSTS (HTTP Strict Transport Security):** Recomendamos ativar o cabeçalho HSTS no Proxy Reverso para forçar os navegadores/clientes a se comunicarem apenas via HTTPS, prevenindo ataques de *Downgrade*.

## **Ocultação de Tecnologias e Cabeçalhos (Headers)**

---

Para evitar que atacantes identifiquem a tecnologia do servidor e explorem vulnerabilidades específicas, os seguintes cabeçalhos de resposta devem ser removidos na configuração do proxy reverso (ou via `web.config` caso utilize IIS como proxy):

| **Header a ser removido** | **Motivo da Remoção** |
| --- | --- |
| `Server` | Oculta a identificação do Kestrel, IIS ou Nginx. |
| `X-Powered-By` | Oculta a tecnologia base utilizada (ex: ASP.NET). |
| `X-AspNet-Version` | Remove a versão exata do framework .NET utilizado. |

## **Headers de Segurança Ofensiva**

---

Assim como no portal legado, a aplicação deve responder com cabeçalhos que instruam os navegadores e clientes a se protegerem contra ataques comuns. Certifique-se de injetar os seguintes headers via Proxy de Borda:

* **X-Content-Type-Options: nosniff** (Evita que o navegador tente inferir o tipo de arquivo, mitigando ataques MIME).
* **X-Frame-Options:  DENY  ou  SAMEORIGIN** (Impede que a API/Interface seja embutida em iframes de sites maliciosos - *Clickjacking*).
* **X-XSS-Protection: 1; mode=block** (Ativa os filtros nativos dos navegadores contra *Cross-Site Scripting*).

## **Proteção de Dados (Paginação Máxima e CORS)**

---

* **Paginação Limitada:** Nossas APIs possuem mecanismos de proteção nativa contra extração massiva de dados (*Scraping/Vazamento*).   
  Por padrão, consultas sem paginação retornam 20 registros.   
  Existe um **teto máximo rígido** imposto pela aplicação (que pode ser variável por endpoint); mesmo que um cliente solicite milhares de registros em uma única requisição, a aplicação processará apenas o limite seguro estabelecido.
* **CORS (Cross-Origin Resource Sharing):** Não é permitido o uso de curingas (`*`) para CORS em ambientes produtivos.   
  Os domínios (front-ends) que consumirão as APIs devem ser explicitamente listados na configuração de segurança (Whitelist).

## **Prevenção de Abuso (Rate Limiting)**

---

Para ambientes expostos, é **mandatório** configurar limites de requisição (Rate Limit) por IP ou por sessão no **Proxy Reverso/WAF corporativo**.   
Isso garante a proteção da aplicação contra ataques de Negação de Serviço (**DDoS**) e ataques de força bruta, preservando o consumo de CPU e Memória.

## **Tratamento de Erros em Produção**

---

* **Variável de Ambiente:** Certifique-se de que a variável de ambiente do sistema operacional `ASPNETCORE_ENVIRONMENT` esteja definida estritamente como `Production`.
* Isso garante que a aplicação não exiba páginas de erro detalhadas (Stack Trace) para o cliente final, retornando apenas códigos HTTP padronizados (ex: 500 Internal Server Error) e logando os detalhes reais em arquivos locais ou no visualizador de eventos do sistema para auditoria.

## **Anexo: Exemplos de Configuração de Proxy Reverso**

---

TERMO DE RESPONSABILIDADE E MANUTENÇÃO CONTÍNUA

Os blocos de configuração, regras de firewall e topologias apresentados neste documento servem exclusivamente como **exemplos iniciais (baselines)** para auxiliar no direcionamento da implantação da nossa solução.

O cenário de ameaças digitais e as tecnologias de proteção (Proxies, WAFs, Gateways) evoluem constantemente. Por isso, a adaptação destas regras à realidade do ambiente, o ajuste fino de performance, bem como a **conferência, atualização e auditoria recorrente das melhores práticas de segurança de borda**, são de **inteira e exclusiva responsabilidade do cliente** e de suas respectivas equipes de Infraestrutura e Segurança da Informação.

Recomendamos fortemente que toda e qualquer configuração de infraestrutura seja validada e homologada em um ambiente de pré-produção antes de ser aplicada ao ambiente produtivo oficial.

* **Configuração para Microsoft IIS**

  Microsoft IIS (Clique para expandir)
  + Para utilizar o IIS como Proxy Reverso, é necessário ter os módulos **URL Rewrite** e **Application Request Routing (ARR)** instalados no servidor. A configuração abaixo deve ser inserida no arquivo `web.config` do site configurado no IIS.

    xmlMidnightIIS
























    ]]>Nota para IIS

    O limite de requisições (Rate Limit) no IIS geralmente é configurado através da funcionalidade "Dynamic IP Restrictions" no painel do Gerenciador do IIS, bloqueando IPs que excedam um número máximo de requisições concorrentes.
* **Configuração para Nginx**

  Nginx (Clique para expandir)
  + O Nginx é o proxy reverso mais adotado para aplicações modernas e possui mecanismos nativos excelentes de Rate Limit e segurança. A configuração abaixo deve ser inserida no seu arquivo de bloco de servidor (ex: `/etc/nginx/sites-available/sua-api.conf`).

    ymlMidnightNginx
