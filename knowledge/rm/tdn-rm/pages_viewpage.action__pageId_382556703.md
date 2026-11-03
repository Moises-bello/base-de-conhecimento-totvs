---
content_hash: 953fffef5d67e2f274318133b7974ae458a54ad37c32632963f7115641ce68bc
fetched_at: '2026-06-29T00:09:04.163863+00:00'
page_id: '382556703'
product: rm
source: tdn-rm
title: 2187117 DSAUGHCOM-98 DT Processo de exames de laboratório e resultados on-line
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=382556703
version: 1
---

# Processo de exames de laboratório e resultados on-line

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Controle de Pedido de Exames |
| **Situação/Requisito:** | Processo de exames de laboratório e resultados on-line com problemas na versão 12.1.18.  Ao realizar diversas vezes a liberação de resultados o executável do RM Saúde vai aumentando a memória, chegando ao ponto que fecha sozinho. |
| **Solução/Implementação:** | Criada uma função chamada MemoryClear, responsável por limpar a memória após o uso da liberação de resultados, também foi ajustado para o cliente utilizar o relatório .Net (Resultado de Exame Laboratorial). Alguns trechos de código que impactam na rotina também foram refatorados para ter os objetos responsáveis pela liberação. |
| **Tickets relacionados:** | [Ticket #2187117](https://totvssuporte.zendesk.com/agent/tickets/2187117 "Open ticket in Zendesk Support") |
