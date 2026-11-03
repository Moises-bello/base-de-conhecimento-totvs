---
article_id: 360047561434
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 4e305aad8ff0c03b9bf32af6516c5cab3dcbeda6b37153e31876f92a95425cc3
fetched_at: '2026-06-28T22:38:32.696166+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP-FAT-type mismatch on compare  on CANPROCITVL(CTBXSEM.PRW) '
type: support-article
updated_at: '2021-04-28T15:53:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047561434-MP-FAT-type-mismatch-on-compare-on-CANPROCITVL-CTBXSEM-PRW
---

**Ocorrência**

Ao efetuar a contabilização off-line(**CTBANFS**), ocorre o erro:

**type mismatch on compare  on CANPROCITVL(CTBXSEM.PRW) 31/03/2020 09:58:44 line : 493**  
   
 **Ambiente**

Microsiga Protheus - todas as versões.  
   
 **Causa**

O erro ocorre por que o parâmetro **mv\_ctbsert** está como carácter, sendo o correto numérico.  
   
 **Solução**

Efetue o ajuste no parâmetro, via Configurador, Ambiente, Cadastros, Parâmetros, o deixando com o tipo numérico ao invés de carácter, desta forma, o erro deixará de ocorrer.

![](https://totvssuporte.zendesk.com/attachments/token/axlBrQvrvKwfqxqNVWzv7laae/?name=inline483571140.png)
