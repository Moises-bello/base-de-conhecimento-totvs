---
article_id: 26356729288599
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 04d997b884c49f9430e0f808d30e5a95423b01fe127c4bc01397b6a29c1ffdde
fetched_at: '2026-06-28T22:38:56.842757+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA185 - Coluna "Quantidade
  a Requisitar" zerada
type: support-article
updated_at: '2026-03-04T19:02:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26356729288599-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA185-Coluna-Quantidade-a-Requisitar-zerada
---

Ao baixar uma pré-requisição no TOTVS Protheus, a coluna "Quantidade a Requisitar" fica zerada quando o campo "Quantidade disponível para entrega" do produto está zerado no cabeçalho. Essa coluna reflete diretamente a quantidade disponível para entrega do produto, podendo ser zero ou parcial conforme o saldo disponível.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26356729266711) Tempo aproximado para leitura: **00:01:47 min**  
  
**Dúvida**  
O que fazer quando, ao clicar para Baixar uma pré-requisição, a Coluna "Quantidade a Requisitar" fica zerada?  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Normalmente este comportamento se dá quando o produto do qual está sendo baixado o saldo, está, em seu cabeçalho com o campo "Quantidade disponivel para entrega" zerado. A coluna Quantidade a Requisitar vai validar diretamente o que tem disponivel para entrega do produto. Exemplos.

Produto **sem** quantidade disponivel para entrega, então a coluna "Qtde a Requisitar" vem zerada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26356729270935)

Produto **com** quantidade disponível para entrega, então a coluna "Qtde a Requisitar" vem com o que tem disponível (mesmo que parcial):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26356729276311)

Produto **com** quantidade disponível para entrega, então a coluna "Qtde a Requisitar" vem com o que tem disponível (neste caso o total do saldo da pré-requisição é o que está disponível para entrega:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26356757337879)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
