---
article_id: 360055302394
category: RH - Soluções para error.log
content_hash: 1027f04dfe917833aef2969b10a362a16645d0fca4490608d894bef09572c03f
fetched_at: '2026-06-28T22:44:08.726130+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ao acessar o Wizard de Configuração ocorre erro:
  array out of bounds [1] of [0]  on GPEAWIZD(GPEAWIZD.PRW)'
type: support-article
updated_at: '2025-08-22T18:18:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055302394-RH-Linha-Protheus-GPE-Ao-acessar-o-Wizard-de-Configura%C3%A7%C3%A3o-ocorre-erro-array-out-of-bounds-1-of-0-on-GPEAWIZD-GPEAWIZD-PRW
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34378077999639)** Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**Ao acessar a rotina de Wizard de Configuração, **GPEAWIZD**, gera *error log: **array out of bounds*** **[1]** ***of*** **[0]** ***on*** **GPEAWIZD(GPEAWIZD.PRW).****Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - à partir da versão 12.  
  
**Causa**O erro ocorre quando o campo do endereço **REST** possui mais de 50 caracteres  
  
**Solução**Para solucionar o problema é necessário aplica o pacote abaixo:  
[MP - GPE - Como fazer o download (baixar) do pacote de acumulado do eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051585234-MP-GPE-Como-fazer-o-download-baixar-do-pacote-de-acumulado-do-eSocial?source=search)  
  
**Saiba mais:**[Pacote Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
