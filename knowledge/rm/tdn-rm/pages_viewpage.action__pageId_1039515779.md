---
content_hash: 9e79950b5a6679806671070ee5a8f890bfa4b43a00d76882caea5b442c11d499
fetched_at: '2026-06-29T00:05:49.323233+00:00'
page_id: '1039515779'
product: rm
source: tdn-rm
title: DT - Função de Fórmula TR2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1039515779
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Cadastro de Fórmulas |
| País: | Brasil |
| Ticket: | [#25987330](https://totvssuporte.zendesk.com/agent/tickets/25987330) |
| Issue: | [DRHCALCRM-11393](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-11393) |

## **02. VERSÕES**

A partir dos patches:

* + 12.1.2502.277
  + 12.1.2506.242
  + 12.1.2510.166
  + 12.1.2602 e superiores

## **03. SITUAÇÃO/REQUISITO**

A função TR utiliza como rendimento tributável o valor que é passado como parâmetro. Pra ter valor diferente entre rendimento tributável e a base já com o valor dedutível, provavelmente teremos que criar uma nova TR.

## **03. SOLUÇÃO**

Foi criada de uma nova função de formula com o nome de TR2, semelhante a TR que retorna o valor do IRRF, mas com a opção de passar o valor dedutível separado da base de cálculo.

Diferença entre a TR e TR2:

* TR recebe apenas um parâmetro tipo decimal, onde deve ser informado o valor da base de IRRF já abatido o valor dedutível.
* TR2 irá receber 2 parâmetros tipo decimal, um com a base de cálculo do IRRF e outro com o valor dedutível separado. Neste caso o valor dedutível não pode ser abatido da base informada no primeiro parâmetro.

## **04.** **ASSUNTOS RELACIONADOS**

* [Função de Fórmula: TR2](https://tdn.totvs.com.br/pages/viewpage.action?pageId=1039514917)
