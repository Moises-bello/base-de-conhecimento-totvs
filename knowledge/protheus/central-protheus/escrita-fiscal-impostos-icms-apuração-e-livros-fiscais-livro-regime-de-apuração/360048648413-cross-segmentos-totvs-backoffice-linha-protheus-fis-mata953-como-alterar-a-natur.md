---
article_id: 360048648413
category: Escrita Fiscal - Impostos - ICMS - Apuração e Livros Fiscais - Livro - Regime
  de Apuração
content_hash: 911ab86d368a12d0e238427e461d388440005e4c2f6135be957280dcba6c63e9
fetched_at: '2026-06-28T22:39:22.213631+00:00'
product: protheus
section_id: 1500001538681
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- MATA953 - Como alterar
  a Natureza do Título (E2_NATUREZ) gerada para o ICMS Próprio?
type: support-article
updated_at: '2021-12-16T18:02:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048648413-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-MATA953-Como-alterar-a-Natureza-do-T%C3%ADtulo-E2-NATUREZ-gerada-para-o-ICMS-Pr%C3%B3prio
---

**Dúvida**Como alterar a Natureza do Título (E2\_NATUREZ) gerada para o ICMS Próprio?

**Ambiente**Protheus - Todas as versões

**Solução**

Ao gerar o título de ICMS Próprio tanto no lançamento da nota quanto na apuração do ICMS o sistema irá gravar o campo E2\_NATUREZ com o conteúdo preenchido no parâmetro MV\_ICMS.

Para alterar a Natureza no título, uma opção seria alterar o conteúdo do parâmetro, porém esse parâmetro pode refletir também nos títulos de ICMS ST e Difal.

Nesse caso existe o ponto de entrada TITICMST que poderá ser utilizado para alterar a natureza do título.

Segue link abaixo com as orientações desse ponto de entrada.

<https://tdn.totvs.com/display/public/PROT/Ponto+de+Entrada+TITICMST+-+GravaTit+do+programa+FISXAPUR>
