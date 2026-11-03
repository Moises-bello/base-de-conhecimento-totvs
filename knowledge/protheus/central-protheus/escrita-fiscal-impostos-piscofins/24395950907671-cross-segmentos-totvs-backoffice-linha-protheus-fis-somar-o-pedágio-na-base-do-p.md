---
article_id: 24395950907671
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: 4c77c409ed1fdd764075d24dfe76eb74f2cd4133f6c67a810240bceb0aff88a9
fetched_at: '2026-06-28T22:39:36.968362+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – Somar o pedágio na
  base do PIS/COFINS Apuração.
type: support-article
updated_at: '2024-06-24T17:33:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24395950907671-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Somar-o-ped%C3%A1gio-na-base-do-PIS-COFINS-Apura%C3%A7%C3%A3o
---

**Dúvida**Como somar o valor do pedágio na base do PIS/COFINS Apuração?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**

Para que o valor do pedágio seja somado na base do PIS/COFINS, no cadastro da TES ajuste o campo Agr.Vl.Pedg (F4\_AGRPEDG) = 4.

Agr.Vl.Pedg" (F4\_AGRPEDG):  
1=Agr. na base ICMS;  
2=Agr. somente no total NF;  
3=Não considera;  
**4=Agr. na base do PIS/COFINS;**  
**5=Agr. na base do PIS/COFINS e ICMS**

Com isso é possível atender a solicitação da inclusão do valor do Pedágio ou não à Base de PIS/COFINS para tomada de crédito.

**Boletim técnico:**  
[Inclusão de opção para somar valor do pedágio na base do PIS/COFINS no campo F4\_AGRPEDG](https://tdn.totvs.com/pages/releaseview.action?pageId=623878817)
