---
article_id: 5769030436503
category: Comércio Exterior - Easy Import Control - Miscelanea
content_hash: a912c718864f8482bbaafacce9b994360a03841f71645c4ba36509185c08eedd
fetched_at: '2026-06-28T22:39:42.062582+00:00'
product: protheus
section_id: 1500001549702
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Aplicação da mercadoria
  no arquivo txt de integração com o despachante
type: support-article
updated_at: '2022-04-29T16:51:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5769030436503-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Aplica%C3%A7%C3%A3o-da-mercadoria-no-arquivo-txt-de-integra%C3%A7%C3%A3o-com-o-despachante
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Qual o critério para que o campo aplicação da mercadoria seja enviado no arquivo txt de integração com o despachante?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – *Easy Import Control* – Todas versões  
  
**Solução**A aplicação da mercadoria só será enviada no arquivo txt de integração com o despachante nos casos em que a classificação da mercadoria (W1\_CLASS) seja igual a consumo ou revenda. Caso a classificação da mercadoria seja igual a consumo, será enviado 1 e caso seja igual a  revenda, será enviado 2 para o arquivo txt. Para os casos em que a classificação da mercadoria seja diferente de consumo ou revenda, a posição referente a aplicação da mercadoria ficará em branco.  
  
**Saiba mais**   
[Layout de integração de arquivos txt – SIGAEIC](https://tdn.totvs.com/pages/releaseview.action?pageId=394220995)
