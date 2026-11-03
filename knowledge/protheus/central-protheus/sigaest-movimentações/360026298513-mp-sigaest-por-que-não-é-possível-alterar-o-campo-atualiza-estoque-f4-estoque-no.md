---
article_id: 360026298513
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 8c0f2bafd7f3aa40c55d891ab2f3df6d590574318e047b71306f8614979aa80c
fetched_at: '2026-06-28T22:38:58.632809+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: MP - SIGAEST - Por que não é possível alterar o campo 'Atualiza Estoque' (F4_ESTOQUE)
  no cadastro de TES?
type: support-article
updated_at: '2021-06-24T13:23:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026298513-MP-SIGAEST-Por-que-n%C3%A3o-%C3%A9-poss%C3%ADvel-alterar-o-campo-Atualiza-Estoque-F4-ESTOQUE-no-cadastro-de-TES
---

**Dúvida**Por que não é possível alterar o campo 'Atualiza Estoque' (F4\_ESTOQUE) no cadastro do TES (MATA080)?

**Ambiente**Microsiga Protheus – Estoque/Custos – A partir da versão 11.80  
  
**Solução**

O cadastro de TES é de suma importância dentro do sistema, uma vez que este cadastro carregará em suas movimentações, todas as informações de estoque e custo financeiro e fiscal da empresa.

A alteração do campo "Atualiza Estoque" (SF4->F4\_ESTOQUE) é bloqueada, caso o TES tenha gerado registros nas tabelas SF1, SD1 e SD2. Se a alteração fosse permitida, geraria inconsistências em todas as movimentações já realizadas com este cadastro, assumindo a nova configuração.

**E campos fiscais, consigo alterar?**

Para alteração de campos fiscais, o sistema permitirá a alteração para TES com código menor que 500 (ou seja, TES de entrada), porém será necessário o processamento da rotina Refaz Custos de Entrada - MATA190 para reajuste com a nova configuração.

**Saiba mais:**

*[Clique aqui e saiba mais sobre Movimentações no Estoque.](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
