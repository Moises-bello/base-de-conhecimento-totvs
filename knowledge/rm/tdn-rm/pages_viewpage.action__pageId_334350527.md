---
content_hash: 6bae92f2df6ab13e6ad82ca833c265e8889cf4593435694badf6b5083bc94549
fetched_at: '2026-06-29T00:08:50.960814+00:00'
page_id: '334350527'
product: rm
source: tdn-rm
title: 906639 MATESTCNTFTOF01-1279 DT Excluir Fornecedor Cotação Web
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=334350527
version: 3
---

# EXCLUIR FORNECEDOR COTAÇÃO WEB

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Excluir Fornecedor da Cotação. |
| **Situação/Requisito:** | Ao excluir um fornecedor da cotação que foi exportada para web o sistema não exclui os registros das tabelas de Orçamento WEB, Item de Orçamento WEB e Grupo de orçamento WEB. Como os dados das tabelas de Orçamento e Item de Orçamento foram excluídos, ao executar o processo de Importação de Cotação Web é apresentada mensagem de violação de chave estrangeira. |
| **Solução/Implementação:** | Ao excluir o Fornecedor da Cotação a sua referência nas tabelas Orçamento WEB, Item de Orçamento WEB e Grupo de orçamento WEB também serão excluídos.  **Observação:** após aplicar opatch que contém o ajuste, para corrigir a cotação que possui este tipo de inconsistência, será necessário incluir o fornecedor novamente na cotação e realizar a exclusão para que as tabelas da web seja apagadas. |
| **Conversores e Parâmetros:** | Desnecessário. |
| **Tickets relacionados:** | 1104847, 1386040. |
| **Requisito:** | CmpCotacaoAction, CmpImportacaoCotacaoWebAction. |
| **Documento de Referência:** | [http://wikihelp.totvs.com.br/WikiHelp/EST/EST.Cotação.aspx](http://wikihelp.totvs.com.br/WikiHelp/EST/EST.Cota%C3%A7%C3%A3o.aspx) |
