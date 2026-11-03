---
article_id: 360018924192
category: Ativo Fixo - Baixa e Baixa de Adiantamento
content_hash: 7877ff66f4d1e7515505afe63213fded68da493bd9b06fbf29991b8edb65dd50
fetched_at: '2026-06-28T22:41:55.568354+00:00'
product: protheus
section_id: 1500001535901
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF - O QUE CAUSA O HELP:
  AF010JABAI?'
type: support-article
updated_at: '2022-11-28T18:17:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018924192-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-O-QUE-CAUSA-O-HELP-AF010JABAI
---

**Dúvida** **O QUE CAUSA O HELP: AF010JABAI?**

![](https://totvssuporte.zendesk.com/attachments/token/jAidopZxO452uTsq9hogjoiwb/?name=inline1709129354.png)  
  
**Ambiente**

# Cross Segmento - Backoffice Linha Protheus -  Ativo Fixo  – A partir da versão P12

**Solução**

Quando o  Bem está com o campo **N3\_BAIXA** em ' Branco', será validado e apresentado o Help acima, no padrão os campos terão as opções:  0(não baixado) e 1(baixado)

Para correção a base de dados, é necessário executar o UPDDISTR com os dicionários Completo e Diferencial.
