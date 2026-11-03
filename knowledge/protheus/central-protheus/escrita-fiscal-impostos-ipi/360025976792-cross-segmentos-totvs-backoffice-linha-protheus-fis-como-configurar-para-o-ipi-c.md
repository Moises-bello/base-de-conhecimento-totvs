---
article_id: 360025976792
category: Escrita Fiscal - Impostos - IPI
content_hash: 7c56662ba8b80054e05920d6c67eaa4b79c521e96cc09e199049dc24bc44cd03
fetched_at: '2026-06-28T22:39:28.964867+00:00'
product: protheus
section_id: 1500001538641
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar para
  o IPI compor/incidir na base do ICMS ST?
type: support-article
updated_at: '2021-09-23T23:24:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025976792-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-para-o-IPI-compor-incidir-na-base-do-ICMS-ST
---

**Dúvida**

Como configurar para o IPI compor/Incidir na Base do ICMS ST?  
  
**Ambiente**

Protheus– Livros Fiscais– A partir da versão 12.1.17  
  
  
**Solução**

Cadastro de TES:

IPI Bs.ICMST **(F4\_SOMAIPI) =** Sim

Indica se valor do IPI irá compor a base do ICMS-ST

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025436751/mceclip1.png)

Ou pelo parâmetro:

**MV\_SOMAIPI**:

* **T:** O valor de IPI não é considerado para compor a Base de Cálculo do ICMS-ST.
* **F (default):** O valor de IPI é considerado para compor a Base de Cálculo do ICMS-ST.
