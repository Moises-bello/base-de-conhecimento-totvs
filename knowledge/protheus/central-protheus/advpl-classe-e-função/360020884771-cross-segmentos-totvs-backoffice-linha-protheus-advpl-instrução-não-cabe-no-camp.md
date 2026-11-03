---
article_id: 360020884771
category: ADVPL - Classe e Função
content_hash: 73653ae045fc29df5bb8fdc2d5ae7b563de8934c0aeca84232c6a48c9ae66285
fetched_at: '2026-06-28T22:40:20.452158+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Instrução não cabe
  no campo do gatilho ou formulas
type: support-article
updated_at: '2022-01-11T22:34:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020884771-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Instru%C3%A7%C3%A3o-n%C3%A3o-cabe-no-campo-do-gatilho-ou-formulas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Ao utilizar a rotina de formulas ou gatilho a instrução não cabe no campo destinado a este fim. Como deve proceder?   
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Ao utilizar tanto a rotina de Formulas ou Gatilho, pode ser que a instrução que passamos seja maior que o tamanho do campo dispõe, para este caso é sugerido a criação de uma User Fuction com toda a operação necessária a ser realizada naquele momento.

**Exemplo**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360017383152/mceclip1.png)

```
#include 'protheus.ch'  
#include 'parmtype.ch'  
  
user function FONT()  
//Minha Instrução.  
  
Return
```
