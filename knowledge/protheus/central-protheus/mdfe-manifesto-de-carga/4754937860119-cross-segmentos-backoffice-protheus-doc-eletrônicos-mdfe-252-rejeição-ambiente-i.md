---
article_id: 4754937860119
category: MDFe - Manifesto de Carga
content_hash: 532a70364c746dfcb6e7d50deda7ad7125493e4323b2e1ffc5d2a4d5ccf02cd3
fetched_at: '2026-06-28T22:40:08.234416+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE - 252 Rejeição
  – Ambiente informado diverge do Ambiente de recebimento
type: support-article
updated_at: '2025-06-17T17:38:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4754937860119-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-252-Rejei%C3%A7%C3%A3o-Ambiente-informado-diverge-do-Ambiente-de-recebimento
---

**Dúvida**Como corrigir a rejeição 252 – Ambiente informado diverge do Ambiente de recebimento ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Todas as versões

**Solução**

A rejeição ocorre quando **foi autorizada o mdf-e em ambiente de produção** e o **cancelamento está sendo enviado em ambiente de homologação**, ou **vice-versa.**

1. Verifique o ambiente em que o ***MDF-e foi autorizado -> outras ações -> Parâmetros;***

![parametros_mdfe.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4754150199191)

Salve a configuração no botão **+GRUPO ADMINISTRADOR: SALVAR**

2. Após isso, em **Outras ações -> Gerenciar MDF-e**   transmita o cancelamento novamente e monitore.
