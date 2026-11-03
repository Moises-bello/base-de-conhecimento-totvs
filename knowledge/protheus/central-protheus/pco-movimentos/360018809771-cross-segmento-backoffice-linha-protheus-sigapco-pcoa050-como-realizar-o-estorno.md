---
article_id: 360018809771
category: PCO - Movimentos
content_hash: e2a104a02b208a59884e75419455f19efa97aac2f9413b4d8979d103c42ebddd
fetched_at: '2026-06-28T22:37:09.519733+00:00'
product: protheus
section_id: 1500001550962
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAPCO - PCOA050 Como realizar
  o estorno de lançamentos no SIGAPCO
type: support-article
updated_at: '2023-11-21T13:34:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018809771-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-PCOA050-Como-realizar-o-estorno-de-lan%C3%A7amentos-no-SIGAPCO
---

|  |
| --- |
| Primeiramente iremos configurar o ponto de lançamento de inclusão de título a pagar, para visualizarmos melhor a função do campo ESTORNA:        Ao acessar o ponto de lançamento vemos que no conjunto de seus itens, não possui um item especifico de cancelamento ou estorno, onde configuramos o campo ESTORNA = SIM:        Ao configurar o ponto de lançamento de inclusão de título a pagar, iremos incluir um novo título:        Ao incluir o título o mesmo irá atualizar a tabela AKD de movimentos no SIGAPCO, conforme abaixo:        Após incluir o título e constar que o mesmo atualizou a tabela de movimentos no SIGAPCO, iremos excluir o título a pagar:        Título a pagar excluído:        Ao excluir o título a pagar, veja que no movimento gerado no SIGAPCO o lançamento ficou como estornado. A função do campo ESTORNA no cadastro do ponto de lançamento possui essa funcionalidade, de alterar o status (AKD\_STATUS) do lançamento efetuado:        Agora que compreendemos o funcionamento do campo ESTORNA no cadastro do ponto de lançamento, iremos visualizar o ponto de lançamento referente a compensação a pagar (000017). Veja que o lançamento possui **itens de cancelamento** e estorno, onde o campo ESTORNA? não irá fazer efeito, pois como já dito anteriormente o lançamento possui **itens de cancelamento**:        Em seguida incluímos dois título para realizar uma compensação a pagar:        Abaixo a efetivação da compensação entre títulos:            Compensação finalizada:        Ao realizar a compensação a tabela AKD de lançamentos foi atualizada com a movimentação:        Em seguida iremos estornar a compensação:            Estorno finalizado:          Ao realizar o estorno são geradas duas linhas, ao contrário da inclusão a pagar.  O item 000017 – Compensação a pagar possui **itens de cancelamento**, onde o usuário deve configurar no item de inclusão creditando o valor do lançamento e no item de cancelamento debitando o valor, ficando assim com o saldo zerado.    Finalizando, os  pontos de lançamento que possuem itens de cancelamento o campo ESTORNA? não terá efeito, apenas terá efeito em pontos de lançamentos que não possuem **itens de cancelamento**. |
