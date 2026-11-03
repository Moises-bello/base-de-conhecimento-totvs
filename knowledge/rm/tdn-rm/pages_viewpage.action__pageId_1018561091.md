---
content_hash: dad7b8ac6b6dd915e9ee2ce3854784a8a43fb49c9ff2112004f488830eba36a4
fetched_at: '2026-06-29T00:05:47.808101+00:00'
page_id: '1018561091'
product: rm
source: tdn-rm
title: FISCAL01-27551 - NFSe Nacional - Alterar geração do xml
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1018561091
version: 1
---

## **01. DADOS GERAIS**

| Produto: | TOTVS |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | Envio de NFSe |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-27551 |

## **02. SITUAÇÃO/REQUISITO**

De acordo com o manual a regra de geração da IM é:

Se o emitente for o prestador de serviço (tpEmit = 1) e, se não houver registro complementar do contribuinte no CNC do município correspondente ao município emissor da DPS, então o IM não deve ser informado na DPS.

## **03. SOLUÇÃO**

Criado um novo parâmetro nos dados fiscais da filial para informar se a filial possui o Cadastro Nacional de Contribuinte.

Alterada a regra de geração do campo IM do prestador da NFSe nacional para que somente seja gerado se o parâmetro estiver marcado na filial.
