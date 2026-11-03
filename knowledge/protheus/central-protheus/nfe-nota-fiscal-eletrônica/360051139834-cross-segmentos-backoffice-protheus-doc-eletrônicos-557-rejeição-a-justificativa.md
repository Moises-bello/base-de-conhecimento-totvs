---
article_id: 360051139834
category: NFe - Nota Fiscal Eletrônica
content_hash: a39e5333e6b9fe2274890e32611dfa946a7885f8ebe7c307ffe0896a62aafa20
fetched_at: '2026-06-28T22:40:05.130539+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 557 Rejeição :
  A justificativa de entrada em contingencia deve ser informada'
type: support-article
updated_at: '2021-08-23T18:20:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051139834-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-557-Rejei%C3%A7%C3%A3o-A-justificativa-de-entrada-em-contingencia-deve-ser-informada
---

**Dúvida**  
557 Rejeição : A justificativa de entrada em contingencia deve ser informada.

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**Esta rejeição ocorre quando ao configurar a transmissão da nfe para contingência, não é informada a justificativa/motivo da entrada em contingencia.   
Ao escolher qualquer Modalidade diferente de **Normal** em **Outras Ações/Parâmetros/NFe,** deverá informar uma justificativa.  
  
\*Vale lembrar que o texto precisar ser maior que 15 caracteres e não pode conter caracteres especiais.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080885773/mceclip2.png)

Esta é uma informação exigida pela Sefaz e sua falta causa rejeição, vide **pág.236** do **Manual de Orientação do Contribuinte versão 6.0.**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079819694/mceclip0.png)**

Para correção, basta escolher novamente a modalidade de contingência que a nota rejeitada foi transmitida, informar a justificativa e retransmitir a nota nesta mesma modalidade.

Após a retransmissão, retorne a configuração para a modalidade que estava antes.
