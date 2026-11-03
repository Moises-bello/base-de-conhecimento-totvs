---
content_hash: 80b64e16eb32bd8df112ae11682b19f4d2c2db2ebf1a804abb966d9dd6986234
fetched_at: '2026-06-29T00:08:55.847341+00:00'
page_id: '351018973'
product: rm
source: tdn-rm
title: Alunos (WebService)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=351018973
version: 11
---

# Visão Geral dos processos WebSevices de Alunos

O objetivo deste DataServer é possibilitar a busca, inclusão, alteração e exclusão de alunos através de WebService. Tudo o que for realizado, poderá ser visualizado no cadastro de alunos no TOTVS Gestão Educacional.

Através do dataserver "**EduAlunoData**" e por meio dos métodos **ReadRecord, **ReadView,**SaveRecord e DeleteRecord**, é possível realizar busca, inclusão, manutenção e exclusão das informações de alunos no TOTVS Gestão Educacional.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/display/LRM/Webservices)**

Índice

2

## Método ReadRecord

Este método realiza a consulta de um aluno. Algumas informações são obrigatórias e devem ser informadas: o código da coligada e o registro acadêmico.

O sistema irá realizar a consulta de aluno, caso as informações passadas estejam de acordo com algum aluno já existente no sistema.

### **Consulta de aluno**

Para realizar a consulta de um aluno, deve ser utilizado a operação de **ReadRecord**.

Deve ser passado um XML contendo todos os campos de chave primária.

Caso a chave informada não retorne registro, o resultado será o nome do DataSet. Caso contrário, a mesma terá suas informações exibidas através de um XML.

O **XML** deve conter os campos ***CODCOLIGADA******e RA*** como informações da chave para busca do aluno.

xmlExemplo de XML para consulta de um Alunotrue

EduAlunoData

1;EB-00384

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=2
]]>xmlExemplo do retorno de consulta de Alunotrue

1
EB-00384
4105
2
4105
Yasmin Marcela Cavalcanti
38252307671
Cavalcanti
Yasmin
1994-06-10T00:00:00
10
MG
Belo Horizonte
0
0
0
0
0
00
00
00
F
0.00
0
0
1
0
0
0
0
0
0
-1
0
0
mestre
2018-04-03T08:42:41
mestre
2018-04-03T08:42:41
4105
]]]]>
]]>xmlExemplo do retorno sem registrostrue<EduAluno />
]]>

## Método ReadView

Este método retorna os dados de um ou mais alunos de acordo com o filtro informado no XML. Entretanto, somente irá retornar se as informações passadas estejam de acordo com algum aluno já existente no sistema.

### **Consulta de aluno**

Para realizar esta consulta, deve ser utilizado a operação de **ReadView,** sendo necessário informar o DataServerName, Filtro e o Contexto. Para visualizar os nomes dos campos para a montagem do filtro do aluno, acesse: Cadastro do Aluno | Filtro, selecione para criar um novo. Ao passar o mouse em cima dos itens, serão exibidos os nomes dos campos do cadastro do aluno, tais poderão ser utilizados na montagem do filtro no XML. 

xmlExemplo de XML para consulta de um Alunotrue

EduAlunoData

PPESSOA.CPF = '80466346549' AND PPESSOA.NOME = 'ACIDALIA VIEIRA SANTOS'

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1;CODSISTEMA=S
]]>xmlExemplo do retorno de consulta de Alunotrue

2627
1
1
0000160
2627
ACIDALIA VIEIRA SANTOS
F
ACIDALIA CARINE VIEIRA SANTOS
ANISIO HILARIO DOS SANTOS FILH
ROSE MARIA VIEIRA SANTOS
80466346549
06693288 20
1981-03-05T00:00:00
BELO HORIZONTE
SANTOS
S
MG
RUA CONDE DE PORTO ALEGRE 270
IAPI
BELO HORIZONTE
MG
40330200
00
00
00
50
]]]]>
]]>

## Método SaveRecord

Este método realiza a inclusão ou alteração de um aluno. Algumas informações são obrigatórias e devem ser informadas: o código da coligada e o registro acadêmico, além dos outros campos que estão configurados como obrigatórios no sistema.

O sistema irá realizar a inclusão de um aluno, caso o código informado não exista na base.

Se o Registro Acadêmico existir na coligada informada, essa terá as informações alteradas de acordo com o que será passado no arquivo XML.

***Observação***:

1. Caso sejam passadas para o dataserver informações para **campos complementares**, devem ser utilizados os mesmos códigos obrigatórios para que o sistema consiga entender que se referem ao aluno que se deseja alterar.
2. Para a tabela <SAluno> deve-se informar as tags <CODIGO></CODIGO> e <CODPESSOA></CODPESSOA> com os mesmos valores.

### **Inclusão de aluno**

Para realizar inclusão de um aluno, deve ser utilizado a operação de **SaveRecord**.

Deve ser passado um XML contendo todos os campos que serão cadastrados, como informação, para o aluno.

Caso o Registro acadêmico informado não exista, será incluído um novo aluno. Caso contrário, o mesmo terá suas informações atualizadas.

O **XML** deve conter a tabela ***SALUNO***com os campos ***CODCOLIGADA******e RA*** como informações da chave para o cadastro de aluno e, também, os campos obrigatórios para seu cadastro.

A inclusão do Aluno irá levar em consideração as configurações de RA informadas no sistema. Para que o RA seja criado automaticamente, deve-se informar "0" para o registro, nesse caso o xml deve conter apenas um aluno.

xmlExemplo de XML para inclusão de um Alunotrue

EduAlunoData



1
0
0
2
0
Stella Fernanda Aparício
62587463653
Aparício
Fernanda
1994-06-10T00:00:00
10
MG
Belo Horizonte
0
0
0
0
0
00
00
00
F
0.00
0
0
1
0
0
0
0
0
0
-1
0
0
mestre
2018-04-03T08:42:41
mestre
2018-04-03T08:42:41
4105

1
0
mestre
2018-04-03T08:42:42
mestre
2018-04-03T08:42:42
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1
]]>xmlExemplo do retorno da inclusão de Alunotrue1;8001408]]>

Caso a inclusão seja realizada com sucesso, será mostrado o código da coligada e o registro acadêmico inserido no item ***SaveRecordResult.***

### **Alteração de aluno**

Para realizar alteração de um aluno, deve ser utilizado a operação de **SaveRecord**.

Deve ser passado um XML contendo todos os campos que serão atualizados no cadastro de aluno.

O **XML** deve conter a tabela ***SALUNO***com os campos ***CODCOLIGADA******e RA***como informações da chave para a atualização do cadastro de aluno.

xmlExemplo de XML para alteração de informações de Alunotrue

EduAlunoData



1
0
0
2
0
Stella Fernanda Aparício
62587463653
Aparício
Fernanda
1994-06-12T00:00:00
10
MG
Belo Horizonte
0
0
0
0
0
00
00
00
F
0.00
0
0
1
0
0
0
0
0
0
-1
0
0
mestre
2018-04-03T08:42:41
mestre
2018-04-03T08:42:41
4105

1
0
mestre
2018-04-03T08:42:42
mestre
2018-04-03T08:42:42
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1
]]>xmlExemplo do retorno da alteração do cadastro de Alunotrue1;8001408
]]>

Caso a alteração seja realizada com sucesso, será mostrado o código da coligada e o registro acadêmico no item **SaveRecordResult.**

## Método DeleteRecord

Este método realiza a exclusão de um aluno. Algumas informações são obrigatórias e devem ser informadas: o código da coligada e o registro acadêmico, além dos outros campos que estão configurados como obrigatórios no sistema.

O sistema irá realizar a exclusão de um aluno caso encontre o registro.

### **Exclusão de aluno**

Para realizar exclusão de um aluno, deve ser utilizado a operação de **DeleteRecord**.

Deve ser passado um XML contendo todos os campos que fazem parte do registro de aluno.

O **XML** deve conter a tabela ***SALUNO***com os campos ***CODCOLIGADA******e RA*** como informações da chave para o cadastro de aluno e, também, os campos obrigatórios para seu cadastro.

xmlExemplo de XML para exclusão de um Alunotrue

EduAlunoData



1
8001408
45087
2
45087
Stella Fernanda Aparício
62587463653
Aparício
Fernanda
1994-06-12T00:00:00
10
MG
Belo Horizonte
0
0
0
0
0
00
00
00
F
0.00
0
0
1
0
0
0
0
0
0
-1
0
0
mestre
2018-04-03T08:42:41
mestre
2018-04-03T08:42:41
4105

1
8001408
mestre
2018-04-03T08:42:42
mestre
2018-04-03T08:42:42
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=3;CODSISTEMA=S;
]]>xmlExemplo do retorno de exclusão de AlunotrueExclusão de registro(s) realizado com sucesso]]>

Para mais informações segue o link da documentação padrão de uso de DataServers utilizando WebService:

<http://tdn.totvs.com/x/XYlpCw>
