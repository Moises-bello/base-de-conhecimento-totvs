---
article_id: 1500007343221
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 723b24d4a029fdf36c091e31942ff27f0057b5b206f0a2b826103bc433a75b15
fetched_at: '2026-06-28T22:38:29.839952+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Lista de APIs de Faturamento
type: support-article
updated_at: '2026-02-27T14:16:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007343221-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Lista-de-APIs-de-Faturamento
---

**Dúvida**  
Quais são os API´s de Faturamento?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12

**Solução**

Estas são as API´s do módulo Faturamento:

* [**Transportadora: API para a entidade Transportadora (Carrier) para produtos TOTVS**](https://api.totvs.com.br/apidetails/Carrier_v1_000.json)
* [**Cliente/Fornecedor: API para a entidade cliente/fornecedor (customerVendor) para produtos TOTVS**](https://api.totvs.com.br/apidetails/CustomerVendor_v1_000.json)
* [**Limite de credito do Cliente: API para consulta do Limite de credito do Cliente (CustomerCreditLimit) para produtos TOTVS**](https://api.totvs.com.br/apidetails/CustomerCreditLimit_v1_000.json)
* [**Condição de Pagamento: API para a entidade Condição de Pagamento (PaymentCondition) para produtos TOTVS**](https://api.totvs.com.br/apidetails/PaymentCondition_v1_00.json)
* [**Comissão de Venda: API para Comissão de Vendas (SalesCharge) para produtos TOTVS**](https://api.totvs.com.br/apidetails/SalesCharge_v1_000.json)
* [**Tabela de Preços: API para manutenção de tabela de preço para os produtos TOTVS**](https://api.totvs.com.br/apidetails/PriceListHeaderItem_v2_005.json)
* [**Vendedor: API para a entidade Vendedor (seller) para produtos TOTVS**](https://api.totvs.com.br/apidetails/Sellers_v2_000.json)
* [**Impostos do Pedido de Venda: API para Consulta de Valores e Tributos (SalesTaxes) em Pedidos de Venda TOTVS**](https://api.totvs.com.br/apidetails/SalesTaxes_v1_000.json)
* [**Prospects: API para a entidade Prospects (Prospects) para produtos TOTVS**](https://api.totvs.com.br/apidetails/Prospects_v1_000.json)
* [**Suspects: API para a entidade Suspects (Suspects) para produtos TOTVS**](https://api.totvs.com.br/apidetails/Suspects_v1_000.json)

Para acesso da lista de API´s da Totvs, acesse o link: [**https://api.totvs.com.br/**](https://api.totvs.com.br/)  
  
  
  
  
Saiba mais: [**Conceito do consumo de licenças Totvs I**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003971702-Framework-Linha-Protheus-Conceito-do-consumo-de-licen%C3%A7as-Totvs-I)  
  
**Importante:** A licença I é consumida em threads HTTP que são usadas para responder portais ou Web Services.  
Seu consumo segue a configuração contida na chave Instances (<http://tdn.totvs.com/display/tec/Instances>), existente dentro dos arquivos de configuração dos serviços Protheus
