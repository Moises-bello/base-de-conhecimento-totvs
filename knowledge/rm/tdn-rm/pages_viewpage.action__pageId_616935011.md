---
content_hash: 3234d11b39a90b6eafbedb122f2d84177ad5a7ca91f068ca3fa832f8da3b319c
fetched_at: '2026-06-29T00:11:02.380137+00:00'
page_id: '616935011'
product: rm
source: tdn-rm
title: FISCAL01-15273 - DT ECF - Exclusão de Registro - Registro Y560
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=616935011
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | ECF Layout 0007 |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15273 |

## **02. SITUAÇÃO/REQUISITO**

Alterar a geração da ECF para que o registro Y560 não seja gerados a partir do layout de 2021

## **03. SOLUÇÃO**

Foi inserido um novo filtro no layout da ECF para que o registro Y560 não seja gerado caso a versão informada na parametrização da geração seja superior a 0006
