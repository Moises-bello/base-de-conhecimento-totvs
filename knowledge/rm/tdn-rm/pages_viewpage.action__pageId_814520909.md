---
content_hash: 10ede61efe121da04ffce3b59bbe3f51e105963c9b54938504982f37d99f1954
fetched_at: '2026-06-29T00:11:44.306229+00:00'
page_id: '814520909'
product: rm
source: tdn-rm
title: FISCAL01-21175 - DT - Encerramento do Período PIS COFINS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=814520909
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Período de Apuração PIS COFINS |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-21175 |

## **02. SITUAÇÃO/REQUISITO**

Alterar o processo de Encerramento do Período de Apuração para os tributos PIS e COFINS para que o Evento tributário (Delphi) seja considerado no cálculo.  
O Evento não pode ser obrigatório, ou seja, se existir ele deve ser utilizado, senão, nenhum erro deve ser apresentado ao usuário.

## **03. SOLUÇÃO**

Foi alterado o processo de Encerramento do Período de Apuração quando houver eventos tributários cadastrados no Delphi no devido período.

Disponível a partir da biblioteca 12.1.2302
