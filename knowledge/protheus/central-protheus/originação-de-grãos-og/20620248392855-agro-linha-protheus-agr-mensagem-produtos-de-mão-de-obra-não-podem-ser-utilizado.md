---
article_id: 20620248392855
category: Originação de Grãos (OG)
content_hash: fd4a3a5c052e113c99e937064d6f9a9d63f46d6f104ad7e66bd62679c1e9e877
fetched_at: '2026-06-28T22:45:41.002050+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Mensagem Produtos de mão-de-obra não podem ser
  utilizados para esta operação
type: support-article
updated_at: '2025-06-21T16:14:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20620248392855-Agro-Linha-Protheus-AGR-Mensagem-Produtos-de-m%C3%A3o-de-obra-n%C3%A3o-podem-ser-utilizados-para-esta-opera%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20620248344727) Tempo aproximado para leitura: **00:01:05 min****Dúvida**  
Mensagem de Produtos de mão-de-obra não podem ser utilizados para esta operação. Como proceder?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

**1.** Acesse o **cadastro do Produto** e verifique se ele é **mão-de-obra**. Caso seja, não será possível utilizá-lo para a geração de **Nota Fiscal**;

**2.** Verifique se o código do produto é formado pela sigla **MOD + Centro de Custo**, pois isso identifica um produto como Mão-de-Obra;

**3.** Verifique se os campos **B1\_CCCUSTO e B1\_GCCUSTO** estão preenchidos, pois o preenchimento destes campos faz com que o produto seja considerado mão-de-obra. Caso precise que a informação de centro de custo esteja no cadastro de produto, informar na primeira aba campo **B1\_CC-centro de custo** e campo e **B1\_CONTA-conta contábil**.
