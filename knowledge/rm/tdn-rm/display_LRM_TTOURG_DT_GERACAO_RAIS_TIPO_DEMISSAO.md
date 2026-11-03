---
content_hash: b38effbaaa91ec700131707c26776b5e6c8dde28da19373a03d06b394cb2fb8f
fetched_at: '2026-06-29T00:06:29.548681+00:00'
page_id: '234611791'
product: rm
source: tdn-rm
title: TTOURG_DT_GERACAO_RAIS_TIPO_DEMISSAO
type: documentation
url: https://tdn.totvs.com/display/LRM/TTOURG_DT_GERACAO_RAIS_TIPO_DEMISSAO
version: 121
---

# GERAÇÃO RAIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Geração Rais* |
| **Situação/Requisito:** | Email de avisos automáticos de subordinados não são agrupados corretamente. |
| **Solução/Implementação:** | 1 - Foram realizados ajustes em forma de envio por e-mail 1.1 - Quando utilizada forma de envio agrupado por funcionários, os mesmos receberão os e-mails cada um segundo a programação que se refere. 1.1.1 - Quando utilizada forma de envio agrupado por funcionários, com a opção de envio para chefe, a rotina realizará o envio conforme item 1.1 e também realizará agrupamento por chefes, onde cada chefe receberá um único e-mail contemplando somente seus funcionários agrupados nesse. 1.1.2 - Quando utilizada forma de envio agrupado por funcionários, com as opções de envio para chefes e também para supervisores, a rotina realizará o envio conforme itens 1.1 e 1.1.1 e também realizará agrupamento por supervisores de suas equipes. 1.2 - Quando utilizada forma de agrupamento por supervisores, a rotina realizará envio conforme item 1.1.2 sem incluir os funcionários e chefes 1.2.1 - Quando utilizada forma de agrupamento por supervisores, com a opção de envio para chefes, a rotina realizará envio conforme item 1.1.2 sem incluir os funcionários. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTOURG TTOVIF |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.10* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
