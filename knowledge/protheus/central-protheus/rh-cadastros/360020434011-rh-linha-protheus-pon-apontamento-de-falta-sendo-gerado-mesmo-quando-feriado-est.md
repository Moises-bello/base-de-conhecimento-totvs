---
article_id: 360020434011
category: RH - Cadastros
content_hash: 1cdc45983b75e20166410175dfd43208c671fefaf4d1463b97b5da4bb5b96893
fetched_at: '2026-06-28T22:44:52.647852+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON  - Apontamento de falta sendo gerado mesmo quando
  feriado está cadastrado corretamente
type: support-article
updated_at: '2025-12-29T13:29:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020434011-RH-Linha-Protheus-PON-Apontamento-de-falta-sendo-gerado-mesmo-quando-feriado-est%C3%A1-cadastrado-corretamente
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35218967462423) Tempo aproximado para leitura: 00:01:00 min***  
  
**Ocorrência**  
Apontamento de falta sendo gerado mesmo quando feriado está cadastrado corretamente  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Quando o apontamento de falta é gerado em dia de feriado, realize os seguintes passos:

**1.** Verificar na Troca de Turno: **Atualizações > Cadastro de Funcionários > Troca de Turno** e a Regra de Apontamento que está vinculada a esse funcionário:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31411941283223)

**2.** Em **Atualizações > Cadastro do Ponto > Regra de Apontamento**, na **ABA Apontamentos,** localizar o campo **TRAB. FERIADO (PA\_FERIADO) -** seu conteúdo deve ser = **NÃO:**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31411941285143)**

**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
