---
content_hash: 40c22ef465d3001fb6ea464453c21d57a9aa43768ca7e8b81443f680bc1678df
fetched_at: '2026-06-29T00:09:11.482475+00:00'
page_id: '405701561'
product: rm
source: tdn-rm
title: 1463030 FOPCALCULO01-4446 Lançamento FGTS Financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=405701561
version: 1
---

# Lançamento Financeiro

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Lançamento Financeiro |
| **Situação/Requisito:** | Ao demitir funcionário por justa causa e no envelope do funcionário consta mais descontos do que provento ficando com a base de INSS e FGTS negativa, o sistema ao lançar o valor do FGTS para o financeiro está levando R$0,01 para o funcionário quando o lançamento é gerado para toda a filial.  Quando é feito o lançamento para apenas dois colaboradores o sistema leva a base de FGTS zerada e não com o valor de R$0,01. |
| **Solução/Implementação:** | Corrigindo problema com distribuição do lançamento financeiro de Recolhimento de FGTS para não adicionar 0,01 quando a base for negativa. |
| **Tickets relacionados:** | 1463030 |
