---
content_hash: b773032ae9b24ec49aab03ee44253329d17c5e71a8d3ffb70ff97954834d3341
fetched_at: '2026-06-28T21:35:29.100189+00:00'
page_id: '736971727'
product: fluig
source: tdn-fluig
title: Configuração de proxy reverso NGINX com HTTPS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=736971727
version: 35
---

4.\*ndice

# Objetivo

---

O objetivo deste guia é detalhar as configurações necessárias para utilização de *proxy* reverso NGINX com protocolo HTTPS.

# Pré-requisitos

---

* Possuir o NGINX na versão 1.20.1 ou superior instalado. Detalhes de instalação e configuração do NGINX estão disponíveis [na documentação oficial](https://docs.nginx.com/).

  Importante!

  Somente é possível utilizar o NGINX **até a versão** **1.22** por conta da compatibilidade com o módulo nginx-stick-module-ng.
* Possuir um host no DNS configurado para a plataforma, com domínio específico.

* Possuir um certificado digital válido.

# Recomendações

---

* Instalar o NGINX em um servidor separado do servidor onde o Fluig está instalado.

* Faça as alterações necessárias na topologia utilizada, para que o acesso funcione corretamente após implantar o *proxy* reverso. Para saber mais sobre a topologia DMZ, .

  #ebecf0

  trueExemplos de alterações  
  Apontamento de IP na rede interna, liberação de portas, alteração de endereço de acesso do Fluig (usuário wcmadmin).

# Configurando o NGINX como *proxy* reverso com HTTPS

---

Siga o passo a passo, conforme descrito abaixo.

nginx-settingstruestep1Passo 1

* Certifique-se de que a interface de configuração pública esteja preenchida com o IP do servidor (rede interna). Para isso, abra o arquivo **[FLUIG]/appserver/domain/configuration/host.xml,** localize a tag <interface name="public"> e verifique o valor da propriedade "value":

Importante!

Não é recomendado utilizar o valor "0.0.0.0" na interface de configuração pública.

step2Passo 2

* Configure o Fluig em HTTPS na plataforma NGINX conforme documentação disponível em .

  Importante!

  Lembrando que, se o seu ambiente utiliza , a configuração de HTTPS deve ser replicada [manualmente](https://tdn.totvs.com/pages/viewpage.action?pageId=354472893#Configura%C3%A7%C3%A3oHTTPSdaplataforma-Configura%C3%A7%C3%A3odeHTTPSmanual) para todos os servidores do Fluig.

step3Passo 3

* No servidor NGINX, utilize os certificados e o arquivo gerado para realizar a seguinte configuração:
  + Salve os certificados na pasta **/etc/nginx/certs**;
  + Cole o arquivo de configuração gerado no **Passo 2** em **/etc/nginx/conf.d**.

step4Passo 4

* Adicione as diretivas para configuração das notificações em tempo real (serviço Realtime) no arquivo gerado no **Passo 3** - "**/etc/nginx/conf.d**":
  + Informe o DNS do servidor na diretiva "server\_name";
  + Informe o caminho completo dos arquivos de certificado (arquivo .cert) na diretiva ssl\_certificate;
  + Informe o caminho completo dos arquivos de certificado (arquivo .key) na diretiva ssl\_certificate\_key;
  + Informe o IP e a porta onde o serviço do Realtime está em execução, na diretiva "proxy-pass". A porta padrão do Realtime é 7777, caso não tenha sido alterada.

    Midnight

step5Passo 5

* No arquivo "/etc/nginx/conf.d", no contexto "server", que estará ouvindo a porta 443, configure as seguintes diretivas:
  + Informe o caminho completo dos arquivos de certificado (arquivo .cert) na diretiva ssl\_certificate;
  + Informe o caminho completo dos arquivos de certificado (arquivo .key) na diretiva ssl\_certificate\_key;
  + Oculte a versão do NGINX no cabeçalho de resposta das requisições, informando o valor "off" na diretiva "server\_tokens";
  + Adicione as diretivas de cabeçalho ("add\_header") conforme abaixo:

    bashMidnight

Importante!

Substitua "**fluig.suaempresa.com**" pelo endereço a partir do qual você deseja acessar o Fluig.

Nota:

Recomendamos o uso de chaves e protocolos mais modernos e seguros como os indicados no exemplo. Porém, outras chaves também são suportadas:

DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA

Preencha a diretiva **ssl\_ciphers** do conf.d substituindo pelos valores suportados acima que estejam de acordo com sua política de segurança. As chaves podem ser validadas em <https://ciphersuite.info/>.

E também os protocolos: TLSv1, TLSv1.1 e TLSv1.2

Preencha a diretiva **ssl\_protocols** do conf.d substituindo pelos valores suportados acima que estejam de acordo com sua política de segurança.

step6Passo 6

* No contexto "server" que estará ouvindo a porta 443, adicione as seguintes diretivas no contexto "location /", no arquivo "/etc/nginx/conf.d", conforme abaixo:
  + Na diretiva "proxy-pass", informe o IP do servidor do Fluig e a porta definida na instalação da plataforma (a porta padrão é 8080);
  + Adicione as diretivas de cabeçalho para "proxy" conforme abaixo:

    Midnight

step7Passo 7

* Após efetuar os passos anteriores, o arquivo "/etc/nginx/conf.d" estará desta forma:

  Midnight

step8Passo 8

* Reinicie os serviços do Fluig e do NGINX em ambos os servidores.

Importante!

Dependendo do ambiente (versão, sistema operacional utilizado, etc.) algumas diretivas detalhadas nesta documentação podem estar presentes na sua instalação do NGINX também. Isso causará o erro "*directive is duplicate*", impossibilitando a inicialização do serviço do NGINX. Caso isso ocorra, verifique qual diretiva será mantida: dos arquivos de configuração do NGINX ou no arquivo de configuração criado com base nessa documentação.

# Configurar Rate Limit de requisições

---

### Funcionamento do controle de taxa (Rate Limit)

O NGINX gerencia a frequência de requisições através de dois componentes interdependentes:

* **`limit_req_zone` (Definição):** Estabelece a regra global no contexto `http`, configurando a zona de memória compartilhada para armazenar os estados dos IPs e a taxa de transferência permitida (ex: 10 requisições por segundo).
* **`limit_req` (Aplicação):** Ativa a regra definida anteriormente em escopos específicos, como `server` ou `location` (endpoints).
* **Chave de Identificação:** Geralmente utiliza o **`$binary_remote_addr`**, que armazena o endereço IP do cliente de forma compacta (4 bytes para IPv4) para economizar memória no servidor.

### Configuração de limitação por IP

Edite o arquivo de configuração (`/etc/nginx/nginx.conf`) e defina a regra dentro do bloco **http**:

#f2f2f2#f2f2f2Entenda os parâmetros

* **`$binary_remote_addr`**: Identificador binário do IP (mais eficiente que texto).
* **`zone=post_publish_limit:10m`**: Reserva **10MB** para rastrear o estado dos IPs.
* **`rate=5r/s`**: Estabelece o teto de **5 requisições por segundo** por usuário.

## Aplicar ao endpoint específico

---

Para aplicar a regra de controle de fluxo a uma rota específica, utilize a diretiva **`limit_req`** dentro do bloco **`location`** desejado, conforme o exemplo abaixo:

css

## Explicando os parâmetros

---

Esta seção detalha a lógica de controle de fluxo (Rate Limit) aplicada, que define como o servidor processa o volume de requisições e gerencia picos de tráfego:

* **`rate=5r/s`**: Estabelece a velocidade média permitida de 5 requisições por segundo por endereço IP.
* **`burst=10`**: Cria uma "margem de tolerância" para acomodar picos repentinos de até 10 requisições além do limite definido.
* **`nodelay`**: Determina que as requisições dentro da margem de *burst* sejam processadas imediatamente; sem este parâmetro, o NGINX suaviza o tráfego introduzindo atrasos (delay) para manter a taxa constante.

## Customizando resposta (HTTP 429)

---

Por padrão, o NGINX retorna o erro **503** (Service Unavailable). Para indicar explicitamente que o bloqueio ocorreu por excesso de requisições, utiliza-se o código **429 (Too Many Requests)**:

css

## Exemplo completo

---

Esta configuração consolidada implementa uma estratégia de **defesa em profundidade** no NGINX, garantindo a estabilidade da API por meio de um controle rigoroso de vazão. O exemplo abaixo integra a definição da zona de memória, a customização do código de resposta e a aplicação prática em um endpoint crítico.

css

Ao adotar este modelo, o servidor passa a distinguir acessos legítimos de disparos automatizados, preservando os recursos do backend e fornecendo respostas semanticamente corretas (HTTP 429) ao excederem os limites estabelecidos.

# Troubleshotting

---

Erros de *timeout* ou conexão encerrada pelo NGINX.

Nota:

Se não for configurado, o padrão de *timeout* do *proxy* reverso do NGINX é 60 segundos. A configuração recomendada é 300 segundos – que é o *timeout* padrão do TOTVS Fluig – podendo ser ajustado para mais ou para menos de acordo com a necessidade.

nginx-troubleshooting1truet1-step1Passo 1

* Abra o arquivo de configuração do NGINX - /etc/nginx/conf.d - e inclua as diretivas de *timeout* no contexto "server" > "location /" conforme abaixo:

  Midnight

t1-step2Passo 2

* Após incluir as diretivas de *timeout*, o arquivo "/etc/nginx/conf.d" estará desta forma:

  Midnight

t1-step3Passo 3

* Reinicie os serviços NGINX para aplicar a alteração realizada.

Atenção:

Caso o problema de *timeout* persista após aplicar a configuração acima, é necessário avaliar o que está ocorrendo ao invés de apenas aumentar o tempo de *timeout*. Se desejar, entre em contato com o seu ESN e solicite uma proposta de consultoria investigativa Fluig.

# Ocultar informações no cabeçalho HTTP

---

Para prevenir vulnerabilidades, é importante que as informações não fiquem expostas no cabeçalho HTTP.  e saiba como ocultá-las.
