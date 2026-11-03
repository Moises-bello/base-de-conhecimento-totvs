---
article_id: 360011880431
category: Materiais - Compras (SIGACOM)
content_hash: 2589f1cb9eb7399111792387cc85f7065dad9cc1dcb47b94a1659eb711069d3e
fetched_at: '2026-06-28T22:41:08.942611+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - HELP: NFDGSPTZ ao
  realizar o retorno da nota de saída (devolução)'
type: support-article
updated_at: '2022-07-26T13:49:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011880431-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-HELP-NFDGSPTZ-ao-realizar-o-retorno-da-nota-de-sa%C3%ADda-devolu%C3%A7%C3%A3o
---

**Dúvida**Por que o help NFDGSPTZ é apresentado no momento de retornar a NF?  
  
**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
**Solução**

O help (**NFDGSPTZ**) só é apresentado quando sua nota de origem já foi totalmente devolvida. A verificação quanto a devolução total da nota pode ser realizada da seguinte forma:

• Localizar na tabela SD2 a nota original (remessa), e verificar o valor do campo **Ident. PD3** (D2\_IDENTB6). Este campo é utilizado quando a nota controla poder de terceiros e relaciona o registro da tabela SD2 com os registros na tabela SB6.

• Na tabela SB6, utilize o valor encontrado para D2\_IDENTB6 e filtre pelo campo **Seq. Ident.** (B6\_IDENT).

• Após o filtro são apresentados os registros do controle de poder de terceiros, de remessa e de devolução. Destes registros filtrados, identifique o registro de remessa (ele terá B6\_DOC+B6\_SERIE+B6\_CLIFOR+B6\_LOJA iguais ao da nota de remessa e o campo **Poder Terc.** (B6\_PODER3 = **R**).

• Neste registro o campo **Saldo** (B6\_SALDO) estará zerado, por este motivo o help é apresentado, pois a nota já foi retornada.

• A partir desse filtro é possível identificar as notas de retorno. Todos os registros onde o campo **Poder Terc.**  (B6\_PODER3 = **D**) são notas de devolução de poder de terceiros.

**Saiba mais em :**

**[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)**

**[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)**
