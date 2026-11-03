---
article_id: 360047843813
category: ADVPL - Relatório
content_hash: 2b70c83a34619cdf747f989dc12b94904f92c90ac2a4885e8517d9f833b99920
fetched_at: '2026-06-28T22:40:22.852485+00:00'
product: protheus
section_id: 1500001549062
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Exemplo de TREPORT
  utilizando o método PrintGraphic
type: support-article
updated_at: '2024-03-26T14:08:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047843813-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Exemplo-de-TREPORT-utilizando-o-m%C3%A9todo-PrintGraphic
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:20:00 min** **Dúvida**Existe algum exemplo de implementação da classe TREPORT utilizando o método *PrintGraphic*?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão P12.1.25  
  
**Solução**

Abaixo exemplo funcional com o método *PrintGraphic()*

***obs.: Lib Label P12 Lobo - superior 04/05/2020***

```
#INCLUDE "PROTHEUS.CH"  
  
user Function PRINTGRAPH()  
  
Local oReport as Object  
Local oSection as Object  
  
//Classe TREPORT  
oReport := TReport():New('EXEMPLO',"Clientes por UF",/*cPerg*/,{|oReport|ReportPrint(oReport,oSection)})  
  
//Seção 1   
oSection := TRSection():New(oReport,'Clientes')  
  
//Definição das colunas de impressão da seção 1  
TRCell():New(oSection, "A1_COD" , "TRB", "Código", /*Picture*/, /*Tamanho*/, /*lPixel*/, /*{|| code-block de impressao }*/)  
TRCell():New(oSection, "A1_NOME", "TRB", "Razão" , /*Picture*/, /*Tamanho*/, /*lPixel*/, /*{|| code-block de impressao }*/)  
TRCell():New(oSection, "A1_EST" , "TRB", "UF"    , /*Picture*/, /*Tamanho*/, /*lPixel*/, /*{|| code-block de impressao }*/)  
  
//Definção da collection  
oColl:=TRCollection():New("TOTAL UF", "COUNT", /*oBreak*/,"Total POR UF",;  
 /*cPicture*/, /*uFormula*/ oSection:Cell("A1_COD"), /*.lEndSection.*/ .F.,;  
 /*.lEndReport.*/ .T., /*oParent*/ oSection, /*bCondition*/,;  
 /*uContent*/ oSection:Cell("A1_EST") )   
  
oReport:PrintGraphic()  
oReport:PrintDialog()  
  
Return  
  
Static Function ReportPrint(oReport,oSection)  
  
#IFDEF TOP  
  
    Local cAlias := "TRB"  
  
    BEGIN REPORT QUERY oSection  
  
        BeginSql alias cAlias  
            SELECT A1_COD,A1_NOME,A1_EST  
            FROM %table:SA1%   
            ORDER BY A1_FILIAL,A1_EST  
        EndSql  
  
    END REPORT QUERY oSection   
  
    oSection:aCollection[1]:SetGraphic(4,"UF")  
    oSection:PrintGraphic()  
    oSection:Print()  
  
#ENDIF  
  
return
```

Resultado de impressão em PDF na primeira pagina relatório e na segunda o gráfico.

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068721534/mceclip0.png)**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068721994/mceclip2.png)**

**Saiba Mais**

**[Classe TReport](https://tdn.totvs.com/display/public/PROT/TReport)**

**[Método TRCollection](https://tdn.totvs.com/display/public/PROT/TRCollection)**
