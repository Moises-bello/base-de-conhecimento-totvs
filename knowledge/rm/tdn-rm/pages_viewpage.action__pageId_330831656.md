---
content_hash: a312b40a80989f2ef62e11bbc5ed884eb33fccbb55bea274b50907671b1bebb8
fetched_at: '2026-06-29T00:08:49.447886+00:00'
page_id: '330831656'
product: rm
source: tdn-rm
title: 1087138 MATFATCMPCRM01-794 DT Função de Fórmula Maiúscula e Minuscula.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=330831656
version: 2
---

# Função de Fórmula Maiúscula e Minuscula

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Função de Fórmula |
| **Situação/Requisito:** | O usuário estava com dificuldades de comparar os valores informado no movimento no campo CODUSUARIOAPROVADESC, pois o mesmo poderia ser informado em maiúsculo e a comparação na fórmula estar minusculo. |
| **Solução/Implementação:** | Criadas para o usuário as funções de fórmulas MAIUSCULA e MINUSCULA para utilização de acordo com a regra da fórmula.    Exemplo:    SE **MAIUSCULO**(USUARIOCORRENTE) = 'MESTRE' ENTAO 1  SENAO 0  FIMSE  SE **MINUSCULO**(USUARIOCORRENTE) = 'mestre' ENTAO 1  SENAO 0  FIMSE |
| **Conversores e Parâmetros:** | Desnecessário |
| **Tickets relacionados:** | 1087138 |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
