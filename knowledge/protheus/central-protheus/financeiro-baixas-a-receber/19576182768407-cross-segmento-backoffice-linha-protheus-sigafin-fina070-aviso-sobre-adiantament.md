---
article_id: 19576182768407
category: Financeiro - Baixas a Receber
content_hash: deaa7ef8505480bc137fc76c5b1f2cc794b0ac72c3e8c8c67d052ef6504984ba
fetched_at: '2026-06-28T22:37:43.660096+00:00'
product: protheus
section_id: 33820269506967
source: central-protheus
title: Cross Segmento - Backoffice - Linha Protheus - SIGAFIN - FINA070 - Aviso sobre
  adiantamento/título de crédito
type: support-article
updated_at: '2025-07-30T14:50:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19576182768407-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA070-Aviso-sobre-adiantamento-t%C3%ADtulo-de-cr%C3%A9dito
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19576185405335) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como verificar se o cliente tem um credito antes de realizar a baixa.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA070 - Todas as versões  
  
**Solução**

O parâmetro **MV\_VLTITCR**ativa a exibição de aviso sobre adiantamento/título de crédito no momento da baixa do título:

* Caso tenha RA em aberto para o mesmo cliente:  
  **O cliente deste título possui Recebimentos(s) Antecipado(s). Deseja mesmo assim baixá-lo?**
* Caso tenha NCC em aberto para o mesmo cliente**:**  
  **O cliente deste título possui título(s) de crédito. Deseja mesmo assim baixá-lo?**

Tipo: Lógico

Conteúdo: .**T**. ativa, ou .**F**. não ativa

Descrição: Exibe uma mensagem de aviso se houver Adiantamento/Título de crédito no momento da baixa do título na rotina Baixas a Receber (FINA070).

Para a utilização desse parâmetro, é necessário criá-lo no ambiente Configurador (SIGACFG) com valor lógico .**T**.
