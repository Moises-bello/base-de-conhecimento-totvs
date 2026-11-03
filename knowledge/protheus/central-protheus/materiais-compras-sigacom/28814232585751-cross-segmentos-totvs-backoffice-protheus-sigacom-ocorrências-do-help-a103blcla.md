---
article_id: 28814232585751
category: Materiais - Compras (SIGACOM)
content_hash: a58b32673d2e99d2dbc81539a7c2ffc5626df34f93d3ed40e98e6f6187a4da5c
fetched_at: '2026-06-28T22:41:22.023381+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Protheus - SIGACOM - Ocorrências do help
  A103BLCLA
type: support-article
updated_at: '2024-12-27T17:53:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28814232585751-Cross-Segmentos-TOTVS-Backoffice-Protheus-SIGACOM-Ocorr%C3%AAncias-do-help-A103BLCLA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28814211808919) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Quais são as causas da ocorrência do help A103BLCLA?  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28814211809815)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - a partir da 12.1.33  
  
**Solução**

O help A103BLCLA é gerado quando tentamos classificar uma nota que está bloqueada por Tolerância de Recebimento. Dessa forma, temos duas alternativas:

1. Liberamos essa nota na MATA094  
[Como utilizar tolerância de recebimento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006558892-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-utilizar-a-Toler%C3%A2ncia-de-Recebimento-no-m%C3%B3dulo-de-Compras)  
  
2. Alteramos o conteúdo do parâmetro MV\_RESTCLA para 2

[Funcionamento do parâmetro MV\_RESTCLA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006558892-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-utilizar-a-Toler%C3%A2ncia-de-Recebimento-no-m%C3%B3dulo-de-Compras)

MV\_RESTCLA=2, permite a classificação da NF bloqueada por tolerância de recebimento  
MV\_RESTCLA=1 não permite classificação, a liberação deve ser efetuada através da rotina de Liberação - MATA094.

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
