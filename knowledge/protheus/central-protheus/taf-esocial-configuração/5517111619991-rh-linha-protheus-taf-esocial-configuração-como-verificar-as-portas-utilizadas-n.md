---
article_id: 5517111619991
category: TAF - eSocial - Configuração
content_hash: 9921a3880d1cc2dbfdcb47a83955e224088c4ab540b9e7fc4d30aa5c369873f0
fetched_at: '2026-06-28T22:45:14.497265+00:00'
product: protheus
section_id: 1500001536941
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Configuração - Como verificar as portas
  utilizadas no TAF e TSS
type: support-article
updated_at: '2026-06-23T11:36:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5517111619991-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-Como-verificar-as-portas-utilizadas-no-TAF-e-TSS
---

**Dúvida**Como verificar as portas utilizadas no TAF e TSS utilizadas nos serviços do sistema?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Configuração - Todas as versões  
  
**Solução**

**PONTO DE ATENÇÃO:**   
As portas utilizadas neste material não são recomendações de utilização e sim para validarmos como o sistema se comunica com os serviços configurados!

**Verificando** **conexão da aplicação com o DBACCESS:**  
1 - Acesse a pasta do DBACCESS do TAF  e localizar o arquivo dbaccess.ini, TAF\TafDbAccess64

2 - Abre o arquivo e localize a seção [GENERAL] e verifique a porta de conexão:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5516819601303)

3 - Abre o arquivo APPSERVER.INI localizado na pasta BIN/APPSERVER e localize a seção [TOPCONNECT].   
As portas do [GENERAL] deve ser igual a porta no [TOPCONNECT]:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5516829170967)

4 - Volte no arquivo DBACCESS.INI e verifique o nome da conexão do TAF configurado localizado na seção referente ao seu TIPO do BANCO DE DADOS. No exemplo abaixo utilizo o SQL SERVER, logo o tipo será MSSQL, caso for ORACLE o TIPO do BANCO DE DADOS é [ORACLE]:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5516881296791)

5 - Acesse novamente o APPSERVER.INI da pasta APPSERVER e compare novamente o nome da conexão no TOPCONNECT se o parâmetro ALIAS está igual ao do DBACCESS.INI:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5516864951191)

**Conexão do REST (TAF-WS) com o DBACCESS**

6 - Acesse a pasta do DBACCESS do TAF e localizar o arquivo dbaccess.ini;

7 - Abre o arquivo e localize a seção [GENERAL] e verifique a porta de conexão:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5516875433623)

8 - Abre o arquivo APPSERVER.INI localizado na pasta BIN/APP e localize a seção [TOPCONNECT].   
As portas do [GENERAL] deve ser igual a porta no [TOPCONNECT]:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5516927931031)

9 - Volte no arquivo DBACCESS.INI e verifique o nome da conexão do TAF configurado localizado na seção referente ao seu TIPO do BANCO DE DADOS. NO exemplo abaixo utilizo o SQL SERVER, logo o tipo será MSSQL, caso for ORACLE o TIPO do BANCO DE DADOS é [ORACLE]:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5516913531927)

10 - Acesse novamente o APPSERVER.INI da pasta APPSERVER e compare novamente o nome da conexão no TOPCONNECT se o parâmetro ALIAS está igual ao do DBACCESS.INI:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5516933661079)

**Conexão do TSS com o DBACCESS**

**OBSERVAÇÃO:**   
*Geralmente o TSS possui outro DBACCESS configurado, verifique qual DBACCESS o TSS está configurado para seguir a orientação de forma correta!*

11 - Acesse a pasta do DBACCESS do TAF e localizar o arquivo dbaccess.ini;

12 - Abre o arquivo e localize a seção [GENERAL] e verifique a porta de conexão:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5516961769495)

13 - Abre o arquivo APPSERVER.INI do TSS localizado na pasta BIN/APPSERVER e localize a seção [TOPCONNECT]. As portas do [GENERAL] deve ser igual a porta no [TOPCONNECT]:

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5516988243351)

14 - Volte no arquivo DBACCESS.INI e verifique o nome da conexão do TAF configurado localizado na seção referente ao seu TIPO do BANCO DE DADOS. NO exemplo abaixo utilizo o SQL SERVER, logo o tipo será MSSQL, caso for ORACLE o TIPO do BANCO DE DADOS é [ORACLE]:

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5516977936023)

15 - Acesse novamente o APPSERVER.INI da pasta APPSERVER e compare novamente o nome da conexão no TOPCONNECT se o parâmetro ALIAS está igual ao do DBACCESS.INI:

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5517019719575)

**PROCEDIMENTO PARA ATUALIZAR A DBAPI.DLL MANUALMENTE:**

16 - Realize a atualização do DBACCESS conforme material abaixo:  
[Automação Fiscal - ATUALIZAÇÃO - Como atualizar o DBAccess para o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034522854)

17 - Após a atualização, acesse o diretório do DBACCESS e acesse a pasta CLIENT e copie o arquivo DPAPI.DLL;

18 - Acesse as pastas do TAF em BIN/APP e BIN/APPSERVER localize outro arquivo DBAPI.DLL e realize o backup do arquivo e cole o arquivo copiado da pasta CLIENT do DBACCESS;

19 - Após substituição do arquivos nos binários, reinicie os serviços do TAF e realize o teste de conexão e acesso ao sistema;

**Obs.:** Caso tenha alguma dúvida enviar os *CONSOLES.LOG's*, *DBCONSOLE.LOG* e *DBACCESS.LOG*.

**SMARTCLIENT**

20 - Acesse a pasta *BIN/SMARTCLIENT* e abre o arquivo *SMARTCLIENT.INI* e abrir o *APPSERVER.INI* da pasta *BIN/APPSERVER* e comparar as portas da seção [TCP]:

appserver.ini:

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5517077256983)

smartclient.ini:

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5517097612823)

A porta deverá ser a mesma porta para que o SMARTCLIENT se conecte com o APPSERVER.

**REST (TAF-WS)**  
21 - Acesse a pasta do REST  e abrir o APPSERVER do TAF-WS (BIN/APP) e verificar o parâmetro [HTTPREST]:

![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5517116709911)

22 - Ao configurar a integração do RM ou Datasul, deverá utilizar o IP do Servidor onde o TAF está instalado e a porta configurada no [HTTPREST].

**TSS (SPED)**  
Ao configurar o Certificado Digital, verificar local onde o TSS está instalado. Abrir o arquivo APPSERVER.INI do TSS e verificar a porta da seção [HTTP]:

![mceclip15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5517111293847)
