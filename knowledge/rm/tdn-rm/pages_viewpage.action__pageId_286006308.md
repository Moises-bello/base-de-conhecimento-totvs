---
content_hash: 2d1711f40c82b95d4696f688946a287c4a2a6ff05844ebc1e33a7fa7edc6fa18
fetched_at: '2026-06-29T00:08:39.049096+00:00'
page_id: '286006308'
product: rm
source: tdn-rm
title: FINANCEIRO01-1476 Conversão para nova baixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286006308
version: 103
---

# Conversão para nova baixa

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção & Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Cancelamento de Remessa (visão de lançamento) |
| **Situação/Requisito:** | Ao executar a etapa 4 do conversor, que diz respeito a conversão de lançamentos para o novo modelo de baixa, me deparei com um erro que me impede de prosseguir com a conversão.  "Erro ao migrar Venda 6535 (Fechada) - Lançamento 1-123040: SqlDateTime overflow. Must be between 1/1/1753 12:00:00 AM and 12/31/9999 11:59:59 PM" |
| **Solução/Implementação:** | Ajuste no conversor para nova baixa dos lançamentos do TIN: - tratamento dos registro de log sessão de caixa - tratamento dos lançamentos sem data da baixa |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FIN000306 |

divs
