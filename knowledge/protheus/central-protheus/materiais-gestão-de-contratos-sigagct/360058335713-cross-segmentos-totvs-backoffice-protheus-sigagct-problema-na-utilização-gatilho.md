---
article_id: 360058335713
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 43412dc0f004fbc6bb66af8cdd4b1f4b62425767ae71ba313de991cc0190527a
fetched_at: '2026-06-28T22:37:24.049597+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Problema na utilização
  gatilho customizado no campos CNK_TPDOC ou CNK_CONTRA
type: support-article
updated_at: '2022-05-19T21:31:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058335713-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Problema-na-utiliza%C3%A7%C3%A3o-gatilho-customizado-no-campos-CNK-TPDOC-ou-CNK-CONTRA
---

**Dúvida**

Problema na utilização gatilho customizado no campos CNK\_TPDOC ou CNK\_CONTRA

**Ambiente**

Protheus – Gestão de Contrato – Até a versão 12.1.25

**Solução**

Na tabela CNK, referente a inclusão de Documentos do Contrato (CNTA170), ao utilizar gatilho customizado nos campos CNK\_TPDOC ou CNK\_CONTRA o gatilho não funciona

Esta ocorrência de setembro/2019 tratava-se de uma instrução inválida na validação (X3\_VALID) dos campos CNK\_TPDOC e CNK\_CONTRA, e desta forma essa instrução foi removida.

Por se tratar de ajuste de dicionário de dados **o ajuste foi disponibilizado somente no último release, no caso o 12.1.27.**

Abaixo link com a documentação contendo o De/Para referente ao X3\_VALID dos campos acima.

***Saiba Mais:***

[DMANMAT02-18212 DT Inconsistência na validação dos campos CNK\_CONTRA e CNK\_TPDOC](https://tdn.totvs.com/x/ecy2Hg)
