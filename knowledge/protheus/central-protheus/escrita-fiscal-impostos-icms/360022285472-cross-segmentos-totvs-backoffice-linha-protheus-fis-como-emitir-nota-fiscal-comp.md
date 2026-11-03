---
article_id: 360022285472
category: Escrita Fiscal - Impostos - ICMS
content_hash: 77e731f8cab2f821a7e00f167b87d5dbd0c71f1f3141855496071c03d6a990b0
fetched_at: '2026-06-28T22:39:24.417525+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como emitir nota fiscal
  Complementar FECP ICMS Próprio e FECP-ST
type: support-article
updated_at: '2021-07-20T14:24:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022285472-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-emitir-nota-fiscal-Complementar-FECP-ICMS-Pr%C3%B3prio-e-FECP-ST
---

**Dúvida**Como emitir nota fiscal Complementar FECP ICMS Próprio e FECP-ST ?  
   
 **Ambiente**Protheus– Fiscal – A partir da versão 11.80]  
  
**Solução**

O FECP deverá ser configurado pela rotina FISA080- UFXUF:

UF Origem

UF Destino

Aliq FECP

TES:

ISEN FECP = Não

A nota fiscal complementar do FECP - ICMS Próprio deve ser emitida pela Rotina MATA920, configurar:

Valor Unitário

Valor Total

D2\_BASEICM

TES:

Calcula ICMS = Sim

L. Fiscal ICMS = Tributado

Agrega Valor = Não

Para nota fiscal Complementar FECP ICMS-ST, deve ser emitida pela Rotina MATA920, configurar:

Valor Unitário

Valor Total

D2\_BRICMS - Base do ICMS-ST/ FECP-ST

D2\_ICMSRET - Valor ICMS-ST

TES:

Calcula ICMS = Não

L. Fiscal ICMS = Zerado

Agrega Valor = Não

Agrega Solid = Sim

Sit.trib.ICMS **(F4\_SITTRIB)** = 10, 30, 70 e 90

Fórmula**(F4\_FORMULA)** = Amarrar uma fórmula com conteúdo texto = "Complemento" para que o sistema não destaca o ICMS normal nos livros, apenas o ICMS retido

* Para casos de preenchimento do campo Sit. trib. ICMS **(F4\_SITTRIB)**= 10,30,70 e 90, configure o campo Agrega Solidário **(F4\_INCSOL)** = Sim
