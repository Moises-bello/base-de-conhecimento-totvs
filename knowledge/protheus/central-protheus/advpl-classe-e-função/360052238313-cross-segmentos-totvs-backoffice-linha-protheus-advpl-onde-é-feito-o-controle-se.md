---
article_id: 360052238313
category: ADVPL - Classe e Função
content_hash: 39436be0b7760e86571285b542b1a325856c9e1b90cf33263796218e80e27766
fetched_at: '2026-06-28T22:40:20.546746+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Onde é feito o
  controle sequencial da função GetNextAlias
type: support-article
updated_at: '2022-01-11T17:57:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052238313-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Onde-%C3%A9-feito-o-controle-sequencial-da-fun%C3%A7%C3%A3o-GetNextAlias
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Onde é feito o controle sequencial da função GetNextAlias()?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
 **Solução**O **GetNextAlias()** retorna um código para ser utilizado basicamente pelo **dbUseArea**.  
Ele cria um sequenciador em uma variável ***static***, desta maneira possuindo um contatador por ***thread*** do sistema.  
Esse contador é incrementado a cada chamada da rotina, sendo retornado ao valor de   
**000001 ao atingir 999999.**
