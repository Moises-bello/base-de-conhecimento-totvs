---
article_id: 7093136901527
category: SIGAEST - CUSTOS
content_hash: a2bf36681ce7d0d40ebbbbd40bb4a2f455ccc5bc6873cf4be6a13dba84e95830
fetched_at: '2026-06-28T22:39:00.600352+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Apropriação do custo
  em Apontamento de Perda
type: support-article
updated_at: '2025-08-18T19:19:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7093136901527-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Apropria%C3%A7%C3%A3o-do-custo-em-Apontamento-de-Perda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31671859661975) Tempo aproximado para leitura: **00:02:50 min**

**Dúvida**

Tenho perdas informadas na OP (Ordem de Produção) após o Apontamento de Produção (MATA250). Como considerar o custo de total incluindo as perdas ou considerar apenas o custo dos itens consumidos ignorando os itens perdidos na apropriação do Custo?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Para os cenários descritos é possível utilizar o parâmetro "MV\_PERDINF" que foi implementado para atender aos casos de perda nos apontamentos de produção. Seu objetivo é identificar qual o conceito deve ser aplicado ao processo de apontamento de produção, quando for informada a quantidade de perda.

**MV\_PERDINF = .T.**  
O sistema considera que a quantidade de perda, informada nos apontamentos de produção, é apenas “**informativa**”. Neste caso, a baixa de empenhos é realizada proporcionalmente à quantidade  
produzida, desconsiderando a quantidade perdida. Desta forma o custo será proporcional ao que foi produzido.

**MV\_PERDINF = .F.**  
O sistema considera que a quantidade de perda informada nos apontamentos de produção é considerada na composição do saldo da ordem de produção. Neste caso a baixa de empenhos é  
realizada proporcionalmente à quantidade produzida mais a quantidade de perda informada. Desta forma o custo será composto pelo total, pois neste caso a perda também é considerada no apontamento da OP.

**Exemplo:**

Custo Unitário do produto MP: R$ 1,00

![nota.PNG](https://tdn.totvs.com/download/attachments/504817579/nota.PNG?version=1&modificationDate=1564593612630&api=v2)

Estrutura do Produto:

![Estrutura.PNG](https://tdn.totvs.com/download/attachments/504817579/Estrutura.PNG?version=1&modificationDate=1564593612520&api=v2)

Ordem de Produção solicitando a quantidade de 3 PA's:

![OP.PNG](https://tdn.totvs.com/download/attachments/504817579/OP.PNG?version=1&modificationDate=1564593612773&api=v2)

**MV\_PERDINF = .T.**

![img1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7093256974231)

**MV\_PERDINF = .F.**

![img2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7093255461783)

Uma outra alternativa seria fazer a devolução das matérias-primas referente à produção perdida (vinculando a OP) e depois baixar manualmente as matérias-primas (sem vincular a OP).

**Outras informações importantes sobre apontamentos de Perdas:**

***- 1 -*** Sobre a perda de uma Sucata (Produto Destino da Perda) que não tem custo, é possível que não receba custo de alguma maneira padrão?

**Resp.:** Veja [***nesse link***](https://centraldeatendimento.totvs.com/hc/pt-br/articles/31633014918039-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-%C3%A9-poss%C3%ADvel-apontar-perdas-com-Custo-Zerado-para-produto-que-sera-descartado-Sucata) exemplo de Configuração.

***- 2 -*** Quando utilizar o parâmetro [***MV\_A685OPE habilitado***](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025831871-Manufatura-Linha-Protheus-SIGAPCP-Como-realizar-o-Apontamento-de-perda-em-Ordem-de-produ%C3%A7%C3%A3o-encerrada), apresenta o alerta que a OP esta encerrada e o Custo não sera apropriado caso continuar. Nesse cenário deve avaliar a viabilidade de Continuar mesmo assim ou então com a opção de Cancelar, para que em seguida possa estornar o Apontamento de Produção, efetuar o Apontamento de Perda e ai sim com a Perda computada como desejado, Apontar a Produção de forma que o Custo seja considerado inclusive com o apontamento da Perda.

**Obs.:** Esse caso, não se trata de erro e sim o comportamento esperado na rotina padrão. Pois, no padrão, para questões de **Custos em OPs que já foram totalmente apontadas e encerradas** as mesmas não podem ser alteradas.

Caso clicar em Continuar e deseja validar o custo da perda, é necessário realizar [acertos de Custos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057292614-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Acerto-de-Custo-dos-Produtos-em-Estoque) pontuais no produto.

![HELP perda.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/34271581455895)

***Saiba mais:***

[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000049222-SIGAEST-CUSTOS)

[SIGAEST - Como é possível apontar perdas com Custo Zerado para produto que sera descartado (Sucata)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/31633014918039-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-%C3%A9-poss%C3%ADvel-apontar-perdas-com-Custo-Zerado-para-produto-que-sera-descartado-Sucata)
