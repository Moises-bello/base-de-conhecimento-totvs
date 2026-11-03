---
article_id: 25935952256663
category: Rental by ItUp Business
content_hash: 5f46fabdd5a30eb1f49dbaa355b352ddad2da128a8d3c9666be854fbe1cce0d1
fetched_at: '2026-06-28T22:36:20.690676+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Regra de desconto para novas
  linhas de Locação
type: support-article
updated_at: '2026-04-09T12:49:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25935952256663-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Regra-de-desconto-para-novas-linhas-de-Loca%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25935929688343) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Regra de desconto para novas linhas de Locação  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - Todas as versões.  
  
**Solução**

Quando novas linhas de locação são incluídas em um contrato, o desconto aplicado é calculado sobre o montante total do contrato, não em cada item individualmente. Por exemplo, se na linha um do contrato foi aplicado um desconto de 12%, e em outras duas linhas adicionais não foram incluídos descontos, o sistema irá ratear a porcentagem de desconto entre todas as linhas. Isso significa que o desconto de 12% será considerado sobre o valor total do contrato, garantindo que o desconto seja aplicado de forma proporcional ao valor total, e não apenas em itens específicos.

![image-2024-8-26_17-51-17.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25935952217367)  
  
**Explicação**  
Linha 1: Um desconto de 12% foi aplicado, reduzindo o valor base para R$ 880,00.  
Linhas 2 e 3: Não foi aplicado desconto individualmente em cada uma dessas linhas, mas o sistema considera o desconto sobre o valor total do contrato.  
% Desconto Total: A porcentagem de desconto total aplicada ao montante do contrato foi de 4%, considerando o desconto total no valor de R$ 120,00.  
  
O desconto de 4% foi aplicado no valor total do contrato, distribuindo de forma proporcional o desconto inicialmente aplicado apenas na linha 1. Essa abordagem garante que o desconto seja considerado de forma proporcional ao valor total do contrato e não apenas em itens específicos.  
  
**Saiba Mais:** [**Aprovação de projetos**](https://tdn.totvs.com/x/AFUlJ)
