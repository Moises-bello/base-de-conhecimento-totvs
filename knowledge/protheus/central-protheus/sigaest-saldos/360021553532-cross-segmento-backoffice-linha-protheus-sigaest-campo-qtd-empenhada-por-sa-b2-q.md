---
article_id: 360021553532
category: SIGAEST - SALDOS
content_hash: a198a370b6fdeb5b52d43720a67f92dbe5e9072c90985afe3f66c9f1befc4b6a
fetched_at: '2026-06-28T22:39:14.801705+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Campo "Qtd. Empenhada
  por SA" (B2_QEMPSA) no F4 do Produto dentro da rotina MATA010
type: support-article
updated_at: '2023-06-22T14:40:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021553532-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Campo-Qtd-Empenhada-por-SA-B2-QEMPSA-no-F4-do-Produto-dentro-da-rotina-MATA010
---

**Dúvida**Qual a origem do conteúdo no campo Qtd. Empenhada por SA (B2\_QEMPSA)? É possível voltar ele ao Estoque Disponível?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
  
**Solução** O campo Qtd. Empenhada por SA (B2\_QEMPSA) é preenchido com base nas solicitações ao armazém geradas e não baixadas. Deste modo é necessário realizar a analise para um item em específico consultando a tabela de solicitações (SCP) referente aos campo CP\_QUANT e o CP\_QUJE, onde um representa a quantidade da solicitação e o outro representa a quantidade já entregue.

Outra forma é comparar diretamente com o relatório MATR105 (Posição das Solicitações ao Armazém), nele apresentará o saldo conforme o campo "Qtd. Empenhada por SA"

![SOL_ARM.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15501293342615)

Outra opção para localizar em qual SA o saldo esta empenhado, pode usar a rotina de consulta MATC050 com uma data grande e consultar o produto.

Na opção Outras Ações selecionar Ex. todas, conforme print abaixo.

Observe que do lado direito, é apresentado o numero da SA que esta empenhando a quantidade:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9681392097047)

Como fazer o saldo do campo B2\_QEMPSA voltar ao Estoque Disponível?

Para esta finalidade, as alternativas são:

* Na rotina da Baixa de Pré-Requisição, ir em "outras ações" -> "Excluir". **Nesse momento o B2\_QEMPSA já é removido e o saldo volta para o "Disponivel".** E depois, se desejar excluir a Solicitação ao Armazém que criaram para o produto, basta acessar à rotina MATA105 e o registro estará com legenda verde. tendo a opção de ir em "Outras ações" -> "Excluir".

* Outra opção é, na própria rotina da Baixa de Pré-Requisição, posicionar no item, clicar em "Outras Ações" -> Encerrar. Desta forma a Solicitação ao Armazém é encerrada e não há mais a necessidade de estornar nada, nem mesmo desistir e tentar baixar novamente neste mesmo numero de SA.

**Saiba mais:**

[Significado de cada saldo no F4 do Produto (dentro da rotina MATA010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-MP-SIGAEST-Consulta-F4-cadastro-de-produtos)

[Clique aqui e veja mais artigos sobre Saldos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033462-SIGAEST-SALDOS)
