---
article_id: 16775891562263
category: Folha Mensal
content_hash: 1fdb12e7fe8bbac91018c276a1f648e60603cc33dab35178a76fa258655e9cec
fetched_at: '2026-06-28T22:46:58.179028+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Folha mensal - Dias trabalhados para funcionário reintegrado
  considera 30 dias '
type: support-article
updated_at: '2023-08-15T14:30:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16775891562263-RH-RM-FOP-Folha-mensal-Dias-trabalhados-para-funcion%C3%A1rio-reintegrado-considera-30-dias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16775862863767) Tempo aproximado para leitura: **00:01:45 min****Ocorrência**Ao calcular a folha mensal de um funcionário que foi reintegrando, o sistema está considerando 30 dias e não dias proporcionais.  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Isso ocorre, pois, por padrão, os eventos de códigos de cálculos 1 e 2 são sempre calculados com base na data de admissão dos funcionários. Ou seja, o sistema irá calcular o mês integral do funcionário, pois a data informada no registro é apenas para controle.  
  
**Solução**Para solucionar esse problema deverá ser criada uma fórmula para pagamento conforme a data da reintegração e vincular essa fórmula no evento de salário.  Dessa forma, o sistema irá abater os dias. 

**Importante:** O escopo do suporte padrão não auxilia em customização de fórmulas, mas caso necessário possuímos um serviço de consultoria tarifada que poderá ser acionada.

**Saiba Mais**

[RH - RM - FOP - Fórmulas e Funções](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061764374-RH-RM-FOP-F%C3%B3rmulas-e-Fun%C3%A7%C3%B5es?source=search)
