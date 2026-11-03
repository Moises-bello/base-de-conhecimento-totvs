---
article_id: 360052837914
category: RH - Dissídio
content_hash: 8911b4c8b2175269360d03b64af7e5c16f2fd979c9d74422264fd48782101a60
fetched_at: '2026-06-28T22:43:44.295170+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Percentual duplicado sobre a verba de salário -
  id 0031 no cálculo de dissídio
type: support-article
updated_at: '2021-04-30T00:21:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052837914-RH-Linha-Protheus-GPE-Percentual-duplicado-sobre-a-verba-de-sal%C3%A1rio-id-0031-no-c%C3%A1lculo-de-diss%C3%ADdio
---

**Ocorrência**Ao calcular o dissídio o Sistema aplica duas vezes o mesmo percentual informado nos parâmetros para verba de salário - ID 0031.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Causa**O Sistema aplica o percentual de dissídio duas vezes sobre o salário quando os dois campos de cálculo na configuração da verba na aba Dissídio estão preenchidos com Sim.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087946073/mceclip0.png)  
  
**Solução**O campo Recal. lan. vl só deve estar com Sim para verbas em valor e sem identificador de cálculo.   
Essa é a configuração correta para a verba de salário:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360086806374/mceclip0.png)  
  
Faça o ajuste do campo com a rotina de dissídio fechada, exclua o cálculo e calcule novamente para corrigir o valor.  
  
**Saiba mais:** <https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio>
