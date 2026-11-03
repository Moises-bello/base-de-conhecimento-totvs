---
content_hash: 965f30eea759b0a54c5166b85ad972825f5397fca9f6a33deab75c04426beaf2
fetched_at: '2026-06-29T00:06:05.309434+00:00'
page_id: '200913794'
product: rm
source: tdn-rm
title: TTATJ3_DT_Alterar_Unidade_Medida_Produto
type: documentation
url: https://tdn.totvs.com/display/LRM/TTATJ3_DT_Alterar_Unidade_Medida_Produto
version: 3
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque Compras e Faturamento |
| **Função:** | Cadastro de Produtos |
| **Situação/Requisito:** | Após criar um produto sem saldo, criar um movimento 1.2.XX com este produto, posteriormente alterar a unidade de medida do produto para base diferente. Após, editar o movimento ocorre a inconsistência:  "Ocorreu um erro ao efetuar a leitura do registro:  Conversão não permitida: a unidade de origem UN e a de destino KG possuem unidade base diferente." |
| **Solução/Implementação:** | Ajuste no cadastro do produto para não permitir alterar a unidade de medida caso exista qualquer tipo de movimentação com o produto alterado. |
| **Conversores e Parâmetros:** | *Não se aplica* |
| **Chamados relacionados:** | *Não se aplica* |
| **Requisito (ISSUE):** | Não se aplica |
| **Versões/Release:** | *12.1.7* |
