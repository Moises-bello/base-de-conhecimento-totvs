---
article_id: 360024262472
category: TAF - eSocial - Eventos Periódicos
content_hash: 19024e3d88ed2793bd1dc17332b5a1fccfbbfc097a18cf80c634f361ff9d7107
fetched_at: '2026-06-28T22:45:19.006675+00:00'
product: protheus
section_id: 1500001536901
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - Eventos Periódicos - S-1200 - ocorrência
  312 - Descrição: A categoria XX informada deve ser igual a existente no cadastro
  do trabalhador no Ambiente Nacional do eSocial.'
type: support-article
updated_at: '2026-06-25T11:27:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024262472-RH-Linha-Protheus-TAF-eSocial-Eventos-Peri%C3%B3dicos-S-1200-ocorr%C3%AAncia-312-Descri%C3%A7%C3%A3o-A-categoria-XX-informada-deve-ser-igual-a-existente-no-cadastro-do-trabalhador-no-Ambiente-Nacional-do-eSocial
---

**Ocorrência**No módulo TAF, ao enviar o evento S-1200 de um trabalhador ocorre o erro:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022725011)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Eventos Periódicos - S-1200 - Todas as versões  
  
**Causa**Esse incidente ocorre devido divergência das informações referente ao trabalhador enviadas no xml do evento S-1200 com o cadastro inicial S-2200 enviado ao governo (e-social).  
  
**Solução**Para solucionar essa ocorrência, é necessário que confronte os dados do trabalhador no e-social x xml do evento S-1200 como: CPF, Matricula e Categoria

Caso exista qualquer divergência, será necessário que exclua o evento S-2200 e envie novamente com as informações devidamente corrigidas. Após isso, faça o reenvio do S-1200.

**Importante:** O procedimento de correção deve ser realizado no ERP de
