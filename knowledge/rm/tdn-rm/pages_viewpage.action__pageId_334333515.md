---
content_hash: ff840447b368111cefd503e2b461e14bdf0a868b8fabf693eb0e5baa734ef8dd
fetched_at: '2026-06-29T00:08:50.278127+00:00'
page_id: '334333515'
product: rm
source: tdn-rm
title: 1995296 DEDUINTEGRACOES-1457 DT Bolsa Retroativa Não Atualizando Conta Corrente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=334333515
version: 1
---

# Bolsa Retroativa

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Getão Educacional |
| **Função:** | Bolsa Retroativa |
| **Situação/Requisito:** | Foi concedida bolsa retroativa. O sistema concedeu a bolsa sem erros, mas não aplicou a bolsa na parcela que estava baixada com conta corrente.  O correto é conceder a bolsa e devolver o valor pago pelo aluno na conta corrente. |
| **Solução/Implementação:** | Ajuste no processo de bolsa retroativa, pois nos casos de inclusão de uma bolsa retroativa em um lançamento baixado com valor igual a zero, o sistema não estava lançando o crédito da bolsa do aluno na conta corrente. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** |  |
| **Requisito:** |  |
| **Documento de Referência:** |  |
