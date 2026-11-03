---
content_hash: 649439b7b917f8ff2d4562b6c0acf33aff8292e69a38aadd5e0c65320595bfd0
fetched_at: '2026-06-29T00:10:32.080694+00:00'
page_id: '525799483'
product: rm
source: tdn-rm
title: 5114445 FISCAL01-8059 DT SPED Fiscal - Gerar Registro E300 para o estado da
  filial mesmo quando não houver valor apurado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=525799483
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | SPED Fiscal |
| Ticket: | 5114445 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-8059 |

## **02. SITUAÇÃO/REQUISITO**

Quando houver venda com Difal, onde o valor do Imposto é 100% devido na UF destino não está sendo gerado a linha do diferencial de alíquota para UF do remetente.

## **03. SOLUÇÃO**

Foi efetuado o ajuste para que seja gerado a linha do Difal na apuração do tributo para UF do remetente quando não houver valores de diferencial de alíquota. Esta alteração foi necessária devido a obrigatoriedade da UF do remetente na geração do E300.
