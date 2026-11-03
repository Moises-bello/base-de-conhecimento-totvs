---
content_hash: f40b363e7a756e86d8613f438b5bf0132cb32adbabd0dd981da47c94dcbbac9d
fetched_at: '2026-06-29T00:05:48.088239+00:00'
page_id: '1022391668'
product: rm
source: tdn-rm
title: DT - Isenção do Imposto de Renda para quem ganha até 5.000,00 e redução gradual
  até 7.350,00 - LEI 15.270/2025
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1022391668
version: 11
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Cálculo do IRRF |
| País: | Brasil |
| Issue : | [DRHCALCRM-10589](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-10589) |

## **02.** **VERSÓES**

12.1.2502.251

12.1.2506.209

12.1.2510.137

12.1.2602 e superiores

## **03.****SITUAÇÃO/REQUISITO**

O governo sancionou a [Lei nº 15.270, de 26 de novembro de 2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15270.htm), que amplia a faixa de isenção do Imposto de Renda Pessoa Física para contribuintes com renda mensal de até R$ 5.000,00, além de estabelecer novas faixas de descontos para rendimentos de até R$ 7.350,00, com vigência a partir de janeiro de 2026.

Essa mudança impacta diretamente o cálculo do IRRF, exigindo adequações nas regras de tributação, faixas, limites e deduções aplicadas pelo TOTVS Folha de Pagamento.

Dica:

Veja também - [Orientações Consultoria de Segmentos - Novo Cálculo do IRRF](https://tdn.totvs.com/pages/releaseview.action?pageId=1019343450)

## **04.****SOLUÇÃO**

 Implementação para o cálculo da folha para atender a [Lei nº 15.270, de 26 de novembro de 2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15270.htm), que altera o cálculo do IRRF sobre salários.

Regras:

* Para rendimentos tributáveis até R$ 5.000,00 mensais, o IRRF deve resultar em **zero**.

* Para rendimentos entre R$ 5.000,01 e R$ 7.350,00 mensais, deve ser aplicado o redutor conforme a fórmula legal (redução decrescente linear), até zerar para quem atinge R$ 7.350,00

* Para rendimentos superiores a R$ 7.350,00 mensais, o cálculo deve seguir a tabela progressiva normal, sem redução extra.

* A redução não pode exceder o valor do imposto calculado pela tabela progressiva mensal.

A formula da redução deverá ser aplicada na base de tributação de IRRF sem as deduções legais: **978,62 - (0,133145 x rendimentos tributáveis)**

## **05. ASSUNTOS RELACIONADOS**

* [Como calcular a Isenção do Imposto de Renda para quem ganha até 5.000,00 e redução gradual até 7.350,00 - LEI 15.270/2025](https://tdn.totvs.com.br/pages/viewpage.action?pageId=1021212238)
