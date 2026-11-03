---
content_hash: 4010557bcab6f6002fd29d14110653ba279ac9950a50b259f799c855a7c10468
fetched_at: '2026-06-29T00:10:52.105664+00:00'
page_id: '570059924'
product: rm
source: tdn-rm
title: Processo Distrato Contratual (Integração RM TCGI x Backoffice Protheus - EAI2)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=570059924
version: 3
---

Ao criar um plano de financiamento de devolução deverá ser informado o fornecedor para a geração do título a pagar.  
  
Para se gerar Lançamentos a pagar, se faz necessário vincular um Fornecedor ao cadastro do Cliente , pois na Integração Protheus , não se pode  usar a opção de AMBOS no cadastro de Cliente.

Parametrizações:

Ambiente >> Parâmetros >> Totvs Incorporação: Integração Financeira  
  
Integração Financeira >> Bloqueio de Lançamento Distrato  
  
Tipo de Bloqueio:

* Bloqueado (RM irá controlar e somente enviará os títulos ao Protheus quando o distrato for efetivado)
* Provisionado (RM irá enviar o título ao Protheus, assim que gerar o plano de financiamento de devolução, utilizando o tipo de título selecionado, geralmente é utilizado PR)
