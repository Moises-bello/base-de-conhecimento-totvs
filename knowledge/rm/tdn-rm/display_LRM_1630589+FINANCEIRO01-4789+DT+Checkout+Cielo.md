---
content_hash: a4d05eea3326bf77c84378f92b588bc98246b008efd148e1567ffa3e97a78cdc
fetched_at: '2026-06-29T00:08:50.043423+00:00'
page_id: '331858825'
product: rm
source: tdn-rm
title: 1630589 FINANCEIRO01-4789 DT Checkout Cielo
type: documentation
url: https://tdn.totvs.com/display/LRM/1630589+FINANCEIRO01-4789+DT+Checkout+Cielo
version: 1
---

# PAGAMENTO COM CARTÃO DE CREDITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Pagamento com cartão de crédito |
| **Situação/Requisito:** | Ao realizar o pagamento via cartão de crédito, sistema insere uma linha no histórico de transação (FINTEGRACAOCARTAO) com status de Pagamento confirmado, mas com valor incorreto. O valor da baixa é 30,00, por exemplo, e o valor pago está como 3000,00. Neste momento o boleto não é baixado e se realizar o processo de ajuste de transação, além do valor não ser corrigido o sistema baixa o lançamento com o valor errado. |
| **Solução/Implementação:** | Otimizado o processo de baixa de pagamento com cartão de crédito para consistir corretamento a transação do checkout cielo. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
