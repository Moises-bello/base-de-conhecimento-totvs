---
content_hash: 991578743638a548e1ee6f7b324dc7b33ab4004d44bbacd31cffd654b4089f58
fetched_at: '2026-06-29T00:10:41.878432+00:00'
page_id: '546674439'
product: rm
source: tdn-rm
title: 8652982 FISCAL01-12823 DT EFD Contribuições Registro 1011 x 0200
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546674439
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Geração de Arquivo EFD Contribuições |
| Ticket: | 8652982 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-12823 |

## **02. SITUAÇÃO/REQUISITO**

O cliente ao tentar gerar o registro 1011 do Sped EFD Contribuições, ocorrem os seguinte erro:  
O campo 5 é gerado código do item, porém não é relacionado ao campo 02 do registro 0200, o que ocasiona erro no validador

## **03. SOLUÇÃO**

Na EFD Contribuições quando for gerado registro 1011, será gerado o registro 0200 em todas as filiais daquele Item.

Esta implementação se faz necessário devido a exigência do Validador EFD Contribuições.
