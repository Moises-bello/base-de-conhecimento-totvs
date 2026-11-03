---
article_id: 33455628877335
category: SIGAACD - Automação e Coleta de Dados
content_hash: d21a722d3d5b9c70622e44de10506758185413ad91c2dd4339dd5d6d60a5bd82
fetched_at: '2026-06-28T22:39:11.137046+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD -  Deletando registros
  na SC9 sem ordem de separação vinculada.
type: support-article
updated_at: '2025-07-14T16:26:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33455628877335-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Deletando-registros-na-SC9-sem-ordem-de-separa%C3%A7%C3%A3o-vinculada
---

O sistema TOTVS Backoffice (Linha Protheus) pode deletar registros da SC9 quando um produto é gerado parcialmente sem vínculo com a Ordem de Separação. Se a opção "Confere lote" estiver definida como "Não", a Nota Fiscal de Saída por Ordem de Separação estorna os empenhos e liberações, gerando uma nova liberação para a quantidade separada. Caso a opção esteja como "Sim", os registros permanecem inalterados. Para utilizar a quantidade remanescente, é necessário realizar uma nova liberação manualmente.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33455658644247) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
O sistema está deletando os registros da SC9, de um produto gerado parcialmente sem vinculo com Ordem de Separação, como proceder?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**

Caso a separação esteja configurada para **não realizar a verificação do lote no momento da leitura** — ou seja, com a opção **“Confere lote”** na parametrização da rotina de **Ordem de Separação** definida como **“Não”** —, ao gerar a **Nota Fiscal de Saída por Ordem de Separação** no coletor de dados para um produto que possui controle de lote, os empenhos e liberações do pedido de venda serão estornados. Nesse cenário, será gerada uma nova liberação contendo apenas a quantidade efetivamente separada.

Caso haja a necessidade de utilizar a quantidade remanescente do pedido, deverá ser realizada uma nova liberação manualmente para essa quantidade.

Por outro lado, se a opção **“Confere lote”** estiver configurada como **“Sim”**, os registros de liberação do pedido de venda permanecerão inalterados, independentemente da quantidade separada.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
