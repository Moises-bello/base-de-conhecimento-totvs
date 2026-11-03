---
article_id: 360051298394
category: Funcionários
content_hash: 95147d8955ea355ec4a7b2f69f12dab4a964deae5e4e51c1a5fe7997eaf49760
fetched_at: '2026-06-28T22:47:03.423037+00:00'
product: rm
section_id: 1500000861022
source: central-rm
title: RH - RM - FOP - Tentativa de divisão por zero / Attempted to divide by zero
type: support-article
updated_at: '2024-06-14T18:17:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051298394-RH-RM-FOP-Tentativa-de-divis%C3%A3o-por-zero-Attempted-to-divide-by-zero
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:30 min**

**Ocorrência**Ao acessar o envelope de um funcionário, é retornado o erro: **Tentativa de divisão por zero** ou, em inglês **Attempted to divide by zero**.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080556134/mceclip0.png)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Causa**Este erro ocorre, em geral, quando o funcionário é comissionista e/ou seu salário é igual a zero. Em resumo, ao acessar o envelope, o sistema executa um recálculo antes de apresentar as informações. Ao tentar recalcular eventos com fórmula que buscam o salário do funcionário, como seu salário é zero, o sistema não conseguirá executar o recálculo e retornará a mensagem supracitada.

**Solução**Sendo a causa do problema a estruturação de fórmulas, a solução terá caráter manual, ou seja, será necessário identificar qual fórmula busca ou faz referência ao salário do funcionário para que seja reestruturada. Sugere-se o apoio da equipe de TI da empresa para auxiliar na correção ou, caso prefira, acionar nosso serviço de consultoria tarifada, onde um consultor estará à disposição e poderá auxiliar e corrigir o problema.
