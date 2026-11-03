---
content_hash: 85b14a3401bf43e918a286e680296318b09bc6c4f0e77f0bc8649159696dc4dd
fetched_at: '2026-06-29T00:09:03.687749+00:00'
page_id: '382538283'
product: rm
source: tdn-rm
title: 2234077 DEDUINTEGRACOES-2669 DT Valor incorreto de baixa para bolsas condicionais
  perdidas
type: documentation
url: https://tdn.totvs.com/display/LRM/2234077+DEDUINTEGRACOES-2669+DT+Valor+incorreto+de+baixa+para+bolsas+condicionais+perdidas
version: 84
---

# BAIXA DE LANÇAMENTOS FINANCEIROS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional. |
| **Função:** | Baixa de bolsas durante a baixa de lançamentos financeiros oriundos do TOTVS Educacional |
| **Situação/Requisito:** | Caso uma bolsa condicional tenha sido perdida durante a baixa de uma lançamento devido a baixa ter ocorrido após o vencimento da bolsa, o serviço de baixa de bolsas baixava a bolsa com seu valor total. |
| **Solução/Implementação:** | Foi realizada otimização do processo de baixa de bolsas, de forma que o sistema somente considere uma bolsa condicional baixada se o sistema estiver parametrizado para utilizar escalonamento de bolsas e o valor opcional da baixa contiver valor ou se o sistema não utilizar escalonamento de bolsas. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A. |

divs
