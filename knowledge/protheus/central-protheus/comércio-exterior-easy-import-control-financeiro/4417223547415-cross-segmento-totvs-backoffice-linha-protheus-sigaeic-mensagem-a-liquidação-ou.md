---
article_id: 4417223547415
category: Comércio Exterior - Easy Import Control - Financeiro
content_hash: 576e3fef589fe7e2d13e7177e302bf506dc06b2a3f5c9d416da9c3c7185a8182
fetched_at: '2026-06-28T22:39:44.386765+00:00'
product: protheus
section_id: 1500001549642
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Mensagem: A liquidação
  ou estorno não pode ser efetuada após a alteração da parcela. Grave a alteração
  da parcela para posteriormente fazer a liquidação ou estorno.'
type: support-article
updated_at: '2022-04-25T20:20:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417223547415-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Mensagem-A-liquida%C3%A7%C3%A3o-ou-estorno-n%C3%A3o-pode-ser-efetuada-ap%C3%B3s-a-altera%C3%A7%C3%A3o-da-parcela-Grave-a-altera%C3%A7%C3%A3o-da-parcela-para-posteriormente-fazer-a-liquida%C3%A7%C3%A3o-ou-estorno
---

**Ocorrência**No módulo SIGAEIC, dentro da rotina de Câmbio (**EICAP100**), ao tentar estornar uma parcela do processo é apresentada a seguinte mensagem: **"A liquidação ou estorno não pode ser efetuada após a alteração da parcela. Grave a alteração da parcela para posteriormente fazer a liquidação ou estorno".****Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
 **Causa**A mensagem é apresentada pois após qualquer ação de alteração referente a parcela do Câmbio, o sistema exigirá que a mesma seja gravada, ou seja, caso efetuada a alteração da parcela e em seguida solicitado o estorno da mesma sem a devida gravação, será apresentado o aviso.  
  
**Solução**Para solucionar essa ocorrência, após a alteração da parcela selecione o **Salvar** para gravação do título, após procedimento é possível efetuar o estorno da parcela.
