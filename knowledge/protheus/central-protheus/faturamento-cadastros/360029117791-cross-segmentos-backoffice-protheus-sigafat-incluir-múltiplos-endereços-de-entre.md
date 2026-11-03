---
article_id: 360029117791
category: Faturamento - Cadastros
content_hash: b55aaa819dfec7a938b61232d1b2f10effe4f63e9eb0c905fb87b66498d8315d
fetched_at: '2026-06-28T22:38:35.463284+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Incluir múltiplos endereços
  de entrega em um único código de cliente
type: support-article
updated_at: '2026-03-27T18:26:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029117791-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Incluir-m%C3%BAltiplos-endere%C3%A7os-de-entrega-em-um-%C3%BAnico-c%C3%B3digo-de-cliente
---

**Dúvida**

Como incluir múltiplos endereços de entrega em um único código de cliente?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12  
  
**Solução**

No "Cadastro de Clientes (**CRMA980**)" não há como incluir múltiplos endereços de entrega.

Uma alternativa é cadastrar o mesmo cliente com outros endereços e para isso, ajuste o parâmetro (**MV\_VALCNPJ** = 1) e (**MV\_VALCPF** = 1), para que o sistema permita a duplicidade de CNPJ/CPF.

Sugestão é utilizar o mesmo código do cliente mas com lojas diferentes.
