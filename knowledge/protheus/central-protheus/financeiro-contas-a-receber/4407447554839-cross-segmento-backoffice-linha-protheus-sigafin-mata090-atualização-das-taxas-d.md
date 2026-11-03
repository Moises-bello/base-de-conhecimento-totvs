---
article_id: 4407447554839
category: Financeiro - Contas a Receber
content_hash: 8e5abd3f54d110882699a36a30ca2fa0534fdaf0aea1327c509153ed952735d0
fetched_at: '2026-06-28T22:38:12.529837+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - MATA090 Atualização
  das taxas da moeda do Banco Central
type: support-article
updated_at: '2025-11-19T20:43:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407447554839-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-MATA090-Atualiza%C3%A7%C3%A3o-das-taxas-da-moeda-do-Banco-Central
---

**Dúvida**  
Como atualizar taxa da moeda do Banco Central ?

**Ambiente**  
Cross Segmento - BackOffice Linha Protheus – Financeiro – MATA090 - A partir da versão 12.1.17  
  
**Solução**

O sistema permite atualizar as moedas de forma manual ou automática.

Para isso, acesse **Atualizações > Cadastro > Moedas** (rotina **MATA090**).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36453510383895)

No cadastro, serão exibidas as opções de taxas a partir da **moeda 2**.  
Informe a taxa correspondente para cada moeda que será utilizada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36453485528599)

A conversão somente ocorrerá se existir uma taxa cadastrada para a moeda **com a data correspondente ao dia do lançamento do título**.  
Caso não exista taxa informada para aquele dia, **não haverá conversão** para outra moeda.

**Para automatizar essa atualização, você pode utilizar o agendamento de tarefas, conforme orientações disponíveis na documentação abaixo:**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - MATA090 - Cadastrar Taxas de Moeda automaticamente via Schedule FINXTAXA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11821936684183-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-MATA090-Cadastrar-Taxas-de-Moeda-automaticamente-via-Schedule-FINXTAXA)
