---
content_hash: 0be37e8ab4f7af39d0228f128e4c9d3dead4dc856419e04a53e7ca2e64392068
fetched_at: '2026-06-29T00:08:53.095286+00:00'
page_id: '342312311'
product: rm
source: tdn-rm
title: 2224595 FINANCEIRO01-5753 DT Baixa de lançamento na integração Protheus x TIN
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=342312311
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Baixa de lançamento na integração Protheus x TIN |
| **Situação/Requisito:** | Ao efetuar uma baixa de lançamentos no Protheus do tipo Dação, ao tentar fazer a baixa no TOTVS Gestão Financeira está ocorrendo erro de "Não foi possível encontrar o ID do Banco." Esse erro ocorre devido a lançamento do protheus não exigir conta caixa e no TOTVS gestão financeira a conta caixa ser obrigatória. |
| **Solução/Implementação:** | Foi feito tratamento para quando um lançamento do Protheus não exigir conta caixa no TOTVS Gestão Financeira será utilizada a conta caixa padrão para compensação "DEFCOMP001". |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | FINANCEIRO01-5753 |
| **Documento de Referência:** | N/A |
