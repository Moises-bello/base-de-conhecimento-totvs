---
article_id: 360021377992
category: ADVPL - Rotina Automática
content_hash: fec6f3560d07ed9c8151d43c596cd415242a705bb9dd3817295cab71edff9d86
fetched_at: '2026-06-28T22:40:24.152069+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Preciso deixar o PV c/
  status Em Aberto(Legenda Verde)
type: support-article
updated_at: '2021-12-29T19:01:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021377992-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Preciso-deixar-o-PV-c-status-Em-Aberto-Legenda-Verde
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Preciso deixar o PV c/ status Em Aberto(Legenda Verde) ao inclui-lo via rotina automática **MATA410**, pois quando executo a rotina automática, meus pedidos vem sempre como Liberado (Legenda Amarela)   
De qual maneira poderia ter esse efeito ?  
  
**Ambiente**Protheus – ADVPL – A partir da versão 11.8  
  
**Solução**Para que os pedidos de venda seja incluídos sempre com o status **Em aberto**, verifique se o parâmetro "**Sugere Qtde Liber.?**" está igual a "**NÃO**", pois quando esse parâmetro está igual a "**SIM**" o sistema preenche automaticamente a quantidade liberada, deixando o pedido como Liberado.

![Screenshot_5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360018300551/Screenshot_5.png)
