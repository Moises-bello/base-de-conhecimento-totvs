---
article_id: 4411624792343
category: Escrita Fiscal - CIAP
content_hash: 8fb7d3b1b6953de9a4ac3d86325f20d0faf2455c90d5e761799e22ffe48171bc
fetched_at: '2026-06-28T22:39:33.979058+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Procedimento Realizado
  ao Apresentar Alerta A905TUDOK
type: support-article
updated_at: '2021-10-27T19:45:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411624792343-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Procedimento-Realizado-ao-Apresentar-Alerta-A905TUDOK
---

**Dúvida**

Qual procedimento deve ser realizado ao apresentar alerta A905TUDOK? 

**Ambiente**Protheus – Fiscal – A partir da versão 11.80  
  
**Solução**

**Há inconsistência nos dados referentes ao CIAP, verifique o valor do crédito ou se o crédito já foi utilizado.**

Ocorre quando a Nota Fiscal de Entrada foi incluída sem o cálculo de ICMS ou com valor incorreto. Ao informar código do item o Sistema verifica a nota fiscal e não permite a inclusão, pois os dados informados não estão de acordo com a nota fiscal.

Verifique o valor do ICMS calculado para o item e deve ser lançado o valor que consta na nota fiscal.

Verifique cadastro de TES, campo **CRED ICMS** = **SIM**.
