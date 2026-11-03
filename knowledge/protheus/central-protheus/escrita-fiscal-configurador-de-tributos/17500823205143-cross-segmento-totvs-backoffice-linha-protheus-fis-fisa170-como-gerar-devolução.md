---
article_id: 17500823205143
category: Escrita Fiscal - Configurador de Tributos
content_hash: 5dc4b64cbe3635b2b40066356ac6c800c78ddc7e827d65505e0f2324a69345a1
fetched_at: '2026-06-28T22:39:17.454072+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como gerar
  devolução do CST 61 STMONO?
type: support-article
updated_at: '2024-11-12T20:10:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17500823205143-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-gerar-devolu%C3%A7%C3%A3o-do-CST-61-STMONO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17500859428631) Tempo aproximado para leitura: **00:03:30min** **Dúvida** Como gerar devolução do CST 61 STMONO?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Para o sistema gerar a Devolução ou Retorno com o STMONO a nota fiscal de entradas deve ser lançada pela rotina Fisa170  
   
Um exemplo  
   
![](https://totvssuporte.zendesk.com/attachments/token/UD5paIQcqhfWEYtmXSMxXIqzm/?name=image.png)  
   
Configurações do Fisa170 - Entrada e Devolução  
   
![](https://totvssuporte.zendesk.com/attachments/token/R1tlPFraq2SBKp6CLzxt6o9Tt/?name=image.png)  
   
Perfis  
   
Perfil do Produto  
   
![](https://totvssuporte.zendesk.com/attachments/token/Fqjhru6UohkTCiH5hmpYAgmzE/?name=image.png)  
   
Cadastrado no SB1  
   
![](https://totvssuporte.zendesk.com/attachments/token/qgGJHhOr54ejONYnqmP4YCSJl/?name=image.png)  
   
   
Perfil de Operação  
000052 - STMONO  
   
![](https://totvssuporte.zendesk.com/attachments/token/vab5fEy3RC6b6TKEGje5srif9/?name=image.png)  
   
Perfil Participante  
   
![](https://totvssuporte.zendesk.com/attachments/token/0LX1vrHQH6mTYAkYe5ZQu6ERn/?name=image.png)  
   
Perfil Origem / Destino  
   
![](https://totvssuporte.zendesk.com/attachments/token/DMZ4qD5hosJEhwT4JBNCxpEVZ/?name=image.png)  
Regra de Base de calculo  
   
![](https://totvssuporte.zendesk.com/attachments/token/hSqYCSG4rITGC2Xcr1B2mlHlV/?name=image.png)  
   
Regra de Alíquota  
   
![](https://totvssuporte.zendesk.com/attachments/token/S6yEWiZF72j5MQk96AKz7Pb8X/?name=image.png)  
   
Regra de escrituração  
   
![](https://totvssuporte.zendesk.com/attachments/token/NzBU0N8KZVlKWmZA6pHpVEXce/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/ZLSFh9G83lHRzY3oEy9NytkpE/?name=image.png)  
   
Regra de Calculo Documento Fiscal  
   
![](https://totvssuporte.zendesk.com/attachments/token/shjCK47mICjww7WOap7Vjvaov/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/Z5zn13Lalq2qlSRYC1Yq56UAU/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/OaEs94Bo0IvIZplzzFb4zxjXh/?name=image.png)  
   
Formula   
![](https://totvssuporte.zendesk.com/attachments/token/rrq9XC2Nt0xP2mqz6gX5iBEc5/?name=image.png)  
   
   
   
Documento de entradas   
   
![](https://totvssuporte.zendesk.com/attachments/token/2K8TzF1bkUam9lpgYiAvPWobU/?name=image.png)  
   
Foi calculado o ICMS ST Mono , agora vamos fazer a devolução.  
   
Devolução  
   
![](https://totvssuporte.zendesk.com/attachments/token/1OdJjTJIyvV2ch0DkWkMYzmwP/?name=image.png)  
   
   
CD2  
![](https://totvssuporte.zendesk.com/attachments/token/wk1hahRbB5meVOXe56nDyAGXb/?name=image.png)

Boletim

<https://tdn.totvs.com/pages/releaseview.action?pageId=765332384>
