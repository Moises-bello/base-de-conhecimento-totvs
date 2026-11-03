---
content_hash: 63c51a6f24d8b1d1d997fe90f3ef0aecff497405d16c6b58dfa273c3532455d5
fetched_at: '2026-06-29T00:10:59.846034+00:00'
page_id: '616764301'
product: rm
source: tdn-rm
title: FISCAL01-15275 - DT ECF - Exclusão de Registro - Registro Y671 e Registro Y69
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=616764301
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
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15275 |

## **02. SITUAÇÃO/REQUISITO**

Alterar a geração da ECF para que os registros abaixo não sejam gerados a partir do layout de 2021

**Registro Y671** - Outras Informações

**Registro Y690** - Informações de Optantes pelo Paes

## **03. SOLUÇÃO**

Foi inserido um novo filtro no layout da ECF para que os registro Y671 e Y690 não sejam gerados caso a versão informada na parametrização da geração seja superior a 0006
