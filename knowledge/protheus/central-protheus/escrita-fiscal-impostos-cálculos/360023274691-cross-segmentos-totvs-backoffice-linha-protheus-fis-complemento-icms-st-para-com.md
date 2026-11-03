---
article_id: 360023274691
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 99b8085537edfbb9eaac8591ec3dba9b3cbb55c2d96e0e630722a16f529b18c1
fetched_at: '2026-06-28T22:39:30.685295+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Complemento ICMS
  ST para compra '
type: support-article
updated_at: '2021-11-05T17:52:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023274691-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Complemento-ICMS-ST-para-compra
---

**Dúvida**Como emitir nota fiscal Complementar de ICMS-ST pelo Documento de Entrada  ?

**Ambiente**Protheus - Fiscal –  A partir da versão 11.80  
  
  
**Solução**

Incluir um documento de entrada, informado que trata-se de um Complemento de ICMS.

No documento de entrada informe o código do produto da 1º nota e o valor do ICMS complementar nos campos Vlr.Unitario (D1\_VUNIT), Vlr.Total (D1\_TOTAL) e ICMS Solid (D1\_ICMSRET).

É necessário amarrar a nota fiscal de origem através do campo Docto. Origem **(D1\_NFORI).**

**Configuração da TES:**

Credita ICMS **(F4\_CREDICM)** = Não  
Calcula ICMS **(F4\_ICM)** = Não  
Agrega Solidário **(F4\_INCSOL)** = Não  
L. Fiscal ICMS **(F4\_LFIMC)** = ICMS Zerado  
Sit.trib.ICMS **(F4\_SITTRIB)** = 10/30/70

Agrega valor = sim

Fórmula **(F4\_FORMULA)** = Amarrar uma fórmula com conteúdo texto = "Complemento" para que o sistema não destaca o ICMS normal nos livros, apenas o ICMS retido.

Verifique se o ICMS ST foi calculado na aba impostos, confirme a operação e veja o resultado nos livros fiscais.
