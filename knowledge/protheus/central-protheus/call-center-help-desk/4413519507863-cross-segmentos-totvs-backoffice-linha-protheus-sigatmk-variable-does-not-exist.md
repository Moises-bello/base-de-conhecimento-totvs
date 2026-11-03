---
article_id: 4413519507863
category: Call Center - Help Desk
content_hash: 203f4beb2ef34e210809a5af5da5a1cb1231a9b077ff5971ab3636fc6d43fd57
fetched_at: '2026-06-28T22:41:27.643409+00:00'
product: protheus
section_id: 1500001537181
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGATMK - variable does
  not exist ADE_GRUPO
type: support-article
updated_at: '2021-11-18T14:30:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413519507863-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-variable-does-not-exist-ADE-GRUPO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**

Ao tentar incluir, alterar ou visualizar um teleatendimento na rotina TMKA503A sistema apresenta o seguinte error.log: variable does not exist ADE\_GRUPO.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Call Center (SIGATMK) - Todas as versões  
  
**Causa**

Essa ocorrência esta relacionada ao modelo de atendimento informado no cadastro do grupo de atendimento na aba Teleatendimento.

No modelo atual a tabela que esta sendo referenciada e diferente a tabela padrão do sistema ADE. Com isso ao tentar validar um campo na query do modelo de atendimento sistema não o encontra e gera a ocorrência acima.

**Solução**

Solução, alterar o modelo informado no grupo de atendimento e colocar as tabelas corretas ou criar um novo modelo de atendimento.

Segue link da Faq para auxiliar na configuração ideal para o teleatendimento: [**Modelo Atendimento Teleatendimento x ServiceDesk Configuração**](https://tdn.totvs.com/x/3dJoE)
