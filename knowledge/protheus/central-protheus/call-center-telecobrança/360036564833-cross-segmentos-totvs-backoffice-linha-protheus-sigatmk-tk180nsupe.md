---
article_id: 360036564833
category: Call Center - Telecobrança
content_hash: 6045a4d145b889e10e12a2947340d1f47be990bd3d7b551124c27a93cac7d3a9
fetched_at: '2026-06-28T22:41:28.684294+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK- TK180NSUPE
type: support-article
updated_at: '2022-06-22T17:27:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036564833-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-TK180NSUPE
---

**Dúvida**

Ao tentar consultar o monitor do Supervisor é gerado um help: TK180NSUPE

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047146574/mceclip1.png)

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK- todas as versões.  
  
**Solução**

O help ocorre sempre que se tenta acessar o monitor do supervisor (**TMKC030**) como operador.

Desta forma, certifique-se no cadastro do operador (**TMKA090**) , no campo **U7\_TIPO**,  que o operador que está acessando a rotina seja um **Supervisor** e assim, o help não será exibido no acesso da rotina.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047147294/mceclip3.png)
