---
content_hash: 5f5fabc1f7009c968f7463f962c280665a7141f506075b6efe72903b0953669e
fetched_at: '2026-06-29T00:11:11.766380+00:00'
page_id: '649301390'
product: rm
source: tdn-rm
title: Diagnóstico de saldo de estoque por lote
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=649301390
version: 32
---

Toda movimentação que afeta saldo em estoque obrigatoriamente tem que afetar o saldo por lote e vice versa, sendo incorreto que a informações dos mesmos sejam distintas.

Em vista disto o processo de **Diagnóstico de saldo de estoque por lote** tem por finalidade listar produtos com discrepâncias entre o saldo físico x saldo nos lotes, e seus respectivos movimentos, para direcionar os usuários em possíveis ajustes de estoque físico ou nos lotes.

Para o processo de **Diagnóstico de saldo de estoque por lote** a execução da **Regeração de saldos e custos** não é um pré-requisito mas é interessante para que os resultados sejam mais realistas otimizando assim uma ação futura de ajustes de saldos evitando retrabalho. Então, caso o usuário opte por este procedimento prévio, deve-se acessar o menu **Estoque | Processos | Regerar Saldos e Custos** e marcar a opção **(x) Forçar Regeração Total**se a data de fechamento de estoque for “Geral”, ou a opção **(x) Regerar todos os Saldos**se a data de fechamento de estoque for por saldo.

Após a regeração de saldos e custos, caso tenha-se optado por este procedimento, pode-se iniciar a rotina de **Diagnóstico de saldo de estoque por lote** onde o usuário deverá acessar o menu **Estoque | Processos | Diagnóstico de saldo estoque por lote** onde será apresentado um *wizard* que conduzirá o usuário através das várias etapas para gerar e visualizar os resultados da rotina.

**1ª Etapa**

Será apresentada uma tela ao usuário com um breve resumo do que o processo se propõe e sua saída final (LOG).

**2ª Etapa - Saldo a verificar e identificação do produto**

Informar o tipo de saldo a ser utilizado para o diagnóstico e a forma se seleção dos produtos.

 

**3ª Etapa - Parametrização dos tipos de movimentos**

Os tipos de movimentos deverão estar corretamente parametrizados. Caso o "Efeito sobre o Saldo Atual" seja "Aumenta" ou "Diminui", a opção "Consiste Lote" deverá estar marcada para os tipos de movimentos utilizados no controle de produto com lote.

Serão apresentados os tipos de movimentos que tiveram movimentações com produtos com controle de lote onde este tipos de movimentos estão configurados para afetar o saldo mas não estão parametrizados para consistir lotes. Esta listagem ajudará ao usuário identificar se há algum tipo de movimento parametrizado e utilizado de forma errônea gerando diferenças de estoque.

Pode ocorrer de o lote informado no item do movimento não ser um dos lotes do produto informado para o item do movimento, isto é, o item tem um produto e o lote no item ser de outro produto. Este processo tem a habilidade de identificar esta inconsistência e informar ao usuário através de uma mensagem *pop-up* então, ao avançar para a próxima etapa através do botão "Avançar", serão listados, caso existam, os movimentos/itens de movimento que estejam com tal situação.

**4ª Etapa - Produtos com diferença no saldo de lotes**

Serão listados os produtos, divididos por filial e local de estoque, que para o saldo selecionado possuem diferença em relação ao somatório do valor para os lotes e necessitam de ajustes quanto ao saldo selecionado. A busca pelos produtos com tais diferenças consiste de recuperar:

- Produtos controlados por lote cujo saldo difere do saldo por lote por local de estoque (existe diferença entre TPRDLOC e TLOTEPRDLOC);

- Produtos controlados por lote onde existe registro na tabela de controle de lotes por produto por local de estoque mas não existe registros equivalente de produto por local de estoque (existe registro na TLOTEPRDLOC e não existe em TPRDLOC);

- Produtos controlados por lote em que existe o registro de produto por local de estoque mas que não existam registros de controle de lote por produto por local de estoque (existe registro na TPRDLOC e não existe em TLOTEPRDLOC).

Selecione a do produto a verificar e clique em "Avançar" para visualizar sua movimentação.

**5ª Etapa - Análise da movimentação**

Após a apresentação dos produtos com diferenças de saldo é possível visualizar sua movimentação bastando selecionar um dos registros de produto (marcando a caixa de seleção - o *checkbox* - do produto desejado) e clicar em "Avançar".

Serão listados os movimentos que afetaram estoque e não afetaram o saldo por lote e vice versa que podem estar influenciando na diferença entre saldos e podem ser ajustados.

A quantidade dos itens de lote difere da quantidade informada no item de produto. Sugerimos que primeiro sejam acertados os movimentos de entrada e depois os movimentos de saída. Caso não existam movimentos a corrigir, ou todos já tenham sido corrigidos e a diferença no saldo persiste, movimentos novos podem ser gerados para o acerto. Cada movimento deve ser avaliado criteriosamente pois pode haver mais de uma maneira de acertá-lo. A sugestão é que movimentos que tenham quantidade de itens de lote maior que a quantidade do item devem ser corrigidos separadamente.

 

Caso deseje visualizar a movimentação de outro produto, a partir da interface de movimentação, basta clicar no botão "Voltar" e repetir o procedimento acima sempre que desejar ou for necessário.

**Observação**: A quantidade do item e somatório dos lotes está na unidade de controle do produto.

Atenção:

As etapas de recuperação de produtos e movimentos, conforme estiver a parametrização dos tipos de movimentos, produtos e a quantidade de movimentos/itens de movimentos, pode ser demorado visto que serão considerados todos itens em todas filiais x locais de estoque x lotes movimentados para validação. 

Atenção:

Serão apresentados os movimentos com data maior ou igual que a data de fechamento.

**LOG**

Ao final do processo será apresentado um log com a rastreabilidade dos produtos consultados, registros encontrados, entre outros.
