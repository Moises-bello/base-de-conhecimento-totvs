---
article_id: 36810409157527
category: Financeiro - Contas a Pagar
content_hash: 237cd3512fed39f6dabb58e9a2d11462ca36a68864ed23e723abb633d4751c63
fetched_at: '2026-06-28T22:38:07.174420+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Brasil - Cross Segmentos - Backoffice (Linha Protheus) - Financeiro - Contas
  a Pagar - FINA240 - Exclusão de registro na tabela SEA
type: support-article
updated_at: '2025-12-05T17:48:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36810409157527-Brasil-Cross-Segmentos-Backoffice-Linha-Protheus-Financeiro-Contas-a-Pagar-FINA240-Exclus%C3%A3o-de-registro-na-tabela-SEA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36810454627991) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Registro foi excluído da tabela SEA, de que forma isso pode acontecer?  
  
**Solução**

A tabela **SEA** é a tabela padrão do Protheus que armazena as informações de **Borderô**.

**Borderô** é o documento ou agrupamento de títulos (a pagar ou a receber) que serão processados em conjunto, geralmente para envio ao banco (transferência ou cobrança/pagamento via CNAB).

Quando o borderô é cancelado, os registros referentes aos títulos na tabela SEA são excluídos.

**FINA240/FINA241:** O sistema **exclui** o registro do borderô na tabela **SEA** e reverte o status dos títulos na tabela de títulos a pagar (**SE2**).

**FINA060/FINA061:** O sistema **exclui** o registro do borderô na tabela **SEA** e reverte o status dos título na tabela de títulos a receber (**SE1**).
