---
article_id: 115015481988
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 83bdef90a50765d8cbd6a9365c995cdada93b861ab95dd7def978d6a6b306ff0
fetched_at: '2026-06-28T22:38:41.265643+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: MP- FAT- A função A430BLCVLD não e encontrada no processo de reserva para o
  pedido de vendas.
type: support-article
updated_at: '2021-04-28T15:51:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115015481988-MP-FAT-A-fun%C3%A7%C3%A3o-A430BLCVLD-n%C3%A3o-e-encontrada-no-processo-de-reserva-para-o-pedido-de-vendas
---

**Ocorrência**

A função A430BLCVLD não e encontrada no processo de reserva para o pedido de vendas.

**Causa**

A função A430BLCVLD  provavelmente não havia sido declarada no fonte MATA430- Cadastro de Reservas.  
  
**Ambiente**

Microsiga Protheus - versão 12  
  
**Solução**  
  
Para corrigir, aplique o pacote de expedição continua do módulo faturamento, conforme a release utilizada:  **[SIGAFAT](https://tdn.totvs.com/pages/releaseview.action?pageId=521997859)**
