---
content_hash: 745f299b028088af744be055fcc43cf6a4bc91568d20706f4dc54b7dc0ab4335
fetched_at: '2026-06-29T00:08:38.301835+00:00'
page_id: '285647393'
product: rm
source: tdn-rm
title: 1097933 EDUCACIONAL01-1729 Nummeracao Falha Visualizar Atribuir Ultimo Numero
type: documentation
url: https://tdn.totvs.com/display/LRM/1097933+EDUCACIONAL01-1729+Nummeracao+Falha+Visualizar+Atribuir+Ultimo+Numero
version: 101
---

# NUMERAÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | *****Educacional***** |
| **Módulo:** | T*****otvs Educacional***** |
| **Função:** | Alterar situação de matrícula |
| **Situação/Requisito:** | Ao acessar o item "Numeração", ao avançar o processo e selecionar o item "Atribuir último número de diário a novo aluno" e clicar em "visualizar" o sistema emite um erro não tratado. |
| **Solução/Implementação:** | Foi identificado que no momento que o sistema monta a consulta sql para carregar a visualização, não é carregado corretamente todos os parâmetros da consulta, assim gerando o erro, foi feito o ajuste na construção da consulta e assim passou a carregar corretamente a visualização. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
