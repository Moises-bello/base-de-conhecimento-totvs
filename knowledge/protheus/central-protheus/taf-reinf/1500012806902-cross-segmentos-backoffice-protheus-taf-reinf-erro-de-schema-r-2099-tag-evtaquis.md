---
article_id: 1500012806902
category: TAF - REINF
content_hash: 9b2ec8462a87572b32d2771a7ed493c7661e803a687fbf7e03e54cc2a03bad9b
fetched_at: '2026-06-28T22:41:33.554082+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF -  Erro de Schema R-2099
  tag EvtAquis
type: support-article
updated_at: '2023-03-31T16:35:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012806902-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Erro-de-Schema-R-2099-tag-EvtAquis
---

**Dúvida**Como corrigir o erro de Schema com a tag EvtAquis no R-2099?  
  
**Ambiente**TAF – REINF – A partir da versão 12.1.23

**Solução**

**![tag_evtaquis.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402315273495/tag_evtaquis.png)**

Esse erro ocorre quando o campo V0B\_AQUIRU não existe na base de dados. A apuração do R-2099 no layout 1.5 leva a informação se houve ou não R-2055, caso não esteja com a ultima atualização disponível que cria esse campo, ocorre o erro.

1. Atualizar o ambiente TAF e executar o UPDDISTR:

[MP - TAF - REINF - Atualização Completa REINF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026673572-MP-TAF-REINF-Atualiza%C3%A7%C3%A3o-Completa-REINF?source=search)

2. Excluir a apuração inconsistente e apurar novamente.

3. Transmitir o evento.

observação: Caso, por algum motivo, o RPO que foi atualizado tenha sido trocado por algum anterior a atualização e o fonte TAFAPR2099 esteja com data anterior a 01/2021, o campo não será preenchido na apuração e o problema irá persistir. Neste caso, faz-se necessário validar se o RPO em questão está devidamente atualizado.
