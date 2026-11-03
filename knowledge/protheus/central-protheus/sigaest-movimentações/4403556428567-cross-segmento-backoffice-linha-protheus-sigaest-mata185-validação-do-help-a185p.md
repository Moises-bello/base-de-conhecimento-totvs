---
article_id: 4403556428567
category: SIGAEST - MOVIMENTAÇÕES
content_hash: da6e49fd1f49a4c4ff1b5c067c20a7ff2084798299c4a5c032fa5ca983a370fa
fetched_at: '2026-06-28T22:38:56.910722+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA185 - Validação
  do Help A185PRE
type: support-article
updated_at: '2021-07-01T20:40:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403556428567-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA185-Valida%C3%A7%C3%A3o-do-Help-A185PRE
---

**Dúvida**Ao efetuar uma pré-requisição ou exclusão de pré-requisição ao Armazém (MATA185) ocorre o Help A185PRE - Este item não podera ser baixado, pois não foi gerado Pre-Requisição

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Este Help ocorre quando ainda não foi feita a Pré-Requisição ao Armazém (via MATA106). Desta forma, dentro da rotina da Baixa da Pré-Requisição (MATA185), o registro fica com a legenda amarela.

![](https://totvssuporte.zendesk.com/attachments/token/cRVegn8saaFGZHU5BPO5SIQMC/?name=inline-1110566005.png)

Caso precise efetuar a Baixa, basta voltar à rotina MATA106 - Pré-Requisição ao Armazém, selecionar o Item (que estará com legenda verde) e efetuar a geração da Pré-Requisição.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403556340119/mceclip0.png)

Com isso, ao voltar na rotina MATA185 - Baixa de Pré-Requisição - E perceberá que o registro ficará com legenda verde, o que permitirá concluir com a Baixa da Pré-Requisição ao Armazém:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403558163479/mceclip1.png)

**Caso o objetivo seja apenas cancelar/estornar a Requisição**.

Caso o objetivo seja apenas cancelar/estornar a Requisição, basta voltar à rotina MATA105 - Solicitação ao Armazém, selecione a linha do Produto (que estará com legenda verde, que é pendente também), e faça a exclusão.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403558187799/mceclip2.png)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
