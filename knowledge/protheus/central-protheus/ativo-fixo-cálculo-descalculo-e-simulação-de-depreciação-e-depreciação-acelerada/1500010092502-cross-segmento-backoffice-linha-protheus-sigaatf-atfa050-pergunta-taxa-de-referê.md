---
article_id: 1500010092502
category: Ativo Fixo - Cálculo, Descalculo e Simulação de Depreciação e Depreciação
  acelerada
content_hash: a729a7846c7a156993e1a7fda9695e98dbd1595e8c9da0989ff1e892550093c0
fetched_at: '2026-06-28T22:41:43.260482+00:00'
product: protheus
section_id: 1500001536401
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA050 - Pergunta Taxa
  de Referência AFA05005
type: support-article
updated_at: '2023-08-14T19:05:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010092502-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA050-Pergunta-Taxa-de-Refer%C3%AAncia-AFA05005
---

**Dúvida**Qual a finalidade da pergunta Taxa de Referencia (AFA05005) contida na rotina de Calculo de Depreciação ?

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500015680662/mceclip1.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAATF - A partir da versão 12  
  
**Solução**A taxa de referência na rotina **ATFA050** encontra-se na mesma apenas por questão de legado, pois antigamente, em releases anteriores a **P11,** nessa pergunta era definido a taxa de depreciação para a moeda **UFIR**, atualmente extinta.  
  
A partir da P12, todo o calculo do ativo começou a basear-se apenas na taxa cadastrada no próprio bem, especificamente nos campos **N3\_TXDEPR1, N3\_TXDEPR2, N3\_TXDEPR3, N3\_TXDEPR4, entre outros**, não considerando a taxa de referência contido na pergunta da rotina.  
  
Por isso, não é necessário alimentar a taxa de referência na **ATFA050**, pois esta não será considerada, podendo deixar com o valor padrão 0,8287 ou zerado se preferir.
