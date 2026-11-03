---
content_hash: 5a737501fe67192b2845865e6f5dc10205cbf237dec1181bbdf8247fcc727882
fetched_at: '2026-06-29T00:08:10.174126+00:00'
page_id: '240302811'
product: rm
source: tdn-rm
title: 'Como fazer: Inserir e Consultar o PRJPLANILHAATIVIDADESDATA através do Soapui.'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=240302811
version: 6
---

# wsDataServer

1° Validar se o localhost está funcionando. Mais informações em:

2° Abrir  NEW SOAP PROJECT e colocar o endereço do localhost no “**Initial WSDL**”

3° passo: Abrir o “SAVE RECORD – Request 1”

4° passo: Inserir o nome da planilha entre o “<tot:DataServerName>**PRJPLANILHAATIVIDADESDATA**</Tot:DataServerName”

5°passo: Colocar na frente do XML enviado ”<Tot:XML> <![CDATA[<?......................>]]> to:XML>

6°passo: Colocar no <tot:Contexto>**codcoligada=1;CodSistema=M;CodUsuario=mestre**</tot:Contexto>

7°passo: Autenticar mestre\totvs  - Authenticate pre-emptively

Como gerar o XML no SOAPIU

1° Validar se o localhost está funcionando

2° Abrir  NEW SOAP PROJECT e colocar o endereço do localhost no “**Initial WSDL**”

3° passo: Clicar em ReadRecord e abrir o Request 1

4° passo: No  <tot:DataServerName>**PRJPLANILHAATIVIDADESDATA**</tot:DataServerName>

 5° passo: <tot:PrimaryKey>**1;84;1**</tot:PrimaryKey>

Para saber qual a primaryKey, basta abrir o SQL, inserir qual talela pertence a “PrjPlanilhaatividades” clicar em ALT+F1 para verificar qual a sequência da primary.

Neste caso, temos CodColigada;Idprj;idtrf.

6° passo:  <tot:Contexto>**CODCOLIGADA=1;CODUSUARIO=mestre**</tot:Contexto>

7° passo: Autenticar usuário e senha para gerar o xml.

8° passo: Gerar o XML – Clicar em submit request
