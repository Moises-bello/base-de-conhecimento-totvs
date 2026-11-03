---
content_hash: 02f72ba002d07f77dbd3608b621d105fa95f7a9a8e47a81ad9979d9ba5c536ae
fetched_at: '2026-06-29T00:06:27.224371+00:00'
page_id: '232423453'
product: rm
source: tdn-rm
title: TTXLXM_DT_Sefip
type: documentation
url: https://tdn.totvs.com/display/LRM/TTXLXM_DT_Sefip
version: 115
---

# SEFIP

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *SEFIP* |
| **Situação/Requisito:** | Cliente informa que ao gerar a "Guia de INSS de Folha" o campo Deduções está com valores dos eventos '0017 SALARIO MATERNIDAD'E + '0931 DIF DE 13º SAL LICENCA MATERNIDADE', mas após simular o Sefip também da Folha de Dezembro o relatório "Analítico GPS" carrega somente o valor do evento 0017 SALARIO MATERNIDADE para o campo de Deduções  Ou seja, na Guia de INSS de Folha do Labore a Dedução vai CC17 + CC323. E na Sefip de folha dentro do Analítico GPS a Dedução leva somente o valor do CC17 |
| **Solução/Implementação:** | Otimizado SEFIP, incluída regra para tratar os casos onde a funcionária possui valor de diferença de 13° de licença maternidade (CC 323) no mês de dezembro e não está demitida. Caso possua, este valor não pode ser deduzido no SEFIP devido o SEFIP não validar o arquivo pois apenas funcionárias demitidas ou SEFIP 13  podem ter esse valor informado. O cliente deverá utilizar a GPS do produto para realizar a dedução  Nesses casos o produto informará o cliente pelo log de execução |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTXLXM TUIZV7 |
| **Requisito (ISSUE):** |  |

divs
