---
article_id: 360020555111
category: ADVPL - Web Service
content_hash: fe382a4bfc454203222f650257b85910d2a8ef3de08a1ef378b029384ccdfb09
fetched_at: '2026-06-28T22:40:10.259243+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Em um WS REST,
  definir a quantidade de informação retornada em um método GET
type: support-article
updated_at: '2022-04-20T20:05:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020555111-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Em-um-WS-REST-definir-a-quantidade-de-informa%C3%A7%C3%A3o-retornada-em-um-m%C3%A9todo-GET
---

**Dúvida**No retorno da consulta- método *GET*, precisamos retornar vários campos em torno de 70 e vários cadastros de cliente conforme o filtro solicitado. Qual o limite do retorno, tem alguma parametrização específica na configuração do serviço para este retorno? Existe alguma forma de desenvolvimento a cada SetResponse como se fosse um retorno para aplicação que solicitou?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL– A partir da versão 11.80  
  
**Solução**Com relação aos limites de retorno, não está relacionado ao *web service* em si, mas com as limitações da linguagem **ADVPL,** vide documentações em **Saiba mais**.

Com relação a necessidade levantada, o que pode ser feito é definir a quantidade de páginas que a requisição irá retornar, bem como a quantidade de registros exibidos por página.   
A seguir um exemplo de **WS REST** com um método **GET**, utilizando o cadastro de clientes(SA1), para referência;

```
#INCLUDE "PROTHEUS.CH"  
#INCLUDE "RESTFUL.CH"  
  
WSRESTFUL WSRESTA1 DESCRIPTION "Exemplo de serviço REST"  
   
 WSDATA page AS INTEGER OPTIONAL  
 WSDATA pageSize AS INTEGER OPTIONAL  
 WSDATA searchKey AS STRING OPTIONAL  
   
 WSMETHOD GET customers DESCRIPTION "Retorna lista de clientes" WSSYNTAX "/customers " PATH 'customers' PRODUCES APPLICATION_JSON  
  
END WSRESTFUL  
  
//-------------------------------------------------------------------  
/*/{Protheus.doc} GET / customers  
Retorna a lista de clientes.  
  
@param SearchKey , caracter, chave de pesquisa utilizada em diversos campos  
 Page , numerico, numero da pagina   
 PageSize , numerico, quantidade de registros por pagina  
  
@return cResponse , caracter, JSON contendo a lista de clientes  
/*/  
//-------------------------------------------------------------------  
  
WSMETHOD GET customers WSRECEIVE searchKey, page, pageSize WSREST WSRESTA1  
   
 Local aListCli := {}  
   
 Local cAliasSA1 := GetNextAlias()  
 Local cJsonCli := ''  
 Local cSearchKey := ''  
 Local cSearch := ''  
 Local cWhere := "AND SA1.A1_FILIAL = '"+xFilial('SA1')+"'"  
   
 Local lRet := .T.  
   
 Local nCount := 0  
 Local nStart := 1  
 Local nReg := 0  
 Local nAux := 0  
   
 Local oJsonCli := JsonObject():New()   
   
 Default self:searchKey := ''  
 Default self:page := 1  
 Default self:pageSize := 10   
   
 //-------------------------------------------------------------------  
 // Tratativas para a chave de busca  
 //-------------------------------------------------------------------  
 If !Empty(self:searchKey)  
 cSearch := AllTrim( Upper( Self:SearchKey ) )  
 cWhere += " AND ( SA1.A1_COD LIKE '%" + cSearch + "%' OR "  
 cWhere += " SA1.A1_LOJA LIKE '%" + cSearch + "%' OR "  
 cWhere += " SA1.A1_NOME LIKE '%" + FwNoAccent( cSearch ) + "%' OR "  
 cWhere += " SA1.A1_NOME LIKE '%" + cSearch + "%' ) "   
 EndIf  
   
 cWhere := '%'+cWhere+'%'  
   
 //-------------------------------------------------------------------  
 // Query para selecionar clientes  
 //-------------------------------------------------------------------  
 BEGINSQL Alias cAliasSA1  
   
 SELECT SA1.A1_COD, SA1.A1_LOJA, SA1.A1_NOME  
 FROM %table:SA1% SA1  
 WHERE SA1.%NotDel%  
 %exp:cWhere%  
   
 ENDSQL  
   
 If ( cAliasSA1 )->( ! Eof() )  
   
 //-------------------------------------------------------------------  
 // Identifica a quantidade de registro no alias temporário  
 //-------------------------------------------------------------------  
 COUNT TO nRecord  
   
 //-------------------------------------------------------------------  
 // nStart -> primeiro registro da pagina  
 // nReg -> numero de registros do inicio da pagina ao fim do arquivo  
 //-------------------------------------------------------------------  
 If self:page > 1  
 nStart := ( ( self:page - 1 ) * self:pageSize ) + 1  
 nReg := nRecord - nStart + 1  
 Else  
 nReg := nRecord  
 EndIf  
   
 //-------------------------------------------------------------------  
 // Posiciona no primeiro registro.  
 //-------------------------------------------------------------------  
 ( cAliasSA1 )->( DBGoTop() )  
   
 //-------------------------------------------------------------------  
 // Valida a exitencia de mais paginas  
 //-------------------------------------------------------------------  
 If nReg > self:pageSize  
 oJsonCli['hasNext'] := .T.  
 Else  
 oJsonCli['hasNext'] := .F.  
 EndIf  
 Else  
 //-------------------------------------------------------------------  
 // Nao encontrou registros  
 //-------------------------------------------------------------------  
 oJsonCli['hasNext'] := .F.  
 EndIf  
   
 //-------------------------------------------------------------------  
 // Alimenta array de clientes  
 //-------------------------------------------------------------------  
 While ( cAliasSA1 )->( ! Eof() )   
   
 nCount++  
   
 If nCount >= nStart  
   
 nAux++   
 aAdd( aListCli , JsonObject():New() )  
   
 aListCli[nAux]['id'] := ( cAliasSA1 )->A1_COD  
 aListCli[nAux]['name'] := Alltrim( EncodeUTF8( ( cAliasSA1 )->A1_NOME ) )  
 aListCli[nAux]['unit'] := ( cAliasSA1 )->A1_LOJA  
   
 If Len(aListCli) >= self:pageSize  
 Exit  
 EndIf  
   
 EndIf  
   
 ( cAliasSA1 )->( DBSkip() )  
   
 End  
   
 ( cAliasSA1 )->( DBCloseArea() )  
   
 oJsonCli['clients'] := aListCli  
   
 //-------------------------------------------------------------------  
 // Serializa objeto Json  
 //-------------------------------------------------------------------  
 cJsonCli:= FwJsonSerialize( oJsonCli )  
   
 //-------------------------------------------------------------------  
 // Elimina objeto da memoria  
 //-------------------------------------------------------------------  
 FreeObj(oJsonCli)  
   
 Self:SetResponse( cJsonCli ) //-- Seta resposta  
  
Return( lRet )
```

A seguir como fica a requisição, limitando seu retorno a 1 página e apenas 2 registros nesta página;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016467491/mceclip1.png)

**Saiba mais  
[String size overflow](http://tdn.totvs.com/display/tec/String+size+overflow)****[MaxStringSize](http://tdn.totvs.com/pages/viewpage.action?pageId=161349793)**[**Melhoria - Proteções e limites do AdvPL**](http://tdn.totvs.com/pages/viewpage.action?pageId=6065231)[**MaxQuerySize**](http://tdn.totvs.com/display/tec/MaxQuerySize)[**ConsoleMaxSize**](http://tdn.totvs.com/display/tec/ConsoleMaxSize+--+29343)
