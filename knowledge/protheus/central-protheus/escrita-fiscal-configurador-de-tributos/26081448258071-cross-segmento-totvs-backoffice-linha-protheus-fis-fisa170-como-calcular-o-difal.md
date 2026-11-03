---
article_id: 26081448258071
category: Escrita Fiscal - Configurador de Tributos
content_hash: b716e74adad9e0f542cb7b0cd0e38ec0386181ddd21c4fc077776e7a97c2106b
fetched_at: '2026-06-28T22:39:17.359555+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como calcular
  o Difal EC/87 com base dupla?
type: support-article
updated_at: '2025-11-07T22:09:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26081448258071-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-o-Difal-EC-87-com-base-dupla
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26081448238487) Tempo aproximado para leitura: **08:00min** **Dúvida**Como calcular o Difal EC/87 com base dupla  nas saídas no Fisa170?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Calculo Difal ec/87 com base dupla  
   
Venda de SP para DF  
Alíquota 7%  
Alíquota 20%  
   
Valor da mercadoria = 29,90  
Base de calculo do ICMS 29,90/0,80 = 37,38  
37,38\*7% = 2,62  
Base de calculo do Difal EC/87 = 37,38 \*20% = 7,48  
7,48-2,62 = 4,86  
   
MV\_ESTADO = SP  
MV\_PPDIFAL = {{2016,40,60},{2017,60,40},{2018,80,20},{2019,100,0},{2020,100,0},{2021,100,0},{2022,100,0},{2023,100,0},{2024,100,0}}  
   
Cliente = DF  
Tipo consumidor Final  
![](https://totvssuporte.zendesk.com/attachments/token/ofeEEyfu4br3NvJgBoTpcK0Ef/?name=image.png)  
   
FISA170  
   
Perfil cadastro de Produtos  
   
![](https://totvssuporte.zendesk.com/attachments/token/6dxGgYTWBX0q9Ghs37XW614yj/?name=image.png)  
Perfil  de Operação = 000050 - padrão do sistema  
![](https://totvssuporte.zendesk.com/attachments/token/fClwVjSRCZQPpDrIaV4ucrHce/?name=image.png)  
   
Perfil de Participante  
![](https://totvssuporte.zendesk.com/attachments/token/zoevuzs97ZxjyH6pYmJ111t1f/?name=image.png)  
   
Perfil de Origem / Destino = 000002  
![](https://totvssuporte.zendesk.com/attachments/token/dzQejpJbvwlPHpHigTXOlfsfp/?name=image.png)  
   
Regra de Alíquotas  
7%  
![](https://totvssuporte.zendesk.com/attachments/token/wWSccw2Rzm43pSxspRlqtEQDY/?name=image.png)  
20%  
![](https://totvssuporte.zendesk.com/attachments/token/dYeeHzq0vIySHoSW97eoCt4SJ/?name=image.png)  
   
Regra de Base de Cálculo do ICMS  
   
![](https://totvssuporte.zendesk.com/attachments/token/guIleFCHdalmUqJi90FanZaYs/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/59r25Pu28uUZrO2q9KsyZyzVg/?name=image.png)  
   
Regra de Escrituração  
![](https://totvssuporte.zendesk.com/attachments/token/6qLYpEyCtWt6Ughc6cwYRJmCt/?name=image.png)  
   
Regra de Calculo - Documentos Fiscais = ICMS  
![](https://totvssuporte.zendesk.com/attachments/token/rHGBmZpJycoBf9PFMikoceeWg/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/RLvWUGlBm0mAHh9Dsb9qLryEo/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/XZELCPD4t6LNPLJJLrxU6VFN8/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/KFYXF73qPHJMNr41yyTcRykLA/?name=image.png)  
   
Regra de Base de Calculo do Difal EC/87  
   
![](https://totvssuporte.zendesk.com/attachments/token/ICEWLC8TfS8mGAS8izGXQfk4d/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/amUQEkcuzyI4Kr72WUTKuvgpN/?name=image.png)  
   
Regra de escrituração a mesma para o ICMS  
   
Regra de Calculo - Documentos Fiscais - Difal EC/87  
![](https://totvssuporte.zendesk.com/attachments/token/H7ExGvCA5HaZU9RJv2LIYegKW/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/ws6wq4bEz79G8n3OpzpUuM1gT/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/bwLKklG6Jf8nZqMCRNRkTM9Sf/?name=image.png)  
Após criar a regra do Difal, vá em alterar para deduzir o valor do ICMS Próprio  
   
![](https://totvssuporte.zendesk.com/attachments/token/Oox0fuZrYI1ZfWBq0q1rEOE9o/?name=image.png)  
   
TES  
Calcula ICMS = não  
L fiscal ICMS = não  
CFOP = 5102  
CST = 00  
Calc dif icm = não  
Calc difal = não  
Mat consumo = não  
   
Pedido de Vendas  
   
![](https://totvssuporte.zendesk.com/attachments/token/2rErmX1OSKOSQjsz4sWV58Tnm/?name=image.png)  
   
Emissão da NF  
![](https://totvssuporte.zendesk.com/attachments/token/ONFGATzFSbIt7OExmVm8RC7E3/?name=image.png)  
CD2  
![](https://totvssuporte.zendesk.com/attachments/token/9dLzkISN3lPbYD5qwiqGkjJF6/?name=image.png)
