---
content_hash: 06fcca8b6df319f5d23e72d61b87c53dbf0411cf5854c708f56ce0babc463b9d
fetched_at: '2026-06-29T00:08:32.734896+00:00'
page_id: '273999698'
product: rm
source: tdn-rm
title: 612898 EDUCACIONAL01-59 DT Consulta ao acervo lentidao
type: documentation
url: https://tdn.totvs.com/display/LRM/612898+EDUCACIONAL01-59+DT+Consulta+ao+acervo+lentidao
version: 107
---

# CONSULTA AO ACERVO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Consulta ao acervo* |
| **Situação/Requisito:** | *No TOTVS Gestão Bibliotecária foi identificado que eventualmente algumas pesquisar ao acervo apresentam lentidão.* |
| **Solução/Implementação:** | *Foi feito uma análise da base de dados do cliente e teste das consultas e aparentemente são executadas corretamente, porém foi feito a revisão de algumas consultas pela equipe de bando de dados, ocorreram algumas alterações nas estruturas das junções além da alteração do "distinct" para "group by". Além de todas as modificações foi retirado o "replace" das consultas, evitando assim mais um processamento, sendo que o "replace" só será executado nas consultas caso o termo pesquisado possua "C" ou "Ç", assim reduzindo sua utilização. O termo de "número do tombo" agora só aceitará valores numéricos, se informar alguma letra por exemplo o sistema não executa a busca, foi mantido o uso do "like" para este campo pois o usuário pode buscar parte do "número do tombo", não necessariamente o número exato.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Tickets relacionados:** | *N/A* |
| **Requisito (informe o requisito relacionado):** | *N/A* |

divs
