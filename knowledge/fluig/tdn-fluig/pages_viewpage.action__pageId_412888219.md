---
content_hash: 420412110eba5756c811a016c9325e8777f5a7c3006bdece16a72667a04af3c2
fetched_at: '2026-06-28T21:35:26.775555+00:00'
page_id: '412888219'
product: fluig
source: tdn-fluig
title: Construção do Dataset Avançado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=412888219
version: 10
---

# Índice

true.\*ndicenone

# Objetivo

---

Este guia tem o objetivo de apresentar uma introdução para a codificação dos datasets avançados no TOTVS Fluig Plataforma.

# Pré-requisitos

---

Para que se tenha uma compreensão completa destas informações, alguns conhecimentos são considerados pré-requisitos, entre eles:

* Conhecimento sobre o
* Visão geral sobre codificação JavaScript

Atenção!

A partir das atualizações **1.6.5 Liquid**, **1.7.0 Lake** e **1.7.1 Crystal Lake**, os *select* passados por *constraint* em dataset serão bloqueados pelo serviço. Orientamos a leitura da documentação [Datasets acessando banco de dados externo](https://tdn.totvs.com/x/OgFlDw) que contém um exemplo da correta utilização do procedimento.

# Criação de dataset avançado

---

Um dataset avançado é capaz de acessar outros datasets, realizar chamadas a serviços externos ou pode conter valores fixos, codificados conforme a necessidade. Ele é construído a partir de um código-fonte em JavaScript, que pode ser editado na interface disponível no Painel de Controle ou pelo Fluig Studio.

Atenção

Para que um usuário que não é administrador da empresa possa construir datasets via Fluig Studio é necessário que ele possua a permissão "Configurar Datasets". Esta permissão pode ser concedida pelo administrador através do item  disponível no Painel de Controle da plataforma.

A partir da **atualização 1.6.5**, os administradores do sistema conseguem editar o código fonte do Dataset pela plataforma, acessando a opção "Editar em modo avançado", na tela de Datasets no Painel de Controle.

A seguir serão apresentados alguns exemplos para codificação do dataset avançado.

## Dataset com valores fixos no código

---

jsEclipsetrue

Para criar um novo Dataset, é utilizado o método **DatasetBuilder.newDataset()**. Utilizando o objeto retornado por este método é possível adicionar as colunas desejadas (método **addColumn**) bem como adicionar linhas (método **addRow**).

Note que a função javascript **createDataset**, que cria o Dataset para consulta, recebe como parâmetros os campos, as constraints e a ordenação. Cabe ao desenvolvedor utilizar estes valores na lógica de implementação do Dataset avançado. Caso seja desconsiderado algum desdes campos, os filtros não serão aplicados. Os parâmetros "**fields**" e "**sortFields**" são **arrays** de String, que possuem, respectivamente, os nomes dos campos que serão retornados e os nomes dos campos utilizados para ordenação. Já o parâmetro "**constraints**" é um array de objetos do tipo **Constraint**, onde cada objeto deste array possui as seguintes propriedades:

| Propriedade | Descrição |
| --- | --- |
| fieldName | Nome do campo |
| initialValue | Valor inicial para filtro neste campo |
| finalValue | Valor final para filtro neste campo |
| contraintType | Tipo do filtro deste campo, podendo ter os valores abaixo:  **MUST**: O valor informado **precisa** estar nos resultados  **SHOULD**: O valor informado **pode** estar ou não nos resultados  **MUST\_NOT**: O valor informado **não pode** estar nos resultados |

Atenção!

As constraints podem ser utilizadas apenas para Datasets internos. Datasets avançados não aceitam constraints, pelo fato de os dados serem externos, não sendo possível aplicar o filtro em sua origem. Para Datasets avançados o tratamento de filtros deve ser feito na codificação do Dataset, manipulando o objeto retornado e retirando as informações desnecessárias.

Para acessar estas propriedades e analisar os valores de cada item, pode-se utilizar um laço de repetição, conforme implementação abaixo:

jstrue

## Dataset avançado com utilização de constraint

---

jsEclipsetrue

Consulta utilizando a *constraint*:

jsEclipsetrue

Caso necessário, também é possível obter o código da empresa e do usuário autenticado através do método getValue(), conforme exemplo abaixo:

jstrue

## Dataset avançado com permissionamento

---

Abaixo temos um exemplo de como implementar o permissionamento em datasets avançados.

javaEclipsetrueAtenção!

Alguns datasets retornam dados sensíveis, por isso, é altamente recomendado que apenas os usuários responsáveis tenham acesso a esses dados.

## Utilizando zoom composto em Dataset avançado

---

Através do uso de Datasets avançados é possível realizar uma série de buscas compostas.

falseExemplo 11Implementação da Busca Composta

No exemplo abaixo, utilizando o método createDataset foi desenvolvida uma busca constituída por mais de um campo da tabela, que recebe o valor informado no campo zoom e em seguida retorna o dataset avançado com os registros encontrados em ambos ou em um único campo da busca. Caso não seja informado nenhum valor, serão retornados todos os registros encontrados no banco.

jsEclipsetrue 0)
{
c1 = DatasetFactory.createConstraint("mail", "%" + constraints[0].initialValue + "%" , "%" + constraints[0].finalValue + "%", ConstraintType.SHOULD);
c2 = DatasetFactory.createConstraint("mail", "%%", "%%", ConstraintType.SHOULD);
c1.setLikeSearch(true);
c2.setLikeSearch(true);
filter = new Array (c1, c2);
}
var dataset = DatasetFactory.getDataset("colleague", null, filter, sortFields);
return dataset;
}]]>2Implementação do Zoom

Em seguida é apresentado a implementação do zoom para tratar os retornos gerados pela busca composta.

jsEclipse1Exemplo 1true
$(function(ready){
var myTable = FLUIGC.datatable('#target', {
dataRequest: {
url: '/api/public/ecm/dataset/search',
options: {
contentType:'application/json',
dataType: 'json',
method: 'POST',
data: JSON.stringify({
'datasetId' : 'DatasetTeste'
}),
crossDomain: true,
cache: false
},
root: '',
limit:10,
},
renderContent: ['colleagueName'],
multiSelect: false,
search: {
enabled: true,
},
scroll: {
target: '#target',
enabled: true
}
});
});
]]>jsEclipseExemplo 1true]]>

## Dataset avançado de definição de formulário "pai-filho"

---

Para acessar informações de um "pai-filho" de uma definição de formulário pode ser utilizado o WebService "ECMDatasetService", um Dataset avançado (Exemplo 1), ou ainda um evento de processo ou definição de formulário (Exemplo 2).

falseExemplosAvançado 1Exemplo 1jsEclipseExemplo 1trueAvançado 2Exemplo 2jsEclipseExemplo 2true

Utilizando um dos modelos acima, é possível recuperar os valores "filhos" dos formulários ativos, ou seja, da última versão criada. Existem alguns parâmetros obrigatórios que devem ser passados através de *constraints*, onde o valor inicial e final devem ser iguais. A forma de recuperar esses valores é opcional. Segue abaixo a nomenclatura **obrigatória** de cada parâmetro:

| Parâmetro | Descrição |
| --- | --- |
| tablename | Atributo utilizado para nomear cada **tabela** filha do HTML. Exemplo: jsEclipsetrue |

]]>
