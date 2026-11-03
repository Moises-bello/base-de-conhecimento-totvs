---
article_id: 360056075593
category: BI - Business- Intelligence - Workflow
content_hash: cf8d286417558ea71362e58ab8797934d96beb7456a0f0a45483762f1d2b96f1
fetched_at: '2026-06-28T22:37:03.032096+00:00'
product: protheus
section_id: 1500001550762
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Erro Workflow "Tabela
  SXM.dtc"
type: support-article
updated_at: '2023-05-10T17:59:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056075593-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Erro-Workflow-Tabela-SXM-dtc
---

**Ocorrência**Após migração do Dicionário para Banco de dados, o Workflow está gerando o seguinte erro:   
  
**THREAD ERROR ([27972], HTTP:GENPROC, THIS) 14/09/2020 14:44:46**  
**d:\totvs\microsiga\protheus\_data\system\sxm010.dtc: Ctree error - Open - It was not possible to Check Internal Struct of File: d:\totvs\microsiga\protheus\_data\system\sxm010.dtc on TBITABLE:LOPEN(TBITABLE.PRW) 02/06/2017 09:46:05 line : 153****Ambiente**Protheus - WF - Até a versão 12.1.23  
  
**Causa**A tabela SXM ainda não foi migrada para o banco de dados, sendo necessária a utilização do ctree para funcionamento do Workflow.   
  
**Solução**

Ajustado na release 12.1.33, migrado utilização para o banco de dados.
