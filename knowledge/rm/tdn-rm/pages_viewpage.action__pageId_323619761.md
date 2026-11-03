---
content_hash: 0eb1f31822bea4265c2b8b759bf39be80f555ac3f1bb5e5720ba153027fcc72e
fetched_at: '2026-06-29T00:08:48.103173+00:00'
page_id: '323619761'
product: rm
source: tdn-rm
title: 1303879 FINANCEIRO01-2650 DT Baixa de lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=323619761
version: 2
---

# Baixa de lançamentos

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Baixa de Lançamentos |
| **Situação/Requisito:** | Baixa de lançamentos com boleto e sem boletos ao mesmo tempo apresenta mensagem de inconsistência, quando o sistema está com o parâmetro "Não interromper o processo de baixa, caso algum lançamento apresente inconsistência na baixa.  Mensagem:  "Não foi possível concluir o processo de baixa para o(s) lançamento(s) [XXXX].  Não foi informada uma referência de boleto válida para o(s) lançamento(s) a ser(em) baixado(s)." |
| **Solução/Implementação:** | Ajustado processo de baixa para poder baixar os lançamentos sem boleto sem apresentar a mensagem descrita acima, quando parametrizado conforme descrito na Situação/Requisito. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | 1303879 |
| **Requisito:** | FIN000040. |
| **Documento de Referência:** | N/A. |
