---
article_id: 360021109092
category: ADVPL - Relatório
content_hash: d12bddab1f52cd224d4aa100c333a70ec04d93c9137f21a3127e45864f39ea9e
fetched_at: '2026-06-28T22:40:22.933952+00:00'
product: protheus
section_id: 1500001549062
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - TReport formatação
  condicional
type: support-article
updated_at: '2022-09-12T18:05:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021109092-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-TReport-formata%C3%A7%C3%A3o-condicional
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:03:00 min  
  
Dúvida**Como realizar formatação das linhas e dos registros de forma condicional no Totvs Report?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Você pode alterar as formatação das linhas do TReport através das propriedades das células ( **aFormatCond** ), além disso você pode colocar condições para que este processo seja realizado.  
**aFormatCond** é o Array com as condições do usuário para impressão de forma variável da cor  
da célula: Elementos: 1-Condição, 2-Cor de fundo e 3-Cor da fonte.  
Uma observação importante é que caso seja **impressão em planilha ela não irá levar a condicional**.  
  
**Exemplo**

```
#INCLUDE "Topconn.ch"  
#INCLUDE "Protheus.ch"  
  
// Exemplo de relatorio usando tReport com uma Section  
  
User Function RCOMR02()  
  
local oReport  
local cPerg := 'RCOMR02'  
local cAlias := getNextAlias()  
  
  
Pergunte(cPerg, .f.)  
  
oReport := reportDef(cAlias, cPerg)  
oReport:printDialog()  
  
return  
  
//+-----------------------------------------------------------------------------------------------+  
//! Rotina para montagem dos dados do relatório. !  
//+-----------------------------------------------------------------------------------------------+  
Static Function ReportPrint(oReport,cAlias)  
  
local oSecao1 := oReport:Section(1)  
  
oSecao1:BeginQuery()  
  
BeginSQL Alias cAlias  
  
select E1_NUM, E1_VALOR, * from SE1990  
  
EndSQL  
  
oSecao1:EndQuery()  
oReport:SetMeter((cAlias)->(RecCount()))  
oSecao1:Print()  
  
return  
  
//+-----------------------------------------------------------------------------------------------+  
//! FunÃ§Ã£o para criação da estrutura do relatório. !  
//+-----------------------------------------------------------------------------------------------+  
Static Function ReportDef(cAlias, cPerg)  
  
local cTitle := "RelatÃ³rio de Conta Corrente"  
local cHelp := "Permite gerar relatÃ³rio de Conta Corrente de Fornecedores"  
local oReport  
local oSection1  
local cPosit := "E1_VALOR > 100"  
  
Pergunte(cPerg, .f.)  
  
oReport := TReport():New('RCOMR02',cTitle,cPerg,{|oReport|ReportPrint(oReport,cAlias)},cHelp)  
  
//Primeira seÃ§Ã£o  
oSection1 := TRSection():New(oReport,"Conta Corrente",{cAlias})  
  
ocell2:= TRCell():New(oSection1,"E1_NUM", cAlias, "NÃºmero")  
ocell:= TRCell():New(oSection1,"E1_VALOR", cAlias, "Valor")  
  
aAdd(oSection1:Cell("E1_VALOR"):aFormatCond, {"E1_VALOR > 100 .and. E1_VALOR < 1000" ,,CLR_GREEN})  
aAdd(oSection1:Cell("E1_VALOR"):aFormatCond, {"E1_VALOR >= 1000" ,CLR_HGRAY,CLR_RED})  
//aAdd(oSection1:Cell("E1_VALOR"):aFormatCond, {"E1_VALOR >= "+cvaltochar(MV_PAR01) ,,CLR_RED})  
  
Return(oReport)
```

**Saiba mais**[Treport](http://tdn.totvs.com/display/public/PROT/TReport)
