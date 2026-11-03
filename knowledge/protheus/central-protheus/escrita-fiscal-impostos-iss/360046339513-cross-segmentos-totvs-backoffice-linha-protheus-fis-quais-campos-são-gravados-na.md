---
article_id: 360046339513
category: Escrita Fiscal - Impostos - ISS
content_hash: 92643e0f0ee5c9ab19e155692a08a3e69a12aa5b1d47d271e7106952625d3e27
fetched_at: '2026-06-28T22:39:35.239423+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Quais campos são
  gravados na retenção de ISS em uma nota de saída?
type: support-article
updated_at: '2021-06-17T12:43:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046339513-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Quais-campos-s%C3%A3o-gravados-na-reten%C3%A7%C3%A3o-de-ISS-em-uma-nota-de-sa%C3%ADda
---

**Dúvida**Quando efetuar SAÍDA e tiver ISS retido, onde são gravadas as informações de ISS?  
  
**Ambiente**Protheus - Fiscal - A partir da versão 12.1.17  
  
**Solução**

Os campos que gravam retenção de ISS em nota de saída são:

**Tabela SE1**

E1\_BASEISS, E1\_ISS, E1\_VRETISS

**Tabela SF2**

F2\_BASEISS, F2\_VALISS

**Tabela SD2**

D2\_BASEISS, D2\_ALIQISS, D2\_VALISS

**Tabela SFT**

Para retenção de ISS FT\_RECISS=1 é retenção e FT\_RECISS=2 Sem retenção

FT\_TIPO = S

FT\_BASEICM, FT\_ALIQICM, FT\_VALICM, FT\_OUTRICM, FT\_ISENICM

\* Como na SFT não existe um campo para ISS, o sistema utiliza os mesmos campos do ICMS, o que diferencia é o FT\_TIPO = S

\* FT\_VALICM se o livro de ISS estiver como tributado, FT\_OUTRICM se o livro de ISS estiver como outros, FT\_ISENICM se o livro de ISS estiver como isento.

Configuração para tratamento da Retenção ISS:  <https://tdn.totvs.com/pages/releaseview.action?pageId=6076798>
