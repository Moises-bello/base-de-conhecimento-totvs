---
content_hash: 03b47b3db96fbf90bdd19c1b10727ba6144e8578e31f557575022f6e8c7160b9
fetched_at: '2026-06-29T00:06:02.471285+00:00'
page_id: '198945148'
product: rm
source: tdn-rm
title: TSYFXC_DT_TCC_Banca
type: documentation
url: https://tdn.totvs.com/display/LRM/TSYFXC_DT_TCC_Banca
version: 1
---

# CONTROLE DE TCC, MONOGRAFIA E TESE

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Função:** | *Banca do TCC* |
| **Situação/Requisito:** | *Após incluir participante na banca, ir no portal e pedir para expandir o registro da banca criada, o sistema exibe a seguinte mensagem de erro: Subquery returned more than 1 value. This is not permitted when the subquery follows =, !=, <, <=, >, >= or when the subquery is used as an expression.* |
| **Solução/Implementação:** | *Ajuste na consulta que traz os participantes da banca, considerando a coligada, pois a mesma continha um erro que não considerava a coligada para trazer o nome do participante.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.7* |
