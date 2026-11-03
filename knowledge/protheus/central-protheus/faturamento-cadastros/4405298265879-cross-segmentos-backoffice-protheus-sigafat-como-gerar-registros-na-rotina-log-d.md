---
article_id: 4405298265879
category: Faturamento - Cadastros
content_hash: d450cd5e7dc8e51881ed957d88d6c97cd91d107f818722212cfcfcbbcda3e97f
fetched_at: '2026-06-28T22:38:36.747593+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Como gerar registros na rotina
  Log de Produtos (MATC005)
type: support-article
updated_at: '2025-10-31T19:30:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405298265879-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-gerar-registros-na-rotina-Log-de-Produtos-MATC005
---

**Dúvida**Como gerar registros na rotina Log de Produtos (MATC005)?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12  
  
**Solução**Segue exemplo de como gerar registros na rotina **"Log de Produtos" (MATC005)**:

**1 -** Configure o parâmetro **MV\_USALOGP = .T.**

**2 -** Na rotina **"Campos de Produtos Controlados" (MATA013)** incluir o campo que deseja gerar o log:

* **Exemplo:** Tabela = **SB1** / Campo = **B1\_PRV1**

**3 -** No cadastro do produto alterar o preço do produto **"Preco Venda (B1\_PRV1)"**.

Na rotina **(MATC005)** será gerado registro da alteração do campo **(B1\_PRV1)**com os dados da alteração.

**Obs.:** É possível utilizar campos das tabelas **SB1** e **SB5**.
