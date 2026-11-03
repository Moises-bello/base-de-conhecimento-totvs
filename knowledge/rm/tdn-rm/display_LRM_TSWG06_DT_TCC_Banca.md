---
content_hash: d3a4abcc4a9a2897b941981e1343970969bf59131a1a1e1a9eac05afb814f494
fetched_at: '2026-06-29T00:06:02.164127+00:00'
page_id: '198944061'
product: rm
source: tdn-rm
title: TSWG06_DT_TCC_Banca
type: documentation
url: https://tdn.totvs.com/display/LRM/TSWG06_DT_TCC_Banca
version: 3
---

# CONTROLE DE TCC, MONOGRAFIA E TESE

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Função:** | *Banca do TCC* |
| **Situação/Requisito:** | *Após incluir participante na banca, ir no portal e pedir para expandir o registro da banca criada, o sistema exibe a seguinte mensagem de erro: Subquery returned more than 1 value. This is not permitted when the subquery follows =, !=, <, <=, >, >= or when the subquery is used as an expression.* |
| **Solução/Implementação:** | *Ajuste na consulta que traz os participantes da banca considerando a coligada, pois a mesma não estava efetuando esta consideração ao trazer os participantes. ra trazer o nome do participante.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.83.55.169* |
