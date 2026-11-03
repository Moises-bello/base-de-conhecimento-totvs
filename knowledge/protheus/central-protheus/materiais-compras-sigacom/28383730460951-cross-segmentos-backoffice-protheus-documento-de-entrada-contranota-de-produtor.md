---
article_id: 28383730460951
category: Materiais - Compras (SIGACOM)
content_hash: c34999637e00ac89392a541a0d05288aff6f08a9c423789b4fd181fa29660d85
fetched_at: '2026-06-28T22:41:11.849368+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Documento de Entrada - Contranota de
  Produtor
type: support-article
updated_at: '2024-12-09T14:09:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28383730460951-Cross-Segmentos-Backoffice-Protheus-Documento-de-Entrada-Contranota-de-Produtor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28383719476375) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Como Incluir Nota fiscal de Entrada de Contranota de Produtor?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Versão 12

**Solução**

Para Incluir a Nota siga o passo a passo :

1. Incluir uma nota de Entrada com **formulário próprio = Não Espécie = CTE** **(Esta não é transmitida).**

2.Incluir nota de Entrada com formulário próprio = Sim, Espécie = SPED **(Esta é transmitida).** Esta nota deve ser referenciada à anterior que não foi transmitida. E, para referenciar a de origem, os três campos a seguir precisam estar preenchidos:

**D1\_ITEMORI, D1\_SERIORI, D1\_NFORI** (nota de entrada).

OBS : Quando é feita uma nota complementar ou de devolução, elas devem ter formulário próprio = Sim Espécie = SPED e essa nota deve ser referenciada à que foi transmitida e não à primeira, com formulário próprio = Não.

E, para referenciar a de origem, os três campos precisam estar preenchidos:

**D1\_ITEMORI, D1\_SERIORI, D1\_NFORI**(nota de entrada)

![Produtor-Rura-v.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/28383730444695)

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
