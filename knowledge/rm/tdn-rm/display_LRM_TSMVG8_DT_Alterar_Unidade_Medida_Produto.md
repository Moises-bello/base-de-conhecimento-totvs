---
content_hash: d34296a592de7c9cd9d425f28b9f8d86a7c2f6fc3b5469cdf2de5eb75ac04bc6
fetched_at: '2026-06-29T00:06:04.239667+00:00'
page_id: '200907619'
product: rm
source: tdn-rm
title: TSMVG8_DT_Alterar_Unidade_Medida_Produto
type: documentation
url: https://tdn.totvs.com/display/LRM/TSMVG8_DT_Alterar_Unidade_Medida_Produto
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque Compras e Faturamento |
| **Função:** | Cadastro de Produtos |
| **Situação/Requisito:** | Após criar um produto sem saldo, criar um movimento 1.2.XX com este produto, posteriormente alterar a unidade de medida do produto para base diferente. Após, editar o movimento ocorre erro:  "Ocorreu um erro ao efetuar a leitura do registro:  Conversão não permitida: a unidade de origem UN e a de destino KG possuem unidade base diferente." |
| **Solução/Implementação:** | Ajuste no cadastro do produto para não permitir alterar a unidade de medida caso exista qualquer tipo de movimentação com o produto alterado. |
| **Conversores e Parâmetros:** | *Não se aplica* |
| **Chamados relacionados:** | *Não se aplica* |
| **Requisito (ISSUE):** | Não se aplica |
| **Versões/Release:** | *11.82.41* |
