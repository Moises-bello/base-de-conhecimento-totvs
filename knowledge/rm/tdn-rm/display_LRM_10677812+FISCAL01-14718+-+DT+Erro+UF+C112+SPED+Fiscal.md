---
content_hash: 7f18355d3d55618ff03e1bfc896bf93fc0810594fd285f937b2de1be81832374
fetched_at: '2026-06-29T00:10:56.678671+00:00'
page_id: '592292685'
product: rm
source: tdn-rm
title: 10677812 FISCAL01-14718 - DT Erro UF C112 SPED Fiscal
type: documentation
url: https://tdn.totvs.com/display/LRM/10677812+FISCAL01-14718+-+DT+Erro+UF+C112+SPED+Fiscal
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | SPED Fiscal |
| País: | Brasil |
| Ticket: | 10677812 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14718 |

## **02. SITUAÇÃO/REQUISITO**

Registro C112 do SPED Fiscal, que deve ser apresentado, obrigatoriamente, quando no campo "Informações Complementares" da Nota Fiscal constar a identificação de um documento de arrecadação, mas ao gerar o campo 3 referente a UF da guia esta sendo apresentado a UF da filial e não a UF apresentada na guia.

## **03. SOLUÇÃO**

Ajustado para que na geração do SPED Fiscal o sistema leve no Registro C112 a UF da Guia conforme orientado no Layout:

03 - UF - Unidade federada beneficiária do recolhimento.
