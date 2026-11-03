---
article_id: 1500007514802
category: Financeiro - Caixinha
content_hash: 12d54b556de7928279707ff7c24e107fb69a033c691e66b0edf21e8f7e3086ee
fetched_at: '2026-06-28T22:37:53.855981+00:00'
product: protheus
section_id: 1500001550702
source: central-protheus
title: Cross Segmento  Backoffice Linha Protheus - SIGAFIN - FINA550   - Qual será
  o LP correto para contabilizar os movimentos de devolução do caixinha tipo 11
type: support-article
updated_at: '2021-04-28T15:59:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007514802-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA550-Qual-ser%C3%A1-o-LP-correto-para-contabilizar-os-movimentos-de-devolu%C3%A7%C3%A3o-do-caixinha-tipo-11
---

**Dúvida**Qual será o LP correto para contabilizar os movimentos de devolução do caixinha tipo 11 ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro -FINA550 -  Todas as versões  
  
**Solução**Deve utilizar o **LP 57E -  Estorno Reposição Caixinha**?  
  
Um exemplo para configuração seria a expressão no campo **CT5\_VALOR: SEU->EU\_VALOR**

**Importante**Este LP (lançamento padrão) contabiliza on-line e off-line. Quando for off-line a contabilização este parâmetro **Contab. adto. aberto Caixinha? =SIM**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500010516862/mceclip0.png)

**Saiba mais**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=270894393>
