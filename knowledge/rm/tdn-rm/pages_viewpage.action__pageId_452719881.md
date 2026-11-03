---
content_hash: 6c2cc54b6600fc18aaf6aededdd8de363ea30ef2e897d965ce94c8f3d3893df8
fetched_at: '2026-06-29T00:10:10.574660+00:00'
page_id: '452719881'
product: rm
source: tdn-rm
title: Pasta Pareceres - Requisição de Desligamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719881
version: 2
---

**Pasta Pareceres - Requisição de Desligamento**

Os pareceres tem o objetivo de registrar as alterações realizadas na requisição de Desligamento. Cada parecer estará sempre vinculado a uma única requisição, porém, uma requisição poderá ter diversos pareceres. Para acessar o parecer de um requisição de Desligamento o usuário deverá acessar a requisição desejada, Anexos | Parecer de Desligamento.

**Pasta Identificação do Parecer de Desligamento**

Na pasta Identificação os seguinte dados devem ser informados:

**Emitido em -** Este campo exibirá a data e hora da emissão do parecer e não poderá ser alterado.

**Status -** Exibirá o status que a requisição assumiu conforme definição do fluxo de aprovações, porém, se a requisição não tiver sido incluída no fluxo, ou seja, quando o controle estiver sendo feito manualmente, este campo poderá ser alterado. Esta alteração será possível apenas no Totvs Gestão de Pessoas.

**Parecer emitido -** Deve conter o texto do parecer emitido pelo usuário.

**Responsável -** Somente podem ser selecionados chefes das seções da coligada na qual o usuário está logado. Para informações relacionadas aos chefes das seções verifique o cadastro de chefes e supervisores.

Caso o parecer seja incluído pelo "RM Portal" este campo exibirá o nome do usuário logado não podendo ser modificado.

**Filial/Função e E-mail -** Após preenchimento do campo "Responsável" os dados relacionados a estes campos serão preenchidos automaticamente. O campo "Filial/Função" deve exibir o nome da filial seguido do nome da função de lotação do funcionário selecionado no campo "Responsável". Em caso de alteração do nome do responsável, o conteúdo desde campo deverá ser automaticamente atualizado. A informação do campo "E-mail" deverá ser automaticamente atualizada com o e-mail que constar no cadastro do responsável indicado.

Para confirmar esta informação acesse Acompanhamento | Pessoas | Pasta Identificação.  
   
**Pasta Dados da Requisição****Desligamento**

Na pasta Dados da Requisição podem ser visualizados os seguintes dados:

**Previsão -** Por definição, se for selecionado um funcionário, será exibida a data prevista informada no último parecer incluído; caso tenha sido selecionado um ex-funcionário, será exibida a data da efetivação da demissão. Nas requisições que tenham um funcionário vinculado este campo poderá ser alterado no momento da inclusão do parecer, mas se a pessoa vinculada for um ex-funcionário este campo não poderá ser alterado.

**Dias de aviso -** Por definição, se for selecionado um funcionário, o valor para dias de aviso será 30 (trinta) podendo ser alterado para outro valor maior ou igual a 0(zero); caso tenha sido selecionado um ex-funcionário, será exibida o número de dias de aviso concedido.

**Funcionário -** Este campo não permite alteração e exibirá a mesma informação inserida no campo "Funcionário" no momento da criação da requisição.

**Tipo de demissão -** Se a pessoa selecionada for um ex-funcionário será exibido, neste campo, o tipo de demissão realizada. Caso seja um funcionário, deve-se definir qual será o tipo de demissão.

**Motivo da demissão -** Se a pessoa selecionada for um ex-funcionário será exibido, neste campo, o motivo da demissão realizada, caso seja um funcionário deve-se definir qual será este motivo para a demissão.

**Gerar substituição -** Esta opção deverá ser marcada se for necessário manter o número de vagas existentes para a respectiva lotação do funcionário que está sendo demitido. Ccaso esta opção não seja selecionada e se houver parametrização para o controle de lotação, o sistema reduzirá o número de vagas disponíveis ao concluir a requisição. Este procedimento será o mesmo caso a pessoa vinculada à requisição seja um ex-funcionário. A requisição de substituição será baseada nos dados da requisição de desligamento que lhe der origem (requisição pai) sendo criada quando esta requisição for aprovada, e terá, inicialmente, o status "Em andamento".

Para funcionário PCD a requisição de substituição, caso seja criada, no momento da sua utilização validará se a pessoa beneficiada também é PCD.
