---
article_id: 20265853889047
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 1447cb5e3feb3c2b826ce45b7a67e063d81e93459f79c5711a05d5dcba00e3db
fetched_at: '2026-06-28T22:38:42.632290+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento)
  - Faturar produto com poder DE/EM terceiros
type: support-article
updated_at: '2024-01-02T18:58:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20265853889047-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-Faturar-produto-com-poder-DE-EM-terceiros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20265853844503) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como usar o saldo de/em terceiros para realizar uma venda?

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento) - Todas as versões  
  
**Solução**É possível em determinadas ocasiões, usar o produto em poder terceiros para a venda, baixando assim o campo "Qt.Ter.Ns.Pd" (B2\_QTNP).

Basta realizar os 3 passos abaixo:

1 - Crie uma TES saída com poder de/em terceiros:  
"Poder Terc. \* (F4\_PODER3) = 'R - Remessa' ou 'Devolução'

2 - Crie uma TES saída de venda com os campos:  
"Poder Terc. \* (F4\_PODER3)" = 'N - Nao Controla'  
"Sld. Poder (F4\_SLDNPT)" = '1 - Disponivel para faturamento'  
"Tes Ret.Simb (F4\_TESP3)" = Coloque a TES do passo 1

3 - Coloque a TES saída no passo 2 no pedido de venda e fature.

OBS 1: Ao faturar, subtrairá no campo "Qt.Ter.Ns.Pd" (B2\_QTNP)

OBS 2: Ao faturar, criará uma nova linha na tabela SB6 com a quantidade faturada e documento que a gerou de saída, campo "Doc.Original" (B6\_DOC), mesmo que usado para venda, por conta do vínculo com o TES simbólica.

**Saiba mais:**  
[How To | MP - SIGAFAT - Conceito: Poder De/Em Terceiros](https://youtu.be/oS5sdoZBdN8)
