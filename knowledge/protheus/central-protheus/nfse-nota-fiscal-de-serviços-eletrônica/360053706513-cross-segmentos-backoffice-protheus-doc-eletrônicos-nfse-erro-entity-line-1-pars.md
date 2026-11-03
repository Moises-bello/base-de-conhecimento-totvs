---
article_id: 360053706513
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: f9bc96aa7825091db0383690969032fe5c865fecc165803947b54c9ade082aa5
fetched_at: '2026-06-28T22:39:57.423674+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Erro: Entity:
  line 1: parser error : Input is not proper UTF-8, indicate encoding !'
type: support-article
updated_at: '2025-06-25T14:15:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053706513-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Erro-Entity-line-1-parser-error-Input-is-not-proper-UTF-8-indicate-encoding
---

**Ocorrência**Ao realizar a transmissão de um RPS ocorre o erro abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088415533/mceclip0.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Causa**Esse erro ocorre quando está sendo utilizado algum carácter especial ou um carácter não aceito pelo ERP dentro do conteúdo da nota.

**Solução**Para correção deverá remover esse conteúdo, redigitando novamente (evitando copiar e colar de algum local).  
O erro sempre indicará o local exato aonde está o problema (tag + conteúdo).  
Se observar na imagem acima, o erro está ocorrendo na tag <discr> utilizada para informar a discriminação de serviço, onde logo após o carácter **0** procede com um carácter inválido (causador do erro), como ele não é convertido corretamente não é apresentado na imagem.
