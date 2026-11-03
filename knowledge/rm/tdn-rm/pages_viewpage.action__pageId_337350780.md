---
content_hash: 3ff77752ab8df5590a34c355144939bdd774225dd9a3fa4ab335e43db2141734
fetched_at: '2026-06-29T00:08:51.609296+00:00'
page_id: '337350780'
product: rm
source: tdn-rm
title: Instalação License Server Virtual
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=337350780
version: 13
---

7º Passo

# Índice

---

.\*ndice:

# Introdução

---

* O objetivo deste documento é a instalação e configuração do License Server Virtual por completo.

* Link para baixar o arquivo de instalação: <ftp://ftp.totvs.com.br/hlcloud/Instaladores/LicenseServerVirtual/>

# Sistemas operacionais homologados

Portabilidade

Segue abaixo link com todas as versões de sistemas operacionais homologados para o License Server:

<http://tdn.totvs.com/display/tec/TOTVSTEC+NG+-+Sistemas+operacionais>

Java

O instalador do License Server precisa de um ambiente de execução Java (JRE) para funcionar adequadamente. As versões atualmente suportadas são a 7 e a 8. Caso você não possua o JRE instalado, faça o download em <https://www.java.com/pt_BR/download/manual.jsp>

# Procedimento de Instalação

---

passos1º Passo

* Iniciar o processo de instalação executando como administrador.

|  |  |
| --- | --- |

2º Passo3º Passo4º Passo5º Passo6º Passo7º Passo8º Passo9º Passo

# Procedimento de Configuração

* Nestes próximos passos serão executas as configurações para inserir o código ID gerado no site do Suporte do Cliente em Gestão de Licenças. (3º Passo)
* link: <https://totvscst.zendesk.com/hc/pt-br/#home> (Meu Espaço > Gestão de Licenças)

Passo 21º Passo2° Passo3º Passo

* Entrando no portal do Cliente em Gestão de Licenças, após ter aceitado o termo de uso (EULA) será apresentada algumas abas para criação e/ou remanejamento das licenças.
* Para situação de reinstalação ou uma nova instalação possivelmente poderá existir um ou mais id na lista de relação do mesmo [TOTVS ID]. Diante deste fato bloqueie o ID existente sempre antes de se criar outro novo, pois desta forma as licenças serão carregadas de forma automática para o novo ID (não necessitando de remanejamentos futuros)

|  |  |
| --- | --- |

4º Passo

* Inserir o Código ID no campo em branco abaixo copiar e colar.

5º Passo6º Passo7º Passo8º Passo

|  |  |
| --- | --- |

# Totvs Monitor

MonitorTela do Monitor

* Em seguida o Monitor será aberto com as telas contendo suas Licenças.

Log de uso

* Botão de atualização manual do licenciamento TOTVS.

# Regras de Firewall e Acesso de rede

Aviso

* O TOTVS | License Server necessita de acesso à internet para sua instalação e operação.
* O Acesso é realizado através do protocolo HTTPS e toda a comunicação é feita pela porta 443. Caso a sua empresa possua firewall e/ou restrições de acesso à internet, é necessário que o administrador da rede libere o acesso para o endereço <https://licenseservercloud.totvs.com.br/> (Este é o endereço base dos serviços do License Server, assim ao acessar em um **Browse**, será retornada a uma mensagem de erro de serviço). O tipo de conexão realizada é **outbound** (O License Server realiza uma chamada cliente a um servidor na Internet).

Lembrete

* Utilize sempre o endereço DNS [https://licenseservercloud.totvs.com.br](https://licenseservercloud.totvs.com.br/). A utilização do seu respectivo endereço IP pode causar interrupção na atualização diária das licenças caso a Totvs altere o endereço IP. Isso não fará com que o LS Virtual pare de funcionar de imediato, mas pela perda de comunicação diária, passará a exibir a mensagem de expiração da licença e obrigará uma intervenção manual de troca do IP ou alteração para o DNS ([licenseservercloud.totvs.com.br](http://licenseservercloud.totvs.com.br)) na regra do seu servidor.
Teste de comunicação

* Ative o serviço Telnet do Windows na maquina aonde o License Server Virtual foi instalado e faça um teste de comunicação com o Host do RM.
* Execute um Tracert no endereço: [licenseservercloud.totvs.com.br](http://licenseservercloud.totvs.com.br/)

# Dicionário de Terminologias

---

**TOTVS| License Server Virtual (x64):**Programa instalado na arquitetura 64 bits.

**EULA**: Acordo de licença de usuário final.

**TOTVS ID**: É a identificação do contrato do cliente.

**Regras de firewall**: O **firewall** é um sistema de segurança que utiliza **regras** para bloquear ou permitir conexões e transmissão de dados entre o seu computador e a Internet.

**Outbound**: Pacotes que saem da rede interna, realiza uma chamada cliente a um servidor na Internet.

**Servidores DNS:** (Domain Name System, ou sistema de nomes de domínios) são os responsáveis por localizar e traduzir para números IP os endereços dos sites que digitamos nos navegadores.

falsefalse

**Produto:** Framework

false

**Versão:** 11.80.XX, 12.01.XX

false

**Processo:** Instalação License Server Virtual

falsefalse

**Status:** Finalizado

false

**Data:** 08/02/2018

false

**Autores:**

Fernando Rodrigo da Silva
