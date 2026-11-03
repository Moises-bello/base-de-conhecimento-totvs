---
content_hash: 8c9c30ff3c16ddefddbee3a60079c03b29ea7833ce20d6161a9c0ca4d5435340
fetched_at: '2026-06-29T00:09:25.297435+00:00'
page_id: '423938106'
product: rm
source: tdn-rm
title: Estornar Item Não Recebido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938106
version: 13
---

Estornar Item Não RecebidoPasso a Passo

O processo de Estornar Item não Recebido tem como objetivo eliminar os itens não recebidos do movimento e retornar para o tipo de movimento origem (**O estorno só é funcional para movimentos que foram de fato baixado/faturado, se a parametrização do movimento não baixar para o movimento de destino então o estorno não é possível, verifique os parâmetros de baixa em ).**

Poderá ser realizado em movimentações inseridas no Totvs Estoques, Compras e Faturamento como também movimentações oriundas do Totvs Gestão de Obras e Projeto.

**Processo realizado em movimentos oriundos do TCOP**

**Passo a Passo**

O sistema TOTVS Gestão de Construção e Projetos permite ao usuário faturar parcialmente Solicitações de Compra ou de Cotação ou até mesmo informar a desistência de algum insumo no pedido.   
Através do processo de Estorno de Itens Não recebidos é possível informar ao projeto quais foram os itens faturados e apropriados no cronograma de um projeto.

**Pré-condição**

Ter Faturado parcialmente , ou não ter faturado a quantidade do item de uma Solicitação de Compras ou de Cotação vinda de uma Requisição de Materiais do sistema de Construção e Projetos:

* Passo 1 - Selecione o movimento e acesse: Processo/ Estorno de Itens não recebidos;
* Passo 2 - Selecione os itens que deseja estornar a solicitação e clique no botão "Executar";
* Passo 3 - Acesse: TOTVS Projetos/ Gestão de Construção e Projetos;
* Passo 4 - Selecione o projeto qual o movimento pertence e acesse: Planejamento | Geração de Pedidos;
* Passo 5 - Selecione a requisição de materiais que originou o movimento e clique no ícone "Editar";
* Passo 6 - Selecione o item da requisição e clique no ícone "Editar Item do Movimento". O sistema exibira no campo "Quantidade de Estorno" a diferença do valor informado no movimento ao editá-lo e a quantidade solicitada na requisição de materiais.

Restrições do Processo

Esse processo não poderá ser executado para itens de movimento que tenham sido gerados parcialmente através da cotação, e que o saldo restante tenha sido estornado.

Processo

O processo do movimento "Estornar item não recebido" pode ser executado em movimentos de compra parcialmente recebidos ou pendentes e reabrirá a cotação/solicitação de compras relacionada ao movimento.

O processo poderá ser usado para movimentos gerados pelo TCOP.  
  
Observações:

* É preciso dar permissão ao perfil do usuário para ter acesso a este processo na visão de movimentos
* Para o correto funcionamento do processo é preciso que o módulo de cotação esteja parametrizado para que a cotação permita gerar ordem de compra parcialmente cotada.
* Para executar o processo é preciso que o movimento esteja com o status parcialmente recebido ou pendente. Exemplo: O processo de cotação é definido da seguinte forma:
  + Solicitação de compra
  + Cotação
  + Ordem de Compra
  + Nota Fiscal.

Quando uma cotação gera uma ordem de compra e esta é faturada, a cotação fica com o status de concluída e a ordem com status recebido. Porém se ao faturar a ordem é feito o faturamento parcial, a ordem fica com o status parcialmente recebido e neste caso, o processo "estornar item não recebido" pode ser executado para esse movimento e esta ordem mudará o status para recebido. A solicitação que gerou a cotação ficará com o status pendente, assim como a própria cotação.  
O movimento na qual o processo foi executado fica com o status recebido e a solicitação fica como pendente e somente com os itens e quantidades que ainda não foram faturados.

**IMPORTANTE**:

* Ao executar o processo de "Estornar item não recebido" o movimento mudará o status para "Recebido", o que impede o cancelamento do movimento futuramente. Recomendamos que a execução do processo para movimentos com status "Pendente" seja analisada com cautela, principalmente quando houver integrações com outros módulos (Financeiro, Fiscal e etc) . Uma vez que executado, o movimento não poderá ser cancelado.
