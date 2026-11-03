---
content_hash: 5ee521317d254af319028f768aad4a202589a18a8a41341b6ac1afdcd77f07ca
fetched_at: '2026-06-29T00:08:53.389342+00:00'
page_id: '344473139'
product: rm
source: tdn-rm
title: 2178324 FINANCEIRO01-5195 Retorno de Cobrança não Registrada não respeita parâmetro
  por Número de Documento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=344473139
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão Financeira |
| **Função:** | Retorno de Cobrança não Registrada |
| **Situação/Requisito:** | Ao importar o arquivo de retorno de cobrança (para um título não registrado), o sistema está validando indevidamente o número do documento do lançamento ao invés do nosso número mesmo que a flag nos parâmetros com esta finalidade esteja desmarcada. |
| **Solução/Implementação:** | A validação do número do documento passa a respeitar a parametrização. |
| **Conversores e Parâmetros:** | Não se aplica |
| **Tickets relacionados:** | 2178324 |
| **Requisito:** | FIN000172 |
