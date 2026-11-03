---
content_hash: 1cd591342451835220521e61cbbe2b2cff446dd64e9fd379eddd486445cdf9c4
fetched_at: '2026-06-29T00:08:48.078067+00:00'
page_id: '322152249'
product: rm
source: tdn-rm
title: 1759719 EDUCACIONAL01-3517 DT Alterar Situacao Matricula Descricao Nova Situacao
type: documentation
url: https://tdn.totvs.com/display/LRM/1759719+EDUCACIONAL01-3517+DT+Alterar+Situacao+Matricula+Descricao+Nova+Situacao
version: 95
---

# ALTERAR SITUAÇÃO DE MATRÍCULA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | *****Educacional***** |
| **Módulo:** | *****Totvs Educacional***** |
| **Função:** | *Alterar situação de matrícula* |
| **Situação/Requisito:** | *Foi identificado que ao abrir a tela do processo alterar situação de matrícula, é exibido um erro informando o tamanho do campo "descrição".* |
| **Solução/Implementação:** | *Foi identificado que esta situação ocorre quando a descrição da situação de matrícula tem descrição repetida e está no limite do tamanho do campo, assim ao exibir o campo na tela o sistema concatena a descrição com o código da descrição, assim excedendo o limite do campo. Foi feito um ajuste para aumentar o tamanho do campo e assim evitar exceder o limite do campo na concatenação da descrição com o código.* |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
