---
content_hash: d009a9e541f7fd11cc51573c6116efa38d649520c466c2812156468f9e09ba3a
fetched_at: '2026-06-29T00:09:12.253910+00:00'
page_id: '416843504'
product: rm
source: tdn-rm
title: Plano de Aula (Webservice)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=416843504
version: 5
---

# Visão Geral dos processos WebSevices de Plano de Aula

O objetivo deste DataServer é possibilitar a busca, inclusão, alteração e exclusão de plano de aula através de WebService. Tudo o que for realizado, poderá ser visualizado no cadastro de plano de aula no TOTVS Gestão Educacional.

Através do dataserver "**EduPlanoAulaData**" e por meio dos métodos **ReadRecord, SaveRecord e DeleteRecord**, é possível realizar busca, inclusão, manutenção e exclusão das informações de plano de aula no TOTVS Gestão Educacional.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/display/LRM/Webservices)**

Índice

2

## Método ReadRecord

Este método realiza a consulta de um plano de aula. Algumas informações são obrigatórias e devem ser informadas: o código da coligada, o id da turma disciplina e o id do plano de aula.

O sistema irá realizar a consulta do plano de aula, caso as informações passadas estejam de acordo com algum plano de aula já existente no sistema.

### **Consulta de Plano de Aula**

Para realizar a consulta de um plano de aula, deve ser utilizado a operação de **ReadRecord**.

Deve ser passado um XML contendo todos os campos de chave primária.

Caso a chave informada não retorne registro, o resultado será o nome do DataSet. Caso contrário, a mesma terá suas informações exibidas através de um XML.

O **XML** deve conter os campos ***CODCOLIGADA**,****IDTURMADISC e IDPLANOAULA*** como informações da chave para busca do plano de aula.

xmlExemplo de XML para consulta de um Plano de Aulatrue

EduPlanoAulaData

1;4632;311254

CODCOLIGADA=1;CODTIPOCURSO=1;CODSISTEMA=S;CODFILIAL=1
]]>xmlExemplo do retorno de consulta de Plano de Aulatrue

1
4632
1001
9725
1
230401
2037-03-02T00:00:00
07:10
08:00
T1JD
FDJD
Fundamentos do Design de Jogos Digitais
2
N
311254
T
104
07:10
08:00
304
]]]]>
]]>xmlExemplo do retorno sem registrostrue<EduPlanoAula />
]]>

## Método ReadView

Este método realiza a consulta de um plano de aula. Algumas informações são obrigatórias e devem ser informadas:como o contexto e o filtro.

O sistema irá realizar a consulta de plano de aula, caso as informações passadas estejam de acordo com algum plano de aula já existente no sistema.

### **Consulta de plano de aula**

Para realizar a consulta de um plano de aula, deve ser utilizado a operação de **ReadView**.

Deve ser passado um XML contendo os campos no filtro.

Para visualizar os nomes dos campos do plano de aula acesse: Cadastro de Turma Disciplinas | Anexo > Plano de Aula | Filtro.

Ao selecionar um novo filtro é possível visualizar os nomes dos campos do cadastro do plano de aula. 

Exemplo de XML para consulta de um Plano de Aulatrue

EduPlanoAulaData

SPLANOAULA.IDPLANOAULA = '311256'

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1;CODSISTEMA=S
]]>Exemplo de retorno de consulta de Plano de Aulatrue

1
9725
2
07:10
08:00
2037-03-16T00:00:00
1003
4632
T1JD
FDJD
Fundamentos do Design de Jogos Digitais
N
311256
T
230401
104
]]]]>
]]>

## Método SaveRecord

Este método realiza a inclusão ou alteração de um plano de aula. Algumas informações são obrigatórias e devem ser informadas: o código da coligada, o id da turma disciplina e o id do plano de aula, além dos outros campos que estão configurados como obrigatórios no sistema.

O sistema irá realizar a inclusão de um plano de aula, caso o código informado não exista na base.

Se a chave existir na coligada informada, essa terá as informações alteradas de acordo com o que será passado no arquivo XML.

### **Alteração de Plano de Aula**

Para realizar alteração de um plano de aula, deve ser utilizado a operação de **SaveRecord**.

Deve ser passado um XML contendo todos os campos que serão atualizados no cadastro de plano de aula.

O **XML** deve conter a tabela ***SPLANOAULA***com os campos ***CODCOLIGADA**,****IDTURMADISC e IDPLANOAULA***como informações da chave para a atualização do cadastro de plano de aula.

xmlExemplo de XML para alteração de informações de Plano de Aulatrue

EduPlanoAulaData



1
4632
1002
9725
1
230401
2037-03-02T00:00:00
07:10
08:00
T1JD
FDJD
Fundamentos do Design de Jogos Digitais
2
N
311255
T
104
07:10
08:00
304
]]]]>

CODCOLIGADA=1;CODTIPOCURSO=3;CODSISTEMA=S;CODFILIAL=1;CODUSUARIO=mestre
]]>xmlExemplo do retorno da alteração do cadastro de Plano de Aulatrue1;4632;311255
]]>

Caso a alteração seja realizada com sucesso, será mostrado o código da coligada, o id da turma disciplina e o id do plano de aula no item **SaveRecordResult.**

## Método DeleteRecord

Este método realiza a exclusão de um plano de aula. Algumas informações são obrigatórias e devem ser informadas: o código da coligada, o id da turma disciplina e o id do plano de aula, além dos outros campos que estão configurados como obrigatórios no sistema.

O sistema irá realizar a exclusão de um plano de aula caso encontre o registro.

### **Exclusão de plano de aula**

Para realizar exclusão de um plano de aula, deve ser utilizado a operação de **DeleteRecord**.

Deve ser passado um XML contendo todos os campos que fazem parte do registro de plano de aula.

O **XML** deve conter a tabela ***SPLANOAULA***com os campos ***CODCOLIGADA**,****IDTURMADISC e IDPLANOAULA*** como informações da chave para o cadastro de plano de aula e, também, os campos obrigatórios para seu cadastro.

xmlExemplo de XML para exclusão de um Plano de Aulatrue

EduPlanoAulaData



1
4632
1002
9725
1
230401
2037-03-02T00:00:00
07:10
08:00
T1JD
FDJD
Fundamentos do Design de Jogos Digitais
2
N
311255
T
104
07:10
08:00
304
]]]]>

CODCOLIGADA=1;CODTIPOCURSO=3;CODSISTEMA=S;CODFILIAL=1;CODUSUARIO=mestre
]]>xmlExemplo do retorno de exclusão de Plano de AulatrueExclusão de registro(s) realizado com sucesso]]>

Para mais informações segue o link da documentação padrão de uso de DataServers utilizando WebService:

<http://tdn.totvs.com/x/XYlpCw>
