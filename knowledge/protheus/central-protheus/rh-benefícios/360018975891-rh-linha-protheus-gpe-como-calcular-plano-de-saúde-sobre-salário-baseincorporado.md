---
article_id: 360018975891
category: RH - Benefícios
content_hash: 6ab2e7e191dbdaeb403508970a90e605b2192d80c6d619603ed12ad1864cb245
fetched_at: '2026-06-28T22:44:03.724250+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular plano de saúde sobre salário base/incorporado
type: support-article
updated_at: '2025-09-19T11:37:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018975891-RH-Linha-Protheus-GPE-Como-calcular-plano-de-sa%C3%BAde-sobre-sal%C3%A1rio-base-incorporado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26961972406167) Tempo aproximado para leitura: **00:01:30 min****Dúvida**Como calcular plano de saúde sobre salário base/incorporado?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**Na rotina **Cálculo dos Planos de Saúde/Odontológico** existe a pergunta **Calcular sobre salário?**, que define a forma de cálculo do plano do funcionário, se ele é efetuado sobre o salário base ou sobre o salário incorporado.

Procedimentos para utilização:

- No menu do Gestão de Pessoal (SIGAGPE) acessar em **Atualizações>** **Definições de Cálculo> Mnemônicos (GPEA300);**- Localize Mnemônico **P\_SALINC** e deixe seu conteúdo = **.T.**.

![](https://totvssuporte.zendesk.com/attachments/token/vPKIdlNzYcHqj0HLSb18BtG8F/?name=inline1478593022.png)

- Acessar o cadastro das verbas em **Atualizações> Definições de Cálculo> Verbas (GPEA040)** e faça a seguinte configuração:  
  
**1.** Verba do adicional que incorpora salário no campo **RV\_INCORP = SIM** e campo **RV\_BASICAL = Salário Base.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26961972410519)  
  
  
2.** Verba de Desconto do Plano de Saúde com ID 0049 campo **RV\_INCORP = NÃO** e campo **RV\_BASICAL = Salário Incorporado.​**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26961972415767)**- Salvar as alterações e acessar em **Atualizações> Benefícios> Planos de Saúde> Cálculo Planos de Saúde**;- Clicar em**Parâmetros**, informe os dados conforme orientação do help de campo;  
- Clicar em **Ok** e depois **Calcular**.

**Saiba mais:**

[RH - Benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597251-RH-Benef%C3%ADcios)
