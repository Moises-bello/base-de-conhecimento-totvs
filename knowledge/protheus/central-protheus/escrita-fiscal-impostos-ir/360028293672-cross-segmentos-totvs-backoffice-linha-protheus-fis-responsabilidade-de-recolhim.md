---
article_id: 360028293672
category: Escrita Fiscal - Impostos - IR
content_hash: da2efb831e1555523e22ed8c6e8c153db5be7ad83458b68802170807e7e7a2b0
fetched_at: '2026-06-28T22:39:31.927358+00:00'
product: protheus
section_id: 1500001549802
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Responsabilidade
  de recolhimento do IR pelo prestador de serviço, controlando somente pela natureza
  financeira.
type: support-article
updated_at: '2021-06-17T13:01:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028293672-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Responsabilidade-de-recolhimento-do-IR-pelo-prestador-de-servi%C3%A7o-controlando-somente-pela-natureza-financeira
---

**Dúvida**  
Preciso que o IR seja recolhido pelo prestador sem alterar o cadastro do cliente, como proceder?

**Ambiente**

Protheus – Faturamento – A partir da versão 11.80.  
  
**Solução**

Cliente possui o campo Recolhe IRRF (A1\_RECIRRF) = SIM e não deseja toda vez alterar esse campo no cadastro do cliente, pois tem serviços que ele é o responsável pelo recolhimento e outros que o seu cliente é o responsável.

Para essa tratativa o cliente pode controlar essa questão através de duas naturezas, sendo:

**NATUREZA A (AUTO RETENÇÃO):**

Recolhe IRRF (ED\_RECIRRF) = Não (Será gerado um título no contas à pagar).

**NATUREZA B (RETENÇÃO PARA O SEU CLIENTE):**

Recolhe IRRF (ED\_RECIRRF) = Cadastro do cliente (Será gerado um título no contas à receber).
