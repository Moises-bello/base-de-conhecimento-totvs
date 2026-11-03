---
article_id: 1500009813661
category: Call Center - Televendas
content_hash: a81d293710f8da6a7073087d040ebb66473e96378ad6566f53452ac338b94b78
fetched_at: '2026-06-28T22:41:30.347180+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: Cross Seguimentos - TOTVS BackOffice (Linha Protheus) - Call Center (SIGATMK)
  - Help TLVLIBSC9 no Cancelamento do Atendimento
type: support-article
updated_at: '2021-05-07T14:44:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009813661-Cross-Seguimentos-TOTVS-BackOffice-Linha-Protheus-Call-Center-SIGATMK-Help-TLVLIBSC9-no-Cancelamento-do-Atendimento
---

**Ocorrência**Ao tentar realizar o Cancelamento de um Atendimento no Televendas o sistema apresenta o Help **TLVLIBSC9**.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Call Center (SIGATMK) - Todas as versões  
  
**Causa**O help indica que o pedido gerado por este atendimento já foi liberado, ou seja, o atendimento gerou um pedido de vendas e este possui liberação para faturamento.

O sistema verifica se há um número de pedido informado no campo "**Ped SIGAFAT" (UA\_NUMSC5)**, caso possua, ele verifica se este número existe na tabela **SC9** do sistema.

Caso localize, indica que existe liberação e apresenta o Help **TLVLIBSC9**.   
  
**Solução**Localize o pedido com o número descrito no campo **"Ped SIGAFAT" (UA\_NUMSC5)** e estorne a liberação dele para que seja possível Cancelar o atendimento.
