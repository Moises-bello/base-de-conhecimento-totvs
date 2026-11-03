---
content_hash: 871749b8cccb7d9ca2787fc15fdf9749cdeacdd4336b51b6aa3747566a824a23
fetched_at: '2026-06-29T00:08:40.926441+00:00'
page_id: '286517588'
product: rm
source: tdn-rm
title: 1170134 EDUCACIONAL01-2007 DT Consulta Acervo Publicacao Titulo Minusculo
type: documentation
url: https://tdn.totvs.com/display/LRM/1170134+EDUCACIONAL01-2007+DT+Consulta+Acervo+Publicacao+Titulo+Minusculo
version: 105
---

# PESQUISA AO ACERVO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Gestão bibliotecária |
| **Função:** | Pesquisa ao acervo |
| **Situação/Requisito:** | Foi identificado que quando parâmetro "Cadastro em maiúsculo título da publicação" está desmarcado e é cadastrada uma publicação que tenha o "Ç" no título o sistema não busca corretamente ao realizar uma busca ao acervo, não encontra a publicação buscando em minúsculo, somente se a busca for feita em maiúsculo. |
| **Solução/Implementação:** | Foi identificado uma inconsistência nas validações do termo pesquisado para a montagem da consulta sql, foi feito o ajuste e a busca passou a ser feita corretamente. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
