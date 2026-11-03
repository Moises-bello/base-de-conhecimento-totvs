---
content_hash: 0b91ae6ef67b98d26227820f59a5d11a722cc1c80897af9c0383da900c5120e6
fetched_at: '2026-06-29T00:08:27.156532+00:00'
page_id: '271391902'
product: rm
source: tdn-rm
title: MRH-5982 DT Restituicao INSS Ferias Lancado Indevidamente
type: documentation
url: https://tdn.totvs.com/display/LRM/MRH-5982+DT+Restituicao+INSS+Ferias+Lancado+Indevidamente
version: 110
---

# RESTITUIÇÃO DE INSS DE FÉRIAS SENDO LANÇADO INDEVIDAMENTE

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projeto* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Folha Mensal* |
| **Situação/Requisito:** | *Lançamento de restituição de INSS de Férias indevido em envelope vazio.  Em um envelope de pagamento com lançamento de férias no mês.  Criado novo período e somente recalcula o envelope sem incluir nenhum evento.  Está lançando evento de restituição de INSS.* |
| **Solução/Implementação:** | *Ajuste para não considerar INSS de férias já descontado quando o envelope não tiver base de INSS.* |
| **Chamados relacionados:** | MRH-5982 |
| **Requisito (ISSUE):** | MRH-5982 |

divs
