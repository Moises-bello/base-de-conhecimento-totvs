---
article_id: 360026710751
category: ADVPL - Relatório
content_hash: 7fe501f13b6e5a60ea5ad075ccb294e2f166efca489bc85a0ea554bceaf9f57d
fetched_at: '2026-06-28T22:40:22.833191+00:00'
product: protheus
section_id: 1500001549062
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Erro type mismatch
  on +  on TRSECTION:SETQUERY
type: support-article
updated_at: '2022-09-21T20:29:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026710751-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-type-mismatch-on-on-TRSECTION-SETQUERY
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:00 min*****Ocorrência**Ao executar um relatório customizado , utilizando a Classe TReport ocorre o erro

type mismatch on +  on TRSECTION:SETQUERY(REPORT02.PRW)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 12.1.17  
  
**Causa**Erro ocorre devido a instrução errada no parâmetro do método ENDQUERY

```
Forma errada  
  
oreport:EndQuery({{"QRY"},cQuery})
```

**Solução**

O parâmetro é utilizado para tratar opções de perguntas (SX1) que possuem o tipo RANGE.

O formato esperado para o parâmetro é { "condição sql 1", "condição sql 2", ... } e cada uma dessas condições depois é adicionada na cláusula where da query.

[EndQuery](http://tdn.totvs.com/display/public/PROT/EndQuery)

```
Forma Correta  
  
oSection:BeginQuery()  
 BEGINSQL ALIAS cTable  
 SELECT B1_FILIAL, B1_COD, B1_DESC, B1_TIPO, B1_UM  
 FROM %TABLE:SB1% SB1  
 WHERE SB1.%NOTDEL%  
 ENDSQL  
  
 MakeSQLExpr("PRODUCTS") // Pergunta com o parâmetro do Tipo Range  
 oSection:EndQuery({MV_PAR01})
```
