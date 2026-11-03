---
article_id: 360057779053
category: Faturamento - Orçamentos
content_hash: 754cd2cb8fe22722c4f2877d9e9a01100d235d8a82f1402f1bff6b8a75d1aa3e
fetched_at: '2026-06-28T22:38:24.997148+00:00'
product: protheus
section_id: 1500001539281
source: central-protheus
title: MP-FAT-Campos CJ_FRETE e CJ_FRETAUT
type: support-article
updated_at: '2021-04-28T15:15:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057779053-MP-FAT-Campos-CJ-FRETE-e-CJ-FRETAUT
---

**Dúvida**

Qual o uso dos campos CJ\_FRETE e CJ\_FRETAUT no orçamento de vendas (MATA415)?  
  
**Ambiente**

Microsiga Protheus - todas as versões.  
  
**Solução**

Os campos **CJ\_FRETE** e **CJ\_FRETAUT**, tem o mesmo conceito do pedido de venda, sendo que no campo **CJ\_FRETE** deve se informar o valor de frete agregado ao orçamento que uma transportadora cobrará e esta informação irá para o campo **C5\_FRETE** na aprovação do orçamento.  
  
Já **CJ\_FRETAUT** é o frete autônomo, o valor do frete quando autônomo, ou seja, transportadores não contribuintes, onde a nota fiscal emitida com esse tipo de transportador, o valor do ICMS deve ser recolhido pela empresa adquirente do serviço.  Quando a nota fiscal é preparada, o valor do ICMS sobre o frete autônomo é calculado acrescido ao valor da nota fiscal.

Como ainda é um orçamento, a  informação de frete autônomo colocada no orçamento será levada para o Pedido de venda, no campo **C5\_FRETAUT**, após a aprovação do orçamento, e só na geração da nota pelo pedido de venda é que serão tratados os impostos sobre o frete em questão.
