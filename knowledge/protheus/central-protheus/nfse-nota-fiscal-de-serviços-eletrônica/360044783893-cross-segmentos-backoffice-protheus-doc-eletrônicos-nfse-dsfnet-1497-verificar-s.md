---
article_id: 360044783893
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 631611914f368200c188f82c12f5f4646e59fc42908d0df8d0fdc2fb49a712b6
fetched_at: '2026-06-28T22:39:56.465569+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - DSFNET:
  1497 - Verificar se nao houve informacao de retencao indevida no RPS para empresa
  fora de Campinas.'
type: support-article
updated_at: '2025-07-08T20:01:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044783893-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-DSFNET-1497-Verificar-se-nao-houve-informacao-de-retencao-indevida-no-RPS-para-empresa-fora-de-Campinas
---

**Dúvida**Como corrigir a rejeição 1497 - Verificar se não houve informação de retenção indevida no RPS para empresa fora de Campinas?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Para essa rejeição, a prefeitura sugere o envio do tipo de recolhimento igual a A.

O tipo de recolhimento é definido na tag <TipoRecolhimento>, e pode ter os seguintes conteúdos:

“A” - A recolher  
“R” – Retido na fonte.

Esse conteúdo é o reflexo dos campos A1\_RECISS/C5\_RECISS, se 1 no campo a tag envia R, se 2 no campo a tag envia A.

A prefeitura também sugere consultar a situação cadastral do tomador em:  
<https://situacao.campinas.sp.gov.br/>

Entre em contato com a prefeitura para verificar se esse tomador pode ser o responsável por esse recolhimento.
