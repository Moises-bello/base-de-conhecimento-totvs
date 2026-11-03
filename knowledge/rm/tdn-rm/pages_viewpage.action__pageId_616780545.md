---
content_hash: 459039a119be3fd0f72effd1ae7a1f262d57b45558217f89d7a1dba641b329cd
fetched_at: '2026-06-29T00:10:59.864881+00:00'
page_id: '616780545'
product: rm
source: tdn-rm
title: FISCAL01-15276 - DT ECF - Exclusão de Campo - Registro 0010
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=616780545
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
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15276 |

## **02. SITUAÇÃO/REQUISITO**

Alterar a geração da ECF 2021 para que o campo abaixo não seja gerado a partir de 2021

**Registro 0010:** Parâmetros de Tributação: Exclusão de campo e inclusão de regra.

Campo 04 - OPT\_PAES

## **03. SOLUÇÃO**

Foi inserido um novo filtro no layout da ECF para que o campo 04 - OPT\_PAES do registro 0010, não seja gerado, caso a versão informada na parametrização da geração seja superior a 0006
