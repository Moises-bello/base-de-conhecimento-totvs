---
article_id: 360052337734
category: RH - Rescisão
content_hash: 03d48fc3d5e6d8af617310c320b47760caf38cf18dc2947f67f9feb7ab330fb8
fetched_at: '2026-06-28T22:43:49.834433+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - PLR com taxa de negociação na rescisão
type: support-article
updated_at: '2025-07-17T12:28:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052337734-RH-Linha-Protheus-GPE-PLR-com-taxa-de-negocia%C3%A7%C3%A3o-na-rescis%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33530583219991) Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**PLR com taxa de negociação na rescisão.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**No cálculo da rescisão complementar com pagamento (provento) somente de PLR o sistema não efetua a geração da verba de desconto sem id lançada na RGB.  
  
**Solução**Foi realiza a criação do campo RV\_REFPLR no cadastro de verbas, para definir se a verba informada em questão será ou não gerada na rescisão complementar por PLR.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084745734)

Após a criação do campo na verba em questão para calculo na rescisão complementar deixar o campo Ref.PLR = SIM

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27920435466007)

**Saiba Mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
