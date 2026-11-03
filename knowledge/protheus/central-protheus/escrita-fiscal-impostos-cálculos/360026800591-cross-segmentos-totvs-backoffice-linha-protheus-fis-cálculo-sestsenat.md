---
article_id: 360026800591
category: Escrita Fiscal - Impostos - Cálculos
content_hash: dd7c9d5f42e52c68ea61e8652220d4ecfcc62a6c37270005385580fb7075713f
fetched_at: '2026-06-28T22:39:30.659729+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Cálculo SEST/SENAT
type: support-article
updated_at: '2021-07-29T13:22:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026800591-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-C%C3%A1lculo-SEST-SENAT
---

**Dúvida**

Configuração para calcular SEST/SENAT

**Ambiente**

Protheus – Fiscal – A partir da versão 11.80

**Solução**

Para gerar o imposto, basta realizar as seguintes configurações:

**No cadastro de Fornecedor:**

Campo **A2\_RECSEST** = Sim - Neste fornecedor deve ser amarrada uma natureza com os campos **ED\_CALCSES, ED\_BASESES** e **ED\_PERCSES** preenchidos.

**No cadastro de TES:**

Campo **F4\_DUPLIC** = Sim

**Cadastro Natureza:**

Calc.SEST (ED\_CALCSES) = Sim

Base SEST (ED\_BASESES) = Preenchido caso haja redução de Base.

Porc.SEST (ED\_PERCSES) = Alíquota de SEST/SENAT
