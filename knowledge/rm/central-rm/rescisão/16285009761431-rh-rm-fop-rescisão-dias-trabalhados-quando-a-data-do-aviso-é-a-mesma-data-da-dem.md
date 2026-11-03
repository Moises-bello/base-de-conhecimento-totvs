---
article_id: 16285009761431
category: Rescisão
content_hash: 7e849ba2119d4eb7a970062351a35c4a30bb186cc2a1400a0d9e2f91a0ef2cce
fetched_at: '2026-06-28T22:46:54.211075+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - Rescisão: Dias trabalhados quando a data do aviso é a mesma
  data da demissão'
type: support-article
updated_at: '2024-09-16T18:32:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16285009761431-RH-RM-FOP-Rescis%C3%A3o-Dias-trabalhados-quando-a-data-do-aviso-%C3%A9-a-mesma-data-da-demiss%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16285019863703) Tempo aproximado para leitura: **00:01:13 min****Dúvida**Ao calcular uma rescisão, o evento de  dias trabalhados está sendo calculado considerando um dia a menos. Por qual motivo isso pode ocorrer?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Isso ocorre pois o sistema não considera a data do Aviso Prévio como um dia trabalhado, considera apenas como Aviso.

**Exemplo:**

1. Suponha que a data da demissão de um funcionário é 25/07/2023, conforme abaixo: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16284638236311)  
  
2. Ao informar a data do Aviso para 25/07/2023, ou seja, considerando a mesma data do desligamento, o sistema irá considerar 24 dias trabalhados no mês de Julho.

3. Dessa forma,  avaliando o exemplo acima, é necessário alterar a data do Aviso Prévio para 26/07/2023 e recalcular a rescisão para que o sistema considere os 25 dias trabalhados corretamente.

**Saiba Mais:**

[RH - RM - FOP - Aviso Prévio Trabalhado: Cadastro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023001231-RH-RM-FOP-Aviso-Pr%C3%A9vio-Trabalhado-Cadastro)

[RH - RM - FOP - Tipos de rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411052336023-RH-RM-FOP-Tipos-de-rescis%C3%A3o)
