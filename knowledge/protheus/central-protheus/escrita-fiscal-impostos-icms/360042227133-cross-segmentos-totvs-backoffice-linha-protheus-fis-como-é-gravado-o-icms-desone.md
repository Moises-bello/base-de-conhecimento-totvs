---
article_id: 360042227133
category: Escrita Fiscal - Impostos - ICMS
content_hash: f56672bd99608eab39706d93ecfaafdd95bb329b44e05bd8f50aa9f55f7f0de1
fetched_at: '2026-06-28T22:39:24.184976+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como é gravado o
  ICMS desonerado na redução de base de calculo RJ?
type: support-article
updated_at: '2021-07-28T03:17:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042227133-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-%C3%A9-gravado-o-ICMS-desonerado-na-redu%C3%A7%C3%A3o-de-base-de-calculo-RJ
---

**Dúvida**Como é gravado o icms desonerado na redução de base de calculo RJ ?  
  
**Ambiente**Protheus - Fiscal - apartir da versão 12.1.17

**Solução**Temos duas formas de gravar o icms desonerado na redução de base de calculo no RJ:

1) Icms desonerado conforme resolução SEFAZ RJ 13/2019

Parâmetro

MV\_DESONRJ = RJ

TES

Calcula icms = sim

% red icms = 20%

L. fiscal icms = isento ou outros

CST = 20

Mot. Desone = 9

Valor da mercadoria 1000,00

Base de calculo do icms = 200,00

Aliquota do icms = 20% = 40,00

FECP 2% = 4,00

Valor do CD2\_desone = 200,00

Conforme documentação

<https://tdn.totvs.com/pages/releaseview.action?pageId=518467133>

2) Icms desonerado calculo simples para RJ

Parâmetro

MV\_DESONRJ = em branco

TES

Calcula icms = sim

% red icms = 20%

L. fiscal icms = isento ou outros

CST = 20

Mot. Desone = 9

Valor da mercadoria 1000,00

Base de calculo do icms = 200,00

Aliquota do icms = 20% = 40,00

FECP 2% = 4,00

Valor do CD2\_desone =160,00
