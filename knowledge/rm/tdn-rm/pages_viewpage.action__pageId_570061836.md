---
content_hash: 6149ad6e40decede7a0712243f844283eb3a108d119f9182963e708d5dbfa4f1
fetched_at: '2026-06-29T00:10:52.107420+00:00'
page_id: '570061836'
product: rm
source: tdn-rm
title: Cadastro Títulos a Pagar - (Integração RM TCGI x Backoffice Protheus - EAI2)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=570061836
version: 2
---

As parcelas a pagar geradas pelo distrato, serão gerenciadas pelo Protheus assim como no EAI 1.0. Abaixo temos alguns pontos a serem verificados para podermos gerarmos os títulos a pagar no Protheus.

**1) Natureza financeira a pagar.**

É necessário cadastrar no Protheus uma natureza financeira a pagar, esta natureza deve ter o parâmetro "Uso natureza" como LIVRE para funcionar corretamente.

**2) Tipo de Título / Tipo de Documento**

È necessário ativar o parâmetro de integração USESDOCUMENTTYPE caso deseje utilizar o tipo de documento diferente de NF/PR. Assim será possível definir qual tipo de documento será enviado ao backoffice na geração do título.

Este cadastro fica no módulo Integração no RM no menu EAI 2.0 → Parâmetros adapter.
