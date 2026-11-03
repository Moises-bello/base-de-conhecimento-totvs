---
content_hash: 94e868f5e816cac96b87237d857235e7db2c043e6e11b709eda78aa904db6e01
fetched_at: '2026-06-29T00:09:13.614797+00:00'
page_id: '421378420'
product: rm
source: tdn-rm
title: 3870307 FISCAL01-6540 DT Relatórios Fiscais - ISS RJ Modelo 03 - Não Gera Lançamentos
  Cancelados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421378420
version: 1
---

Tempo aproximado para leitura:**02 min**

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Relatórios Fiscais |

## **02. SITUAÇÃO/REQUISITO**

Na geração do relatório Livro ISS RJ modelo 03, as notas canceladas no mesmo período de emissão não estão sendo geradas no arquivo. Segundo o cliente, o relatório é entregue para a Prefeitura após o contador carimbar e gerar a lavratura.

## **03. SOLUÇÃO**

No relatório de ISS do RJ foi ajustado a SQL que carrega os lançamentos fiscais cancelados.
