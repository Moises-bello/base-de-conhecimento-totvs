---
article_id: 36392070081175
category: Financeiro - Análise de Crédito Financeiro
content_hash: ef67fb511e9280512f55c9f9f2f5670fac59b9f5c65223acebb16a8a7fce6657
fetched_at: '2026-06-28T22:37:25.531396+00:00'
product: protheus
section_id: 36607745462423
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINAPP001 - Definição
  de moeda no limite de crédito
type: support-article
updated_at: '2025-12-23T23:16:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36392070081175-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINAPP001-Defini%C3%A7%C3%A3o-de-moeda-no-limite-de-cr%C3%A9dito
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36392074743319) Tempo aproximado para leitura: **05:00 min**

**Dúvida:**  
Como definir a moeda principal no limite de crédito usando a FINAPP001?

**Ambiente:**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - 12.1.33 e superiores  
  
**Solução:**

Quando utilizamos a rotina de **análise de crédito**, qualquer ajuste realizado nos valores de limite de crédito do cliente será salvo no card **“Limite de Crédito”** e nas tabelas **SA1** e **F7F**.

A rotina de análise de crédito preenche o limite com base nas **informações de moeda cadastradas no cliente**.

Para ajustar a **moeda principal** exibida no card “Limite de Crédito”, acesse:

**Cadastro de Clientes (MATA030) → Alterar → Aba “Vendas”**  
e verifique o campo **“Moeda do LC”** (SA1 → A1\_MOEDALC)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36392074744087)

O conteúdo inserido neste cadastro, corresponde a moeda utilizada para composição do card.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36392074744983)

Após realizar o ajuste, recomendamos executar o **reprocessamento das informações do cliente** por meio da rotina **FINA410**, garantindo que os dados sejam atualizados corretamente.
