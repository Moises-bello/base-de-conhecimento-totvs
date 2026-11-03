---
article_id: 15534947690519
category: Férias
content_hash: 8e1228bb7e6d8a6f6197e42370b0c368e6c6ea03bc015868e5ffbeafb68fe066
fetched_at: '2026-06-28T22:46:56.191390+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: 'RH - RM - FOP - Férias: Cálculo 1/3 de férias considerando 30 dias em casos
  de abono pecuniário'
type: support-article
updated_at: '2025-02-20T20:47:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15534947690519-RH-RM-FOP-F%C3%A9rias-C%C3%A1lculo-1-3-de-f%C3%A9rias-considerando-30-dias-em-casos-de-abono-pecuni%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15534900846103) Tempo aproximado para leitura: **00:01:18 min****Dúvida**Ao calcular 1/3 de férias (cc40), em férias com Abono Pecuniário o sistema está calculando o 1/3 de férias considerando 30 dias ao invés de considerar apenas 20 dias. Isso ocorre por qual motivo?  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Causa**Isso pode ocorrer quando o parâmetro "**Pagamento adicional constitucional sobre dias de direito de férias**" está habilitado. Dessa forma, o sistema considera 30 dias para o pagamento do evento de código de cálculo 40 (1/3 de férias), desconsiderando a venda de férias do colaborador.  
  
**Solução**

Para que o cálculo seja efetuado corretamente, acesse  **Configurações | Parametrizador | Férias | Cálculos** e desabilite a flag **Paga Adicional Constitucional sobre dias de direito de férias**conforme demonstrado abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15534399039127)

Após configuração, o sistema irá calcular corretamente.

**Saiba Mais:**

**[RH - RM - FOP - Férias: Lançamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007913092-RH-RM-FOP-F%C3%A9rias-Lan%C3%A7amento?source=search)**
