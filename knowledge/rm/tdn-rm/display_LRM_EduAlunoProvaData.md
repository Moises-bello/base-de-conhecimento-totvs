---
content_hash: 6c1cc71b2a064bc392d5f603dd242b4ba48a957a207312faeaf3e3db20556193
fetched_at: '2026-06-29T00:08:58.835574+00:00'
page_id: '361443449'
product: rm
source: tdn-rm
title: EduAlunoProvaData
type: documentation
url: https://tdn.totvs.com/display/LRM/EduAlunoProvaData
version: 7
---

# Visão Geral dos processos WebSevices de Notas de Avaliação

O objetivo deste DataServer é possibilitar a busca, inclusão e alteração de notas de avaliação através de WebService. Tudo o que for realizado, poderá ser visualizado no menu de notas e faltas de avaliação no TOTVS Gestão Educacional.

Através do dataserver "**EduAlunoProvaData**" e por meio dos métodos **ReadRecord e SaveRecord**, é possível realizar busca, inclusão e manutenção das informações de notas de avaliação no TOTVS Gestão Educacional.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/display/LRM/Webservices)**

Índice

2

**Caso o usuário informado na autenticação, não possua permissão ao menu, o processo não poderá ser executado.**

O caminho da permissão, para que o usuário realize o processo, é: **Matrícula e Avaliação | Mais | Digitação por Aluno | Notas de Avaliação ou Matrícula e Avaliação | Notas de Avaliação.**

## Método ReadRecord

Este método realiza a consulta de uma nota de avaliação. Algumas informações são obrigatórias e devem ser informadas: o código da coligada, código da etapa, código da avaliação, tipo da etapa, id da turma disciplina e registro acadêmico do aluno.

O sistema irá realizar a consulta da nota de avaliação, caso as informações passadas estejam de acordo com alguma nota de avaliação já existente no sistema.

### **Consulta da nota de avaliação**

Para realizar a consulta de uma nota de avaliação, deve ser utilizado a operação de **ReadRecord**.

Deve ser passado um XML contendo todos os campos de chave primária.

Caso a chave informada não retorne registro, o resultado será o nome do DataSet. Caso contrário, a mesma terá suas informações exibidas através de um XML.

O **XML** deve conter os campos ***CODCOLIGADA, CODPROVA, CODETAPA, TIPOETAPA, IDTURMADISC e******RA*** como informações da chave para busca da nota de avaliação.

xmlExemplo de XML para consulta de uma nota de avaliaçãotrue

EduAlunoProvaData

1;1;1;N;4390;MFA2018

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1
]]>xmlExemplo do retorno de consulta da nota de avaliaçãotrue

1
1
1
N
4390
MFA2018
50
0
2
70
100
Avaliação
N
Márcia Francisca Alves
Márcia Francisca Alves
MFA2018
80
0
S
N
Matriculado
70
2018-01-01T00:00:00
2018-12-31T00:00:00
2018-05-14T13:44:35
45627
406
<\_x0031\_\_x0020\_-\_x0020\_Notas>80
80
0
]]]]>
]]>xmlExemplo do retorno sem registrostrue<EduNotas />
]]>

## Método SaveRecord

Este método realiza a inclusão ou alteração de uma nota de avaliação. Algumas informações são obrigatórias e devem ser informadas: o código da coligada, o código da prova, o código da etapa, o tipo da etapa, o id turma disciplina e o registro acadêmico, além dos outros campos que estão configurados como obrigatórios no sistema.

O sistema irá realizar a inclusão de uma nota de avaliação, caso as informações passadas não exista na base.

Se houver um registro já existente com as informações informadas na chave, esse será alterado de acordo com os dados passados no arquivo XML.

### **Inclusão da nota de avaliação**

Para realizar inclusão de uma nota de avaliação, deve ser utilizado a operação de **SaveRecord**.

Deve ser passado um XML contendo todos os campos que serão cadastrados, como informação, para a nota de avaliação.

Se houver um registro já existente com as informações informadas na chave, esse será alterado de acordo com os dados passados.

O **XML** deve conter a tabela ***SNOTAS***com os campos ***CODCOLIGADA, CODPROVA, CODETAPA, TIPOETAPA, IDTURMADISC e******RA*** como informações da chave para o cadastro da nota de avaliação, também, os campos obrigatórios para seu cadastro.

xmlExemplo de XML para inclusão de uma nota de avaliaçãotrue

EduAlunoProva



1
1
1
N
4390
MFA2018
50
0
2
70
100
Avaliação
N
Márcia Francisca Alves
Márcia Francisca Alves
MFA2018
80
0
S
N
Matriculado
70
2018-01-01T00:00:00
2018-12-31T00:00:00
2018-05-14T13:44:35
45627
406
<\_x0031\_\_x0020\_-\_x0020\_Notas>80
80
0
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1
]]>xmlExemplo do retorno da inclusão da nota de avaliaçãotrue1;1;1;N;4390;MFA2018
]]>

Caso a inclusão seja realizada com sucesso, será mostrado o código da coligada, código da avaliação, código da etapa, o tipo da etapa, o id da turma disciplina e o registro acadêmico inserido no item ***SaveRecordResult.***

### **Alteração da nota de avaliação**

Para realizar alteração de uma nota de avaliação, deve ser utilizado a operação de **SaveRecord**.

Deve ser passado um XML contendo todos os campos que serão atualizados no cadastro da nota de avaliação.

O **XML** deve conter a tabela ***SNOTAS***com os campos ***CODCOLIGADA, CODPROVA, CODETAPA, TIPOETAPA, IDTURMADISC e******RA*** como informações da chave para o cadastro da nota de avaliação e, também, os campos obrigatórios para seu cadastro.

xmlExemplo de XML para alteração de informações da nota de avaliaçãotrue

EduAlunoProvaData



1
1
1
N
4390
MFA2018
50
0
2
70
100
Avaliação
N
Márcia Francisca Alves
Márcia Francisca Alves
MFA2018
80
0
S
N
Matriculado
70
2018-01-01T00:00:00
2018-12-31T00:00:00
2018-05-14T13:44:35
45627
406
<\_x0031\_\_x0020\_-\_x0020\_Notas>80
80
0
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1
]]>xmlExemplo do retorno da alteração do cadastro da nota de avaliaçãotrue1;1;1;N;4390;MFA2018
]]>

Caso a inclusão seja realizada com sucesso, será mostrado o código da coligada, código da avaliação, código da etapa, o tipo da etapa, o id da turma disciplina e o registro acadêmico inserido no item ***SaveRecordResult.***
