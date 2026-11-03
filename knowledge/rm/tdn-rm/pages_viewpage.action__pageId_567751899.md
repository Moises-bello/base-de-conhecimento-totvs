---
content_hash: e9e3a3f530cd474212e7599fb057ff3391a5a8020ba571abeaa99dad951769ba
fetched_at: '2026-06-29T00:10:51.415430+00:00'
page_id: '567751899'
product: rm
source: tdn-rm
title: 9206740 FISCAL01-13996 DT Período de Apuração - Encerrar Período ICMS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=567751899
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Período de Apuração |
| Ticket: | 9206740 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-13996 |

## **02. SITUAÇÃO/REQUISITO**

Cliente entrou em contato pois ao encerrar o período de apuração do tributo ICMS é apresentado a inconsistência abaixo. Erro: A coluna 'CODCOLIGADA, IDPER, CODETD' está restrita a conter valores exclusivos. O valor '1, 21461, RJ' já existe.

## **03. SOLUÇÃO**

Foram ajustados os parâmetros e também a consulta para que ela retorne a UF correta. O processo de Escrituração Fiscal busca na tabela o histórico do CliFor a última alteração que seja anterior à data de criação do Movimento atual, a fim de obter a parametrização do Cliente Fornecedor no exato momento em que o Movimento foi criado.
