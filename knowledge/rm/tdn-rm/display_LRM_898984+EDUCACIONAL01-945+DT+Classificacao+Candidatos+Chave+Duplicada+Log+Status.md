---
content_hash: 013bdc2f19529dccba763e1a0ab87f8914a3cd20a61077ea7014226a898b2775
fetched_at: '2026-06-29T00:08:34.887621+00:00'
page_id: '274850738'
product: rm
source: tdn-rm
title: 898984 EDUCACIONAL01-945 DT Classificacao Candidatos Chave Duplicada Log Status
type: documentation
url: https://tdn.totvs.com/display/LRM/898984+EDUCACIONAL01-945+DT+Classificacao+Candidatos+Chave+Duplicada+Log+Status
version: 96
---

# CLASSIFICAÇÃO DE CANDIDATOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Processo Seletivo* |
| **Função:** | *Classificação de candidatos* |
| **Situação/Requisito:** | *Quando o processo de classificação de candidatos utiliza fórmula de classificação ou desempate e esta fórmula chama alguma função de alteração de status do candidato, se o ambiente onde o processo está sendo executado possui alto desempenho e está configurado para gerar log de alteração de status, pode eventualmente acontecer um problema de chave duplicada ao salvar o log, pois uns dos campos que compõem a chave é a data e como o processamento pode ser muito rápido a data pode ser igual.* |
| **Solução/Implementação:** | **Foi feito um ajuste incluindo um campo sequencial para compor a chave da tabela, assim evitando qualquer eventual problema relacionado a chave duplicada pela situação descrita.** |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
