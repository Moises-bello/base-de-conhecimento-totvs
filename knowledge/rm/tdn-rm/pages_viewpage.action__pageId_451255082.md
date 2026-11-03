---
content_hash: c8cbfe3b723c39fdc6eab77db87eb1bdeffd53bbe0264a2c63bda6c53b1d5d52
fetched_at: '2026-06-29T00:09:58.117085+00:00'
page_id: '451255082'
product: rm
source: tdn-rm
title: 4765728 FINANCEIRO01-10656 Pagamento de cartão de credito via portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=451255082
version: 1
---

# **BAIXA DE LANÇAMENTO**

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Baixa de Lançamento |
| **Situação/Requisito:** | No processo de pagamento de cartão de credito via portal, ocorreu a duplicidade de pagamento gerado dois itens de baixa. Isto ocorre quando a Cielo envia duas transações para o mesmo pagamento, ou seja, no ambiente da Cielo possui apena um pedido porém no sistema é gerado duas transações para o mesmo pedido. |
| **Solução/Implementação:** | Otimizado o controle de concorrência no processo de baixa de lançamento. E criado uma tag de segurança no cadastro de perfil para permitir o cancelamento de baixa de transação de cartão de crédito do Checkout Cielo. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A |
| **Documento de Referência:** | N/A. |
| **Pacote:** | N/A. |
