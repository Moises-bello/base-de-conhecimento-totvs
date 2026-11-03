---
content_hash: bbbe2ea08779be833b896a1b8ce52cd13552eeffd6ed083d71f425ef759bbdfa
fetched_at: '2026-06-29T00:08:53.258762+00:00'
page_id: '344465042'
product: rm
source: tdn-rm
title: 2410464 EDUCACIONAL01-4300 Frequência diária digitação aulas dadas com fórmula
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=344465042
version: 90
---

# DIGITAR NÚMERO DE AULAS DADAS NA FREQUÊNCIA DIÁRIA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Frequência diária* |
| **Situação/Requisito:** | Ao digitar número de aulas dadas na frequência diária, o sistema não estava gravando o valor retornado pela fórmula de falta. |
| **Solução/Implementação:** | Na “Digitação de frequência diária”, ao preencher o campo “Número de aulas dadas”, o sistema deverá dar prioridade ao valor retornado por fórmula, caso exista.  Por exemplo, ao utilizar a fórmula GRAVACAMPOETAPA(1,'AULASDADAS',3), será gravado o Valor 3 na tabela SNOTAETAPA independente do que o usuário digitar na tela. |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
