---
article_id: 360056057273
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: f3555e0b798abf093e241a641161435160f17ed0b4a9070584e4deddae7bb393
fetched_at: '2026-06-28T22:39:58.641687+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - WSCERR064
  / Invalid Content-Type return. 403 Forbidden (São Paulo)
type: support-article
updated_at: '2025-06-20T11:42:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056057273-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-WSCERR064-Invalid-Content-Type-return-403-Forbidden-S%C3%A3o-Paulo
---

**Ocorrência**Ao transmitir ou realizar a consulta de um RPS pela prefeitura de São Paulo, ocorre o erro: **"007-Falha ao tentar consultar o RPS. WSCERR064 / Invalid Content-Type return... 403 Forbidden..."**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093847733/mceclip1.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Causa**Esse incidente ocorre quando o certificado digital que está sendo utilizado está vencido ou não foi configurado corretamente dentro da rotina **FISA022**.  
  
**Solução**Para correção deverá refazer o Wizard.cfg por completo dentro da rotina **FISA022**, importando um Certificado Digital válido. Feito isso basta realizar novos testes.  
  
*Obs.: Vale lembrar que esse erro vale tanto para consulta RPS quanto para a própria transmissão em si.*
