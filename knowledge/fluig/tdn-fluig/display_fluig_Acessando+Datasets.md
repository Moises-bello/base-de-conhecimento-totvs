---
content_hash: 0dedb59ddb4a5d40fd2a40101f3f980600535a13727470e1b33b6aea2a3b7fba
fetched_at: '2026-06-28T21:35:19.244381+00:00'
page_id: '200901786'
product: fluig
source: tdn-fluig
title: Acessando Datasets
type: documentation
url: https://tdn.totvs.com/display/fluig/Acessando+Datasets
version: 46
---

# Índice

true.\*ndicenone

# Objetivo

---

Um Dataset pode ser acessado de várias formas: no desenvolvimento de widgets, formulários, *webservices*, eventos globais, eventos de formulários e eventos de processos.  
O objetivo desse guia é mostrar como acessar o Dataset nestes cenários.

# Pré-requisitos

---

Para que se tenha uma compreensão completa destas informações, alguns conhecimentos são considerados pré-requisitos, entre eles:

* Visão geral sobre o TOTVS Fluig Plataforma e sobre o .

Atenção!

A partir das atualizações **1.6.5 Liquid**, **1.7.0 Lake** e **1.7.1 Crystal Lake**, os *select* passados por *constraint* em dataset serão bloqueados pelo serviço. Orientamos a leitura da documentação [Datasets acessando banco de dados externo](https://tdn.totvs.com/x/OgFlDw) que contém um exemplo da correta utilização do procedimento.

# Acessando um *Dataset*

---

Vários locais da plataforma podem fazer uso dos dados retornados pelos *Datasets*. Serão apresentadas abaixo as variações na forma de acessá-los ou de manuseá-los.

## Widgets

No desenvolvimento de um widget, é possível acessar dados de *Datasets*, através da linguagem *Javascript*, utilizando a biblioteca *DatasetFactory*.

Consulte a documentação .

## eventos-de-formulariosVia pontos de customização

Quando um *Dataset* é acessado via um ponto de customização como eventos globais, eventos de processos, eventos de formulário ou mesmo em outros *Datasets*, isto é feito através de chamadas JavaScript que serão executadas no lado servidor.

O exemplo abaixo apresenta um exemplo simples de chamada a um *Dataset*:

jsEclipsetrue

No exemplo acima, o código JavaScript faz o acesso ao Dataset interno [*group*](http://tdn.totvs.com/display/fluig/Datasets+internos+fluig#Datasetsinternosfluig-group-Gruposdeusu%C3%A1rios), e retorna a quantidade de linhas disponíveis (rowsCount). O objeto **DatasetFactory** é a "porta de entrada" para o acesso a qualquer *Dataset*. Além de permitir a carga de um *Dataset*, ela também permite navegar entre todos os *Datasets* disponíveis no sistema.

O acesso a um *Dataset* é feito através do método **getDataset** do objeto **DatasetFactory**, onde seus parâmetros são:

* **Nome do Dataset:** Nome do Dataset a ser buscado;
* **Campos:** Array com os campos do Dataset que serão retornados. Caso seja informado null, retorna todos os campos do Dataset;
* **Constraints:** Array com os condições de busca do Dataset. Caso seja informado null, retorna todos os registros do Dataset.
* **Ordem:** Array com os campos para ordenação dos registros do Dataset. Caso seja informado null, retorna os registros com a ordenação padrão.

Já para a criação das constraints é utilizado o método **createConstraint**do objeto **DatasetFactory**, onde seus parâmetros são:

* **Campo:** Nome do campo que será filtrado;
* **Valor Inicial:** Valor inicial da faixa de valores do filtro
* **Valor Final:** Valor final da faixa de valores do filtro
* **Tipo:** Tipo da condição, podendo ser:  
  + **MUST:** indica que todos os registros do Dataset devem satisfazer a esta condição.
  + **SHOULD:** indica que os registros do Dataset podem ou não atender à condição. Esse tipo é mais comum quando se necessita que um mesmo campo tenha valores A ou B (onde cada um será uma condição de busca com tipo SHOULD).
  + **MUST\_NOT:** indica que nenhum dos registros pode satisfazer a condição.

Após a criação da constraint, é possível informar que esta será utilizada na consulta em formato de LIKE, ou seja, o valor retornado poderá conter qualquer letra ou sequência de letras no lugar do símbolo '%'. Isso é feito chamando o método setLikeSearch(true) para a constraint que se deseja este comportamento, conforme exemplificado na implementação abaixo, na constraint c5, onde pretende-se retornar todos os registros que NÃO possuam (pois é uma constraint MUST\_NOT) a palavra "teste" na descrição do documento.

Exemplo:

jsEclipsetrue

Após a criação da constraint, utiliza-se a função likeSearch utilizando a biblioteca vcXMLRPC.js, deve ser adicionado mais um parâmetro no método DatasetFactory.createConstraint, e não utilizar o método setLikeSearch(true). Exemplo:

jsEclipsetrue

Isto é válido apenas para a utilização da biblioteca vcXMLRPC.js.

Aqui é feito o uso de duas constrainsts do tipo SHOULD. A primeira indica que o campo 'documentType' pode retornar os registros do tipo 2. Já a segunda constraint indica que o campo documentDescription pode retornar todos os registros que possuam pelo menos a palavra teste em seu corpo, e isso se deve ao like estar habilitado por meio de "setLikeSearch(true)"

##### Exemplo:

jsEclipsetrue

##### Constraints Avançadas

Existe uma constraint em especial que é utilizada para limitar o número de registros na consulta SQL chamada de **sqlLimit**. Então é possível definir o número máximo de registros que uma consulta SQL pode retornar, porém o número de registros pode ser menor que o esperado, devido algumas validações que são feitas após o retorno dos dados. Por exemplo: O **sqlLimit** tem um valor 100 e é feita uma consulta em um serviço de dados de uma definição de formulário, esta consulta retornará os 100 registros, porém após isso são executadas validações para verificar se o formulário está ativo e se o usuário corrente tem permissão para visualizar os dados fazendo com que o retorno possa ser menor que 100. Para o **sqlLimit** é utilizada a seguinte sintaxe:

jsEclipsetrueImportante

O valor considerado no sqlLimit é sempre o **initialValue**, o que for informado no finalValue não será considerado.

Existe outra constraint especial utilizada somente para acesso a Datasets de definições de formulário, ela indica se ao buscar o serviço de dados devem ser retornados APENAS os dados dos formulários da definição de formulário principal. A constraint é a **onlyMainCards** e por padrão seu valor é false, ou seja, são retornados os dados dos formulários da definição de formulário principal e das definições de formulários filhas.

jstrueObservação

O valor considerado no onlyMainCards é sempre o initialValue, o que for informado no finalValue não será considerado.

Existe ainda, outra constraint especial que é a **checkSecurity** essa constraint é válida somente para Datasets de formulário e quando utilizada, fará o retorno dos registros do formulário validarem a segurança, ou seja, o Dataset retornará somente os registros de formulário que o usuário possua permissão para visualização.

javatrueAtenção

As constraints são aplicáveis apenas a Datasets internos. Em Datasets avançados, elas podem não ser suportadas, pois os dados provêm de fontes externas. No entanto, é possível implementar filtros na codificação do Dataset, desde que o desenvolvedor tenha preparado o código para aceitar e processar essas restrições, manipulando o objeto retornado para remover informações desnecessárias.

Dica

A constraint 'offset' define o ponto de início da pesquisa no dataset, permitindo a implementação de paginação.

A constraint *offset* permite definir quantos registros iniciais devem ser ignorados no resultado da consulta, retornando os próximos registros.

Exemplo: Ao usar a constraint *offset* com o valor *10*, os primeiros 10 registros encontrados na consulta serão ignorados, e os próximos registros serão retornados conforme o limite definido.

##### Exemplificação de uso de Constraints

Considere os valores da tabela abaixo sendo utilizadas como um serviço de dados a partir de uma definição de formulário para exemplificação dos exemplos:

| Código | Nome | Cidade |
| --- | --- | --- |
| 1 | Javier Spiva | São Paulo |
| 2 | Cody Ballow | Rio de Janeiro |
| 3 | Javier Naramore | São Paulo |
| 4 | Max Nevius | Rio de Janeiro |
| 5 | Noemi Roiger | São Paulo |
| 6 | Lonnie Cadwallader | Rio de Janeiro |
| 7 | Lorrie Spece | Brasília |

Verifique os exemplos de retorno de dados abaixo:

false0.5falseconstraintsamplesfadetrue1Exemplo 1

Para retornar somente as linhas que os códigos estejam entre 1 á 4 usar a seguinte constraint:

jsEclipsetrue

Retorno:

| Código | Nome | Cidade |
| --- | --- | --- |
| 1 | Javier Spiva | São Paulo |
| 2 | Cody Ballow | Rio de Janeiro |
| 3 | Javier Naramore | São Paulo |
| 4 | Max Nevius | Rio de Janeiro |

2Exemplo 2

Para retornar somente as linhas que os nomes sejam "Noemi Roiger", "Javier Naramore" e "Lonnie Cadwallader" ou que a cidade seja Brasília, usar as seguintes constraints:

jsEclipsetrue

Retorno:

| Código | Nome | Cidade |
| --- | --- | --- |
| 3 | Javier Naramore | São Paulo |
| 5 | Noemi Roiger | São Paulo |
| 6 | Lonnie Cadwallader | Rio de Janeiro |
| 7 | Lorrie Spece | Brasília |

3Exemplo 3

Para retornar todas as linhas exceto onde a cidade seja Brasília, usar a seguinte constraint:

jsEclipsetrue

Retorno:

| Código | Nome | Cidade |
| --- | --- | --- |
| 1 | Javier Spiva | São Paulo |
| 2 | Cody Ballow | Rio de Janeiro |
| 3 | Javier Naramore | São Paulo |
| 4 | Max Nevius | Rio de Janeiro |
| 5 | Noemi Roiger | São Paulo |
| 6 | Lonnie Cadwallader | Rio de Janeiro |

## Nova funcionalidade de pesquisa de informação de datasets

---

No exemplo abaixo, o código JavaScript faz o acesso ao Dataset interno **“documents”**, e retorna a quantidade de linhas disponíveis . O objeto datasets é a **"porta de entrada"** para o acesso a qualquer Dataset. Além de permitir a carga de um Dataset, ela também permite navegar entre todos os Datasets disponíveis no sistema.

O acesso a um Dataset é feito através do método **get** do objeto **dataset**, passando o parâmetro

* **Nome do Dataset:** Nome do Dataset a ser buscado;

No método **search** é informado os parâmetros que irão compor os filtros, ordenação e limite da busca.

**Campo:** Nome do campo que será filtrado.

+ **Value**: Valor a ser filtrado,
+ **Not**: Séria para a mesma lógica de **MUST\_NOT**, onde não deve satisfazer condição ou valor passado.

* **Like:** Realizar pesquisa para encontrar correspondência com o valor informado.

* **Between:** Esse parâmetro é para realizar a pesquisa entre um valor inicial e final.

* **SHOULD:** Indica que os registros do Dataset podem ou não atender à condição. Esse tipo é mais comum quando se necessita que um mesmo campo tenha valores A ou B (onde cada um será uma condição de busca com tipo **SHOULD**).

**Limit:** Total de registros que irá ser retornado.

**Offset:** Define quantas linhas devem ser puladas antes que os resultados comecem a ser retornados.

**Order:** Especifica a coluna pela qual deseja ordenar os resultados.

Exemplo da utilização do **search** com os **filtros, limit e offset**.

O parâmetro **SHOULD,** deve ser utilizado da seguinte forma.

**Observação**: Por enquanto é permitido utilizar apenas uma vez o **SHOULD**, não vai ser permitido utilizar para dois tipos diferentes.

**Retorno dos registros.**

O retorno dos registros é feito no formato JSON.

Exemplo:

Para recuperar os dados e adicionar nas colunas do dataset, é possível recuperar os dados de duas formas

* **[index][“campo”]**, passando a String do campo
* **[index].campo**, ou pelo objeto.

**Observação:** Para campos que é necessário acessar outros dados, como o id e a versão do documento, vai ser possível recuperar passando a String dentro de uma chave, **“[index]["documentPK.documentId"]”.**

Nos exemplos a seguir, será mostrado das duas formas.

No exemplo a seguir é feito uma busca dos documentos com o filtro do tipo **SHOULD,** onde e para retornar os documentos do tipo 1 e 2 **(Pasta e documento).**

No exemplo a seguir, será realizada a pesquisa de documentos para retornar os registros que contenham a palavra **“API”,** utilizando o like e como o limite de cinco registros.

jsEclipse

## Formulários

Em formulários, é possível que um ou mais campos possam exibir ou consultar dados de Datasets utilizando Javascript ou tags.

### Via JavaScript em formulário

---

É possível acessar os Datasets via código JavaScript no HTML de uma definição de formulário utilizando a biblioteca **vcXMLRPC.js**para utilização do *DatasetFactory*. Para isto, basta incluir a linha abaixo antes da tag body do HTML:

jsEclipsetrue]]>Importante

Este modelo de acesso faz com que o Dataset seja transportado do servidor para o cliente, ou seja, o navegador do usuário. Por isso, é importante observar a quantidade de informações que será manuseada, caso contrário pode-se ter problemas de consumo excessivo de banda ou performance.

**Exemplo:**

jsEclipsetrue";
//Monta o cabeçalho
tabela += "|";
for (var i = 0; i < dataset.columns.length; i++) {
tabela += " " + dataset.columns[i] + " |";
}
tabela += "
| --- |
";
//Monta os registros
for (var x = 0; x < dataset.values.length; x++) {
tabela += "|";
var row = dataset.values[x];
for (var y = 0; y < dataset.columns.length; y++) {
tabela += " " + row[dataset.columns[y]] + " |";
}
tabela += "
";
}
tabela += "";
return tabela;
}]]>

No exemplo acima, percebe-se que a forma de se invocar um Dataset é semelhante ao método via pontos de customização, através do DatasetFactory. A função showDataset apresenta um exemplo de código que permite apresentar os dados do Dataset.

Assim como no método via pontos de customização, quando é preciso filtrar um Dataset é preciso criar as constraints que serão utilizadas na busca. Os argumentos utilizados no método getDataset também são os mesmos que apresentados anteriormente:

jsEclipsetrue

### Via Tags no Formulário

É possível especificar um Dataset em um campo select (combo-box). Quando isto é feito, as opções do combo são automaticamente criadas de acordo com os dados do Dataset. Para isso, é necessário adicionar três propriedades adicionais à tag:

| Propriedade | Descrição |
| --- | --- |
| dataset | Determina o Dataset utilizado |
| datasetkey | Determina qual coluna do Dataset será utilizada como valor do campo |
| datasetvalue | Determina qual coluna do Dataset será utilizada como rótulo das opções do combo |

No exemplo abaixo, o campo "estado" foi configurado para que as opções do combo sejam criadas a partir do Dataset "estadosBR". Como valor do campo será utilizado o campo "Sigla", embora para o usuário será apresentado o campo "Estado".

|  |  |
| --- | --- |
| 1 | `<select name=``"estado"` `dataset=``"estadosBR"` `datasetkey=``"Sigla"` `datasetvalue=``"Estado"``></select>` |

Exemplo

Permitir que o usuário selecione treinamentos utilizando o

## Webservices

A plataforma disponibiliza um  que permitem integrar aplicações de terceiros à plataforma. Dentre os serviços disponibilizados, o serviço ECMDatasetService permite fazer o acesso a um Dataset. Para verificar a lista de serviços disponíveis, acesse a URL http://<servidor>:<porta>/webdesk/services.

A forma de uso de um Web Service varia de acordo com a tecnologia utilizada pela aplicação cliente. Consulte a documentação da tecnologia escolhida pra obter detalhes sobre como acessar Web Services.

## Via DataTable

Para consumir um Dataset dentro de um DataTable, também utilizamos a função DatasetFactory. É necessário incluir a biblioteca **vcXMLRPC.js**no final dos arquivos edit.ftl e view.ftl do *widget* para que seja possível utilizar a função.

jstrue]]>

Após configurado o arquivo **vcXMLRPC.js**, edite o arquivo .js do widget chamando o Dataset que desejar consumir. Abaixo segue um exemplo de uma chamada para o consumo do Dataset *colleague*:

jstrue 0) {
var records = datasetReturned.values;
for ( var index in records) {
var record = records[index];
that.mydata.push({
id: record.userTenantId,
name: record.colleagueName,
email: record.mail
});
}
}
that.myTable = FLUIGC.datatable('#idtable' + "\_" + that.instanceId, {
dataRequest: that.mydata,
renderContent: ['id', 'name', 'email'],
header: [{
'title': 'Code',
'dataorder': 'name',
'size': 'col-md-4'
}, {
'title': 'Name',
'standard': true,
'size': 'col-md-4'
}, {
'title': 'EMAIL',
'size': 'col-md-4',
'dataorder': 'ASC'
}],
search: {
enabled: false,
},
scroll: {
target: ".target",
enabled: true
},
actions: {
enabled: false,
},
navButtons: {
enabled: false,
},
draggable: {
enabled: false
},
}, function(err, data) {
if (err) {
FLUIGC.toast({
message: err,
type: 'danger'
});
}
});
that.myTable.on('fluig.datatable.loadcomplete', function() {
if (!that.tableData) {
that.tableData = that.myTable.getData();
}
});
},]]>

Para um exemplo completo do uso de *widget* com DataTable acesse [*Widget* com DataTable](https://git.fluig.com/projects/SAMPLES/repos/style-guide/browse/style-guide-wcm/widget/exemplo3), lembrando de trocar a function *loadTable* do *widget* pela função *loadTable* do exemplo acima.

Para um exemplo completo do uso de modal com Datable acesse [Modal com DataTable e Dataset](https://git.fluig.com/projects/SAMPLES/repos/projetos/browse/form-modal-datatable), lembrando sobre a limitação do datatable, no qual não é possível efetuar paginação pois não possui os recursos de offset e limit.

## Acessar dataset via API

### Via serviço REST

---

Disponibilizamos uma nova forma para acessar os datasets através de API utilizando serviços tipo REST. Para isso apresentamos logo abaixo um exemplo de como realizar essa pesquisa, siga os passos abaixo:

A API que fará a pesquisa é a API Dataset ([servidor\_fluig]/dataset/swagger-ui/#/Dataset\_handle/searchDatasetValues)

**datasetId**: Nome do dataset onde será realizado a pesquisa, este é o único parâmetro requerido.

**field**: Campos do dataset que serão retornados, caso não seja passado os valores todos os campos serão retornados.

**offset**: Quantos registros serão “pulados” antes de retornar os valores, esse campo é usado junto com o **limit** para realizar a paginação. Caso o dataset chamado for um dataset avançado, esse parâmetro pode ser acessado como uma *constraint* de nome **offset**.

**limit**: Quantidade máxima de registros que serão retornados na pesquisa. Caso o dataset chamado for um dataset avançado, esse parâmetro pode ser acessado como uma *constraint* de nome **sqlLimit**.

Importante

É importante definir o **limit** para evitar uma pesquisa com muitos registros, o que pode resultar em um retorno lento.

**orderby**: Nome do campo onde será feita a ordenação, pode ser adicionado **\_ASC** ou **\_DESC** para pesquisar em ordem ascendente e descendente respectivamente.

**constraintsField**: Nome do campo onde será passado o valor para pesquisa. Pode ser passado múltiplos campos mas para cada um deles será preciso passar um valor.

**constraintsInitialValue**: Valor que será usado para realizar o filtro de acordo com o campo passado no parâmetro **constraintsField**. Caso tenha passado mais de um campo para pesquisa será preciso passar os valores na mesma ordem para o filtro ser criado corretamente.

**constraintsFinalValue**: Caso o filtro desejado for uma faixa de valores o parâmetro **constraintsInitialValue** será o valor inicial e **constraintsFinalValue** será o valor final. Caso tenha passado mais de um campo para pesquisa será preciso passar os valores na mesma ordem para o filtro ser criado corretamente. Caso for passado o mesmo valor que o parâmetro **constraintsInitialValue** será feito a pesquisa somente por esse valor ignorando a faixa de valores.

**constraintsType**: Tipo de filtro que será aplicado no campo, os valores permitidos são:

* **MUST**: Se utiliza quando os valores retornados precisam ser iguais ao valor passado na **constraintsInitialValue** e **constraintsFinalValue** para o campo **constraintsField.**
* **MUST\_NOT**: Se utiliza quando os valores retornados precisam ser diferentes ao valor passado na **constraintsInitialValue** e **constraintsFinalValue** para o campo **constraintsField.**
* **SHOULD** : Assim como o **MUST** os valores retornados precisam ser iguais ao valor passado na **constraintsInitialValue** e **constraintsFinalValue** para o campo **constraintsField.** Esse tipo deve ser utilizado quando for feito mais de um filtro para o mesmo campo. **Por exemplo**: Pesquisar todos os colaboradores com o nome Antônio ou João.

Caso tenha passado mais de um campo para pesquisa será preciso passar os valores na mesma ordem para que o filtro seja criado corretamente.

**constraintsLikeSearch**: Valor booleano que determina se os valores nos campos **constraintsInitialValue** e **constraintsFinalValue** podem ser somente parte do valor total caso o booleano seja verdadeiro ou se os  
valores precisam ser exatos caso o booleano seja falso. Quando o valor for verdadeiro poderá ser usado o símbolo **%** para determinar que será aceito qualquer valor a partir desse ponto, **por exemplo**: se na **constraintsInitialValue** for passado o valor “Anderson%” e o **constraintsLikeSearch** estiver como *true* será retornado todos os valores que comecem com “Anderson”. Caso tenha passado mais de um campo para a pesquisa será preciso passar os valores na mesma ordem para que o filtro seja criado corretamente.
