---
article_id: 37342480640919
category: Financeiro - Cadastros
content_hash: 9832de6e440101f8e93238b73f73643689d309ed413be241a7baf58d0b0bb735
fetched_at: '2026-06-28T22:37:53.155886+00:00'
product: protheus
section_id: 1500001550722
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - MATA090 - Projeção de
  Moedas
type: support-article
updated_at: '2025-12-31T11:01:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37342480640919-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-MATA090-Proje%C3%A7%C3%A3o-de-Moedas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37342480626583) Tempo aproximado para leitura: 04**:00 min**

**Dúvida:**  
Como realizar a projeção de moedas?

**Ambiente:**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - 12.1.33 e superiores

**Solução:**

A projeção de moedas permite automatizar o preenchimento das taxas para períodos futuros, evitando a necessidade de digitação diária manual. O sistema utiliza métodos estatísticos (Regressão Linear) ou baseados em índices informados (Inflação Projetada) para calcular esses valores.

Acesse o módulo **Financeiro (SIGAFIN)**;

Acesse a rotina a partir da data inicial da qual deseja realizar a projeção;

Vá em **Atualizações > Cadastros > Moedas (MATA090)**;

Clique no botão **Outras Ações** e selecione a opção **Projetar**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37342502822679)

Na tela de parâmetros, selecione quais **moedas** deverão ser projetadas;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37342502823703)

Determine o **período de projeção**, indicando a quantidade de dias;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37342480630679)

Selecione o **método de projeção**:

* **Regressão Linear:** O sistema analisa o comportamento dos valores em dias anteriores para projetar a tendência futura (requer ao menos dois valores anteriores preenchidos).
* **Inflação Projetada:** O sistema aplica um percentual de inflação mensal informado sobre a última taxa cadastrada.

Clique em **Confirmar** para concluir o processo e gravar as taxas na tabela SM2.
