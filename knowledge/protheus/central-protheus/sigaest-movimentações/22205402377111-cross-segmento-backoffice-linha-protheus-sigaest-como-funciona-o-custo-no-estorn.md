---
article_id: 22205402377111
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 9649cf6444a50c311c0b361002509056c37fc6088917f21d2f509210a56a93c4
fetched_at: '2026-06-28T22:38:54.414077+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como funciona o custo
  no estorno de movimentações vinculadas a uma OP?
type: support-article
updated_at: '2025-03-12T12:26:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22205402377111-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-funciona-o-custo-no-estorno-de-movimenta%C3%A7%C3%B5es-vinculadas-a-uma-OP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22205369390871) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como funciona o estorno de movimentações vinculadas a uma OP? Como estornar uma requisição contra OP? como estornar uma movimentação contra OP em outro periodo? Como fica o custo no estorno de uma movimentação contra OP?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
  
**Solução**Nesse boletim, o time de Estoque Custos ira abordar situações questionadas em relação a processos de estorno de uma OP, tais movimentações aqui exemplificadas com a utilização do seguinte cenario:

* Movimentos produtivos (MATA250), com requisições automaticas contra OP e movimentações contra OP manuais(MATA241), com o objetivo de entendimento para realização de estornos.

**Como realizar o estorno de uma OP?**

Primeiro, é preciso entender qual o tipo de estorno? Existe duas situações mapeadas:

**-Primeira situação:** **Movimento automatico contra OP, exemplo RE1:**

Quando se trata de estornar movimentos automaticos, estamos falando de "**Estornar o Apontamento da OP**", ***não há outra forma***, e assim sendo o estorno deve ser realizado através da rotina que foram realizados os apontamentos(exemplo MATA250), selecionando o movimento de **produção > Outras Ações >Estornar.**

**Caso tente efetuar o estorno do movimento produtivo, onde foi gerado o consumo das movimentações de forma automatica, o sistema irá lhe apresentar a seguinte mensagem devida: HELP A240NAO**

[Manufatura - Linha Protheus - SIGAPCP - Mensagem A250NAO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026661672-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-A250NAO)

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/22205402370327)**

**-Segunda situação:** **Movimento manual contra OP, exemplo RE0:**

Nesse caso, como se trata de um movimento AVULSO, que é realizado diretamente via rotina de movimentação interna(MATA241) com o relacionamento da digitação da OP, aqui nessa situação pode-se realizar sim a movimentação de estorno do movimento manual gerado seja RE0/DE0 porque é um movimento AVULSO contra OP, em outras ações > estornar da rotina de movimentação utilizada.

**Mais sobre os tipos de movimentações:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Quais os significados dos códigos dos tipos de Movimentos Internos RE/DE?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007057091-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Quais-os-significados-dos-c%C3%B3digos-dos-tipos-de-Movimentos-Internos-RE-DE)

**Eu posso realizar o estorno de um apontamento ou movimentação contra OP, que se encontra em um periodo fechado?**

Nesse caso não é possivel, movimentações que ocorreram em um periodo ja encerrado, não podem sofrer mais alterações, caso tente sera apresentado o seguinte: HELP FECHTO

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - HELP FECHTO Não pode ser digitado movimento com data anterior a última data de fechamento (virada de saldos)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16419065822999-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-HELP-FECHTO-N%C3%A3o-pode-ser-digitado-movimento-com-data-anterior-a-%C3%BAltima-data-de-fechamento-virada-de-saldos)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22205369392535)

**Mas você precisa realizar o estorno, oque fazer?**

Somente mediante a reabertura do periodo onde a OP se encontra, e então sera possivel efetuar o estorno.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA038 - Processo de Reabertura de Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6420543172247-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA038-Processo-de-Reabertura-de-Estoque)

**SOBRE O CUSTO NO ESTORNO DE UMA OP.**

**Se eu realizado um movimento AVULSO contra OP (RE0) no periodo A que tem custo 10 do movimento, e depois em outro periodo a OP ainda não foi encerrada, e eu presico estornar o RE0, então realizo um (novo) movimento de devolução (DE0) contra OP, como assumir o CUSTO que foi feito antigamente no movimento RE0 para que seja utilizado no novo movimento de devolução DE0?**

A amarrção entre os dois tipos de movimento contra OP são distintas, ou seja avulsas, nenhuma tem relação com a outra, e caso efetue a devolução em um periodo o qual o custo médio ja sofreu alterações, o movimento DE0 vai assumir o custo médio em questão, não há vinculo com a origem, e nem mesmo se trata de uma devolução da requisição efetuada.

A unica forma de efetuar a devolução do RE0, somente se o periodo estiver em ABERTO, e então utilizar a opção da rotina de movimentação contra OP realizada na opções de Outras ações > Estornar.

***Saiba mais:***

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
