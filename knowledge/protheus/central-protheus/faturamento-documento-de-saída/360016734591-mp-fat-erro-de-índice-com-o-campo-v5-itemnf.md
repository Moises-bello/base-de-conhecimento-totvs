---
article_id: 360016734591
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: e1cb74faf835bf6b7c39ac61ee9bae141b0c578fc5c97d354b923a345d2d25d2
fetched_at: '2026-06-28T22:38:45.201004+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: MP - FAT -  Erro de índice com o campo V5_ITEMNF
type: support-article
updated_at: '2021-04-28T15:13:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016734591-MP-FAT-Erro-de-%C3%ADndice-com-o-campo-V5-ITEMNF
---

**Ocorrência**

 Erro de índice com o campo V5\_ITEMNF

**Ambiente**

Microsiga Protheus - versão 12.

**Causa**

Na preparação da seleção das notas de devoluções de venda dentro do processamento da desoneração da folha de pagamento ocorre uma inconsistência com relação à configuração do tamanho necessário do campo do Item da NF (**V5\_ITEMNF** - da Tabela **SV5):**

DB error (Insert): -37 File: SV5010 - Error : 2601 (23000) (RC=-1) - [Microsoft][ODBC SQL Server Driver][SQL Server]Cannot insert duplicate key row in object 'dbo.SV5010' with unique index 'SV5010\_UNQ'.

A possível causa do erro é o tamanho do campo de item na tabela SV5.

**Solução**

Realizado o ajuste do tamanho do campo do Item da NF da tabela **SV5** para **4 dígitos**.

Saiba mais: **[Ajuste do tamanho do campo V5\_ITEMNF](http://tdn.totvs.com/display/PROT/2193658+DSERFAT-5024+DT+Ajuste+do+tamanho+do+campo+V5_ITEMNF%20%20%C2%A0)**
