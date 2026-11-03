---
content_hash: 0dcdb89b60a64a73691cc2a818015ab749791045769ee17a463c6380d2690ec7
fetched_at: '2026-06-29T00:06:11.975735+00:00'
page_id: '204966818'
product: rm
source: tdn-rm
title: TTEA43_DT_ERRO_Impressao_Bematech_Autor_Incorreto
type: documentation
url: https://tdn.totvs.com/display/LRM/TTEA43_DT_ERRO_Impressao_Bematech_Autor_Incorreto
version: 2
---

# IMPRESSÃO BEMATECH

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Bibliotecária* |
| **Função:** | *Impressão Bematech* |
| **Situação/Requisito:** | *Ao ser impresso os recibos de empréstimo padrão Bematech, devolução, multa todos estão trazendo o autor cadastrado incorreto para o exemplar.*  *Ele está usando o segundo autor mesmo o primeiro sendo autor principal.* |
| **Solução/Implementação:** | *Foi realizado o ajuste da consulta responsável por retornar o autor. O registro do autor que é retornado agora é considerado de acordo com o campo Ordem de Cadastro.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.8* |
