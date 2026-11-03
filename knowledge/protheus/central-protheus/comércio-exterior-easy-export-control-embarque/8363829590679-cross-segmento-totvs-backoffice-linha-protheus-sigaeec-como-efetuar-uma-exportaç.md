---
article_id: 8363829590679
category: Comércio Exterior - Easy Export Control - Embarque
content_hash: 4b585fd378ebc8d35463d1cb7dd9d2403e04b96dd452b3594f82d263fadc4388
fetched_at: '2026-06-28T22:36:39.142507+00:00'
product: protheus
section_id: 1500001549322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Como Efetuar uma
  Exportação Amparada pelo Regime de Drawback
type: support-article
updated_at: '2022-08-23T12:48:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8363829590679-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Como-Efetuar-uma-Exporta%C3%A7%C3%A3o-Amparada-pelo-Regime-de-Drawback
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como efetuar uma exportação amparada pelo regime de *Drawback*, com o CFOP de saída = 7.127, quais as configurações e parâmetros a serem utilizados para geração da nota fiscal com o número do ato concessório do *Drawback* e tags específicas no arquivo xml da nfe?  
Isso em um cenário onde não é utilizado o módulo de **SIGAEDC** (***EASY DRAWBACK CONTROL***), somente o módulo **SIGAEEC** (***EASY EXPORT CONTROL***).   
  
**Ambientes**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões  
  
**Solução**Para o cliente efetuar uma exportação para o regime de *Drawback* sem integração como módulo *Drawback* (**MV\_EEC\_EDC= F**) o cliente o pode utilizar código fiscal de saida 7127 na fase do pedido de exportação sem problemas e se ele utiliza integração com o faturamento (**MV\_EECFAT = S)** liberar o pedido de vendas, fazer faturamento e gerar o documento de saída.  
O cliente pode informar o numero do ato concessório na fase embarque exportação (**EECAE100**) nos itens através do campo Ato Concessório (**EE9\_ATOCON**) e a Sequencia do Ato Concessório (**EE9\_SEQED3**).  
Uma vez preenchida estas informações e salvas no Embarque de Exportação ao transmitir a DUE as tags que serão levadas são *AdditionalDocument*, *CategoryCode*, *ID*, *DrawbackHsClassification*, *DrawbackRecipientId*, *ValueWithExchangeCoverAmount*, *ItemID* e *QuantityQuantity*.   
Estas informações ela são gravadas na tabela **EK7** (Dados Fabr. Itens Embarque Exp). Segue abaixo um exemplo das tags , qual o campo leva informação e a descrição de cada uma delas:

```
<AdditionalDocument>  
<CategoryCode>AC</CategoryCode> (Campo EK7_TPAC - TIPO DE ATO CONCESÓRIO)  
<ID>99999</ID> (Campo EK7_ATOCON - Ato concessório informado no embarque)   
<DrawbackHsClassification>84716059</DrawbackHsClassification> (Campo EK7_POSIPI - NCM do produto)   
<DrawbackRecipientId>04743835000192</DrawbackRecipientId> (Campo EK7_CNPJ - CNPJ do Fornecedor)   
<ValueWithExchangeCoverAmount>0000000010000.00</ValueWithExchangeCoverAmount> (Campo EK7->EK7_VALOR - EK7->EK7_VLSCOB -Valor Total - Valor S/Cobertura de Cambio)  
<ItemID>01</ItemID> (Campo EK7_SEQED3 - Sequencia Ato Concessório)   
<QuantityQuantity>0000001000.00000</QuantityQuantity> (Campo EK7_QTD - Quantidade produto intermediário)   
</AdditionalDocument>
```
