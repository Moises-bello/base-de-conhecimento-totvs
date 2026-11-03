---
article_id: 360035400954
category: NFe - Nota Fiscal Eletrônica
content_hash: d2248482523552ab448a652b335533d872ecd72175a95c556824be34bf29e737
fetched_at: '2026-06-28T22:40:00.203513+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  221 Rejeição
  : Confirmado o recebimento da NF-e pelo destinatário'
type: support-article
updated_at: '2023-03-24T14:19:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035400954--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-221-Rejei%C3%A7%C3%A3o-Confirmado-o-recebimento-da-NF-e-pelo-destinat%C3%A1rio
---

**Ocorrência**

221 Rejeição : Confirmado o recebimento da NF-e pelo destinatário  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Causa**

Quando o destinatário da NF-e confirma o recebimento do documento através do evento de manifestação e o emitente realiza o registro de um evento de cancelamento, este será rejeitado pelo motivo "221 - Confirmado o recebimento da NF-e pelo destinatário"

**Solução**

1. Veja o exemplo abaixo de um NF-e que foi ***autorizada e confirmado*** o recebimento pelo destinatário:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046103874/mceclip0.png)

2. Para conseguir cancelar esta nota, deve-se entrar em contato com o destinatário da NF-e e solicitar que ***registre outro evento de manifestação, (Operação não realizada ou desconhecida)*** sobre a NF-e que ele confirmou. Com qualquer um desses eventos homologados após a confirmação do operador, a NF-e poderá ser cancelada.
