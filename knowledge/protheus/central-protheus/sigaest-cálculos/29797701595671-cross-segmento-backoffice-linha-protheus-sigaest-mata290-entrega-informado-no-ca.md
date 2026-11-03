---
article_id: 29797701595671
category: SIGAEST - CÁLCULOS
content_hash: 980552e2988473c300dfa16e55772f4bc9597f3662baf673f931cc16fc770d18
fetched_at: '2026-06-28T22:39:04.133909+00:00'
product: protheus
section_id: 1500001550082
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA290 - Entrega
  (informado no Cadastro de Produtos)
type: support-article
updated_at: '2025-03-12T12:20:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29797701595671-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA290-Entrega-informado-no-Cadastro-de-Produtos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29797694554775) Tempo aproximado para leitura: **00:02:21****min** **Dúvida**O que é o conceito de Entrega (campo do Cadastro de Produtos) e qual sua influência no Sistema?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
  
**Solução**

É a quantidade de horas, dias, semanas, meses, etc, que indica para o sistema, qual o tempo de entrega ou fabricação de um produto, a partir do recebimento de seu pedido, ou da abertura de sua OP.

Para produtos cujo prazo de entrega dependem de outras grandezas ou características, não sendo um período fixo, pode ser utilizada fórmula que deve ser cadastrada no Configurador.

Neste caso, informa-se o campo **Fórmula Prazo**, pois o campo **Prazo de Entrega** utiliza-se para prazos fixos.

O sistema utiliza preferencialmente o campo **Fórmula Prazo** e na sua falta o **Prazo de Entrega** tradicional.

Utiliza-se a variável **QUANTIDADE** na fórmula do prazo de entrega para se obter a quantidade real que se pretende avaliar o prazo de entrega. Por exemplo:

Supondo um produto cujo prazo de entrega seja de 10 lotes econômicos por dia, a fórmula para expressar o prazo de entrega deste produto no campo **Fórmula Prazo** é:

Round((QUANTIDADE/(10\*B1\_LOTE)),0)

Esta fórmula retorna o prazo em **DIAS**, necessários para a produção de uma determinada quantidade planejada pelo MRP ou o tempo total a ser gasto para a produção de uma determinada **Ordem de Produção** e demais rotinas que tratam o prazo de entrega.

**Saiba mais:**

*[Lote Econômico - MATA290 - Tudo sobre a rotina](https://tdn.totvs.com/pages/viewpage.action?pageId=347442943)*

*[Clique aqui e veja mais artigos sobre Cálculos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550082-SIGAEST-C%C3%81LCULOS)*
