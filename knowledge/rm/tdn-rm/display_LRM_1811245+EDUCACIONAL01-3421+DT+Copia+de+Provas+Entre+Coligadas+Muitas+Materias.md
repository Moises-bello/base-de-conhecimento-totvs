---
content_hash: 167799fa71c145c67cd9c5d7210faf2112c4ab111a5c7321bccd8db315a0f4b1
fetched_at: '2026-06-29T00:08:47.668801+00:00'
page_id: '319790397'
product: rm
source: tdn-rm
title: 1811245 EDUCACIONAL01-3421 DT Copia de Provas Entre Coligadas Muitas Materias
type: documentation
url: https://tdn.totvs.com/display/LRM/1811245+EDUCACIONAL01-3421+DT+Copia+de+Provas+Entre+Coligadas+Muitas+Materias
version: 96
---

# CÓPIA DE PROVAS ENTRE COLIGADAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Cópia de provas entre coligadas* |
| **Situação/Requisito:** | *Foi identificado um erro ao copiar uma prova entre coligada, o sistema retorna um erro informando que excedeu o número máximo (2100) de parâmetros na consulta sql, neste caso o grande número de matérias que causada a falha.* |
| **Solução/Implementação:** | **Foi feito um ajuste na função para que se identificado que os dados da consulta podem exceder o limite de parâmetros o sistema irá quebrar os parâmetros e executar a consulta mais vezes com menos parâmetros.** |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
