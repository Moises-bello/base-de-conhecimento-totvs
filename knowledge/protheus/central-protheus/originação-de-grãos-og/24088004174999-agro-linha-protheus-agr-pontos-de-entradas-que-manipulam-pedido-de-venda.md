---
article_id: 24088004174999
category: Originação de Grãos (OG)
content_hash: 3ec2a0f9cc3112571ab7d24d80a058b37a712c424ed25ab02b034d6d82c5b892
fetched_at: '2026-06-28T22:45:36.888471+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR -  Pontos de Entradas que manipulam pedido de venda
type: support-article
updated_at: '2026-02-27T17:50:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24088004174999-Agro-Linha-Protheus-AGR-Pontos-de-Entradas-que-manipulam-pedido-de-venda
---

|  |  |
| --- | --- |
| **Linha de Produto:** | Protheus |
| **Segmento:** | Agroindústria |
| **Módulo:** | SIGAAGR |

**Ponto de Entrada.**

| **Descrição:** | Permitir intervir na confirmação do romaneio(com e sem pesagem). |
| **Localização:** | Antes de confirmação do romaneio. |
| **Programa Fonte:** | OGA250 |
| **Parâmetros:** | | Nome | Tipo | Descrição | Obrigatório | | --- | --- | --- | --- | | PARAMIXB[1] | Caracter | Filial do romaneio | Sim | | PARAMIXB[2] | Caracter | Código do romaneio | Sim | |
| **Retorno:** | | Nome | Tipo | Descrição | Obrigatório | | --- | --- | --- | --- | | lRet | Lógico | Valida a continuação do processo de confirmação. | Sim | |
| **Observação:** | Não se aplica. |

**Exemplo: XGFECALF**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15 | `#include``'protheus.ch'`  `#include``'parmtype.ch'`    `user``function` `OG250NFVD()`  `Local cFilPed   := PARAMIXB[``1``]`  `Local cNumRom   := PARAMIXB[``2``]`  `Local lRet      := .F.`    `DbSelectArea( "NJJ" )`  `DbSetOrder(``1` `)`  `If` `NJJ->( DbSeek( cFilPed + cNumRom ) )`  `alert("Romaneio barrado pelo PE: " + cNumRom )`  `endIf`    `Return lRet` |
