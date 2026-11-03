---
article_id: 26495823824663
category: Faturamento - Integrações
content_hash: 2a8b44cb16ea6bc29539f6fcf8d853f3c8cdb7125b9836fb236937420c34444e
fetched_at: '2026-06-28T22:38:26.445039+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - TAGS Importantes
  no XML da Integração NeoGrid x Pedidos de Venda
type: support-article
updated_at: '2024-09-19T21:07:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26495823824663-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-TAGS-Importantes-no-XML-da-Integra%C3%A7%C3%A3o-NeoGrid-x-Pedidos-de-Venda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26495823810711) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Quais TAGS são utilizadas no XML de Integração entre o NeoGrid e o Pedido de Venda (MATA410)?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões

**Ambiente**  
Abaixo uma lista das principais TAGS e quais informações são alimentadas através delas:

| TAG | CAMPO / NOME | EXEMPLO |
| --- | --- | --- |
| funcmsgorder | Função da mensagem | 9-Original |
| OrderPurpose | Objetivo do Pedido | 1-Compra / 2-Venda |
| ordertypecode | C5\_TIPO | 001-Pedido Normal |
| RegisterDate | C5\_EMISSAO |  |
| OrderId | C6\_PEDCLI |  |
| FreightType | C5\_TPFRETE | 1-CIF / 2-FOB / 3-SFT (Sem frete) |
| VendorGovInfo | CNPJ da empresa (SM0) | O fornecedor é o Protheus (sua base), esse é o CNPJ que deve estar cadastrado em seu ambiente |
| CustomerGovInfo | Cliente |  |
| DeliveryCustomerGovernmentalInformation | Cliente Entrega |  |
| PAYMENTTERMCODE | Condição de Pagamento | Dificilmente é informada, pois o cliente geralmente, não possui tal informação. Caso não seja informada, a busca ocorre por meio do campo A1\_COND |
| typecodprod | Tipo de código de produto | EN' ou 'UP' - Busca o produto por meio do código de barras (B1\_CODBAR) 'BP' - Busca pela amarração de clientes x produtos (A7\_PRODUTO) |
| ItemCode | C6\_PRODUTO |  |
| Quantity | C6\_QTDVEN |  |
| UnityPrice | C6\_PRCVEN | Se a tabela de preços está vazia, utiliza a informação da tag, senão  utiliza o campo B1\_PRV1 para gravar no campo C6\_PRCVEN |
| netunitaryprice | Preço unitário líquido do item |  |
| DiscountPercentage | Descontos |  |
| TotalPrice | Total Bruto |  |
| valnetlineitem | Total Líquido |  |
| unitvaltradedisc | Valor desconto no item |  |
| ordertotalnetamount | Valor Bruto Total do Pedido |  |
