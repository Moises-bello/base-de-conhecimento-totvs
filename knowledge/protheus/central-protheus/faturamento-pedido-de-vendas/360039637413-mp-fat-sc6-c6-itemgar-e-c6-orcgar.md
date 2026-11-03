---
article_id: 360039637413
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 36c03daef73bbdf7c31254aba0505a40939d7ed971124f21ae4b09ea5d3c0a5c
fetched_at: '2026-06-28T22:38:41.314579+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: MP-FAT-SC6 -> C6_ITEMGAR e C6_ORCGAR
type: support-article
updated_at: '2021-04-28T15:50:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039637413-MP-FAT-SC6-C6-ITEMGAR-e-C6-ORCGAR
---

**Dúvida**

Qual a utilização dos campos C6\_ITEMGAR e C6\_ORCGAR?  
   
 **Ambiente**

Microsiga Protheus - a partir da versão 10.

**Solução**

Os campos **C6\_ITEMGAR** e **C6\_ORCGAR** são uma implementação para uso de complemento de garantia estendida **Front-Loja/Venda Assistida (LOJA980),** onde esses campos geram vínculos entre os produtos Garantia ( Produto tipo GE ) e produtos que possuam garantia estendida.

Este vinculo é necessário para o processo de devolução , possibilitando realizar a devolução do item  
Garantia ou da Garantia e do produto . Os itens de Garantia Estendida (Produto tipo GE ) serão  
gravados apenas na tabela de Itens de Orçamento (**SL2**) e em mais nenhuma tabela que faça parte da  
venda ( Nota Fiscal , Itens de Nota Fiscal e Itens de Pedido ) ou livros fiscais.

Para mais informações do procedimento, acesse o boletim técnico: **[Garantia Estendida BRA - TFNIS8](https://tdn.totvs.com/display/PROT/Garantia+Estendida+BRA+-+TFNIS8)**
