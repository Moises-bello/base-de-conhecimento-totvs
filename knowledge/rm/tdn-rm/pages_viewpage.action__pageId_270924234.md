---
content_hash: ebacf2f049bf9aaaabac726305d4a1bd608f92641b692b2e9afd5a1d51fa3bf2
fetched_at: '2026-06-29T00:08:25.713533+00:00'
page_id: '270924234'
product: rm
source: tdn-rm
title: 169160 MRH-3286 DT Atestado de Saúde Ocupacional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270924234
version: 110
---

# Atestado de Saúde Ocupacional

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Segurança e Saúde Ocupacional |
| **Função:** | Atestado de Saúde Ocupacional |
| **Situação/Requisito:** | Ao acessar a MDI, ir em Executar, pesquisar por "Atestado de Saúde Ocupacional" o menu é encontrado. Mas ao clicar nele ocorre mensagem que "Para executar este processo é necessário selecionar somente um registro. |
| **Solução/Implementação:** | Realizado ajuste para que o "Atestado de Saúde Ocupacional" (SmtASOAction) não seja listado no menu Executar. Esta action não pode ser aberta pelo menu executar porque ela depende do contexto da consulta para ser executada. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** | 169160 |
| **Requisito (informe o requisito relacionado):** |  |

divs
