---
content_hash: 14c2981eb7f2b440a85c12d53807397fcd7cb4298ae0d28fef395390cc851ca7
fetched_at: '2026-06-29T00:08:27.175027+00:00'
page_id: '271395539'
product: rm
source: tdn-rm
title: 273847 MEDU-1577 DT Resultado Classificacao Geral Portal Injecao SQL
type: documentation
url: https://tdn.totvs.com/display/LRM/273847+MEDU-1577+DT+Resultado+Classificacao+Geral+Portal+Injecao+SQL
version: 111
---

# PORTAL - RESULTADOS - CLASSIFICAÇÃO GERAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Portal - Resultados - Classificação geral* |
| **Situação/Requisito:** | *Foi identificado um possível ponto de injeção de comando sql. Ao acessar a divulgação de resultados e selecionar a opção por área é possível interceptar e alterar o requisição POST da lookup, assim gerando um erro que retorna toda a estrutura da tabela, facilitando uma possível exploração de dados.* |
| **Solução/Implementação:** | *Foi feito uma alteração para tratar exceções da lookup de área de interesse para que identifique de onde veio a requisição, se for web (portal) não será retornado a mensagem original gerada pela exceção, será exibido um texto informando o erro mas sem exibir os detalhes da tabela relacionada, porém para a aplicação desktop não foi feita nenhuma alteração.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Tickets relacionados:** | *N/A* |
| **Requisito (informe o requisito relacionado):** | *N/A* |

divs
