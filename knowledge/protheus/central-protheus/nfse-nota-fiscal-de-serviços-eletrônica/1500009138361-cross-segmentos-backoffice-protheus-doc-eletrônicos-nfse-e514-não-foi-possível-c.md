---
article_id: 1500009138361
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 4a2bd95f0e895b9dead5d3190a28526989c757a41d5c7adbb0d3f6c6ae643fd0
fetched_at: '2026-06-28T22:39:57.378683+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - E514 - Não
  foi possível converter os dados do XML enviado
type: support-article
updated_at: '2025-07-08T19:51:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009138361-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-E514-N%C3%A3o-foi-poss%C3%ADvel-converter-os-dados-do-XML-enviado
---

**Ocorrência**Ao realizar a transmissão de um RPS ocorre a rejeição: 'E514 - Não foi possível converter os dados do XML enviado'.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Causa**Essa rejeição é causada quando utilizado algum tipo de caractere especial no conteúdo da nota.  
  
**Solução**Para correção, precisará remover qualquer tipo de caracteres(s) especial do XML.  
Geralmente está presente dentro da discriminação de serviços, exemplo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013959461/mceclip0.png)  
  
Porém poderá também estar presente nos dados do cliente ou do prestador, por este motivo é importante validar o próprio XML para identificação.
