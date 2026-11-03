---
content_hash: 6bc2b8137e1f8404650df641b36b92b9b2d60b94a5197588719e2f6559f9c84c
fetched_at: '2026-06-29T00:08:47.714047+00:00'
page_id: '320375133'
product: rm
source: tdn-rm
title: Professores
type: documentation
url: https://tdn.totvs.com/display/LRM/Professores
version: 13
---

# Visão Geral dos processos WebSevices de Professores

O objetivo deste DataServer é possibilitar a busca, inclusão, alteração e exclusão de professores através de WebService. Tudo o que for realizado, poderá ser visualizado no cadastro de professores no TOTVS Gestão Educacional.

Através do dataserver "**EduProfessorData**" e por meio dos métodos **ReadRecord, SaveRecord e DeleteRecord**, é possível realizar busca, inclusão, manutenção e exclusão das informações de professores no TOTVS Gestão Educacional.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/display/LRM/Webservices)**

Índice

2

## Método ReadRecord

Este método realiza a consulta de um professor. Algumas informações são obrigatórias e devem ser informadas: o código da coligada e o código de professor.

O sistema irá realizar a consulta de professor, caso as informações passadas estejam de acordo com algum professor já existente no sistema.

### **Consulta de professor**

Para realizar a consulta de um professor, deve ser utilizado a operação de **ReadRecord**.

Deve ser passado um XML contendo todos os campos de chave primária.

Caso a chave informada não retorne registro, o resultado será o nome do DataSet. Caso contrário, a mesma terá suas informações exibidas através de um XML.

O **XML** deve conter os campos ***CODCOLIGADA******e CODPROF*** como informações da chave para busca do professor.

xmlExemplo de XML para consulta de um Professortrue

EduProfessorData

1;43

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=3;CODSISTEMA=S;
]]>xmlExemplo do retorno de consulta de Professortrue

1
003154
43
619
2
619
RODRIGO BRUME
1980-03-27T00:00:00
M
10
7
RUA EUGENIO WOLTER
COSTA E SILVA
SC
Joinville
89217440
10392880652
3578
33333333333
33333333333
23.226.110-6
SSP/SC
1996-11-22T00:00:00
325300660167
19
104
0459838724
0030
0
00000000000
Joinville
SC
0
0
0
0
TOTVS241@totvs.com.br
0
0
003154
0
0
Professor Assistente AS1D
1998-01-30T00:00:00
1998-11-01T00:00:00
16 CSM
Alistado
0
0
0
0
61b33186-9463-4b1c-a3bd-3a11747a519e
0
0
0
2013-08-01T00:00:00
0
0
1
1
0
0
0
0
0
0
0
0
0
mestre
2016-09-19T09:49:07
mestre
2018-03-12T08:28:05

1
43
]]]]>
]]>xmlExemplo do retorno sem registrostrue<EduProfessor />
]]>

## Método SaveRecord

Este método realiza a inclusão ou alteração de um professor. Algumas informações são obrigatórias e devem ser informadas: o código da coligada e o código do professor, além dos outros campos que estão configurados como obrigatórios no sistema.

O sistema irá realizar a inclusão de um professor, caso o código informado não exista na base.

Se o código do professor existir na coligada informada, essa terá as informações alteradas de acordo com o que será passado no arquivo XML.

***Observação***: Caso sejam passadas para o dataserver informações para **campos complementares**, devem ser utilizados os mesmos códigos obrigatórios para que o sistema consiga entender que se referem ao professor que se deseja alterar.

### **Inclusão de professor**

Para realizar inclusão de um professor, deve ser utilizado a operação de **SaveRecord**.

Deve ser passado um XML contendo todos os campos que serão cadastrados, como informação, para o professor.

Caso o código e professor informado não exista, será incluído um novo professor. Caso contrário, o mesmo terá suas informações atualizadas.

O **XML** deve conter a tabela ***SPROFESSOR***com os campos ***CODCOLIGADA******e CODPROF*** como informações da chave para o cadastro de professor e, também, os campos obrigatórios para seu cadastro.

xmlExemplo de XML para inclusão de um Professortrue

EduProfessorData



1
003154
43
619
2
619
RODRIGO BRUME
1980-03-27T00:00:00
M
10
7
RUA EUGENIO WOLTER
COSTA E SILVA
SC
Joinville
89217440
10392880652
3578
33333333333
33333333333
23.226.110-6
SSP/SC
1996-11-22T00:00:00
325300660167
19
104
0459838724
0030
0
00000000000
Joinville
SC
0
0
0
0
TOTVS241@totvs.com.br
0
0
003154
0
0
Professor Assistente AS1D
1998-01-30T00:00:00
1998-11-01T00:00:00
16 CSM
Alistado
0
0
0
0
61b33186-9463-4b1c-a3bd-3a11747a519e
0
0
0
2013-08-01T00:00:00
0
0
1
1
0
0
0
0
0
0
0
0
0
mestre
2016-09-19T09:49:07
mestre
2018-03-12T08:28:05

1
43
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=3;CODSISTEMA=S;
>
]]>xmlExemplo do retorno da inclusão de Professortrue1;43]]>

Caso a inclusão seja realizada com sucesso, será mostrado o código da coligada e o código do professor inserido no item ***SaveRecordResult.***

### **Alteração de professor**

Para realizar alteração de um professor, deve ser utilizado a operação de **SaveRecord**.

Deve ser passado um XML contendo todos os campos que serão atualizados no cadastro de professor.

O **XML** deve conter a tabela ***SPROFESSOR***com os campos ***CODCOLIGADA******e CODPROF***como informações da chave para a atualização do cadastro de professor.

xmlExemplo de XML para alteração de informações de Professortrue

EduProfessorData



1
003154
43
619
2
619
RODRIGO BRUME
1980-03-27T00:00:00
M
10
7
RUA EUGENIO WOLTER
COSTA E SILVA
SC
Joinville
89217440
10392880652
3578
33333333333
33333333333
23.226.110-6
SSP/SC
1996-11-22T00:00:00
325300660167
19
104
0459838724
0030
0
00000000000
Joinville
SC
0
0
0
0

0
0
003154
0
0
Professor Assistente AS1D
1998-01-30T00:00:00
1998-11-01T00:00:00
16 CSM
Alistado
0
0
0
0
61b33186-9463-4b1c-a3bd-3a11747a519e
0
0
0
2013-08-01T00:00:00
0
0
1
1
0
0
0
0
0
0
0
0
0
mestre
2016-09-19T09:49:07
mestre
2018-03-12T08:28:05

1
43
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=3;CODSISTEMA=S;
]]>xmlExemplo do retorno da alteração do cadastro de Professortrue1;43]]>

Caso a alteração seja realizada com sucesso, será mostrado o código da coligada e o código do professor no item **SaveRecordResult.**

## Método DeleteRecord

Este método realiza a exclusão de um professor. Algumas informações são obrigatórias e devem ser informadas: o código da coligada e o código do professor, além dos outros campos que estão configurados como obrigatórios no sistema.

O sistema irá realizar a exclusão de um professor caso encontre o registro.

### **Exclusão de professor**

Para realizar exclusão de um professor, deve ser utilizado a operação de **DeleteRecord**.

Deve ser passado um XML contendo todos os campos que fazem parte do registro de professor.

O **XML** deve conter a tabela ***SPROFESSOR***com os campos ***CODCOLIGADA******e CODPROF*** como informações da chave para o cadastro de professor e, também, os campos obrigatórios para seu cadastro.

xmlExemplo de XML para exclusão de um Professortrue

EduProfessorData



1
003154
43
619
2
619
RODRIGO BRUME
1980-03-27T00:00:00
M
10
7
RUA EUGENIO WOLTER
COSTA E SILVA
SC
Joinville
89217440
10392880652
3578
33333333333
33333333333
23.226.110-6
SSP/SC
1996-11-22T00:00:00
325300660167
19
104
0459838724
0030
0
00000000000
Joinville
SC
0
0
0
0
TOTVS241@totvs.com.br
0
0
003154
0
0
Professor Assistente AS1D
1998-01-30T00:00:00
1998-11-01T00:00:00
16 CSM
Alistado
0
0
0
0
61b33186-9463-4b1c-a3bd-3a11747a519e
0
0
0
2013-08-01T00:00:00
0
0
1
1
0
0
0
0
0
0
0
0
0
mestre
2016-09-19T09:49:07
mestre
2018-03-12T08:28:05

1
43
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=3;CODSISTEMA=S;
]]>xmlExemplo do retorno de exclusão de ProfessortrueExclusão de registro(s) realizado com sucesso]]>

Para mais informações segue o link da documentação padrão de uso de DataServers utilizando WebService:

<http://tdn.totvs.com/x/XYlpCw>
