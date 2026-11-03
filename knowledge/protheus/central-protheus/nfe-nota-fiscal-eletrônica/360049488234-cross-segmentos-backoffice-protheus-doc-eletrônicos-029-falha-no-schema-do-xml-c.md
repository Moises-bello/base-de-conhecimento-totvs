---
article_id: 360049488234
category: NFe - Nota Fiscal Eletrônica
content_hash: 1c3e75c69f798277d330b329642fc84b02c754cbf95898af74deefe206cbd24a
fetched_at: '2026-06-28T22:40:00.415603+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 029 : Falha no
  schema do XML, com schema válido'
type: support-article
updated_at: '2024-08-07T21:07:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049488234--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-029-Falha-no-schema-do-XML-com-schema-v%C3%A1lido
---

**Dúvida**Como identificar a crítica do schema quando ocorre a mensagem 029: Falha no schema do XML, mas ao clicar em schema para visualizar a crítica, retorna schema válido?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Após transmitir uma nota que retorne 029: Falha no schema do XML, mas ao clicar em **Schema** para visualizar a crítica, apresenta **Schema válido**, conforme print a seguir:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075408313/mceclip0.png)

Este incidente, geralmente, está relacionado ao uso de caracteres especiais na nota.

Para que consiga identificar a crítica do xml acesse o console log do TSS, logo após a ocorrência acima, e procure pelas palavras **Falha de Schema**.

Conforme print abaixo, após identificar a tag e o conteúdo criticado, corrija e retransmita a nota.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075409433/mceclip1.png)

Caso o incidente persista ou não esteja encontrando a causa da falha de schema, abra um ticket no Suporte Totvs anexando o xml com a falha, para análise da equipe de NFe/TSS.
