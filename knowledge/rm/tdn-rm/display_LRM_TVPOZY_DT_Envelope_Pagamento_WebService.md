---
content_hash: 0b7268bbcd6972dac5af8b8aa6925a616c9df479ad711a5425ffbe4c4cc1af32
fetched_at: '2026-06-29T00:08:17.267800+00:00'
page_id: '255755202'
product: rm
source: tdn-rm
title: TVPOZY_DT_Envelope_Pagamento_WebService
type: documentation
url: https://tdn.totvs.com/display/LRM/TVPOZY_DT_Envelope_Pagamento_WebService
version: 120
---

# ENVELOPE DE PAGAMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Envelope de Pagamento - WebService* |
| **Situação/Requisito:** | Ao tentar inserir eventos no envelope de pagamento do funcionário utilizando o dataserver FopEnvelopeData quando não existe o período criado é apresentada a mensagem de erro abaixo:  Violação de concorrência: UpdateCommand afetou 0 dos registros 1 esperados. |
| **Solução/Implementação:** | *Ajustado DataServer FopEnvelopeData para que seja possível incluir um período (PFPERFF) pelo WebService.* |
| **Chamados relacionados:** | *TVPOZY* |

divs
