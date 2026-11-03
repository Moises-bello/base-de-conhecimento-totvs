---
article_id: 16618587210263
category: Escrita Fiscal - Configurador de Tributos
content_hash: c0af26c842ecd4cfdaba55a4edbf074d241c7d0de065fbdc43237291d9d83374
fetched_at: '2026-06-28T22:39:17.446445+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como descontar
  do ICMS diferido da base do PIS/COFINS?
type: support-article
updated_at: '2026-02-13T11:53:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16618587210263-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-descontar-do-ICMS-diferido-da-base-do-PIS-COFINS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16618619228183) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como descontar do ICMS diferido da base do PIS/COFINS?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**Composição do valor do icms Diferido 100%  
   
Valor da mercadoria = 1750,00  
Alíquota do ICMS = 18%  
Valor do ICMS = 315,00  
Diferido = 100%  
Base de calculo do Pis e Cofins = 1435,00  
Alíquota do PIS = 1,65% = 23,67  
Alíquota do Cofins = 7,6% = 109,06  
Valor do Custo = 1617,27  
   
Para essa nota fiscal precisa tratar ICMS DIFERIDO / PIS / COFINS pelo configurador  
   
FISA170  
TRIBUTO  
   
![](https://totvssuporte.zendesk.com/attachments/token/pc47VGePro5p8YKNzUkbmoALc/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/ldrwQVemqZd01rtoqCW0Bk2Wh/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/283ypNfcKnxpBjHs0Dq7c1eOj/?name=image.png)  
   
**Perfis**  
   
Perfil do  Produto  
   
![](https://totvssuporte.zendesk.com/attachments/token/Xkbsvt9Fvunu8N7qr4bF1GLfT/?name=image.png)  
   
Perfil de Operação  
   
![](https://totvssuporte.zendesk.com/attachments/token/OTNui10tJxMJbmKduviVGEcHu/?name=image.png)  
   
Perfil Participante  
![](https://totvssuporte.zendesk.com/attachments/token/O48RA4SAURCUQpkLcb02q4iaS/?name=image.png)  
   
Perfil Origem / Destino = 000001  
   
![](https://totvssuporte.zendesk.com/attachments/token/YhRGL9dOT84MUGHWbTDvlgDe0/?name=image.png)  
   
Regra base de calculo ICMS = 000035  
![](https://totvssuporte.zendesk.com/attachments/token/y9kOzRVKu8rseb3lX8salEAwU/?name=image.png)  
   
Regra Alíquota do ICMS  
   
![](https://totvssuporte.zendesk.com/attachments/token/lRslgXkpEvje61Sms6rutu24j/?name=image.png)  
   
Regra de  Escrituração  = 000035  
   
![](https://totvssuporte.zendesk.com/attachments/token/QqCJSElNg90DSxdyXj055P4wJ/?name=image.png)  
   
Regra de Calculo Documento Fiscal = 000035  
   
![](https://totvssuporte.zendesk.com/attachments/token/maorhEpdW9QWzZQdGeCHCbeNv/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/Ro90RILdvtnq5gIuQ6bHMZ1OG/?name=image.png)![](https://totvssuporte.zendesk.com/attachments/token/q8pk53d82HdxMyUQi9FyVzKuf/?name=image.png)  
Formula  
![](https://totvssuporte.zendesk.com/attachments/token/qcx1v08sOlI9vyMLmLl4FBmHX/?name=image.png)  
   
lançamento da nota fiscal no mata103  
   
![](https://totvssuporte.zendesk.com/attachments/token/IgIPEb3Cknim4It9SBt8hdd5Q/?name=image.png)  
   
Regra de base de calculo PIS = 000036  
   
![](https://totvssuporte.zendesk.com/attachments/token/cgMlMOr6qLBLts7IRdenHJvvy/?name=image.png)  
   
Formula  
   
![](https://totvssuporte.zendesk.com/attachments/token/cHd5Y0GkhrARuBEWpDXoZYBML/?name=image.png)  
   
Regra de alíquota do PIS = 000036  
![](https://totvssuporte.zendesk.com/attachments/token/N4SnxQZwgx4x2TGE8u8QvadBK/?name=image.png)  
Regra de Escrituração do PIS = 000036  
   
![](https://totvssuporte.zendesk.com/attachments/token/GVJp8vplmBJZxkzr9k4u6wpFM/?name=image.png)  
   
Regra de calculo Documento Fiscal = 000036  
   
![](https://totvssuporte.zendesk.com/attachments/token/ihBl96w1uNxLAlk0L1R1mk5KO/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/sLOK3pGECCZU4LlVJ699PJ7A3/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/kQjpZcBD8aoA32hmf0xfKq5Sp/?name=image.png)  
Formula  
![](https://totvssuporte.zendesk.com/attachments/token/89KnNVBQKKA8CBS3zRxEXXIyZ/?name=image.png)  
   
Documento Fiscal  
   
![](https://totvssuporte.zendesk.com/attachments/token/WYJY8XQpDfxaG0DY3W2ASzeCO/?name=image.png)  
   
Regra da base de calculo do Cofins = 000037  
![](https://totvssuporte.zendesk.com/attachments/token/VRWbVvpheejl4KxN7cbaw4kTm/?name=image.png)  
Formula  
   
![](https://totvssuporte.zendesk.com/attachments/token/fPdHnGdywIsivzcj6orCFXdL0/?name=image.png)  
   
Regra da Alíquota do COFINS = 000037  
   
![](https://totvssuporte.zendesk.com/attachments/token/jbSPAHp03LUcBmR612QPHu0HY/?name=image.png)  
   
Regra de escrituração do COFINS = 000037  
   
![](https://totvssuporte.zendesk.com/attachments/token/pDtlbM2mu3XZgHgwoFRhMSY2S/?name=image.png)  
   
   
Regra de calculo Documento Fiscal = 000037  
   
![](https://totvssuporte.zendesk.com/attachments/token/hOzVnq4DJuDLZGygaxKPoNqDk/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/4hf5Xp4iBrBA6wgNcuhfGP2WV/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/I5yKNNXrn4da45wb2fLZzGWBs/?name=image.png)  
Documento de entradas  
   
![](https://totvssuporte.zendesk.com/attachments/token/xHH6Ze9M8Ao4R96wUva4lyTNb/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/mrxZBor37cSSBrJCvAL2b0PzJ/?name=image.png)  
   
   
Custo na SD1  
   
![](https://totvssuporte.zendesk.com/attachments/token/ljKbUpK4q8t1xjRr8QU4HqpsZ/?name=image.png)  
   
   
Configuração da TES para o calculo correto  
   
![](https://totvssuporte.zendesk.com/attachments/token/qJGLOduw7n4w0JPEHFXjC51b5/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/w5QlZ2Cl7sjBheFPZyOD0epF3/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/gpzrbSlZoSyx0uBkOLu0QJQaq/?name=image.png)
