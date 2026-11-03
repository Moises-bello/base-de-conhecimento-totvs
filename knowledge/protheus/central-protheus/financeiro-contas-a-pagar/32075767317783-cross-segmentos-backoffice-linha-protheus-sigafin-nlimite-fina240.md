---
article_id: 32075767317783
category: Financeiro - Contas a Pagar
content_hash: a7247a80bbcb702a08ec1e2cfd4f3b40b003d690c8ff8a5211b784429cb8486e
fetched_at: '2026-06-28T22:38:07.148102+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - NLIMITE - FINA240
type: support-article
updated_at: '2025-05-13T17:56:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32075767317783-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-NLIMITE-FINA240
---

**Ocorrência**

Ao inserir um valor no campo **NLIMITE**, traz todos os títulos do ambiente não respeitando o valor inserido

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32075776082967)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**

Para garantir o correto funcionamento da funcionalidade, é essencial que o campo em questão seja validado em conjunto com o parâmetro de pergunta (F12) **"Marca Títulos Automático?"**.

* **Quando o parâmetro estiver definido como "SIM"**, o sistema irá considerar os valores dos títulos existentes, somando-os ao valor inserido no campo.
* **Quando definido como "NÃO"**, o sistema irá considerar apenas o valor informado no campo, desconsiderando os títulos existentes.

Essa validação conjunta assegura que a funcionalidade opere conforme esperado, refletindo corretamente os valores dos títulos conforme a configuração do parâmetro.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32075776085655)
