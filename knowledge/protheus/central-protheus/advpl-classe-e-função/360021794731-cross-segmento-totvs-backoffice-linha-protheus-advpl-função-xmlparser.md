---
article_id: 360021794731
category: ADVPL - Classe e Função
content_hash: c5515bf5d88efa9a2185bf68daf99cd448d4f27a441bfcd09f4617d207db64fe
fetched_at: '2026-06-28T22:40:16.848630+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Função XmlParser
type: support-article
updated_at: '2021-10-25T22:10:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021794731-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-XmlParser
---

**Dúvida**Existe uma função para retornar um XML?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Solução**Esta função permite retornar um objeto, que possui uma estrutura XML, recebido de um arquivo por parâmetro.

**Exemplo:**

```
#INCLUDE "TOTVS.CH"  
#INCLUDE "XMLXFUN.CH"  
  
User Function getObjXML()  
  
Local cError   := ""  
Local cWarning := ""  
Local oXml := NIL  
   
//Gera o Objeto XML  
oXml := XmlParser( GeraXML(), "_", @cError, @cWarning )  
  
If (oXml == NIL )  
  MsgStop("Falha ao gerar Objeto XML : "+cError+" / "+cWarning)  
  Return  
Endif  
  
// Mostrando a informação do Node  
MsgInfo(oXml:_PEDIDO:_NOME_CLIENTE:Text,"Cliente")  
  
Return oXml  
  
// função para gerar uma string contendo um xml  
Static Function GeraXML()  
  
Local cScript  
  
cScript := '<?xml version="1.0" encoding="ISO-8859-1"?>'  
cScript += "<pedido>"  
cScript += "    <Nome_Cliente>Microsiga Software</Nome_Cliente>"  
cScript += "    <Endereco>Av. Braz Leme</Endereco>"  
cScript += "    <Numero>1361</Numero>"  
cScript += "    <Data>22-03-2005</Data>"  
cScript += "    <Itens>"  
cScript += "        <Item>"  
cScript += "            <Produto>Protheus</Produto>"  
cScript += "            <Quantidade>1</Quantidade>"  
cScript += "            <Preco>100.00</Preco>"  
cScript += "        </Item>"  
cScript += "    </Itens>"  
cScript += "</pedido>"  
  
Return cScript
```

**Saiba Mais  
[XmlParserFile](http://tdn.totvs.com/display/tec/XmlParserFile)**
