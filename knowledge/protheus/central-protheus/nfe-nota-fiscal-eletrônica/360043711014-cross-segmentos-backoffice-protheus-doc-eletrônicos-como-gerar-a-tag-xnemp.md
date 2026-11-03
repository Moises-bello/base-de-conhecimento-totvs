---
article_id: 360043711014
category: NFe - Nota Fiscal Eletrônica
content_hash: 64437813affe1bca463938b7040ecf017e1d929b0f6a76b6788a82b81a434882
fetched_at: '2026-06-28T22:40:00.197209+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: '  Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar a
  TAG xNEmp '
type: support-article
updated_at: '2021-08-10T14:57:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043711014--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-a-TAG-xNEmp
---

**Dúvida**Como gerar a TAG xNEmp ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**​  
1- Para gerar a TAG habilitar o parâmetro no configurador:

* **MV\_NFORGPU=** .T.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042828414/mceclip0.png)

2- Para gerar a TAG configurar o parâmetro conforme abaixo:

* **MV\_SPEDNAT=** .F.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043668053/mceclip1.png)

3- Informar no campo **Nt Empenho** **C5\_NTEMPEN** o número do documento que será gerado nessa nota com série mais número.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043668293/mceclip2.png)

* A TAG é gerada **conforme o exemplo abaixo:**  
    
  ![](https://totvssuporte.zendesk.com/attachments/token/bFGIdkzll0beuUydDDNfJaWzp/?name=inline445464377.png)
