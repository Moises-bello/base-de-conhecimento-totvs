---
article_id: 360026157632
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: cca0bf07f6adad3eaeb7e68bde609daa85e4e01b8a5a1492e7849670a401eaa5
fetched_at: '2026-06-28T22:39:56.463305+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Discriminação
  Retenção e/ou Dedução Varginha - MG
type: support-article
updated_at: '2025-07-08T20:02:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026157632-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Discrimina%C3%A7%C3%A3o-Reten%C3%A7%C3%A3o-e-ou-Dedu%C3%A7%C3%A3o-Varginha-MG
---

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025624872/mceclip1.png)

**3.** Criar o parâmetro "Descrição da Dedução" (MV\_DISCDED).  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025640491/mceclip2.png)  

 O conteúdo do parâmetro deverá ser o campo que criado no item anterior.  
  
  
**4.** Incluindo o documento na rotina Pedido de Venda (MATA410.PRX).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025625092/mceclip3.png)  
  
  
O campos abaixo deverão ser preenchido:  
• "xDesc Deducao" (customizado) Descrição da Dedução.  
• "Abatim ISS" e "Abat. Mat" (Padrão) para ser calculado dedução.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025625152/mceclip4.png)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025625212/mceclip5.png)  
  

2.Rotina de Transmissão da NFSe (FISA022.PRW), preencher os parâmetros do documento a ser gerado.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025625292/mceclip6.png)

Processo realizado com sucesso.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025640871/mceclip7.png)  
  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025625432/mceclip0.png)

3.Arquivo texto

Na tag "DiscrDed" a descrição do campo Customizado foi gerado no arquivo com sucesso.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025625532/mceclip2.png)  
  
**4.**Conforme manual NFS-e arquivo texto, o conteúdo da tag "DiscrDed" (Discriminação de retenção e/ou dedução) será gerada somente se a tag "VlDed" (Valor de Dedução) for maior que zero, com isso, mesmo que o parâmetro esteja preenchido somente será exibido conforme regra do manual.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025641191/mceclip3.png)

Caso a descrição não seja apresentada no documento, verifique se os parâmetros abaixo estão validados corretamente:

MV\_NFSEDED = .T.
