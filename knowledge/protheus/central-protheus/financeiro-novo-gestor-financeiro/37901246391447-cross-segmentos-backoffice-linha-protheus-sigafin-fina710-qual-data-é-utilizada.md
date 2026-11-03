---
article_id: 37901246391447
category: Financeiro - Novo Gestor Financeiro
content_hash: 1ab8f0846c9bd6fc35b1826759d577063ecc930fef434870ae7dad51bf09e4fb
fetched_at: '2026-06-28T22:37:41.500287+00:00'
product: protheus
section_id: 33830415324183
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710 - Qual data
  é utilizada para o provisionamento de Pedidos de Compras?
type: support-article
updated_at: '2026-01-26T18:37:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37901246391447-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Qual-data-%C3%A9-utilizada-para-o-provisionamento-de-Pedidos-de-Compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37901246365079) Tempo aproximado para leitura: **00:04 min**  
  
**Dúvida**  
Qual é a data de referência (campo "Data Saldo") utilizada pelo Painel do Gestor Financeiro para o cálculo e exibição do provisionamento (previsão financeira) de Pedidos de Compra?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release  12.1.33.  
  
**Solução**

No Painel do Gestor Financeiro, o conteúdo do campo "data saldo" corresponde à data utilizada para o cálculo do provisionamento (ou previsão financeira) de pedidos de compras, é a **Data de Vencimento Prevista para Pagamentos**.

O Painel do Gestor Financeiro utiliza a data em que o desembolso financeiro é esperado para compor o fluxo de caixa. Essa data é calculada com base nas **Condições de Pagamento** negociadas e inseridas no Pedido de Compra (ex: 30 dias após a emissão, parcelamentos em 30/60/90, etc.).

Desta forma, o sistema projeta a saída de caixa conforme o compromisso financeiro assumido com o fornecedor, e não pela data física de recebimento da mercadoria.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37901373465111)
