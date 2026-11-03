---
article_id: 15360171608215
category: SIGAEST - SALDOS
content_hash: f7c25e64e0acf28081952fba775915c48fa1bdb96e9205b2c59df6907a33ad5a
fetched_at: '2026-06-28T22:39:14.895962+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA226 - campo BF_DATAVEN
  não apresenta a Data de Validade dos Lotes
type: support-article
updated_at: '2023-06-16T16:43:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15360171608215-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA226-campo-BF-DATAVEN-n%C3%A3o-apresenta-a-Data-de-Validade-dos-Lotes
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15360135397143) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Na rotina **SALDOS POR ENDEREÇO (MATA226)** o campo ***Data Vencimento (BF\_DATAVEN)*** esta vazio.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15360477660055)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

Na tabela SBF o campo **BF\_DATAVEN** que é apresentado no browser da rotina **SALDOS POR ENDEREÇO (MATA226)** é um campo obsoleto, atualmente sem uso. Toda a parte de validade do lote é gravado na tabela SB8 e controlado pelo **campo B8\_DTVALID.** Por exemplo, pode ser avaliado pelo relatório de **Posição de saldo por lote (MATR225)**.

***Dica:*** Caso desejar, excluir do browser o **BF\_DATAVEN** na rotina **SALDOS POR ENDEREÇO (MATA226)** para não gerar dúvidas nos usuários. Veja um passo a passo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15360979773335)

**Observe o resultado:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15361085189527)

***Saiba Mais:***

[*Clique aqui e veja mais artigos sobre SALDOS no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538801-SIGAEST-SALDOS)

*[SIGAEST - Conceito e tabelas de controle de Lote e Endereço no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-tabelas-de-controle-de-Lote-e-Endere%C3%A7o-no-Protheus)*
