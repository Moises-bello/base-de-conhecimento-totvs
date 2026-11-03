---
content_hash: ce630ef1bc4390703317deaf7e7b6bdb9f809a01eb029d1bf8cd34d066150243
fetched_at: '2026-06-29T00:09:26.763818+00:00'
page_id: '423938413'
product: rm
source: tdn-rm
title: Alocação de Patrimônios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938413
version: 6
---

Este processo é responsável por permitir realizar e consequentemente controlar onde os patrimônios estão alocação. A necessidade desse processo ocorre em situações que o patrimônio está sob controle de uma , , , centro de custo, local e\ou responsável especifico, mas não necessariamente estão alocados nestes. Não sendo necessário realizar uma transferência de controle, apenas uma alocação de patrimônio.

**Regras para realização da Alocação de Patrimônio**

* O patrimônio a ser alocado não poderá ser um título.
* Patrimônios totalmente baixados ou baixados em período anterior não poderão ser alocados.
* Patrimônios inativos não poderão se alocados.

**Para alocação Interna:**

* Caso o patrimônio esteja associado a um departamento a alocação só poderá ocorrer para outros departamentos da mesma filial.
* Só poderão ser informados responsáveis de destino que estejam ativos.
* Só poderão ser informados locais de destino que estejam ativos.
* A alocação não poderá ser realizada se a data passada pelo usuário for menor que a data da última alocação.
* Para ser alocado o patrimônio deverá estar em uma filial ou um departamento ou uma localização ou um centro de custo ou com um responsável diferente do atual.
* Se o parâmetro "Vincular localização com responsável" estiver marcado, o campo "Responsável de destino" estiver vazio, o campo "Local de destino" estiver preenchido e o local de destino vinculado a um responsável, será gravado o responsável associado ao local de destino. Se o responsável de destino for informado e o local de destino não, deverá ser verificado se o local atual está vinculado a um responsável que não poderá ser diferente do responsável de destino.
* Se o parâmetro "Vincular localização com centro de custo" estiver marcado, o campo "Local de destino" estiver preenchido e o local de destino vinculado a um centro de custo, será gravado o centro de custo associado ao local de destino.

**Para alocação Externa:**

Será validado apenas o cliente/fornecedor. Ele não poderá ser igual ao cliente/fornecedor atual

**Retorno de controle atual:**

Serão realizadas as mesmas validações da alocação interna com exceção das situações abaixo:

* Se o parâmetro "Vincular localização com responsável" estiver marcado, o campo "Responsável de destino" estiver vazio, o campo "Local de destino" estiver preenchido e o local de destino vinculado a um responsável, será gravado o responsável associado ao local de destino. Se o responsável de destino for informado e o local de destino não, deverá ser verificado se o local atual está vinculado a um responsável que não poderá ser diferente do responsável de destino.
* Se o parâmetro "Vincular localização com centro de custo" estiver marcado, o campo "Local de destino" estiver preenchido e o local de destino vinculado a um centro de custo, será gravado o centro de custo associado ao local de destino.

**Realizando uma Alocação de Patrimônio**

Existem duas maneiras de executar o processo de alocação de patrimônio, a partir do menu Operações Patrimoniais/Alocar Patrimônios e pela tela de visão de patrimônios cadastrados na opção processos.

Ao utilizar a transferência a partir do menu operações patrimoniais deve-se informar o patrimônio a ser transferido.

Lembre-se que na opção acima podem der informados mais de um patrimônio.

Após selecionar o(s) patrimônio(s) deve-se informar se a alocação será interna, externa ou se irá apenas retornar para o controle atual.

Na alocação interna, o sistema permite selecionar o cliente\fornecedor destino, na alocação interna é possível selecionar a filial, departamento, centro de custo, local e responsável destino.

Selecionando a opção retorna para controle atual, o sistema irá identificar onde o patrimônio está sob controle, e retorna-los.

O próximo passo é informar a data da transferência (obrigatório), o número do documento e um texto de observação.

Ao marcar a opção "Transferir patrimônios agregados" todos os patrimônios que possuem outros patrimônios agregados a eles serão transferidos. Nesta situação, para o(s) patrimônio(s) agregado(s) serão aplicadas as mesmas regras de exceção como patrimônio inativo ou totalmente baixado.

Para utilizar o processo de alocação a partir da visão de patrimônios cadastrados deve selecionar o(s) patrimônio(s) desejado(s) e escolher a opção "Alocação de Patrimônios" em "Processos". A diferença entre esta forma de chamar o processo com a que acessa o menu Operações Patrimoniais é que nesta opção não aparecerá a tela onde se pode informar o(s) patrimônio(s), visto que os mesmos já foram selecionados na visão de patrimônios cadastrados.

**Alocações de Patrimônios já realizadas**

Após realizar a alocação de patrimônio com sucesso pode-se conferir seu resultado por destino a partir da tela de cadastro de patrimônio. Para isto é necessário editar o patrimônio transferido e acessar a aba de históricos de alocação.

Esta aba apresentará o histórico por Filial, Centro de custo, Departamento, Responsável, Localização e Fornecedor. Essas informações também poderão ser visualizadas através do menu Operações Patrimoniais\Consulta de Alocações.

Veja também

* Consulta Alocação de Patrimônio
