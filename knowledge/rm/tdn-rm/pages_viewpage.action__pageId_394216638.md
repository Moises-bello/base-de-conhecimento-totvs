---
content_hash: c6b71f8d90022e0808bdc9b87feae6c28525b4b1b1dfe41f2468c83383af056d
fetched_at: '2026-06-29T00:09:09.921858+00:00'
page_id: '394216638'
product: rm
source: tdn-rm
title: DSAUGCIH-279 DT Filtros dos BI's não se mantém os mesmos ao mudar o período
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=394216638
version: 1
---

# DT Filtros dos BI's não se mantém os mesmos ao mudar o período

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Controle de Infecção Hospitalar |
| **Função:** | BI's |
| **Situação:** | Ao realizar a montagem de um BI e filtrar alguma das dimensões, quando mudamos o período pesquisado, o sistema não mantém os filtros que foram selecionados exibindo informações diferentes das selecionadas. |
| **Solução:** | Ajuste realizado no preenchimento do pivot grid para que quando o mesmo já estiver filtrado e o dataset seja atualizado com novas informações, o componente não altere o filtro conforme o padrão do componente para esta situação. |
