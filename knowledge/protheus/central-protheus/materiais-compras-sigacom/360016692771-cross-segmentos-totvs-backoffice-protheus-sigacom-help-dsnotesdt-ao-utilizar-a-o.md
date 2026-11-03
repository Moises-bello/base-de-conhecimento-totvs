---
article_id: 360016692771
category: Materiais - Compras (SIGACOM)
content_hash: a70c5e4afd881cc091f78a23f6da0221cd2ac27e33b4c5ac140202692b5b107b
fetched_at: '2026-06-28T22:41:07.344348+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus -  SIGACOM - Help DSNOTESDT ao
  utilizar a opção Retornar e selecionar a Nota Fiscal Origem
type: support-article
updated_at: '2025-06-27T14:08:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016692771-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-DSNOTESDT-ao-utilizar-a-op%C3%A7%C3%A3o-Retornar-e-selecionar-a-Nota-Fiscal-Origem
---

**Dúvida**No momento que utiliza a opção Retornar do Documento de Entrada **(MATA103)** e seleciona a nota origem apresenta a mensagem de Help **DSNOTESDT**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4421526322327)

**Ambiente**

Protheus - Compras - A partir da versão 12  
  
**Solução**

O HELP " **DSNOTESDT** "é apresentado quando no cadastro da TES não possui o campo **Tes Devol (F4\_TESDV)** preenchido com o TES de devolução. Ao vincular o TES de devolução o HELP não será apresentado e efetuará a devolução corretamente.  
  
Conferir se no cadastro do TES de saída o campo "TES devol" está preenchido com o TES de devolução, desta forma não teremos a exibição da mensagem salvo se a NF já foi devolvida, situação que poderá avaliar com o preenchimento dos campos D2\_QTDDEV e D2\_VALDEV pelo seu setor de TI.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
