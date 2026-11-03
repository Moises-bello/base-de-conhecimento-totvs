---
article_id: 360018652091
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: fb794503598a763fa6358a32ebd3a98e87ea103103e232f8f3cc7a635bf9006d
fetched_at: '2026-06-28T22:38:31.180305+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-Como é feito o calculo da verba de venda para abatimento do saldo concedido
  ao vendedor
type: support-article
updated_at: '2021-04-28T15:55:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018652091-MP-FAT-Como-%C3%A9-feito-o-calculo-da-verba-de-venda-para-abatimento-do-saldo-concedido-ao-vendedor
---

**Dúvida**

Como é feito o cálculo da verba de venda (**FATA190**) para o abatimento do saldo concedido ao vendedor (**ACL->ACL\_SALDO**) quando feito um Pedido de Venda (**mata410**) e aplicado um desconto a mais do que fora definido na Regra de Negocio (**fata100**), aba descontos.  
   
 **Ambiente**

Microsiga Protheus - a partir da versão 11.  
   
**Solução**

Cálculo feito pelo sistema para abater o saldo **ACL->ACL\_SALDO** da verba de venda.

**(C6\_QTDVEN \* C6\_PRCVEN) - (C6\_QTDVEN \* C6\_PRUNIT)** = Abatimento do ACL->ACL\_SALDO

OBS: São realizadas as operações de multiplicação e posteriormente a operação de subtração para obter o resultado.

Para visualizar o exemplo, acesse a FAQ: **[Como é feito o calculo da verba de venda para abatimento do saldo concedido ao vendedor](http://tdn.totvs.com/pages/viewpage.action?pageId=236433683)**
