---
content_hash: 9f8425cd239a23c0ff2bdb272c54d2f76c9b45f845dccf0d9d5cd7c4eedde0c4
fetched_at: '2026-06-29T00:09:55.582528+00:00'
page_id: '448594738'
product: rm
source: tdn-rm
title: 4744499 DEDUINTEGRACOES-4109 DT O sistema permite inserção de data de competência
  final menor que data de competência inicial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=448594738
version: 78
---

# CADASTRO DE CONTRATOS, PLANOS DE PAGAMENTO E MATRÍCULA NO PERÍODO LETIVO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Inclusão / alteração de contratos Inclusão / alteração de planos de pagamento Matrícula no período letivo |
| **Situação/Requisito:** | Sistema permitia a data de competência inicial ser maior do que a data de competência final |
| **Solução/Implementação:** | Inclusão da validação de datas de competências na inclusão ou alteração do contrato, plano de pagamento e matrícula no período letivo. As validações incluídas foram: \* Data de competência inicial informada e data de competência final não informada \* Data de competência final informada e data de competência inicial não informada \* Data de competência inicial maior do que a data de competência final  Foi feita uma alteração no form de matrícula no período letivo a fim de só mostrar a mensagem de alerta de competência não informada caso o usuário não preencha as mesmas e o parâmetro de data contábil está setado para "Contrato e Plano de pagamento". Anteriormente, o alerta era sempre exibido ao entrar na aba de datas de competências. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
