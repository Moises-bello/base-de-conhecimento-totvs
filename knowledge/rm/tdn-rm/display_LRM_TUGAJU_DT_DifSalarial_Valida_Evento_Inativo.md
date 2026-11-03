---
content_hash: 86ecf5b33b3098484d8131420075591c8db602e2598f74845e8a5cb50ec1adc5
fetched_at: '2026-06-29T00:06:27.865355+00:00'
page_id: '233736622'
product: rm
source: tdn-rm
title: TUGAJU_DT_DifSalarial_Valida_Evento_Inativo
type: documentation
url: https://tdn.totvs.com/display/LRM/TUGAJU_DT_DifSalarial_Valida_Evento_Inativo
version: 3
---

# DIFERENÇA SALARIAL ESTÁ CONSIDERANDO EVENTO INATIVO NA VALIDAÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Diferença Salarial* |
| **Situação/Requisito:** | *No processo de Diferença Salarial, ao efetuar a validação de evento único com código de cálculo 37, está considerando também eventos inativos.* |
| **Solução/Implementação:** | *Ajuste no filtro da validação de evento único com código de cálculo 37, do módulo de Diferença Salarial, para desconsiderar os eventos inativos.* |
| **Chamados   relacionados:** | *TUGAJU, TUJVO3* |
| **Versões/Release:** | *11.82.43, 12.1.11* |
