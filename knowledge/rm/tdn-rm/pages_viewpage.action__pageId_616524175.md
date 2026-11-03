---
content_hash: fb21181b9768149bdbd0d1a95285b781f80c7766783602f1a2ab54b29baf60b0
fetched_at: '2026-06-29T00:10:59.823572+00:00'
page_id: '616524175'
product: rm
source: tdn-rm
title: FISCAL01-15272 - DT ECF - Exclusão de Registro - Registro Y550
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=616524175
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | ECF Layout 007 |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15272 |

## **02. SITUAÇÃO/REQUISITO**

Alterar a geração da ECF para que o registro Y550 não seja gerados a partir do layout de 2021

## **03. SOLUÇÃO**

Foi inserido um novo filtro no layout da ECF para que o registro Y550 não seja gerado caso a versão informada na parametrização da geração seja superior a 0006
