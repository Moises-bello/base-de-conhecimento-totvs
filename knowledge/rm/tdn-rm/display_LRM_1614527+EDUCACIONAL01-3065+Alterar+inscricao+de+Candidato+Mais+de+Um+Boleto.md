---
content_hash: a9ef45917ebd02d3d1e98b0dcbbe4782e7c0d8379737a3ee569a4b423d917082
fetched_at: '2026-06-29T00:08:45.657125+00:00'
page_id: '312152392'
product: rm
source: tdn-rm
title: 1614527 EDUCACIONAL01-3065 Alterar inscricao de Candidato Mais de Um Boleto
type: documentation
url: https://tdn.totvs.com/display/LRM/1614527+EDUCACIONAL01-3065+Alterar+inscricao+de+Candidato+Mais+de+Um+Boleto
version: 94
---

# INSCRIÇÃO DE CANDIDATOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Processo Seletivo* |
| **Função:** | *Inscrição de candidatos* |
| **Situação/Requisito:** | *Ao editar uma inscrição de um candidato em um processo seletivo o mesmo retorna um erro de chave duplicada.* |
| **Solução/Implementação:** | *Foi identificado que a situação ocorre pois o candidato possui dois boletos para o lançamento, um cancelado e outro em aberto, assim ocorre o erro no momento de carregar os dados e salvar, pois carrega duplicado o registro do candidato assim gerando o erro ao salvar, foi feito um ajuste para que o sistema carregue corretamente somente um registro com o boleto válido, assim evitando o erro.* |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
