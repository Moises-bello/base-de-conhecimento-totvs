---
content_hash: 72523bf233f424785c24a40ba2c327cecee85039477891cd833707974848f7bd
fetched_at: '2026-06-29T00:08:27.493683+00:00'
page_id: '271413436'
product: rm
source: tdn-rm
title: 444488 MEDU-2413 DT Pesquisa Publica Um Ou Mais Erros
type: documentation
url: https://tdn.totvs.com/display/LRM/444488+MEDU-2413+DT+Pesquisa+Publica+Um+Ou+Mais+Erros
version: 108
---

# PESQUISA PÚBLICA - PORTAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Pesquisa pública - portal* |
| **Situação/Requisito:** | *Foi identificado que na pesquisa pública do portal está ocorrendo um erro intermitente informando "um ou mais erros" quando é feita uma pesquisa ao acervo.* |
| **Solução/Implementação:** | **Foi identificado que o erro ocorre por uma inconsistência nos acessos a base de dados pelo processamento paralelo da pesquisa, erro causado pela concorrência de acesso a dados, sendo assim foi feito um ajuste na função de pesquisa para que faça um alinhamento da pesquisa sem utilizar o processamento paralelo porém sem degradar o tempo de pesquisa, sendo assim, foi feito o ajuste para correção do problema e o desempenho da pesquisa não foi alterado, mesmo para pesquisas que retornem muitos títulos.** |
| **Conversores e Parâmetros:** | *N/A* |
| **Tickets relacionados:** | *N/A* |
| **Requisito (informe o requisito relacionado):** | *N/A* |

divs
