---
article_id: 1500005394901
category: Meu RH - Férias
content_hash: 201f568c3d28c50720559926def9fc5c2ba72422894d7b64ff52073d37dece66
fetched_at: '2026-06-28T22:47:31.715506+00:00'
product: rm
section_id: 1500000835241
source: central-rm
title: RH - RM - Meu RH - Onde são armazenadas as aprovações de férias
type: support-article
updated_at: '2025-09-17T13:05:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005394901-RH-RM-Meu-RH-Onde-s%C3%A3o-armazenadas-as-aprova%C3%A7%C3%B5es-de-f%C3%A9rias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:01:45 min****Dúvida**Em qual tabela é armazenada as solicitações de férias do Meu RH?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH – Todas as versões  
  
**Solução**Quando o funcionário faz uma Sugestão de Férias via Meu RH, a sugestão será armazenada na tabela **PFUFERIASPER** , assim como todas as férias no RM.  
  
Para saber quais já foram ou não aprovadas, segue abaixo consultas SQL para apoio.  
**1-** Quando o funcionário sugere férias, as férias ficam na situação "Aguardando aprovação do Gestor".  
  
Consulta SQL:  
select \* from pfuferiasper where situacaoferias='G'  
  
**2-** Quando o Gestor realizar a aprovação das férias do funcionário, a situação das férias será alterada para "Aguardando aprovação do DP".  
  
Consulta SQL:  
select \* from pfuferiasper where situacaoferias='D'  
  
**Saiba Mais**Para saber mais como consultar férias no Meu RH **[CLIQUE AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029082872-RH-RM-Meu-RH-Consulta-f%C3%A9rias?source=search)**.
