---
article_id: 13342164470551
category: Folha Mensal
content_hash: f1f9f1d99652a3fa3065191d30cf9ff66c1de5dfa4ecd685a6b2da2b5b376bd4
fetched_at: '2026-06-28T22:46:58.248516+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Evento cc415 não é lançado automaticamente no envelope
type: support-article
updated_at: '2024-06-11T13:19:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13342164470551-RH-RM-FOP-Evento-cc415-n%C3%A3o-%C3%A9-lan%C3%A7ado-automaticamente-no-envelope
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20667838951959) Tempo aproximado para leitura: **00:02:03 min****Ocorrência**  
Ao realizar o processo de Diferença Salarial, o sistema não lança no envelope o evento cc415 - Base INSS Diferença Salarial por Dissídio.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Isso ocorre, pois o evento de código de cálculo 415 é utilizado para a verificação de valores da base de INSS folha  sobre as diferenças salariais pagas no mês, e como benefício facilitar a conferência de dados entre RM x Retorno do Governo. Dessa forma, o evento não é lançado automaticamente no envelope, pois se trata de um evento opcional.   
  
O CC 415 será inserido apenas na aba Verbas de diferença, na ficha financeira.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13344888741783)  
  
**Observação:**   
O evento será inserido somente na diferença salarial por dissídio.  
Pode ser visualizado na aba de 'Verbas Geradas por Diferença’ da ficha financeira no mês/ano correspondente a diferença.  
  
**Saiba Mais**[Código de Cálculo 415 - BASE DE INSS DIFERENÇA SALARIAL POR DISSÍDIO](https://tdn.totvs.com.br/pages/releaseview.action?pageId=488864232)  
[RH - RM - FOP - Códigos de Cálculo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412890806807-RH-RM-FOP-C%C3%B3digos-de-C%C3%A1lculo#:~:text=Os%20c%C3%B3digos%20de%20c%C3%A1lculos%20s%C3%A3o,de%20f%C3%B3rmulas%20para%20serem%20calculados.)  
[RH - RM - FOP - Encargo R - Base: incidência de INSS Dissídio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7276287385623-RH-RM-FOP-Encargo-R-Base-incid%C3%AAncia-de-INSS-Diss%C3%ADdio?source=search)
