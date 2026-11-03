---
content_hash: b9cfe507c6e3194c5dc0d287bf14630dc2d4f9dd01645b346b2274cc7d319b22
fetched_at: '2026-06-29T00:08:53.255179+00:00'
page_id: '344464971'
product: rm
source: tdn-rm
title: Turma/Disciplinas (WebService)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=344464971
version: 8
---

# Visão Geral dos processos WebSevices da Turma/Disciplinas

O objetivo deste DataServer é possibilitar a busca, inclusão, alteração e exclusão de turma/disciplina através de WebService. Tudo o que for realizado, poderá ser visualizado no cadastro de turma/disciplina no TOTVS Gestão Educacional.

Através do dataserver "**EduTurmaDiscData**" e por meio dos métodos **ReadRecord, SaveRecord e DeleteRecord**, é possível realizar busca, inclusão, manutenção e exclusão das informações de Turma/Discplina no TOTVS Gestão Educacional.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/display/LRM/Webservices)**

Índice

2

## Método ReadRecord

Este método realiza a consulta de uma turma/disciplina. Algumas informações são obrigatórias e devem ser informadas: o código da coligada e o ID da turma/disciplina.

O sistema irá realizar a consulta de uma turma/disciplina caso as informações passadas estejam de acordo com alguma turma/disciplina já existente no sistema.

### **Consulta da turma/disciplina**

Para realizar a consulta de uma turma/disciplina, deve ser utilizado a operação de **ReadRecord**.

Deve ser passado um XML contendo todos os campos de chave primária.

Caso a chave informada não retorne registro, o resultado será o nome do DataSet. Caso contrário, a mesma terá suas informações exibidas através de um XML.

O **XML** deve conter os campos ***CODCOLIGADA e******IDTURMADISC*** como informações da chave para busca da turma/disciplina.

xmlExemplo de XML para consulta de uma Turma/Disciplinatrue

EduTurmaDiscData

1;2943

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1;CODSISTEMA=S
]]>xmlExemplo do retorno de consulta da Turma/Disciplinatrue

1
2943
1
Turma B
98
BD
304
403
1000
50
25
3
2018-01-01T00:00:00
2018-12-31T00:00:00
5
ADS-BD
P
ADS
1
1
N
N
S
N
S
0
3
2018/01

1
2943
S
]]]]>
]]>xmlExemplo do retorno sem registrostrue<EduTurmaDisc />
]]>

## Método SaveRecord

Este método realiza a inclusão ou alteração de uma turma/disciplina. Algumas informações são obrigatórias e devem ser informadas: o código da coligada, o código da filial, o id do período letivo, o código da turma, além dos outros campos que estão configurados como obrigatórios no sistema.

O sistema irá realizar a inclusão de uma turma/disciplina, caso o código informado não exista na base.

Se o código da turma/disciplina existir na coligada informada, essa terá as informações alteradas de acordo com o que será passado no arquivo XML.

***Observação***: Caso sejam passadas para o dataserver informações para **campos complementares**, devem ser utilizados os mesmos códigos obrigatórios para que o sistema consiga entender que se referem à turma/disciplina que se deseja alterar.

### **Inclusão da turma/disciplina**

Para realizar inclusão de uma turma/disciplina, deve ser utilizado a operação de **SaveRecord**.

Deve ser passado um XML contendo todos os campos que serão cadastrados, como informação, para a turma/disciplina.

Levando em consideração que o campo de ***IDTURMADISC*** é auto-Incremento, o mesmo deve ser preenchido com o valor 0.

Caso o código e turma/disciplina informada não exista, será incluída uma nova turma/disciplina. Caso contrário, a mesma terá suas informações atualizadas.

O **XML** deve conter a tabela ***STURMADISC***com os campos ***CODCOLIGADA e******IDTURMADISC***como informações da chave para o cadastro da turma/disciplina e, também, os campos obrigatórios para seu cadastro.

xmlExemplo de XML para inclusão de uma Turma/Disciplinatrue

EduTurmaDiscData



1
0
1
Turma B
98
BD
304
403
1000
50
25
3
2018-01-01T00:00:00
2018-12-31T00:00:00
5
ADS-BD
P
ADS
1
1
N
N
S
N
S
0
3
2018/01
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1;CODSISTEMA=S
]]>xmlExemplo do retorno da inclusão da Turma/Disciplinatrue1;2943
]]>

Caso a inclusão seja realizada com sucesso, será mostrado o código da coligada e o id da turma/disciplina inserido no item ***SaveRecordResult.***

### **Alteração de turma/disciplina**

Para realizar alteração de uma turma/disciplina, deve ser utilizado a operação de **SaveRecord**.

Deve ser passado um XML contendo todos os campos que serão atualizados no cadastro da turma/disciplina.

O **XML** deve conter a tabela ***STURMADISC***com os campos ***CODCOLIGADA e******IDTURMADISC*** como informações da chave para a atualização do cadastro da turma/disciplina.

xmlExemplo de XML para alteração de informações da Turma/Disciplinatrue

EduTurmaDiscData



1
2943
1
Turma B
98
BD
304
403
100
50
25
3
2018-01-01T00:00:00
2018-12-31T00:00:00
5
ADS-BD
P
ADS
1
1
N
N
S
N
S
0
3
2018/01

1
2943
S
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1;CODSISTEMA=S
]]>xmlExemplo do retorno da alteração do cadastro da Turma/Disciplinatrue1;2943
]]>

Caso a alteração seja realizada com sucesso, será mostrado o código da coligada e o id da turma/disciplina no item **SaveRecordResult.**

## Método DeleteRecord

Este método realiza a exclusão de uma turma/disciplina. Algumas informações são obrigatórias e devem ser informadas: o código da coligada e o id da turma/disciplina, além dos outros campos que estão configurados como obrigatórios no sistema.

O sistema irá realizar a exclusão de uma turma/disciplina caso encontre o registro.

### **Exclusão da turma/disciplina**

Para realizar exclusão de uma turma/disciplina, deve ser utilizado a operação de **DeleteRecord**.

Deve ser passado um XML contendo todos os campos que fazem parte do registro da turma/disciplina.

O **XML** deve conter a tabela ***STURMADISC***com os campos ***CODCOLIGADA e******IDTURMADISC*** como informações da chave para o cadastro da turma/disciplina e, também, os campos obrigatórios para seu cadastro.

xmlExemplo de XML para exclusão de uma Turma/Disciplinatrue

EduTurmaDiscData



1
2943
1
Turma B
98
BD
304
403
500
50
25
3
2018-01-01T00:00:00
2018-12-31T00:00:00
5
ADS-BD
P
ADS
1
1
N
N
S
N
S
0
3
2018/01

1
2943
S
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1;CODSISTEMA=S
]]>xmlExemplo do retorno de exclusão da Turma/DisciplinatrueExclusão de registro(s) realizado com sucesso
]]>

Para mais informações segue o link da documentação padrão de uso de DataServers utilizando WebService:

<http://tdn.totvs.com/x/XYlpCw>
