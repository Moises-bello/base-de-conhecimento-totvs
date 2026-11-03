---
content_hash: 14e03cac55ad5517e9c4519334cf2351d49ac3681fcd4283700aa770fa6a346e
fetched_at: '2026-06-29T00:08:32.629026+00:00'
page_id: '273993619'
product: rm
source: tdn-rm
title: 766999 CONTROLADORIA01-124 DT Geração de Fato Contábil na ECD
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273993619
version: 104
---

# Geração de Fato Contábil na ECD

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Geração de Fato Contábil na ECD |
| **Situação/Requisito:** | Ao validar o arquivo do sped ECD e gerar o relatório balanço patrimonial no PVA da RCB o saldo das contas de ativo são preenchidos com Parênteses(credora), assim está incorreto pois a natureza das contas de ativo são "Devedoras" (Sem parênteses).  Ao validar o arquivo do sped ECD onde foi utilizada a ferramenta de demonstração contábil de balanço patrimonial o registro o campo 4 do registro J100 está sendo preenchido com 2 para as contas de ativo, onde o correto seria 1. Ver regra de validação:  04 IND\_GRP\_BAL  Indicador de grupo do balanço:  1 – Ativo;  2 – Passivo e Patrimônio Líquido; |
| **Solução/Implementação:** | O problema ocorre pois os fatos que representam o grupo do Ativo no balanço foram cadastrados com "01" no lugar de "1" e isto fez com que a geração do arquivo ficasse incorreta.  Desta forma foi feito ajuste para que o processo consiga identificar o grupo Ativo e Passivo desde que os mesmos comecem com 1 e 2 respectivamente ou ainda comecem com (01, 001, 0001,...) ou (02, 002, 0002,...). |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados**: | [770178](https://totvssuporte.zendesk.com/agent/tickets/770178 "Open ticket in Zendesk Support") |
| **Requisito (informe o requisito relacionado):** | N/A |

divs
