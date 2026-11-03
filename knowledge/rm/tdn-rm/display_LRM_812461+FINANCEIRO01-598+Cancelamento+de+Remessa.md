---
content_hash: fca1980dd64618a12d07ce8ee7130d13cdccb1654c31de858409b1e36287a718
fetched_at: '2026-06-29T00:08:38.396745+00:00'
page_id: '285651687'
product: rm
source: tdn-rm
title: 812461 FINANCEIRO01-598 Cancelamento de Remessa
type: documentation
url: https://tdn.totvs.com/display/LRM/812461+FINANCEIRO01-598+Cancelamento+de+Remessa
version: 102
---

# Lançamento - Cancelamento de Remessa

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção & Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Cancelamento de Remessa (visão de lançamento) |
| **Situação/Requisito:** | Ao utilizar a opção "cancelamento de remessa" que fica no menu "Processos" da visão de lançamentos financeiros, o sistema altera o STATUS CNAB do lançamento para Não Remetido, mas não altera o Status da Remessa do boleto. Ressalto que para "borderôs" o sistema adequadamente informa que o cancelamento deve ser feito pela própria visão de borderôs. |
| **Solução/Implementação:** | Ajuste na validação para os lançamentos a receber do processo de "Cancelamento de Remessa" da visão de lançamentos, onde para os mesmos deve ser feito pela visão de boletos. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000306 |

divs
