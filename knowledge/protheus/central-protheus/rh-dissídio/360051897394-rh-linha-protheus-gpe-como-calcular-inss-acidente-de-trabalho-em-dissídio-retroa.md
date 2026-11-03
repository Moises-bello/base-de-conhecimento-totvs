---
article_id: 360051897394
category: RH - Dissídio
content_hash: 587d5f53a61fb65b729abf2f21d8d9491774b8c6932a7917b0edfd2ab8fc24dc
fetched_at: '2026-06-28T22:43:43.259003+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular INSS acidente de trabalho em dissídio
  retroativo quando houve mudança de percentual
type: support-article
updated_at: '2025-09-11T11:29:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051897394-RH-Linha-Protheus-GPE-Como-calcular-INSS-acidente-de-trabalho-em-diss%C3%ADdio-retroativo-quando-houve-mudan%C3%A7a-de-percentual
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32612827957143)**Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como calcular INSS acidente de trabalho em dissídio retroativo quando houve mudança de percentual?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**O RAT ajustado (Acidente de Trabalho) sempre será calculado com o percentual atual da tabela S037, sobre a diferença do dissidio, para atender o cálculo efetuado pelo e-Social, desde que na S037 tenha o histórico referente ao período do cálculo do Dissidio.

**Exemplo: Calculo do dissidio para o periodo de 10/2024 a 02/2025 onde em 01/2025 ocorreu alteração da aliquota do Acidente de trabalho**

**Tabela S037**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32612799753751)

Na tabela S037 preencher o histórico com o mês e ano que irá calcular o dissidio.

No cálculo do dissídio retroativo, o sistema irá considerar a diferença do dissidio com percentual atual (3,8847%), ignorando o percentual da época de acordo com o E-social.

**Calculo Dissidio**

Valor Origem 6.200,00 \* 3,3696% = 208,92

**Valor Calculado 230,02 \* 3,8847% = 8,94**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32612799756695)**

**OBS:**Em casos que o percentual atual for menor que o percentual aplicado na época, também será calculado sobre a diferença do dissidio considerando o percentual atual.

Abaixo a documentação oficial da Consultoria de Segmentos , sobre a alteração no produto para atender o cálculo de acordo com o E-social:   
[Orientação Consultoria de Segmentos - Dissídio Retroativo](https://tdn.totvs.com/pages/releaseview.action?pageId=746496020)

**Saiba Mais:**

[Pagina Centralizadora Dissidio Retroativo](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)

####
