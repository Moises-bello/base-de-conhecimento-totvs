---
article_id: 360019551152
category: ADVPL - Classe e Função
content_hash: 60449f4039ee85f40a86668e4456017e967a50dce98cc87fd08b2474f3e56202
fetched_at: '2026-06-28T22:40:20.530485+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Não arredondar
  valores com mais de oito digitos
type: support-article
updated_at: '2022-06-01T18:23:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019551152-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-N%C3%A3o-arredondar-valores-com-mais-de-oito-digitos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Quando retornado um valor com mais de oito casas decimais, esse valor está sendo arredondado na 8ª casa.  
  
**Ambiente**  
Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Causa**Por padrão, o Protheus exibe até oito casas decimais, assim sendo, normalmente os valores com mais de oito casas decimais acabam sendo arredondados na 8ª casa.  
  
**Solução**Para aumentar a quantidade de casas decimais para mais que oito e até quinze dígitos, utilize a chave FLOATINGPOINTPRECISE = 1 na seção GENERAL.  
  
**Saiba mais**  
[FLOATINGPOINTPRECISE](http://tdn.totvs.com/display/tec/FloatingPointPrecise)
