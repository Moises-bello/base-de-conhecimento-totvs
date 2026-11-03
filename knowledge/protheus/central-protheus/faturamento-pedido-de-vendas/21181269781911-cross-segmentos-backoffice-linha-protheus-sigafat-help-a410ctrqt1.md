---
article_id: 21181269781911
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 2a93ebb5e5d9ab18e6fd7da0cfa7a4b6c23a176dd7cf6f72242b488f95df001e
fetched_at: '2026-06-28T22:38:42.503895+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Help "A410CTRQT1"
type: support-article
updated_at: '2024-02-07T12:11:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21181269781911-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Help-A410CTRQT1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21181269760919) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como solucionar o Help "A410CTRQT1"?

**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**Esse help ocorre quando pedido de venda é gerado pelo o contrato de parceria existe e quando o campo  "Pedido Cobrança (ADB\_PEDCOB)" do contrato está vazio e o campo "TES Cobrança (ADB\_TESCOB)" preenchido.

A validação do help é gerado quando é alterado:

* Uma quantidade "Quantidade (C6\_QTDVEN)" diferente do contrato de parceria "Quantidade (ADB\_QUANT)"
* A TES "Tipo Saida (C6\_TES)" diferente do contrato de parceria "TES Cobrança (ADB\_TESCOB)".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21181269761175)

Para resolver help, basta não alterar ou ajustar, para que a quantidade no pedido de venda seja igual a quantidade no contrato de parceria e a TES cobrança seja a mesma na hora de fazer o pedido de venda com o primeiro vínculo com o contrato de parceria.
