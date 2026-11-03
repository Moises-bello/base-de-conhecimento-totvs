---
content_hash: fe6b1db8dfdf0222e5f51e0c5d87a2a1d993c6609ed67a8658ab32ec2919841c
fetched_at: '2026-06-29T00:10:52.109042+00:00'
page_id: '570061918'
product: rm
source: tdn-rm
title: Processo Títulos a Pagar - (Integração RM TCGI x Backoffice Protheus - EAI2)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=570061918
version: 3
---

**1) Baixa de títulos a pagar**

Todo o módulo de contas a pagar será gerenciado pelo Protheus.

A baixa e o cancelamento de baixa será feito como no EAI 1.0.

A baixa total ou parcial do título refletirá nos lançamentos  do RM TCGI.

A mensagem responsável por esse processo é a **ACCOUNTPAYABLEDOCUMENTDISCHARGE**.

**6) Cancelamento de baixa.**

O cancelamento da baixa será feito também pelo Protheus.

O resultado da baixa também será refletido no RM TCGI.

A mensagem responsável por esse processo é a **REVERSALOFACCOUNTPAYABLEDOCUMENTDISCHARGE**.
