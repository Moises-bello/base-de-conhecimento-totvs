---
content_hash: ab96b44e911901757afbf71ffd1ffd85b1abc695f4d560fbb36e8b09d98d2fdd
fetched_at: '2026-06-29T00:10:53.124213+00:00'
page_id: '577187500'
product: rm
source: tdn-rm
title: FISCAL01-14407 DT Período de Apuração - Encerrar período ICMS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=577187500
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Período de Apuração |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14407 |

## **02. SITUAÇÃO/REQUISITO**

Ao encerrar o Período de Apuração do ICMS ocorre a seguinte mensagem:

Erro: A coluna 'CODCOLIGADA, IDPER, CODETD' está restrita a conter valores exclusivos. O valor '1, 21461, RJ' já existe.

## **03. SOLUÇÃO**

Foi ajustada a consulta realizada durante o processo de Escrituração Fiscal, a fim de obter a parametrização do Cliente Fornecedor no exato momento em que o Movimento foi criado.
