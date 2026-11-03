---
article_id: 24473848681367
category: ADVPL - Web Service
content_hash: 13cd2bc709ffd8d9229b4fbf314140c19229d6737446064c41c93e324c7d67eb
fetched_at: '2026-06-28T22:40:10.591712+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Paginação com page
  e pageSize
type: support-article
updated_at: '2024-07-01T16:48:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24473848681367-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Pagina%C3%A7%C3%A3o-com-page-e-pageSize
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24473835678359) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como utilizar a paginação no desenvolvimento de uma API?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - AdvPL - Todas as versões  
  
**Solução**

Para paginação em API, você pode utilizar o page e pageSize.  
No seu código fonte, pode definir o page e o pageSize com conteúdo Default, por exemplo:

```
Default self:page := 1  
Default self:pageSize := 10
```

Dessa forma, se não for passado nada na URL no queryparam, por padrão a página definida para listar os itens será a 1 e o número de registros nesta página, 10.  
  
Para tratativa da definição da página e quantidade de registros, segue um exemplo que pode utilizar numa API com método GET para listagem de clientes(SA1):

```
BEGINSQL Alias cAliasSA1  
  
SELECT SA1.A1_COD, SA1.A1_LOJA, SA1.A1_NOME  
FROM %table:SA1% SA1  
WHERE SA1.%NotDel%  
%exp:cWhere%  
  
ENDSQL  
  
If ( cAliasSA1 )->( ! Eof() )  
  
// Identifica a quantidade de registro no alias temporário  
COUNT TO nRecord  
  
// nStart -> primeiro registro da pagina  
// nReg -> numero de registros do inicio da pagina ao fim do arquivo  
  
If self:page > 1  
nStart := ( ( self:page - 1 ) * self:pageSize ) + 1  
nReg := nRecord - nStart + 1  
Else  
nReg := nRecord  
EndIf  
  
// Posiciona no primeiro registro.  
( cAliasSA1 )->( DBGoTop() )  
  
// Valida a exitencia de mais paginas  
If nReg > self:pageSize  
oJsonCli['hasNext'] := .T.  
Else  
oJsonCli['hasNext'] := .F.  
EndIf  
Else  
  
// Nao encontrou registros  
oJsonCli['hasNext'] := .F.  
EndIf
```

No postman por exemplo, a minha URL ficaria dessa forma para definir a página e quantidade de itens por página:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24561845021079)

Dessa forma, estaria listando a página 2 e 5 registros neste página. **Saiba mais:**[Guia de implementação AdvPL](https://tdn.totvs.com/display/public/INT/Guia+de+implementacao+das+APIs+TOTVS#GuiadeimplementacaodasAPIsTOTVS-Pagina%C3%A7%C3%A3o)  
[ADVPL - Em um WS REST, definir a quantidade de informação retornada em um método GET](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020555111-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Em-um-WS-REST-definir-a-quantidade-de-informa%C3%A7%C3%A3o-retornada-em-um-m%C3%A9todo-GET)
