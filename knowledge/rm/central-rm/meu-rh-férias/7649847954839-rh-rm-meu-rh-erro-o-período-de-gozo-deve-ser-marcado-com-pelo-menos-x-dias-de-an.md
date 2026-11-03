---
article_id: 7649847954839
category: Meu RH - Férias
content_hash: 5c5e1be704bbf70252a6ee73d693d11af56209d944b6461104d79e9215b0c859
fetched_at: '2026-06-28T22:47:31.653447+00:00'
product: rm
section_id: 1500000835241
source: central-rm
title: 'RH - RM - Meu RH - Erro: O período de gozo deve ser marcado com pelo menos
  x dias de antecedência'
type: support-article
updated_at: '2024-11-28T18:18:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7649847954839-RH-RM-Meu-RH-Erro-O-per%C3%ADodo-de-gozo-deve-ser-marcado-com-pelo-menos-x-dias-de-anteced%C3%AAncia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:50 min****Ocorrência**Ao realizar a solicitação de férias no **Meu RH** retorna o erro: **"O período de gozo deve ser marcado com pelo menos x dias de antecedência"**  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Causa**O erro acontece quando são solicitas férias antes do intervalo de tempo definido na configuração do Parametrizador do RM.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Ao realizar a marcação de férias, o Meu RH retorna o erro:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7649424050455/mceclip0.png)  
  
2. A quantidade de dias de antecedência é definida em **Folha de Pagamento | Configurações | Parametrizador | RM Portal | edite o grupo de quiosque | Férias;**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7649443753879/mceclip1.png)  
  
3. O parâmetro verifica a data atual + quantidade de dias de antecedência para solicitação, exemplo:

Considerando a data de hoje sendo **22/07/2022** e informando **30 dias** no parâmetro, a data início das férias deverá considerar hoje+30 dias, o mínimo para marcação nesse cenário é dia **21/08/2022;**

O sistema no momento do erro retornará qual a data mínima a ser solicitada as férias, para correção do erro deverá ajustar o parâmetro compreendendo a data desejada ou acatar a sugestão do sistema como demonstra no erro:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7649747104023/mceclip2.png)
