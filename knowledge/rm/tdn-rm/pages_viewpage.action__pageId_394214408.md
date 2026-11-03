---
content_hash: b6dd7166a51e1aecfa8a7b8a831d648587301f009d3fa4d7ce70750ebe26cbcd
fetched_at: '2026-06-29T00:09:09.892888+00:00'
page_id: '394214408'
product: rm
source: tdn-rm
title: 1351878 FOPCALCULO01-4414 Criação de Código de Cálculo 378 - Adiantamento de
  Abono Pecuniário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=394214408
version: 2
---

# Adiantamento Abono Pecuniário

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Lançamento de Férias |
| **Situação/Requisito:** | As informações referentes aos descontos de adiantamento de férias não são descriminadas em dois eventos, lançando o valor do 'Desconto de adiantamento de Férias' e 'Desconto de abono pecuniário de férias' em um único evento: CC 43 - Adiantamento conforme recibo.  De acordo com a resposta da consultoria tributária, o sistema deveria separar os valores para que pudesse então utilizar as duas rubricas abaixo, conforme o manual de orientação do eSocial (MOS), visto que é possível associar apenas uma rubrica por evento:  9221 - Desconto de férias  9226 - Desconto de férias abono |
| **Solução/Implementação:** | Criado um parâmetro 'Lança adiantamento de abono separado dos valores de férias' em Configurações | Parametrizador | Folha de Pagamento | Férias que, quando marcado, irá lançar o adiantamento de férias conforme recibo separando o liquido de férias no mês do liquido de abono pecuniário.  Para que o lançamento seja feito separado, foi criado o código de cálculo 378 - Adiantamento de Abono pecuniário. |
| **Tickets relacionados:** | 1351878 |
| **Documento de Referência:** | <http://wikihelp.totvs.com.br/WikiHelp/FOP/FopControleFerias.aspx>  <http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.AdiantamentoAbonoPecuniario.aspx> |
