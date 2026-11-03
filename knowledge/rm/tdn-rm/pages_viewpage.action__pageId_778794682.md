---
content_hash: 3b3b11c9ed415e17bcad5577e0a0e5b0d144ef1804242dc908607a7540b618a0
fetched_at: '2026-06-29T00:11:37.902469+00:00'
page_id: '778794682'
product: rm
source: tdn-rm
title: Júpiter - Geração de Pedido Web
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=778794682
version: 7
---

**Pedido**

 A Geração de Pedido Web surgiu como um facilitador parar criação de requisições (Compra, Cotação, Estoque e Produção).

Premissas:

1. Ter o cronograma planejado;
2. Parametrizar o TCOP (TOTVS Construção Obras e Projetos);
3. Parametrizar o BackOffice.

[Requisitos necessários para gerar integração com Suprimento/Faturamento](https://tdn.totvs.com/pages/viewpage.action?pageId=421385546) 

[Parametrizando o Totvs Obras e Projetos](https://tdn.totvs.com/pages/viewpage.action?pageId=421385523) 

[Parametrizando BackOffice RM Suprimento/Faturamento](https://tdn.totvs.com/pages/viewpage.action?pageId=421385209) 

De acordo com o Cronograma Planejado, uma tarefa pode gerar vários movimentos de compra ou de cotação, esses movimentos são gerados a partir do número de períodos previstos ou agrupados em uma única requisição.

O Movimento de Compras é gerado com base no planejamento, a partir dele é calculada a necessidade de consumo de recursos em cada tarefa, essa necessidade é transformada em pedidos de compra através da requisição, integrando assim o planejamento com a compra e gestão.

O Movimento de Cotação deve ser utilizado somente para efetuar o processo de cotação através do Gestão de Estoque Compras e Faturamento. Durante a execução do projeto, deve-se solicitar as compras gerando os movimentos de solicitação de compra.

O Movimento de Pedido de Histórico é gerado a qualquer momento podendo ser registrado no Totvs Obras e Projetos um pedido de histórico de compras. Deve ser utilizado para implantação de projeto que já se encontra em andamento ou ainda utilizá-lo para pedidos feitos via Protheus na obra.

**Requisição**

A requisição pode ser modificada (alterada ou agrupada). Depois ela pode gerar no Gestão de Estoque Compras e Faturamento um movimento de requisição (de tipo de acordo com a parametrização feita no Totvs Obras e Projetos) para cada período selecionado com os insumos componentes de cada tarefa planejada.

A Requisição de Pedido obedece o Tipo de Compra cadastrado no Insumo.

As requisições são geradas por tarefa ou por obra e por período, ou seja, é gerada uma requisição (compra ou cotação) ou pedido histórico para cada período que tenha cronograma previsto, e itens de movimento para cada insumo dentro de cada tarefa ou obra, de acordo com os filtros determinados por você. Se for feito agrupamento, pode ser gerado um movimento para um insumo de uma tarefa, acumulando vários períodos em um único.

Quando o tipo de geração, no Pedido, estiver definido por obra é enviada a obra no item de movimento e gerado um item por obra.  Quando o tipo de geração, no Pedido, estiver definido por tarefa é enviado nulo na tarefa do item e são enviadas as tarefas no rateio de centro de custo do item.

Na Geração de Pedido: não há necessidade, pois, este tipo de pedido não utiliza tarefa de valor cotado. No Pedido Extra: Somente exibe os produtos com a mesma natureza orçamentária definida na tarefa. Quando não for definida Natureza Orçamentária na tarefa não haverá o filtro e qualquer produto poderá ser selecionado.

O Núcleus sempre considera a Natureza Orçamentária do produto para os itens de movimento (pedidos e contratos).

**Processo da Requisição**

Para ter acesso ao processo, acessar Menu /Planejamento/ Geração de pedidos;  
Na tela de Pedido clicar em novo.

**Selecionar faixa de períodos** para a realização da Requisição – período inicial e período final;

**Selecionar as Tarefas,** com opção de:

**Intervalo de tarefas:** o usuário deverá informar uma tarefa inicial e uma tarefa final;

**Tarefa por tarefa:** o usuário deverá selecionar as tarefas desejadas uma a uma.

**Selecionar o Tipo de Requisição;** Compra, Cotação ou Pedido Histórico

**Requisição de Compra:** Pedido para o planejado.

**Requisição de Cotação:** Pedido de orçamento para o planejado.

**Pedido Histórico:** Pedido para controle de saldo líquido.

**Selecionar os Grupos de Custos** desejados.

**Selecionar os Insumos** (Caso existam insumos sem produtos para os filtros escolhidos nos passos anteriores, os mesmos serão listados para o usuário. Não será permitido selecionar esses insumos para a requisição. Caso queira selecionar os insumos sem produtos para a requisição, será necessário efetuar a associação de produto para esses) e executar o processo. Em seguida será criada a requisição com status de "Aguardando Envio". 

A requisição poderá ser editada ou excluída. Ao ser editada será exibida e tela Pedido com as seguintes informações:

**Código do pedido:** Código do Pedido,

**Data da requisição:** A data que a requisição foi criada.

**Utiliza preço orçado:** Este campo indica se o pedido usará o preço orçado no envio para suprimentos. (Geração do movimento)  
  
**Calculo do preço orçado:**O preço será recuperado do insumo respeitando o parâmetro de vigência de preço. (Será utilizado o campo Valor com Leis). Caso não seja possível recuperar o preço do Insumo o preço será recuperado do produto.

Preço Calculado

Para utilização do preço orçado é importante que o preço do insumo esteja calculado.

Informações detalhadas a respeito do pedido e seus processos, clique em uma das opções disponíveis abaixo:

* [Visão Geral do Pedido](https://tdn.totvs.com/pages/viewpage.action?pageId=778796316)

**Tipo de Requisição:** Este campo informa o tipo da requisição (compra/armazém/histórico/cotação).

**Status Geração:** Informa status da geração da requisição podendo ser aguardando envio para Suprimento e Faturamento ou Enviada para Suprimento e Faturamento.

**Tipo de Movimento:** Tipo de movimento que foi criado.

**Local de Estoque:** Local de estoque que está vinculado a obra.

**Tipo de Geração:** Tipo de geração de requisição se é por obra ou tarefa.

Será exibida também uma grid com as informações detalhadas da requisição contendo:

**Nome da tarefa:** Nome da tarefa.

**Quantidade Pedida:** Quantidade pedida na requisição.

**Código da tarefa:** Código da tarefa vinculada na requisição.

**Preço Unitário orçado:** Preço unitário orçado.

**Descrição da tarefa:** Descrição da tarefa vinculada a requisição.

**Código do insumo:** Código do insumo vinculado a tarefa que está na requisição.

**Nome fantasia:** Nome fantasia do insumo.

**Unidade:** unidade de medida utilizada.

**Quantidade da necessidade:** Quantidade da necessidade.

**Data de entrega:** Data da entrega da requisição.

**Data de pedido:** Data do pedido.

**Data de necessidade:** Data da necessidade.

**Contrato:** Contrato vinculado a requisição.

**Observação:** Campo para colocar alguma observação sobre o pedido.

**Prazo de ressuprimento:** Prazo de ressuprimento.

**Unidade do Produto:** unidade de medida do produto.

**Quantidade do estorno:** Quantidade da requisição que foi solicitada, mas não foi utilizada.
