---
content_hash: c4d3c45cf81b4f0e01e31ea9769bf9c28c07a9518faa38b7e16a535102e69dd0
fetched_at: '2026-06-29T00:06:21.080061+00:00'
page_id: '223159985'
product: rm
source: tdn-rm
title: TTVH44_DT_Lancamento_Financeiro_Por_Formula
type: documentation
url: https://tdn.totvs.com/display/LRM/TTVH44_DT_Lancamento_Financeiro_Por_Formula
version: 1
---

# LANÇAMENTO FINANCEIRO CALCULADO POR FÓRMULA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Lançamento Financeiro* |
| **Situação/Requisito:** | *Lançamento Financeiro calculado por fórmula, utilizando a variável L, está saindo com valor duplicado.* |
| **Solução/Implementação:** | *Ajuste na função de fórmula L, quando chamada de uma fórmula no processo de Lançamento Financeiro, para não carregar o mesmo envelope duas vezes.* |
| **Chamados   relacionados:** | *TTVH44* |
| **Versões/Release:** | *12.1.9* |
