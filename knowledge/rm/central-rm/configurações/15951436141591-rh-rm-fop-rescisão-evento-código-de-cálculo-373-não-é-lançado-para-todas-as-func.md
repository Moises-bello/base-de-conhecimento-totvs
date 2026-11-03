---
article_id: 15951436141591
category: Configurações
content_hash: 0548fd7717274a8a54c3f2125cb937ea9a8c9fb837404c0f3ae6125b1c45ba3f
fetched_at: '2026-06-28T22:46:49.468418+00:00'
product: rm
section_id: 1500000834621
source: central-rm
title: 'RH - RM - FOP - Rescisão: Evento código de cálculo 373 não é lançado para
  todas as funcionárias de licença maternidade'
type: support-article
updated_at: '2025-03-05T17:30:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15951436141591-RH-RM-FOP-Rescis%C3%A3o-Evento-c%C3%B3digo-de-c%C3%A1lculo-373-n%C3%A3o-%C3%A9-lan%C3%A7ado-para-todas-as-funcion%C3%A1rias-de-licen%C3%A7a-maternidade
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15951427788183)**Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Ao efetuar a rescisão de funcionárias que tiveram licença maternidade no ano, o evento de código de cálculo 373 (13° Rescisão Licença Maternidade Provento) é levado automaticamente para o envelope de algumas funcionárias, porém de outras funcionárias o evento não é lançado automaticamente.

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**O erro ocorre quando a funcionária demitida possui cálculo de média nas férias e o evento de código de cálculo 373 está com a prioridade inferior ao evento de código de cálculo 48.

Para funcionárias que não possuem médias, o evento é levado automaticamente, independente da sua prioridade. Sendo assim, para corrigir esse incidente é necessário informar uma prioridade maior no evento com código de cálculo 373, veja: 

**Código de cálculo 373:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15951262722071)

**Código de cálculo 48:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15951319759127)

Após esse processo, o evento será lançado automaticamente.  **Saiba Mais**

**[Código de Cálculo 373 – 13º Rescisão Licença Maternidade Provento](https://tdn.totvs.com/pages/releaseview.action?pageId=452719525)**
