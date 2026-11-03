---
content_hash: ced80d222e0b362d7fcae3f2928ebac8e409b0c3aeebe41e8bfa29209193e494
fetched_at: '2026-06-29T00:08:57.768086+00:00'
page_id: '354476272'
product: rm
source: tdn-rm
title: 2663604 RMFIN-1923 DT Erro de Chave Primária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=354476272
version: 1
---

# Erro de Chave Primária

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Recurso de Glosa |
| **Situação/Requisito:** | Ao acessar o menu de recurso de glosa, procurar uma fatura e efetuar um Recurso Total, estava estourando erro d chave primária. |
| **Solução/Implementação:** | Foi realizado um ajuste querys das telas onde carregava os itens de SADT, pois estava triplicando e ao salvar no banco, estourava erro de chave primária. |
