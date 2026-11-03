---
article_id: 360020985391
category: ADVPL - Relatório
content_hash: 5dcb079fd57cada80aea554e3cc181d68522437771fc5dcb50c6d2040ae128e5
fetched_at: '2026-06-28T22:40:22.882043+00:00'
product: protheus
section_id: 1500001549062
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Quais são as propriedades
  para formatar o corpo e cabeçalho do totvs reports
type: support-article
updated_at: '2022-01-03T20:32:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020985391-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Quais-s%C3%A3o-as-propriedades-para-formatar-o-corpo-e-cabe%C3%A7alho-do-totvs-reports
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Quais são as propriedades para formatar e definir o Corpo e Cabeçalho do Totvs Reports?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Segue propriedades disponíveis na Classe

```
oReport := TReport():New("Fonte","TITULO","",{|oReport| PrintReport(oReport)}  
  
oReport:SetTotalInLine(.F.) //Define se os totalizadores serão impressos em linha ou coluna  
oReport:SetTitle('Protheus Report Utility') //Define o título do relatório  
oReport:SetLineHeight(30) //Define a altura da linha na impressão  
oReport:SetColSpace(1)    //Define o espaçamento entre as colunas  
oReport:SetLeftMargin(0)  //Define a margem à esquerda do relatório  
oReport:cFontBody := 'Courier New'   
oReport:nFontBody := 6   
oReport:lBold := .F. //Imprime a fonte em negrito  
oReport:lUnderLine := .F. //Aponta se a fonte é sublinhada  
oReport:lHeaderVisible := .T.   
oReport:lFooterVisible := .T.   
oReport:lParamPage := .F.  
 
```

**Saiba mais**[TReport](http://tdn.totvs.com/display/public/PROT/TReport)
