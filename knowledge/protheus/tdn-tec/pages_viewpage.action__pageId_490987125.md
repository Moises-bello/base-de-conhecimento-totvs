---
content_hash: 7d86b348f2babf5cd553a678aae6bf54201ec17dc4ea52d723fffd37bee7d2c6
fetched_at: '2026-07-02T19:24:24.921573+00:00'
page_id: '490987125'
product: protheus
source: tdn-tec
title: Correção - Método TTree:SetColsAlign() faz o SmartClient fechar inesperadamente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=490987125
version: 1
---

A chamada do método não ocasiona mais o fechamento do SmartClient.

|  |  |
| --- | --- |
| Situação | SmartClient fecha inesperadamente ao chamar o método TTree:SetColsAlign(). |
| Ocorrência | O problema acontece por causa do garbage collector tentar excluir as informações da memória da troca de mensagens, tentando apagar as informações de alinhamento que ainda estão em uso. |
| Correção | As informações de alinhamento são guardadas e usadas de outra forma pra garantir que o garbage collector possa limpar as mensagens passadas. |
| Informações adicionais | * Referente à ocorrência: MTEC-2504 * Disponível em builds superiores a 17.3.0.8 |
