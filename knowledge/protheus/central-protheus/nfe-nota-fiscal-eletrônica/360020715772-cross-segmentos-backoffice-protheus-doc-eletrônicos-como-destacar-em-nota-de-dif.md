---
article_id: 360020715772
category: NFe - Nota Fiscal Eletrônica
content_hash: 504beb03d87ff07917987581cc870700b1206ace3e7d53a8a53743b4b8fec70d
fetched_at: '2026-06-28T22:40:05.666743+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como destacar em
  nota de diferimento BC.ICMS e V.ICMS no XML e Danfe
type: support-article
updated_at: '2025-06-17T12:08:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020715772-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-destacar-em-nota-de-diferimento-BC-ICMS-e-V-ICMS-no-XML-e-Danfe
---

**Dúvida**

Como destacar em nota de diferimento BC.ICMS ( Base de calculo do ICMS) e V.ICMS (Valor do ICMS) no XML e Danfe ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /****Cadastros / Parâmetros** clicar em editar **MV\_ART186 = .T.**

* **Para não destacar BC.ICMS e V.ICMS no XML e Danfe**

2. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /****Cadastros / Parâmetros** clicar em editar **MV\_ART186 = .F.**

* **Para destacar BC.ICMS e V.ICMS no XML e Danfe**

* **Saiba Mais:**

Alteração desse parâmetro pode causar a rejeição 929 conforme o link de documentação abaixo:

[MP - NFE - 929 Rejeição: Informado CST de diferimento sem as informações de diferimento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033190014)
