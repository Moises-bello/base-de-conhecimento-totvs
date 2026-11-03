---
article_id: 360012315132
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 0cc26f3444ea02d2dcd1b8c9e974da98435dc12b2e2dbb6bea7206838cdc026f
fetched_at: '2026-06-28T22:39:56.455624+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Discriminação
  de Serviço com mais de 250 caracteres
type: support-article
updated_at: '2025-05-22T18:35:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012315132-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Discrimina%C3%A7%C3%A3o-de-Servi%C3%A7o-com-mais-de-250-caracteres
---

**Dúvida**Como informar a **Discriminação de Serviço** com mais de 250 caracteres?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Para que seja informado uma discriminação de serviços com mais de 250 caracteres, realize as configurações abaixo em seu ambiente:  
  
**1.** Crie um campo do tipo 'MEMO' na tabela SC5 para utilizar como discriminação dos serviços.

**2.** Configure os parâmetros abaixo:

**MV\_NFSEMOD** = **.T.**  
**MV\_NFEDESC** = **.F.** *(concatena com a descrição do X5\_DESCRI )* ou **.T.** *(somente o conteúdo do campo MEMO).*  
**MV\_NFESERV** = **1**  
**MV\_CMPUSR** = Informe o nome do campo do tipo MEMO criado na tabela SC5.  
  
Exemplo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069873733)

**3.** Após isso, valide incluindo um novo pedido de vendas e preenchendo o campo com a discriminação desejada.
