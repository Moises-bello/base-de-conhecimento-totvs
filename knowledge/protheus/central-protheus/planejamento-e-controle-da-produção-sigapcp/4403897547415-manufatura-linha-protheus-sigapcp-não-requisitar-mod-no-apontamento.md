---
article_id: 4403897547415
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 664b58ea49b68e5aac1d7beed393d54e8f97b48c3d78e7c1294138d3cd9878d4
fetched_at: '2026-06-28T22:42:44.609400+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Não requisitar MOD no apontamento
type: support-article
updated_at: '2021-07-08T13:22:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403897547415-Manufatura-Linha-Protheus-SIGAPCP-N%C3%A3o-requisitar-MOD-no-apontamento
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:40 min**  
**Dúvida**No apontamento via **MATA680 - Produção Mod I** ou **MATA681 - Produção Mod II** é possível fazer com que o Sistema não requisite a **MOD** - **mão de obra** correspondente ao tempo apontado?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Quando o campo **H6\_TEMPO - Tempo Real do Apontamento**, possui informação, será feita a requisição da **MOD** correspondente ao centro de custos vinculado ao recurso apontado, a não ser que o usuário através do ponto de entrada **A680MOD** retorne o valor **0.  
  
Saiba mais**Para informações sobre o ponto de entrada **A680MOD** consulte a documentação disponível em: [A680MOD - Customizar mão de obra](https://tdn.totvs.com/pages/releaseview.action?pageId=6089321)
