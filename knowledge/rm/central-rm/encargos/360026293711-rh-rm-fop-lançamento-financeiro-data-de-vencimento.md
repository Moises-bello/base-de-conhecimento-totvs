---
article_id: 360026293711
category: Encargos
content_hash: 7cdf22004d8351c914a93ad1c8a50f3a49d52dc77704c2f241a30fdaf98e4828
fetched_at: '2026-06-28T22:46:53.339594+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: 'RH - RM - FOP - Lançamento Financeiro: Data de vencimento'
type: support-article
updated_at: '2024-10-11T20:14:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026293711-RH-RM-FOP-Lan%C3%A7amento-Financeiro-Data-de-vencimento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Qual a parametrização do sistema disponível para alteração da **Data de Vencimento** na geração do **Lançamento Financeiro**?**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Existem três parametrizações básicas necessárias para verificar a Data de Vencimento do lançamento financeiro. Veja abaixo cada uma delas:  
  
1. **Parametrização no Fluxus**  
Uma das parametrizações que pode alterar a **Data de Vencimento** do lançamento financeiro no RM Folha de pagamento é uma configuração do RM FLuxus, que impede a geração dos lançamentos para finais de semana e feriados e gera este lançamento no primeiro dia útil posterior ou anterior, conforme parametrização abaixo.  
  
Acesse: **Back Office | Gestão Financeira | Ambiente | Parâmetros | TOTVS Gestão Financeira | 02.01.01 - Manutenção de Lançamentos | Inclusão a pagar** e verifique as parametrizações dos parâmetros **Aceita Vencimento a Pagar em Finais de Semana** e **Feriados e Aceita Previsão de Baixa a pagar em Finais de Semana e Feriados.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13584870831511)  
  
2. **Parametrização no Lançamento Financeiro**  
Para os tipos de lançamento financeiro 2 correspondente a **Líquido rescisão** e 3 correspondente ao **Líquido férias**, o sistema disponibiliza o parâmetro **Usar data de pagamento para vencimento do lançamento**. Este campo irá gerar os lançamentos financeiros com a data de vencimento conforme a data de pagamento da rescisão ou das férias, conforme o tipo de lançamento financeiro que estiver sendo lançado.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13584968653207)  
  
3. **Parametrização na geração do Lançamento Financeiro**  
Caso a parametrização no Fluxus não interfira e o tipo do lançamento financeiro não seja 2- Líquido rescisão ou 3- Líquido férias, então a única parametrização válida será a parametrização da geração do lançamento financeiro. Acesse **Encargos | Geração dos Lançamentos** e informe a **Data de Vencimento** e finalize a geração do lançamento financeiro:  
  
![](https://centraldeatendimento.totvs.com/hc/pt-br/article_attachments/13585023539735/e0fc701e3c4a28e75f9f26f88aa9929ff40bc5ca3758a0ee2e4dd0dc2673cd44.png)
