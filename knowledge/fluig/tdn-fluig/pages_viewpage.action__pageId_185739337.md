---
content_hash: 6381c4a15df9dcceda00f66f695b00f74cdc50f410a0fe8e9d1a8fd659a4f046
fetched_at: '2026-06-28T21:35:18.824262+00:00'
page_id: '185739337'
product: fluig
source: tdn-fluig
title: Integrando widget com formulários/datasets do Fluig Plataforma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185739337
version: 15
---

# Índice

4true.\*ndicenone

# Objetivo

O objetivo deste guia é demonstrar a integração de *widgets* com formulários/datasets do TOTVS Fluig Plataforma.

Exemplo completo

Deseja um exemplo completo de consumo de dados de formulários/datasets no Fluig Plataforma? Faça o *download* dos códigos-fonte do Kit Intranet no [repositório Git](https://git.fluig.com/projects/SAMPLES/repos/kit-intranet/browse).

# Armazenamento

Frequentemente é necessário armazenar dados além daqueles que a plataforma Fluig já guarda nativamente. Pensando nisso, o TOTVS Fluig Plataforma disponibiliza a [personalização de formulários](http://tdn.totvs.com/pages/viewpage.action?pageId=75270483#DesenvolvimentodeFormul%C3%A1rios-Customiza%C3%A7%C3%A3odeFormul%C3%A1rios), uma forma de guardar seus dados de forma simples e ágil:

Esse é um recurso valioso da plataforma Fluig e preparado para realizar soluções completas e complexas. Entretanto, pode ser usado de forma bem fácil para atender as demandas mais simples. Utilizando *[datasets](http://tdn.totvs.com/pages/viewpage.action?pageId=75270483#DesenvolvimentodeFormulários-Dataset)*, o processo de armazenamentos de dados torna-se rápido.

Imagine que você deseja guardar o nome, o dia e o mês do aniversário dos colaboradores de sua empresa. Considere os passos abaixo:

* Siga os [passos para criar um formulário](http://tdn.totvs.com/pages/viewpage.action?pageId=75270483#samples-1);

* No [arquivo HTML do formulário](http://tdn.totvs.com/pages/viewpage.action?pageId=75270483#samples-4), inclua três campos. Para mais detalhes sobre a forma de apresentação, veja a sessão [controles visuais](http://tdn.totvs.com/pages/viewpage.action?pageId=75270483#DesenvolvimentodeFormulários-Controlesvisuais):

xml
...
...
...
...
]]>

Feito isso, basta seguir os [passos de exportação de um artefato Fluig para um servidor Fluig](http://tdn.totvs.com/pages/viewpage.action?pageId=128681226#samples-1) e seu formulário já estará pronto para armazenamento. Uma dica é escolher a pasta padrão "Formulários Fluig" para armazenar os formulários no momento da exportação para a plataforma.

# Utilização

Com seu formulário pronto e preenchido com os dados desejados, basta buscar a identificação do seu formulário no início do arquivo JavaScript.

Dúvidas para criar o *widget*? Siga o .

De posse da identidade do registro, é simples buscar os dados dele. Em seu [arquivo .js](http://tdn.totvs.com/pages/viewpage.action?pageId=185735923#Meucódigonãoestáfuncionando.Eagora?-MeuarquivoJavascriptnãocarregou) execute uma chamada ao [DatasetFactory](http://tdn.totvs.com/display/fluig/Desenvolvimento+de+Datasets#DesenvolvimentodeDatasets-DatasetFactory). A seguir é apresentado um exemplo simples:

js

Onde:

| Elemento | Descrição |
| --- | --- |
| datasetReturned | Objeto contendo os registros do formulário retornados. |
| ``` "kit_news" ``` | Código escolhido para o formulário/dataset (definido [aqui](http://tdn.totvs.com/pages/viewpage.action?pageId=75270483#samples-2)). |

Datasets Internos

A mesma técnica que é utilizada para consumir datasets de formulários, permite consultar também [datasets internos do Fluig](https://tdn.totvs.com/x/SgKeCQ). Basta substituir o código do dataset e seus respectivos campos.

O consumo desses registros pode ser efetuado da seguinte forma:

js 0){
var records = datasetReturned.values;
for (var index in records) {
var record = records[index];
// ... restante do código omitido
}
}]]>

Onde:

| Elemento | Descrição |
| --- | --- |
| ``` datasetReturned ``` | Objeto contendo os registros do formulário retornados. |
| ``` records ``` | Um *array* de objetos *(Object[ ])* contendo os registros. |
| ``` index ``` | Índice do registro corrente conforme o laço (*for*) avança pelo *array.* |
| ``` record ``` | É o registro, ou seja, o objeto contendo as propriedades de um registro de formulário.  Considerando o exemplo do formulário de notícias, podemos assumir para esse caso que as propriedades desse objeto serão as seguintes:   * *record.newTitle* * *record.newDescription* * *record.newsSourceURL* |

Veja o exemplo em nosso repositório [aqui](https://git.fluig.com/projects/SAMPLES/repos/style-guide/browse).
