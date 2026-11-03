---
article_id: 360018977351
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: b0d2054797d6659548ed39ea21bb8d0498db476b8fe3c0935d9090803ffd1b9d
fetched_at: '2026-06-28T22:42:02.358040+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - O campo 10 do registro C190 não está sendo preenchido quando o COD_SIT é diferente
  de 00 e 01
type: support-article
updated_at: '2025-02-11T21:22:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018977351-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-O-campo-10-do-registro-C190-n%C3%A3o-est%C3%A1-sendo-preenchido-quando-o-COD-SIT-%C3%A9-diferente-de-00-e-01
---

**Ocorrência**O campo 10 do registro C190 não está sendo preenchido quando o campo COD\_SIT é diferente de 00 e 01.  
   
 **Ambiente**Microsiga Protheus – Livros Fiscais – A partir da versão 11.80.  
  
**Causa**De acordo com o Guia Prático do Sped Fiscal, o campo 10 (VL\_RED\_BC) do registro C190 somente será preenchido no seguinte caso:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014604611/mceclip2.png)  
   
 **Solução**Para solucionar essa ocorrência, verifique qual é o COD\_SIT do Registro mestre C100 e qual é a CST do ICMS. Caso não se enquadre na validação do campo 10 do registro C190, o valor será zerado.

**Tabela Situação do Documento:**

* 00 Documento regular
* 01 Documento regular extemporâneo
* 02 Documento cancelado
* 03 Documento cancelado extemporâneo
* 04 NF-e ou CT-e - Denegado
* 05 NF-e ou CT-e - Numeração inutilizada
* 06 Documento Fiscal Complementar
* 07 Documento Fiscal Complementar extemporâneo.
* 08 Documento Fiscal emitido com base em Regime Especial ou Norma Específica
