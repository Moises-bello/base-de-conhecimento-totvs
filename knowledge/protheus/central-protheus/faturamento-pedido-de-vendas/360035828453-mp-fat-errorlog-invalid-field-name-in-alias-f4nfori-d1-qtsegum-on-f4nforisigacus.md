---
article_id: 360035828453
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 4dc85129abb6022c5f6f39f037e97fcbb51b4cc7c30bd5942b1189c8b1aef67b
fetched_at: '2026-06-28T22:38:41.228595+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: MP - FAT - Errorlog invalid field name in Alias F4NFORI->D1_QTSEGUM on F4NFORI(SIGACUS.PRW)
type: support-article
updated_at: '2021-04-28T15:50:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035828453-MP-FAT-Errorlog-invalid-field-name-in-Alias-F4NFORI-D1-QTSEGUM-on-F4NFORI-SIGACUS-PRW
---

**Ocorrência****:**

***invalid field name in Alias F4NFORI->D1\_QTSEGUM on F4NFORI(SIGACUS.PRW)***  
  
**Ambiente**

Protheus – A partir da versão 11.80.

**Causa**

Ao tentar fazer uma nota de devolução, selecionamos o campo **NF ORIGINAL** (para vincular com a NF original) e ao apertar o botão **F4**, é exibido o errolog:   
***invalid field name in Alias F4NFORI->D1\_QTSEGUM on F4NFORI(SIGACUS.PRW)***

O erro ocorre devido a erro na estrutura do campo D1\_QTSEGUM.  
  
**Solução**

Para solucionar o errorlog, verifique se o campo **D1\_QTSEGUM**esta conforme estrutura abaixo, caso não esteja , será necessário recriar, utilizando **UPDDISTR** com um dicionário padrão baixado do portal do cliente.  
Segue abaixo a estrutura do campo, caso seja preciso criá-lo (ou deixar como padrão):  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001072042/mceclip0.png)​  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001148681/mceclip1.png)  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102153833/mceclip2.png)  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001072102/mceclip3.png)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099972734/mceclip4.png)
