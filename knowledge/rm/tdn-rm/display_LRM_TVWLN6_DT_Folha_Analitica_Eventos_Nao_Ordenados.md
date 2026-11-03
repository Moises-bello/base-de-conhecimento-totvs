---
content_hash: fd808e4c9e64c7f399f7014442a2de489f78578d67104bfeb2f8fe5d793c7d7e
fetched_at: '2026-06-29T00:08:19.933367+00:00'
page_id: '267798980'
product: rm
source: tdn-rm
title: TVWLN6_DT_Folha_Analitica_Eventos_Nao_Ordenados
type: documentation
url: https://tdn.totvs.com/display/LRM/TVWLN6_DT_Folha_Analitica_Eventos_Nao_Ordenados
version: 114
---

# FOLHA ANALÍTICA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos.* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Folha Analítica.* |
| **Situação/Requisito:** | Ao realizar a geração da folha analítica em TXT os eventos de provento estão saindo desordenados (Bases misturadas com proventos) e eventos de descontos desordenados (na PDF gera por ordem de código de evento). |
| **Solução/Implementação:** | *Foi ajustado o sistema para poder levar os eventos de proventos ordenados primeiro pelo tipo, desta forma sairão os proventos primeiro depois os eventos de base de cálculo, e dentro desta ordenação, os mesmos serão ordenados também por código.*  *Já os eventos de desconto, todos serão ordenados pelo seu código.* |
| **Chamados relacionados:** | TVWLN6 |

divs
