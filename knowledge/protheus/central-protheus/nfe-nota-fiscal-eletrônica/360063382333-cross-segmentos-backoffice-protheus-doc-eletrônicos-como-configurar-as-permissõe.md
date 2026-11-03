---
article_id: 360063382333
category: NFe - Nota Fiscal Eletrônica
content_hash: ffaf7cc58ef747241151b9b4480d3781e9cab0f5fd60be00e9ca30d64efcd618
fetched_at: '2026-06-28T22:40:03.445624+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  Como configurar
  as permissões na rotina SPEDNFE
type: support-article
updated_at: '2021-09-08T12:27:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063382333-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-configurar-as-permiss%C3%B5es-na-rotina-SPEDNFE
---

**Dúvida**

Como configurar as permissões na rotina SPEDNFE ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

O parâmetro**MV\_ADMNFE** controla a regra utilizada para o acesso no botão parâmetros:

1- Entre no Configurador -> **Ambiente -> Cadastros -> Parâmetros**e configure com **.T .**= Usuários **que sejam do grupo do administrador**

![MV_ADMNFE.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003119622/MV_ADMNFE.gif)

ou

2- Entre no Configurador -> **Ambiente -> Cadastros -> Parâmetros**e configure com **.F.** = **Qualquer** usuário

![MV_ADMNFE.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4408065510167/MV_ADMNFE.gif)
