---
content_hash: 3b55c55488f5895e241800c4647cb3def3eac8b4cca148d8bd3736bff1c984a3
fetched_at: '2026-06-29T00:11:45.705948+00:00'
page_id: '821179190'
product: rm
source: tdn-rm
title: Equivalência (WebService)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=821179190
version: 6
---

# Visão Geral dos processos WebSevices de Equivalência

O objetivo deste DataServer é possibilitar a busca, inclusão, alteração e exclusão de equivalência através de WebService. Tudo o que for realizado, poderá ser visualizado no cadastro de equivalência no TOTVS Gestão Educacional.

Através do dataserver "**EduEquivalenciaData**" e por meio dos métodos **ReadRecord, **ReadView,** SaveRecord e DeleteRecord**, é possível realizar busca, inclusão, manutenção e exclusão das informações de equivalência no TOTVS Gestão Educacional.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/display/LRM/Webservices)**

Índice

2

## Método ReadRecord

Este método realiza a consulta de uma equivalência. Algumas informações são obrigatórias e devem ser informadas: **o código da coligada, o id. do grupo de disciplinas e id. do grupo de disciplinas equivalentes**.

O sistema irá realizar a consulta da equivalência, caso as informações passadas estejam de acordo com alguma equivalência já existente no sistema.

### **Consulta de equivalência**

Para realizar a consulta de uma equivalência, deve ser utilizado a operação de **ReadRecord**.

Deve ser passado um XML contendo todos os campos de chave primária.

Caso a chave informada não retorne registro, o resultado será o nome do DataSet. Caso contrário, a mesma terá suas informações exibidas através de um XML.

O **XML** deve conter os campos ***CODCOLIGADA******e IDGRUPOEQ e IDGRUPOEQEQUIV*** como informações da chave para busca da equivalência.

xmlExemplo de XML para consultatrue




EduEquivalenciaData

1;85;86

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1;CODSISTEMA=S
]]>xmlExemplo do retorno de consultatrue




1
85
86
N
1

1
85

1
86

1
A002-1
85
MATEMÁTICA

1
A012-1
86
ESTATÍSTICA APLICADA À ADMINISTRAÇÃO
]]]]>
]]>xmlExemplo do retorno sem registrostrue





]]>

## Método ReadView

Este método retorna os dados de uma ou mais equivalências de acordo com o filtro informado no XML. Entretanto, somente irá retornar se as informações passadas estejam de acordo com alguma equivalência já existente no sistema.

### **Consulta de equivalência**

Para realizar esta consulta, deve ser utilizado a operação de **ReadView,** sendo necessário informar o DataServerName, Filtro e o Contexto. Para visualizar os nomes dos campos para a montagem do filtro de equivalência, acesse: Currículo e Oferta | Estrutura Curricular | Mais | Equivalências | Filtro, selecione para criar um novo. Ao passar o mouse em cima dos itens, serão exibidos os nomes dos campos do cadastro de equivalência, tais poderão ser utilizados na montagem do filtro no XML.

xmlExemplo de XML para consultatrue




EduEquivalenciaData

SDISCGRUPOEQ.CODDISC = 'A002-1'

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1;CODSISTEMA=S
]]>xmlExemplo do retorno de consultatrue




1
85
86
N
1
1
Ensino Superior
A002-1 - MATEMÁTICA
A012-1 - ESTATÍSTICA APLICADA À ADMINISTRAÇÃO
]]]]>
]]>

## Método SaveRecord

Este método realiza a inclusão ou alteração de uma equivalência.

O sistema irá realizar a inclusão de uma equivalência, caso o código informado não exista na base.

Se a equivalência existir na coligada informada, essa terá as informações alteradas de acordo com o que será passado no arquivo XML.

### **Inclusão de equivalência**

Para realizar inclusão de uma equivalência, deve ser utilizado a operação de **SaveRecord**.

Deve ser passado um XML contendo todos os campos que serão cadastrados, como informação, para a equivalência.

Caso a equivalência informada não exista, será incluída uma nova. Caso contrário, a mesma terá suas informações atualizadas.

O **XML** deve conter as tabelas conforme exemplo abaixo.

Vale ressaltar que no exemplo abaixo será criado uma equivalência entre duas disciplinas, sendo o lado esquerdo a A002-1 e do lado direito a A012-1. Outro ponto importante os campos IDGRUPOEQ e IDGRUPOEQEQUIV da tabela SEQUIVALENCIA estão respectivamente com -1 e -2, o campo IDGRUPOEQ da SGRUPOEQ está com -1 e -2 nos respectivos registros, o mesmo vale para o IDGRUPO da tabela SDISCGRUPOEQ.

| Lado esquerdo | Lado direito |
| --- | --- |
| A002-1 | A012-1 |

xmlExemplo de XML para inclusãotrue




EduEquivalenciaData



1
-1
-2
N
1

1
-1

1
-2

1
A002-1
-1

1
A012-1
-2
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1;CODSISTEMA=S
]]>xmlExemplo do retorno da inclusãotrue


1;87;88
]]>

Caso a inclusão seja realizada com sucesso, será mostrado o código da coligada, id. do grupo de disciplinas e id. do grupo de disciplinas equivalentes inserido no item ***SaveRecordResult.***

### **Inclusão de grupo de equivalência**

Caso seja necessário **incluir** um **grupo de equivalência**, ou seja, do lado **esquerdo uma** disciplina e do lado **direito duas** disciplinas, segue exemplo.

| Lado esquerdo | Lado direito |
| --- | --- |
| A002-1 | 146-1 |
| A012-1 |

xmlInserindo grupo de equivalênciatrue




EduEquivalenciaData



1
-1
-2
N
1

1
-1

1
-2

1
A002-1
-1

1
146-1
-2

1
A012-1
-2
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1;CODSISTEMA=S
]]>

### **Alteração de equivalência**

Para realizar alteração de uma equivalência, deve ser utilizado a operação de **SaveRecord**.

Deve ser passado um XML contendo todos os campos que serão atualizados no cadastro de equivalência. Para obter o XML deve-se rodar o **ReadRecord**, a partir daí fazer as alterações que desejar.

Como exemplo vamos alterar a disciplina de código A012-1 para 146-1.

| Antes da alteração | | Depois da alteração | |
| --- | --- | --- | --- |
| Lado esquerdo | Lado direito | Lado esquerdo | Lado direito |
| A002-1 | A012-1 | A002-1 | 146-1 |

xmlRetorno do XML do ReadRecordtrue




1
87
88
N
1

1
87

1
88

1
A002-1
87
MATEMÁTICA

1
A012-1
88
ESTATÍSTICA APLICADA À ADMINISTRAÇÃO
]]]]>
]]>

Exemplo de alteração da disciplina.

xmlExemplo de XML para alteraçãotrue




EduEquivalenciaData



1
87
88
N
1

1
87

1
88

1
A002-1
87
MATEMÁTICA

1
146-1
88
ESTATÍSTICA APLICADA À ADMINISTRAÇÃO
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1;CODSISTEMA=S
]]>xmlExemplo do retorno da alteração do cadastro de Alunotrue


1;87;88
]]>

Caso a alteração seja realizada com sucesso, será mostrado o código da coligada, id. do grupo de disciplinas e id. do grupo de disciplinas equivalentes inserido no item ***SaveRecordResult.***

### **Alteração de equivalência - adicionando mais uma disciplina**

Caso seja necessário incluir mais uma disciplina do lado direito para forma um grupo de equivalência, segue exemplo.

| Antes da alteração | | Depois da alteração | |
| --- | --- | --- | --- |
| Lado esquerdo | Lado direito | Lado esquerdo | Lado direito |
| A002-1 | A012-1 | A002-1 | A012-1 |
| 146-1 |

xmlRetorno do XML do ReadRecordtrue




1
89
90
N
1

1
89

1
90

1
A002-1
89
MATEMÁTICA

1
A012-1
90
ESTATÍSTICA APLICADA À ADMINISTRAÇÃO
]]]]>
]]>

Exemplo de alteração.

xmlExemplo de XML para alteraçãotrue




EduEquivalenciaData



1
89
90
N
1

1
89

1
90

1
A002-1
89

1
A012-1
90

1
146-1
90
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1;CODSISTEMA=S
]]>

## Método DeleteRecord

Este método realiza a exclusão de uma equivalência. Algumas informações são obrigatórias e devem ser informadas: **o código da coligada, o id. do grupo de disciplinas e id. do grupo de disciplinas equivalentes**.

O sistema irá realizar a exclusão de uma equivalência caso encontre o registro.

### **Exclusão de equivalência**

Para realizar exclusão de uma equivalência, deve ser utilizado a operação de **DeleteRecord**.

Deve ser passado um XML contendo todos os campos que fazem parte do registro de equivalência.

Segue exemplo de XML para exclusão.

xmlExemplo de XML para exclusão de um Alunotrue




EduEquivalenciaData



1
87
88
N
1

1
87

1
88

1
A002-1
87
MATEMÁTICA

1
A012-1
88
ESTATÍSTICA APLICADA À ADMINISTRAÇÃO
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1;CODSISTEMA=S
]]>xmlExemplo do retorno de exclusão de Alunotrue


Exclusão de registro(s) realizado com sucesso
]]>

Para mais informações segue o link da documentação padrão de uso de DataServers utilizando WebService:

<http://tdn.totvs.com/x/XYlpCw>
