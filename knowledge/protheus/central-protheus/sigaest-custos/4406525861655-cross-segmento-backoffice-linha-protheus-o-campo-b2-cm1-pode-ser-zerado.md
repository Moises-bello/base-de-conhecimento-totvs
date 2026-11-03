---
article_id: 4406525861655
category: SIGAEST - CUSTOS
content_hash: aca4ffbeaee95b4d70a48af8d99fbf3d01383e8c7d5fc8b61322563de108253f
fetched_at: '2026-06-28T22:39:00.516597+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - O campo B2_CM1 pode ser zerado?
type: support-article
updated_at: '2025-03-12T12:45:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406525861655-Cross-Segmento-Backoffice-Linha-Protheus-O-campo-B2-CM1-pode-ser-zerado
---

**Dúvida**O Campo B2\_CM1(Custo Unitário do produto) pode ter seu valor zerado?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos -  A partir da versão 12.

**Solução**Não, o campo B2\_CM1 é referencia ao custo médio gravado pelo produto, ele se torna um campo histórico, e o mesmo não pode ser zerado.

**Exemplo**

No Kardex abaixo, foi feita um movimento requisitando a quantidade e valor total do produto.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406516719255/mceclip1.png)

Observe na tabela SB2 (consulta realizada via APSDU), que o campo B2\_CM1 se mantem, mesmo que não exista mais "Quantidade" ou "Valor", pois ele se trata de um campo histórico, a ser levado custo para os próximos movimentos.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406525342999/mceclip0.png)

**Saiba mais**

*[O valor processado no campo B2\_CMFIM1 é repassado para o campo B2\_CM1?](https://tdn.totvs.com/pages/releaseview.action?pageId=284351848)*

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
