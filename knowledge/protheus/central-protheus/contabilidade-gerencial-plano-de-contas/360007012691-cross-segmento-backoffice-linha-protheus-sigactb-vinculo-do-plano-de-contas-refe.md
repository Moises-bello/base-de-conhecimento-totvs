---
article_id: 360007012691
category: Contabilidade Gerencial - Plano de Contas
content_hash: 6d79f9e8b964e2a6dd260815cdd6b7a1c7c3fde628efa96e672a6a43cb47529e
fetched_at: '2026-06-28T22:40:33.379091+00:00'
product: protheus
section_id: 1500001549022
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - VINCULO DO PLANO DE
  CONTAS REFERENCIAL
type: support-article
updated_at: '2022-06-10T23:27:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007012691-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-VINCULO-DO-PLANO-DE-CONTAS-REFERENCIAL
---

**Ocorrência**Ao tentar vincular uma conta contábil no momento do cadastro, a uma conta do plano referencial o sistema está apresentando erro e fechando:

"variable does not exist CPLANOREF on CTBFILVERS(CTBXCTB.PRW)"  
   
 **Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 12.1.17  
   
 **Causa**

A consulta padrão está como CVN3 quando o correto seria CVN2.  
  
 **Solução**No campo CVD\_CTAREF, caso a Cons. Padrão (X3\_F3) estiver com CVN3, alterar para:  
  
![cvd_ctaref.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029310992/cvd_ctaref.png)​
