---
content_hash: 72a0305ab1d3b516e924d92c99b7008b7b33dd16a728de8716c2c18ae70bdab8
fetched_at: '2026-06-29T00:09:00.933404+00:00'
page_id: '370608693'
product: rm
source: tdn-rm
title: 2679881 FINANCEIRO01-7374 DT Retorno de Cobrança não baixa todos os lançamentos
  com código de ocorrência de Baixa.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=370608693
version: 5
---

# 2679881 FINANCEIRO01-7374 DT IMPOSSÍVEL BAIXAR LANÇAMENTOS COM CÓDIGO DE RETORNO 06

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Baixa de Lançamentos |
| **Situação/Requisito:** | Ao executar o retorno bancário com a opção 'Não Baixar' se pagamento a menor, diversos boletos com mais de um lançamento não foram baixados |
| **Solução/Implementação:** | Constatamos erro no rateio do valor baixado, gerando diferenças a menor e a maior. A falha foi corrigida de modo que o rateio seja executado de forma correta. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | .2679881 |
| **Requisito:** | FIN000040 |
| **Documento de Referência:** | N/A |
