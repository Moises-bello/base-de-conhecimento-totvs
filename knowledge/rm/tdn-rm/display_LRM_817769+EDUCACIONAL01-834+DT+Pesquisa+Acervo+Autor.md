---
content_hash: c715cff1762a95bf790b45cd8293ec9b214ecea286011b87296e74e5733626c6
fetched_at: '2026-06-29T00:08:34.934533+00:00'
page_id: '274854337'
product: rm
source: tdn-rm
title: 817769 EDUCACIONAL01-834 DT Pesquisa Acervo Autor
type: documentation
url: https://tdn.totvs.com/display/LRM/817769+EDUCACIONAL01-834+DT+Pesquisa+Acervo+Autor
version: 104
---

# PESQUISA ACERVO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Pesquisa acervo* |
| **Situação/Requisito:** | *Foi identificado que ao utilizar a consulta ao acervo para determinado autor, o sistema retorna um erro não tratado.* |
| **Solução/Implementação:** | *Foi identificado que a situação ocorre pois existem duas publicações com o mesmo nome, mesmo autor, porém somente uma publicação possui exemplar, a segunda não possui, assim, na busca o sistema retorna estes as duas publicações, porém uma delas não tem exemplar o que faz que o código da filial e unidade fiquem nulos para a publicação que não possui exemplar, gerando o erro no momento de organizar os resultados pela filial unidade, foi feito o ajuste na consulta SQL para que não retorne publicações sem exemplares.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Tickets relacionados:** | *N/A* |
| **Requisito (informe o requisito relacionado):** | *N/A* |

divs
