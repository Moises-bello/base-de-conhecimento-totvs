---
article_id: 360015681712
category: Financeiro - Contas a Pagar
content_hash: 2e9364dba5e5445a898d5eb9beec7d64d935cc10ef0b504b15664efa288d2ce0
fetched_at: '2026-06-28T22:38:06.866636+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento  Backofficce Linha Protheus- FINA080 - Como gerar PA sem movimento
  e posteriormente gerar movimentação bancária
type: support-article
updated_at: '2025-02-12T19:38:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015681712-Cross-Segmento-Backofficce-Linha-Protheus-FINA080-Como-gerar-PA-sem-movimento-e-posteriormente-gerar-movimenta%C3%A7%C3%A3o-banc%C3%A1ria
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29942715550871) Tempo aproximado para leitura: **00:05 min**

**Dúvida**Como gerar PA sem movimento e posteriormente gerar movimentação bancária?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – Todas as versões

**Solução**

Ao incluir o registro no **Contas a Pagar** referente a uma **PA**, pressione **F12** para acessar os parâmetros. Na tela exibirá os parâmetros, os campos abaixo devem ser configurados da seguinte forma:

* **Gerar Chq. p/ Adiant** = "Sim"
* **Movi. Banc. sem Cheque** = "Não"

Com essa configuração, será gerado um movimento na **SE5**, onde o campo **E5\_TIPODOC** será registrado como **BA** (sem movimentação bancária).

Para liberar a **PA** e permitir a geração da movimentação bancária, acesse a rotina **Geração de Cheques do Contas a Pagar (FINA190)**. Em **Outras Ações**, selecione a opção **Liberar Cheque**.

Na tela exibida, preencha as informações necessárias e confirme a operação.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/29931313166103)**

Após a confirmação, será gerado um movimento com **E5\_TIPODOC = CH**, registrando a movimentação bancária correspondente.
