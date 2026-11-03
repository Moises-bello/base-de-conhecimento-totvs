---
content_hash: 363cce0fe91a184a8128ec36a23af029aa18fcb5120d0d4745522094270d49be
fetched_at: '2026-06-29T00:08:51.561719+00:00'
page_id: '337349281'
product: rm
source: tdn-rm
title: 2178860 FINANCEIRO01-5293 DT Integração Bancária - Retorno de Cobrança
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=337349281
version: 1
---

# Integração Bancária - Retorno de Cobrança

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projeto |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Integração Bancária - Retorno de Cobrança |
| **Situação/Requisito:** | Erro ao importar arquivo de retorno: "Não é possível realizar a operação '=' em System.String e System.Int32" |
| **Solução/Implementação:** | Otimização no retorno de cobrança ao buscar o lançamento por numero do documento e o nosso numero. A alteração foi adicionar os aspas simples na condição do select. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | 2237222; 2240123; 2240123 |
| **Requisito:** | FIN000169 |
| **Documento de Referência:** | N/A |
