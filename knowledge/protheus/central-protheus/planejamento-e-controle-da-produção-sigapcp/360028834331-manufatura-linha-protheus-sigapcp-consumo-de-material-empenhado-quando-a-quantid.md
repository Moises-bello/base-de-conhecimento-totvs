---
article_id: 360028834331
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 429739ddeb98a179099bd0556764cb2053276910029500d6629299bcccb3d049
fetched_at: '2026-06-28T22:42:42.138961+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Consumo de material empenhado quando
  a quantidade do apontamento excede a quantidade da ordem de produção
type: support-article
updated_at: '2022-11-14T17:41:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028834331-Manufatura-Linha-Protheus-SIGAPCP-Consumo-de-material-empenhado-quando-a-quantidade-do-apontamento-excede-a-quantidade-da-ordem-de-produ%C3%A7%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como ocorre o consumo do material empenhado quando a quantidade apontada excede a quantidade da **OP - Ordem de Produção**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Quando a quantidade produzida é maior do que a prevista através da **OP**, o excedente pode ser classificado como ganho de produção ou produção a maior. No ganho de produção, não ocorre o consumo adicional de material, já quando a produção é identificada como produção a maior, o Sistema requisita uma quantidade a mais dos materiais empenhados na proporção do excedente produzido.  
Para isso existem os parâmetros **MV\_PERCPRM - Percentual da quantidade da ordem de produção que será permitido apontar a maior** e **MV\_GANHOPR - Utilizado para verificar se permite o conceito de ganho de produção na inclusão do apontamento de produção**.
