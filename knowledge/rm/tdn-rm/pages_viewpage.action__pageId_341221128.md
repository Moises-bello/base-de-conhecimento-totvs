---
content_hash: 3be5e5f5935ef1a2a2ace79eeb1e4a16a04154f1740171a81595146152cdcdcc
fetched_at: '2026-06-29T00:08:52.570862+00:00'
page_id: '341221128'
product: rm
source: tdn-rm
title: 1870314 FINANCEIRO01-4461 DT Baixa de lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=341221128
version: 2
---

# Baixa de Lançamentos

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Baixa de Lançamentos |
| **Situação/Requisito:** | Ao baixar um lançamento financeiro informando o Meio de Pagamento Cartão de Crédito e com mais de uma parcela, usuário desabilita a opção Compensar Extrato e ao concluir operação, sistema gera os respectivos itens de baixa e os extratos de caixa. No entanto, apenas o primeiro extrato gerado fica como Não Compensado. Os demais extratos gerados são automaticamente compensados, mesmo o usuário desabilitando esta opção ao informar o Meio de Pagamento. |
| **Solução/Implementação:** | Ajustado processo de baixa, onde, ao selecionar forma de pagamento Cartão de Crédito, caso houver parcelamento o comportamento definido para compensar ou não o extrato seja igual em todas as parcelas. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | 1870314 |
| **Requisito:** | FIN000040. |
| **Documento de Referência:** | N/A. |
