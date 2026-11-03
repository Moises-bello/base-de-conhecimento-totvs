---
content_hash: 52764a40199abb7db7e8bbddff5bc33cd24c250b86b290b1e0d560b1cf747e97
fetched_at: '2026-06-29T00:09:27.967406+00:00'
page_id: '423938593'
product: rm
source: tdn-rm
title: Lote Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938593
version: 25
---

Chamamos de ***Lote*** um agrupamento de lançamentos que pode ser originado do próprio TOTVS Gestão Contábil ou de outros aplicativos e tem por finalidade o controle de débitos, créditos e lançamentos com a mesma característica.

O TOTVS Gestão Contábil trabalha com dois tipos de lotes de lançamentos: um chamado *Lote Zero* e outro *Lote N*.

* ***Lote Zero*** é o lote oficial da contabilidade e de onde o sistema retira todas as informações necessárias para elaboração e emissão de relatórios, controle e consulta de saldos, apuração de resultados, rotinas legais, enfim, é do lote zero onde o sistema retira todas as informações necessárias para o controle da escrituração contábil.
* ***Lote N*** são lotes de lançamentos que tem por finalidade facilitar o controle sobre lançamentos que ainda não fazem parte dos dados oficiais da contabilidade.

Se a empresa trabalhar de forma integrada com outros aplicativos, os lançamentos contábeis gerados por estes aplicativos serão trazidos para o TOTVS Gestão Contábil através de lotes de lançamentos. Depois de conferidos e ajustados, estes lançamentos deverão ser *integrados* ao lote principal da contabilidade para passarem, assim, a fazer parte dos dados oficiais da contabilidade.

Na tela principal é possível visualizar o cadastro geral de Lotes. Pode-se também criar filtros para seleção dos Lotes através do Gerenciador de Filtros (localizado na Barra de Ferramentas). Além disto, através dos *Parâmetros do Sistema*, é possível definir entre outros, se os lotes sem lançamentos que tiveram origem em outros aplicativos serão visualizados ou não.

Cada um dos lotes visualizados na janela principal poderá ser aberto para que seus lançamentos sejam visualizados, excluídos ou alterados, bastando dar um "*duplo clique*" sobre a linha do lote. Feito isto, antes da apresentação dos lançamentos, será apresentada uma janela de Filtro para que sejam selecionados os lançamentos desejados. Se o lote tiver origem em outro aplicativo e se você não for usuário supervisor ou o perfil associado ao seu usuário não tiver as devidas permissões para incluir/editar/excluir lançamentos em lote ou então acessar lotes de outros módulos, ao abri-lo o sistema irá solicitar a indicação de um usuário/senha com estas características para permitir tal acesso.

Exclusão de Lote

Para excluir um lote, basta selecioná-lo e acionar o botão Excluir. Ao excluir um lote todos os seus lançamentos serão excluídos e, feito isto, não há como recuperá-los.

A partir da versão 11.81 e para quem acessa o sistema pela nova interface que dá acesso a todos os segmentos (RM.EXE) é possível através do menu "**Lançamentos do Lote**" visualizar somente os lançamentos de determinado lote, para isto, dentro do módulo de Lotes, acesse este menu e indique o número do lote desejado. É possível também acessar automaticamente a tela de edição de uma partida de determinado lançamento que se encontra em lote, para isto, dentro do módulo de Lotes, acesse o menu "**Acesso Rápido**", indique o lote e os dados para a pesquisa rápida desta partida.

---

### Informações necessárias para cadastrar Lotes

Informações sobre os campos da Capa do Lote

**Código:**O código do lote deverá ser sempre numérico e deverá ser único para cada lote. Os lotes com origem em outros aplicativos têm o Código definido na própria origem. Este código não poderá ser alterado posteriormente, portanto, certifique-se de que o número informado está de acordo com o código desejado. Se o Parâmetro do Sistema "Verifica duplicidade de lote na criação" estiver marcado, ao criar um novo lote, o sistema verifica primeiro se já existe ocorrência de algum lote que utilize este mesmo código junto aos lançamentos integrados e, caso já exista, será emitida uma mensagem advertindo-o sobre a existência deste lote, permitindo que se opte por continuar ou não a criação.

**Digitar Capa:**Esta opção permite fazer um controle maior sobre as datas dos lançamentos e o valor do lote. Esta não é uma opção de preenchimento obrigatório, mas caso seja marcada, torna-se obrigatório o preenchimento das datas inicial e final assim como informar o valor para o lote. Uma vez informados, só será permitida a inclusão de lançamentos cujas datas estejam dentro das datas informadas para a capa do lote e também dentro do período contábil e do período permitido para o usuário, assim como só será permitida a inclusão de lançamentos até o valor informado na capa do lote. Se esta opção estiver desmarcada os campos para informações das datas inicial/final e valor ficarão desabilitados e, na inclusão da capa do lote, estas datas receberão as datas do período contábil e serão reajustadas automaticamente conforme as datas dos lançamentos à medida que forem incluídos no lote. O valor ficará zerado, sendo recalculado a cada inclusão/edição de lançamentos feitos no lote.

Atenção ao parâmetro **"Não calcular/atualizar capa do lote automaticamente ao abrir a visão de lotes":** Foi incluído um novo parâmetro que valida o cálculo da capa dos lotes. Para mais informações

**Data Inicial / Data Final**

Campos habilitados somente se a opção Digitar Capa estiver marcada e representa o período válido para inclusão de lançamentos no lote.  
Não será permitida a alteração das datas da capa do lote, se existirem lançamentos no lote que ficarão fora do novo período informado.

**Valor**

Campo habilitado somente se a opção Digitar Capa estiver marcada e representa o valor total dos lançamentos no lote.   
Quando a opção Digitar Capa estiver marcada, na integração do lote será realizada uma consistência entre o valor total dos lançamentos e valor do lote informado neste campo.

**Maior lote cadastrado até o momento**

Neste espaço, como informação, será mostrado o número do maior lote já cadastrado até o momento, independente do seu aplicativo de origem. Para encontrar o maior número, o sistema irá procurar entre os códigos dos lotes já integrados ao lote principal e não integrados. Assim, se desejar incluir lotes com números sequenciais, é só consultar esta informação e atribuir um número ao lote que se está incluindo, maior que o número aqui informado.

**Campos Referentes ao Fluxo de Aprovação**

Campos abaixo terão visibilidade apenas pra Lotes Contábeis quando o Parâmetro "**Utilizar Fluxo de Aprovação**" estiver marcado e não podem ser editados manualmente (Mais detalhes em [Fluxo de aprovação de lançamentos](https://tdn.totvs.com/pages/viewpage.action?pageId=838210925)).

* **Status de Aprovação**

Identifica qual tipo de Status de Aprovação o lote esta. "**Em edição**" , "**Aguardando aprovação**" e "**Aprovado**".

* **Usuário Solicitante**

Identifica o Usuário Solicitante, apenas será preenchido quando for efetuado o processo de **Solicitação de Aprovação** para o lote.

Observação

Vale observar que este é o cadastro da *Capa de Lote*. Para a inclusão/edição dos lançamentos, deve-se selecionar o lote desejado e dar um "duplo clique" sobre ele.

* **[Fluxo de Aprovação](https://tdn.totvs.com/pages/viewpage.action?pageId=838210925)**Lotes com Status: "**Aguardando aprovação**" ou "**Aprovado**" não podem ter lançamentos incluídos, alterados ou excluídos.

* **Identificação do Lote:**Cada Lote de lançamentos será identificado por um código que deverá ser único para cada Lote. Deverá ser também definido um intervalo de datas permitidas para a inclusão dos lançamentos no Lote, assim como um valor total para os lançamentos do Lote. A este conjunto de dados e informações chamamos de *Capa de Lote*.

Cada Lote, então, possui uma Capa de Lote. Este é o cadastro que permite a sua inclusão e manutenção.

---

Anexos

* [Diferenças em lançamentos do lote](http://tdn.totvs.com.br/pages/viewpage.action?pageId=423938711)
Processos

* Agrupamento de Lançamentos Contábeis
* Desfazer Agrupamento de Lançamentos Contábeis
* Integração de Lotes
* Bloquear Lotes
* Desbloquear Lotes
* [Copiar Lotes entre Coligadas](https://tdn.totvs.com/display/LRM/Copiar+Lotes+entre+Coligadas)
