---
article_id: 360036800153
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: c9bebbce12e20d8b2aae4b505dc4560fcfe689c2eaba142ccf73e5c4042bd4e0
fetched_at: '2026-06-28T22:38:32.645450+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-Sugerir a Tes conforme a mudança da natureza do pedido
type: support-article
updated_at: '2021-04-28T15:54:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036800153-MP-FAT-Sugerir-a-Tes-conforme-a-mudan%C3%A7a-da-natureza-do-pedido
---

**Dúvida**

Existe alguma maneira de vincular ou criar um gatilho para quando colocar a natureza no pedido(**MATA410**), o sistema sugerir as **TES (MATA080)** conforme a **natureza(FINA010)**, ou algum tipo de operação alterar a natureza e a tes?  
   
 **Ambiente**Microsiga Protheus - todas as versões.  
  
**Solução**

No padrão do sistema,  não há configuração para isso, ou a tes está no produto(**MATA010**) para trazer automaticamente ao pedido quando for selecionado ou se usa tes inteligente.

Neste caso, se parametriza a tes inteligente(**MATA089**) pelo código de operação , porém, no cadastro da tes inteligente não há busca por natureza.

Caso necessite de criar gatilhos, contate a equipe de n1\_advpl para orientação.
