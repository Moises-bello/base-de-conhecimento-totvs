---
article_id: 5130459055255
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 5eb3e88013bbae9366a2ee45c75f369ab538cf028141e1e88e455632b6e03e5c
fetched_at: '2026-06-28T22:38:44.195321+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT)
  - Preenchimento do campo F2_DTENTR
type: support-article
updated_at: '2022-03-31T13:37:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5130459055255-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Preenchimento-do-campo-F2-DTENTR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Qual o critério para preenchimento do campo F2\_DTENTR  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Faturamento - Todas as versões  
  
**Solução**Este campo não é de uso do módulo de faturamento, o mata461, gerador da nota de saída não tem tratamento para o mesmo.  
  
O campo é utilizado pelo GFE e da rotina OMSA320 de OMS.  
  
Para o GFE, é validado o campo GW1->GW1\_SIT e de acordo com este, preenche o F2\_DTENTR.  
  
Para o OMS, é validado o parâmetro MV\_OMSRETP, que verifica se trata de uma entrega parcial e se existe nota sem data de entrega, mas não foi possível localizar como o OMs preenche esta informação.  
  
Via módulo de Faturamento, para utilização do campo F2\_DTENTR somente tratamento por gatilho, caso tenha dúvida em como criar, solicite apoio a equipe de atendimento ADVPL.
