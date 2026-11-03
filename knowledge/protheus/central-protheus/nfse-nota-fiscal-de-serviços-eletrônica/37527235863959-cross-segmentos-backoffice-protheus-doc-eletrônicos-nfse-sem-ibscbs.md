---
article_id: 37527235863959
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: e788283eeb7e3de8b44ec3f5dd0b2743c9b3d4ac26ff3ad889b63c739c43da32
fetched_at: '2026-06-28T22:39:58.672115+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE sem IBS/CBS
type: support-article
updated_at: '2026-04-01T19:32:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37527235863959-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-sem-IBS-CBS
---

**Dúvida**   
Como configurar o Protheus para que as NFse sejam transmitidas sem considerar IBS e CBS?

**Ambiente**   
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões

**Solução**  
Gostaria de reforçar que algumas prefeituras flexibilizaram o envio das novas tags da reforma tributária IBS/CBS, estendendo a data de obrigatoriedade para 01/04/2026. Dessa forma, as NFSE podem ser geradas sem incluir os valores e informações dos novos tributos.

**PARAMETRIZAÇÕES**

Foi criado o parâmetro **MV\_RTCNFSE** com valor padrão **01/01/2026** nos fontes do TSS, que corresponde à data de início da obrigatoriedade para geração das novas tags de **IBS/CBS**.  
  
Se desejar **adiar os envio com as novas TAGs IBS/CBS**, é necessário configurar o valor do parâmetro com uma data **posterior à data atual** na tabela SPED000 do TSS, conforme o exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37527204919063)
