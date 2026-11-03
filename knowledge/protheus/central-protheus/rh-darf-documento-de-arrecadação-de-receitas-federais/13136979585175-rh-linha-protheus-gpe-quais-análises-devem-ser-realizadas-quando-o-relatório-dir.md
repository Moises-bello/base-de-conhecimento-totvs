---
article_id: 13136979585175
category: RH - DARF (Documento de Arrecadação de Receitas Federais)
content_hash: 4b8969c755f8b3dcf73ed85c8968d449bf5c76d26d9e712a1fde329a9639b0f5
fetched_at: '2026-06-28T22:43:30.221020+00:00'
product: protheus
section_id: 360010781754
source: central-protheus
title: RH - Linha Protheus - GPE - Quais análises devem ser realizadas quando o relatório
  Dirf Mensal (GPER050) duplica os valores?
type: support-article
updated_at: '2025-06-16T20:27:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13136979585175-RH-Linha-Protheus-GPE-Quais-an%C3%A1lises-devem-ser-realizadas-quando-o-relat%C3%B3rio-Dirf-Mensal-GPER050-duplica-os-valores
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32852655978775) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Quais análises devem ser realizadas quando o relatório Dirf Mensal (GPER050) duplica os valores?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução** **1º** Duplicidade do IR das Férias

- Verifique se no cálculo das férias as datas de pagamento estão iguais, no cabeçalho das férias e nas verbas calculadas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13136503389463)

- Verifique nos Acumulados ( Consulta / Cadastros / Acumulados), caso a folha esteja fechada, ou na rotina Consulta / cálculo / por funcionário, caso a folha esteja aberta, se a data de pagamento é a mesma gravada no cálculo das férias.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13136580310423)

**2º** Duplicidade do IR da Rescisão

- Verifique se no cálculo da rescisão as datas de pagamento estão iguais, no cabeçalho da rescisão e nas verbas calculadas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13136938599063)

- Verifique nos Acumulados ( Consulta / Cadastros / Acumulados), caso a folha esteja fechada, ou na rotina Consulta / cálculo / por funcionário, caso a folha esteja aberta, se a data de pagamento é a mesma gravada no cálculo da rescisão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13140285134359)

- Verifique no cadastro do período pelo caminho >Atualizações >Definições cálculos >Períodos, se os campos Data de Integração e Data de Pagamento estão preenchidos corretamente, o campo Dt. Integ deve estar preenchido obrigatoriamente se o período já estiver fechado ou o roteiro FOL calculado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13423815159319)

**Saiba mais**  
[RH - DARF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010781754-RH-DARF-Documento-de-Arrecada%C3%A7%C3%A3o-de-Receitas-Federais-)
