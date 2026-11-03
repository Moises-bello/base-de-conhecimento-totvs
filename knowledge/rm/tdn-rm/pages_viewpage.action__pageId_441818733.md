---
content_hash: 03f1a65b3ec95f40df4bbbb37419a6bd3e9998ef6cdc58b3bd42a353b811d763
fetched_at: '2026-06-29T00:09:53.759366+00:00'
page_id: '441818733'
product: rm
source: tdn-rm
title: 4186596 MATESTCNTFTOF01-3934 Lote Movimentado no Registro de Produção
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=441818733
version: 2
---

# ENTRADA DE PRODUÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Planejamento e Controle da Produção. |
| **Função:** | Dar entrada de produtos no Estoque da ordem selecionada. |
| **Situação/Requisito:** | Ao executar o processo de Entrada de Produção de um Produto Acabado controlado por lote, a tabela de lotes movimentados não está sendo atualizada. |
| **Solução/Implementação:** | Foi identificado que a base do cliente utiliza a parametrização de Gera Número de Lote Sequencial (Parâmetros Gestão de Estoque, Compras e Faturamentos \ Parâmetros Gerais \ Tabelas  \ Produtos \ Lote). Com esta configuração o número do lote é gerado pelo serviço de inclusão de movimento no momento da entrada em estoque. Sendo assim, quando o produto acabado for controlado por lote e a base estiver configurada para gerar número de lote sequencial, será recuperado o número do lote criado para o item do movimento de entrada. |
| **Conversores e Parâmetros:** | Informe os conversores/parâmetros. |
| **Tickets relacionados:** | 4186596 |
| **Requisito:** | Entrada de Produção. |
| **Pacote:** | Baixar na central de downloads o RMFactor.exe 12.1.21.2 |
