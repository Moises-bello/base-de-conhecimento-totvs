---
article_id: 12947229812119
category: Anuais
content_hash: 51fead4ddc562f2f786adefc69733284e096a6f8a9df54dce2bb741073ace6ad
fetched_at: '2026-06-28T22:46:51.041588+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: 'RH - RM - FOP - DIRF: eventos de férias de funcionário transferido'
type: support-article
updated_at: '2025-01-24T14:57:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12947229812119-RH-RM-FOP-DIRF-eventos-de-f%C3%A9rias-de-funcion%C3%A1rio-transferido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:16 min****Dúvida**No módulo da Folha de Pagamento, como parametrizar o sistema, para que as férias do funcionário transferido sejam levadas para DIRF?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para que os valores sejam informados ao gerar a DIRF, acesse a ficha financeira do funcionário transferido e insira os eventos abaixo, para que o sistema reconheça na transferência.  
  
335 - Base IRRF Férias Transferida Para Outra Filial

336 - IRRF Férias Transferida Para Outra Filial

337 - INSS Férias Transferida Para Outra Filial

338 - Pensão Férias Transferida Para Outra Filial

339 - Abono  Férias Transferida Para Outra Filial  
  
Quando é realizada a transferência do funcionário com férias e a base irá constar os eventos acima, de forma que o sistema irá alimentar a ficha financeira automaticamente.  
  
Para maiores informações quanto aos códigos de cálculos acima, acesse a documentação abaixo:  
  
[RH - RM - FOP - Códigos de Cálculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412890806807-RH-RM-FOP-C%C3%B3digos-de-C%C3%A1lculo#:~:text=Os%20c%C3%B3digos%20de%20c%C3%A1lculos%20s%C3%A3o,de%20f%C3%B3rmulas%20para%20serem%20calculados.)
