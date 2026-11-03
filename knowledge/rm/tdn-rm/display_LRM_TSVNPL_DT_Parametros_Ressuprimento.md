---
content_hash: 59cccac1d961b1a1fe3b1a4dca1292c0427679c9e82cc2663e7ccc976b60b743
fetched_at: '2026-06-29T00:06:02.623879+00:00'
page_id: '198948042'
product: rm
source: tdn-rm
title: TSVNPL_DT_Parametros_Ressuprimento
type: documentation
url: https://tdn.totvs.com/display/LRM/TSVNPL_DT_Parametros_Ressuprimento
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Função:** | Parametrização do Ressuprimento |
| **Situação/Requisito:** | Ao iniciar o processo o ressuprimento, ao final ocorre a mensagem de erro "Ocorreu um erro ao efetuar a leitura dos parâmetros. Favor verificar os parâmetros gerais do módulo de ressuprimento." e o processo não é concluído. |
| **Solução/Implementação:** | Ao acrescentar uma nova filial ou local de estoque, não é incluído automaticamente um registro na tabela de parâmetros de Ressuprimento, causando problemas para o usuário que deseja utilizar os parâmetros. Então foi realizado uma alteração para incluir o parâmetro caso o mesmo não exista. |
| **Conversores e Parâmetros:** | NA |
| **Chamados relacionados:** | NA |
| **Requisito (ISSUE):** | NA |
| **Versões/Release:** | 12.1.7 |
