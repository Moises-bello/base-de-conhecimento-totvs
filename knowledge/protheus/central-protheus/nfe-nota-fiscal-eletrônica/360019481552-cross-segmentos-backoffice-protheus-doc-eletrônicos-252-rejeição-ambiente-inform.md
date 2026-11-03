---
article_id: 360019481552
category: NFe - Nota Fiscal Eletrônica
content_hash: b2f5fe60ffe73869c9d8cc6c5900744ff6ce04313b14d60116bb8953693c9a46
fetched_at: '2026-06-28T22:40:03.173831+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  252 Rejeição –
  Ambiente informado diverge do Ambiente de recebimento
type: support-article
updated_at: '2025-07-25T18:58:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019481552-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-252-Rejei%C3%A7%C3%A3o-Ambiente-informado-diverge-do-Ambiente-de-recebimento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33722131229335) Tempo aproximado para leitura: **00:00:30 min**

**Dúvida**Como corrigir a rejeição 252 – Ambiente informado diverge do Ambiente de recebimento  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

A rejeição ocorre quando **foi autorizada a nota em ambiente de produção** e o **cancelamento está sendo enviado em ambiente de homologação**, ou **vice-versa.**

1- Verifique os parâmetros de transmissão das notas em **Outras ações -> Parâmetros -> NFe** , o ambiente em que a nota foi autorizada.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061523533)

2- Depois verifique os parâmetros de evento **Outras ações -> Parâmetros ->** **Eventos**, o ambiente precisa ser o mesmo em que a nota foi autorizada.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060589694)

Salve a configuração no botão **+ GRUPO ADMINISTRADOR: SALVAR**

3- Após isso, em **Outras ações -> Transmissão faça novamente a  transmissão** da nota e monitore.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061523793)
