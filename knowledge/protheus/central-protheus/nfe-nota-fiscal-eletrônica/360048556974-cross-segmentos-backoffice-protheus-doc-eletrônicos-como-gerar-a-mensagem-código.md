---
article_id: 360048556974
category: NFe - Nota Fiscal Eletrônica
content_hash: e12cd26dec0334d83ae707d430075b8b630648ee363696167c6b9f16221ca436
fetched_at: '2026-06-28T22:40:01.667874+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar a mensagem
  "Código Suframa: 999999999"'
type: support-article
updated_at: '2021-08-17T19:44:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048556974--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-a-mensagem-C%C3%B3digo-Suframa-999999999
---

**Dúvida**

Como gerar a mensagem Código Suframa com a inscrição do destinatário ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1- Será necessário que o parâmetro **MV\_SUFRAMA = .T.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049705833/mceclip0.png)

2- Preencher no cadastro de cliente o campo **Suframa A1\_SUFRAMA**com a inscrição

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048809114/mceclip1.png)

**Será gerado no XML:**

* TAG **ISUF conforme o exemplo abaixo:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073214533/mceclip0.png)**

* TAG **InfAdic conforme o exemplo abaixo:**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073214773/mceclip2.png)**

* **Saiba mais:**

Para configuração de suframa há o link abaixo:

<http://tdn.totvs.com/pages/releaseview.action?pageId=185751494>

1- Além disso, Configurar no  **TES** no campo **Sit. trib. ICMS** **F4\_SITTRIB =**40, 41 ou 50 ou quando houver calculo de ICMS-ST no campo **Sit. trib. ICMS** **F4\_SITTRIB =**= 30

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041920134/mceclip2.png)

2- Preencher no**TES** na Aba **Outros**o campo **Mot. Desone.** F4\_MOTICM = 7- Suframa

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042764713/mceclip3.png)
