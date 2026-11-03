---
article_id: 360026432472
category: BI - Business Intelligence - Smart analytics
content_hash: 2a446e78f403229b3da532831d0ace3b9bb77d51a736c1d6eb9560cecb7023e8
fetched_at: '2026-06-28T22:37:04.150242+00:00'
product: protheus
section_id: 1500001539741
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Extração do gooddata
  para TES que não gera duplicata
type: support-article
updated_at: '2022-07-27T18:08:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026432472-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Extra%C3%A7%C3%A3o-do-gooddata-para-TES-que-n%C3%A3o-gera-duplicata
---

**Dúvida**As notas de simples remessas que não deveriam ser extraídas estão subindo para o GoodData impactando no faturamento.**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Smart Analytics – A partir da versão 12  
  
**Solução**Este problema ocorre quando o parâmetro do Wizard do Extrator BI **"Considerar notas em que a TES gera duplicata"** está como **"Ambos"** ou **"Não".  
  
Configure o parâmetro conforme imagem abaixo:****![TES.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360026028471/TES.PNG)**

Desta forma, as notas em que o **TES** correspondente estiver configurado para **não gerar duplicata**, não subirão para o **GoodData**.
