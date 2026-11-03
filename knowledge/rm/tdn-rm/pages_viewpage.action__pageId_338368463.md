---
content_hash: c85f9707db37419c000a4dc49b42fe1f73b7e08a40f8a4c4e6b37fb16fa07990
fetched_at: '2026-06-29T00:08:51.907956+00:00'
page_id: '338368463'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-1660 DT Gravar valores de cada vencimento para emissão dos
  boletos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=338368463
version: 90
---

# GERAÇÃO DE LANÇAMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional. |
| **Função:** | Geração de lançamentos |
| **Situação/Requisito:** | Ao gerar um lançamento financeiro, é necessário que todos os descontos por antecipação calculados no momento da geração, sejam gravados no banco de dados. Dessa forma, o desconto considerado (maior desconto) deve possuir um flag para o distinguir dos demais. |
| **Solução/Implementação:** | Foi realizada otimização do processo de geração de lançamentos, permitindo ao sistema, registrar todos os itens de desconto por antecipação aplicáveis a um determinando lançamento financeiro. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A. |

divs
