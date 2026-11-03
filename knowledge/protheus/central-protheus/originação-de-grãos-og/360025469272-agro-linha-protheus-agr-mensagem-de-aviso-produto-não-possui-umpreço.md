---
article_id: 360025469272
category: Originação de Grãos (OG)
content_hash: bf6aa3558b7e23dd88cf77bcbc15da6001f4a591eb67407feee71766d1759bb9
fetched_at: '2026-06-28T22:45:40.999084+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Mensagem de Aviso Produto não possui UM.preço
type: support-article
updated_at: '2025-06-21T16:13:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025469272-Agro-Linha-Protheus-AGR-Mensagem-de-Aviso-Produto-n%C3%A3o-possui-UM-pre%C3%A7o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20613344484375)***Tempo aproximado para leitura: **00:01:35****min****Ocorrência**Ao acessar os **Contratos de Compra**, **Venda** ou **Outros** - **OGA280 - Contrato de Compra**, **OGA290 - Contrato de Venda** e **OGA260 - Contrato de terceiro**, ao informar o campo de **Cod. Produto**, é retornada uma mensagem de ajuda com um alerta: **Produto não possui UM.Preço**.

![pre_.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360064432854)

**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Causa**Essa mensagem ocorre, pois o produto não foi configurado corretamente no cadastro de produto, para ser utilizado no módulo **Originação de Grãos**.  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
**1.** É necessário cadastrar o produto na rotina de **Complemento do Produto - MATA180**;

![f1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360024550092)

**2.** Em seguida, na pasta **Agro,** informar a**Unidade de Medida do Preço.**

![f2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360024550332)  
  
![f3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360024564291)

**3.** Após essas alterações o alerta não será mais exibido.
