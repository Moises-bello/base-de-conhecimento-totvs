---
article_id: 360047563554
category: Escrita Fiscal - Impostos - IPI
content_hash: fc7f2fcfabf20974d64d558b5c1be74051cef91afcb1ca34544cf5d99c4badbb
fetched_at: '2026-06-28T22:39:29.054404+00:00'
product: protheus
section_id: 1500001538641
source: central-protheus
title: 'MP - FIS - Como configurar o IPI na Base do ICMS ST ? '
type: support-article
updated_at: '2023-04-29T15:42:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047563554-MP-FIS-Como-configurar-o-IPI-na-Base-do-ICMS-ST
---

**Dúvida**Qual a configuração do Sistema para que o IPI seja considerado na Base do ICMS-ST?

**Ambiente**Protheus - Fiscal -  A partir da versão 11.80  
  
**Solução**

Para que o IPI seja considerado na Base de ICMS-ST é necessário verificar a configuração do parâmetro **MV\_SOMAIPI**:

* **T:** O valor de IPI não é considerado para compor a Base de Cálculo do ICMS-ST.
* **F (default):** O valor de IPI é considerado para compor a Base de Cálculo do ICMS-ST.
