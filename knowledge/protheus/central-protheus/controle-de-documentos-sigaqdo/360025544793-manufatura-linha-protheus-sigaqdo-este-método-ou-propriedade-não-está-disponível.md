---
article_id: 360025544793
category: Controle de Documentos (SIGAQDO)
content_hash: 766a4dcd1d724b290f93b608e6ae9b48f7a75bd792c5c60d12a0e0296fcd0841
fetched_at: '2026-06-28T22:42:29.058361+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Este método ou propriedade não está
  disponível porque este comando não está disponível para leitura
type: support-article
updated_at: '2021-09-08T12:58:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025544793-Manufatura-Linha-Protheus-SIGAQDO-Este-m%C3%A9todo-ou-propriedade-n%C3%A3o-est%C3%A1-dispon%C3%ADvel-porque-este-comando-n%C3%A3o-est%C3%A1-dispon%C3%ADvel-para-leitura
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:40 min**  
 **Ocorrência**Ao distribuir documentos na rotina **QDOA110 - Distribuição**, é apresentada a mensagem **Este método ou propriedade não está disponível porque este comando não está disponível para leitura**.  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
 **Causa**Esta situação ocorre porque o arquivo **mpword.dll** existente na pasta do **SmartClient** do **Protheus** está **desatualizado**.  
  
 **Solução**Extrair o arquivo **mpword.zip** disponível no anexo na pasta do **SmartClient**, substituindo a **dll** existente. Recomendamos que antes da substituição seja realizado um **backup** do arquivo **mpword.dll**.   
  
**Anexo**
