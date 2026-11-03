---
article_id: 24476215996439
category: Financeiro
content_hash: 0fc379b49145de2418232163ba56492fc93ae3c3be5afd7d388192536fa591e7
fetched_at: '2026-06-28T22:38:03.168327+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA715 Job de Retorno
  de Recebimento API - Contabilização Online do Retorno API
type: support-article
updated_at: '2024-07-08T12:39:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24476215996439-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA715-Job-de-Retorno-de-Recebimento-API-Contabiliza%C3%A7%C3%A3o-Online-do-Retorno-API
---

## 

## **Ocorrência**

## No módulo Financeiro, ao tentar realizar Retorno de Cobrança, a contabilização não está sendo realizada pela data base.

## Ambiente Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro

## **Solução**

## Para resolver essa situação, siga estas instruções:

## 1. Vá para o módulo Financeiro, Atualizações, Cadastros> Parâmetros, Bancos e insira a quantidade de dias no campo dias de retenção.

## 2. Ajuste o parâmetro MV\_DTCNBX = 2

## 3. No novo painel gestor, certifique-se de que em configurações de contas o campo Contabiliza Online esteja marcado como sim.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24476168536471)

## **Saiba mais:**

## [Fique por dentro das atualizações Reinf Protheus](https://tdn.totvs.com/display/public/PROT/Protheus+-+REINF+Suporte+Financeiro#Eventos--839875140)

[Comunicação bancaria - FINA713](https://tdn.totvs.com/pages/releaseview.action?pageId=612548392)
