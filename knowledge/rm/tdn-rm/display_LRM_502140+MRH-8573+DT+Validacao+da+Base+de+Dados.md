---
content_hash: 6ec44730c544f000945dd7ee5cf3d3af3135b86c6f192d0459c6977b397861a1
fetched_at: '2026-06-29T00:08:30.305337+00:00'
page_id: '272420985'
product: rm
source: tdn-rm
title: 502140 MRH-8573 DT Validacao da Base de Dados
type: documentation
url: https://tdn.totvs.com/display/LRM/502140+MRH-8573+DT+Validacao+da+Base+de+Dados
version: 110
---

# Validar Eventos da ficha financeira inconsistentes.

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projeto |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Validação da base de Dados. |
| **Situação/Requisito:** | Ao realizar a geração da DIRF o sistema apresentava erro de referência de objeto.   O erro era causado pois o cliente possuía um evento especifico na ficha financeira porém este mesmo evento não existia no cadastro de eventos.   Causando assim o erro ao montar o envelope. |
| **Solução/Implementação:** | Como a mensagem não era clara e não ajudava o suporte a identificar tal erro, foi implementado no processo de validação de base de dados uma mensagem para alertar quando existirem eventos referenciados na ficha financeira que não existirem no cadastro de eventos. |
| **Tickets relacionados:** | * + 502140 |

divs
