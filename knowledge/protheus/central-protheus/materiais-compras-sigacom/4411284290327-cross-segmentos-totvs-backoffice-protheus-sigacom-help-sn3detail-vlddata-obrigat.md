---
article_id: 4411284290327
category: Materiais - Compras (SIGACOM)
content_hash: 061b7971d5adc4cdc5f638c0d88f7f4b815135cb7351d32165498348cec29a25
fetched_at: '2026-06-28T22:41:25.497463+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos Totvs Backoffice Protheus - SIGACOM - HELP SN3DETAIL VLDDATA_OBRIGAT
  SN3
type: support-article
updated_at: '2022-10-26T14:02:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411284290327-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-HELP-SN3DETAIL-VLDDATA-OBRIGAT-SN3
---

**Ocorrência**Ao incluir um documento de entrada com vínculo de Ativo, aparece o HELP por exemplo:  
(Apenas exemplo de um HELP relacionado)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411284152471/mceclip0.png)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - A partir da versão 11.80  
  
**Causa**O help pode ocorrer pois foi criado um campo customizado como obrigatório na SN3 e ao gerar uma NF de entrada que não possui integração com esse campo, será apresentado o HELP, pois de fato o campo não está sendo preenchido.

**Solução**Retirar a obrigatoriedade do campo ou criar algum tratamento que preencha o campo informado no erro.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)

[MV\_VLRATF - INTEGRAÇÃO DOCUMENTO DE ENTRADA COM ATIVO FIXO](https://tdn.totvs.com/pages/releaseview.action?pageId=235596102)

[MP - SIGAATF - INCONSISTÊNCIA REFERENTE A MOEDA NA VERIFICAÇÃO DE INTEGRIDADE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017523572-MP-SIGAATF-INCONSIST%C3%8ANCIA-REFERENTE-A-MOEDA-NA-VERIFICA%C3%87%C3%83O-DE-INTEGRIDADE-)
