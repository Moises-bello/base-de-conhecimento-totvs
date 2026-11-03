---
article_id: 7406000650391
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: e9ee849826232eec66005483075ba6bb69e9ff763b02719bc931c0c30f5a725b
fetched_at: '2026-06-28T22:38:28.584732+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Incidente There
  is a source name conflict ao utilizar Ponto de Entrada
type: support-article
updated_at: '2025-01-10T20:16:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7406000650391-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Incidente-There-is-a-source-name-conflict-ao-utilizar-Ponto-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Ao utilizar ponto de entrada CRMA980 ocorre o incidente;

**There is a source name conflict (CRMA980.PRW) that prevents continuing securely. on EXISTBLOCK**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

O incidente ocorre, pois não é permitido no MVC definir o nome do fonte com o mesmo de uma rotina Padrão, devido a isso apresenta o Incidente de "There is a source name conflict" pois por padrão o nome da rotina já é CRMA980.  
   
Para solução do incidente, altere o nome do fonte exemplo; **"INCRMA980" ou "ALTCRMA980"**sendo o nome diferente do padrão CRMA980.

**Saiba Mais:**

**[Tabela DE / PARA](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=604230458)**
