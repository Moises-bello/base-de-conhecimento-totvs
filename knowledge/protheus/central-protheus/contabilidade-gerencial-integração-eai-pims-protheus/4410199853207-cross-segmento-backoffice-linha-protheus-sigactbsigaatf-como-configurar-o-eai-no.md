---
article_id: 4410199853207
category: Contabilidade Gerencial - Integração EAI PIMS Protheus
content_hash: e540901cd44f1a013bbf197c67d4bf49c3725ed27dfce0b1fed2d00f3479f2bd
fetched_at: '2026-06-28T22:40:54.146483+00:00'
product: protheus
section_id: 1500001537541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB/SIGAATF - Como Configurar
  o EAI no Protheus
type: support-article
updated_at: '2021-10-07T17:00:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410199853207-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-SIGAATF-Como-Configurar-o-EAI-no-Protheus
---

**Dúvida**Como configurar o ambiente para a utilização da integração EAI?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial - A partir da versão 12  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

1. Primeiramente é necessário configurar o AppServer.ini para receber e enviar requisições via WebService SOAP, temos duas maneiras de efetuar esse processo:

1º) Utilizando o assistente **ApWebWizard** conforme a documentação do link: [ApWebWizard](https://tdn.totvs.com/display/framework/Como+iniciar+um+servidor+de+Webservices+no+Protheus)

2º) Colocando diretamente as tags dentro do AppServer.ini, segue exemplo com tags funcionais:

**[http]**  
enable=1  
port=8077

**[OnStart]**  
jobs=JOB\_WS\_9901  
RefreshRate=120

**[localhost:8077/ws]**  
ENABLE=1  
PATH=C:\Program Files\TOTVS12\protheus\_data\web\ws  
ENVIRONMENT=P12.1.25  
INSTANCENAME=ws  
RESPONSEJOB=JOB\_WS\_9901  
DEFAULTPAGE=wsindex.apw

**[JOB\_WS\_9901]**  
TYPE=WEBEX   
ENVIRONMENT=P12.1.25  
INSTANCES=1,10  
SIGAWEB=WS   
INSTANCENAME=ws  
ONSTART=\_\_WSSTART  
ONCONNECT=\_\_WSCONNECT  
PREPAREIN=99,01  
WEBSERVICELOCATION=http://localhost:8077/ws

2. Após configurar o AppServer.ini, suba o appserver do Protheus e veja se o WebService SOAP está ativo ou não, para verificar utilize o caminho usado na Tag WEBSERVICELOCATION no seu navegador, caso tenha dado certo, aparecerá conforme a imagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410197743767/mceclip0.png)

3. Agora no módulo do configurador(SIGACFG), será necessário parametrizar o sistema para utilizar o EAI utilizando o SOAP:

* **MV\_EAIURL2** - Parâmetro que indica ao **EAI Protheus** para qual endereço de *Webservices* a mensagem será disparada. Este parâmetro é utilizado quando o **adapter** está cadastrado com o **Canal Envio** (XX4\_CHANEL) =EAI;  
    
  Exemplo de preenchimento:   
  ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410192726935/mceclip1.png)
* **MV\_EAIUSER** – Parâmetro para envio do usuário de acesso a camada de *Webservices* no sistema destino. Este parâmetro é utilizado quando o **adapter** está cadastrado com o **Canal Envio** (XX4\_CHANEL) =EAI. Este parâmetro somente deve ser configurado quando o sistema que irá receber a mensagem oriunda do **EAI Protheus** possuir autenticação de usuários na camada de *Webservices*;
* **MV\_EAIPASS** – Parâmetro para envio da senha do usuário de acesso a camada de *Webservices* no sistema destino. Este parâmetro é utilizado quando o **adapter** está cadastrado com o **Canal Envio** (XX4\_CHANEL) =EAI. Este parâmetro somente deve ser configurado quando o sistema que irá receber a mensagem oriunda do **EAI Protheus** possuir autenticação de usuários na camada de *Webservices*;

4. O próximo passo é configurar as empresas/filiais do Protheus que irão interagir com os outros sistemas da TOTVS, nesse processo é usado a rotina APCFG050, que fica no seguinte caminho Ambiente > Schedule > Emp. Filial Mensagem Única. Nessa rotina atrelamos uma empresa/filial do Protheus na empresa/filial do outro sistema, conforme imagem abaixo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410198578583/mceclip2.png)

No exemplo da imagem acima, informo que a empresa 1 e filial 1 do RM se comunicará com o grupo de empresas 99 e filial 01 do Protheus.

5. Com isso, para a comunicação via canal EAI funcionar, é necessário cadastrar os Adapters que deseja integrar entre os sistemas, a rotina do adapter é a CFGA020 e seu caminho no configurador é Ambiente > Schedule > Adapter e.a.i. Os adapter são responsáveis pelo processamento da mensagem no sistema, nele você define quais rotinas serão processadas e se o Protheus envia ou recebe essa mensagem. Também definimos se a mensagem no Protheus funcionará de maneira síncrona(Recebe retorno imediato do outro produto) ou assíncrona(Não aguarda o retorno do outro produto, recebendo posteriormente), segue exemplo de um cadastro de ADAPTER:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410199031063/mceclip3.png)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410201815959/mceclip4.png)

6. Para efeito de testes, caso queira validar a mensagem única, mas não possui um outro produto da TOTVS como o RM, LOGIX e etc, há uma ferramenta chamada SOAP UI, onde ela encaminha os arquivos XML para o Web Service do Protheus, assim o Protheus recebe o mesmo e o processa conforme o adapter. Segue a documentação de como configurar o SOAP UI: [Como configurar o SOAP UI](https://tdn.totvs.com/pages/releaseview.action?pageId=224395491)
