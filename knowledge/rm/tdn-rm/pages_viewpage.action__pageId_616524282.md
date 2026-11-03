---
content_hash: 530dc64301eec6527237d6b6bce6548d6da4e2a34e9a8b85de6969307b8ae252
fetched_at: '2026-06-29T00:10:59.826945+00:00'
page_id: '616524282'
product: rm
source: tdn-rm
title: FISCAL01-15271 - DT ECF - Exclusão de Registro - Registro Y540
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=616524282
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
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15271 |

## **02. SITUAÇÃO/REQUISITO**

Alterar a geração da ECF para que o registro Y540 não seja gerados a partir do layout de 2021

## **03. SOLUÇÃO**

Foi inserido um novo filtro no layout da ECF para que o registro Y540 não seja gerado caso a versão informada na parametrização da geração seja superior a 0006
