---
content_hash: 02e789ae4c85bfc3b168a33d130dca864b46ee13976d0f2769dcf563c959919e
fetched_at: '2026-06-29T00:08:53.292265+00:00'
page_id: '344466773'
product: rm
source: tdn-rm
title: Curso
type: documentation
url: https://tdn.totvs.com/display/LRM/Curso
version: 8
---

# Visão Geral dos processos WebSevices de Curso

O objetivo deste DataServer é possibilitar a busca, inclusão, alteração e exclusão de Cursos através de WebService. Tudo o que for realizado, poderá ser visualizado no cadastro de Cursos no TOTVS Gestão Educacional.

Através do DataServer "**EduCursoData**" e por meio dos métodos **ReadRecord, SaveRecord e DeleteRecord**, é possível realizar busca, inclusão, manutenção e exclusão das informações de Curso no TOTVS Gestão Educacional.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/display/LRM/Webservices)**

Índice

2

## Método ReadRecord

Este método realiza a consulta de um Curso. Algumas informações são obrigatórias e devem ser informadas: o código da coligada e o código do Curso.

O sistema irá realizar a consulta de um Curso, caso as informações passadas estejam de acordo com algum curso já existente no sistema.

### **Consulta do Curso**

Para realizar a consulta de um Curso, deve ser utilizado a operação de **ReadRecord**.

Deve ser passado um XML contendo todos os campos de chave primária.

Caso a chave informada não retorne registro, o resultado será o nome do DataSet. Caso contrário, o mesmo terá suas informações exibidas através de um XML.

O **XML** deve conter os campos ***CODCOLIGADA e CODCURSO*** como informações da chave para busca de Curso.

xmlExemplo de XML para consulta de um Cursotrue

EduCursoData

1;12-1

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1;CODSISTEMA=S
]]>xmlExemplo do retorno de consulta de Cursotrue


1
12-1
ENGENHARIA DE AUTOMAÇÃO
1
P

1
12-1
]]]]>
]]>xmlExemplo do retorno sem registrostrue<EduCursoData />
]]>

## Método SaveRecord

Este método realiza a inclusão ou alteração de um Curso. Algumas informações são obrigatórias e devem ser informadas: o código da coligada, o código da filial e o codtipocurso, além dos outros campos que estão configurados como obrigatórios no sistema.

O sistema irá realizar a inclusão de um Curso, caso o código informado não exista na base.

Se o código do Curso existir na coligada informada, essa terá as informações alteradas de acordo com o que será passado no arquivo XML.

***Observação***: Caso sejam passadas para o DataServer informações para **campos complementares**, devem ser utilizados os mesmos códigos obrigatórios para que o sistema consiga entender que se referem ao Curso que se deseja alterar.

### **Inclusão de Curso**

Para realizar inclusão de um Curso, deve ser utilizado a operação de **SaveRecord**.

Deve ser passado um XML contendo todos os campos que serão cadastrados, como informação para o Curso

Caso o código do Curso informado não exista, será incluído um novo Curso. Caso contrário, o mesmo terá suas informações atualizadas.

O **XML** deve conter a tabela ***SCURSO***com os campos ***CODCOLIGADA e o******CODCURSO***como informações da chave para o cadastro de Curso, também os campos obrigatórios para seu cadastro.

xmlExemplo de XML para inclusão de um Cursotrue

EduCursoData



1
3-12
ENGENHARIA\_EXCLUIR- Automação
 
 
1

1
3-12
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1;CODSISTEMA=S
]]>xmlExemplo do retorno da inclusão de Cursotrue1;3-12
]]>

Caso a inclusão seja realizada com sucesso, será mostrado o código da coligada e o cod. do curso inserido no item ***SaveRecordResult.***

### **Alteração de Curso**

Para realizar alteração de um Curso, deve ser utilizado a operação de **SaveRecord**.

Deve ser passado um XML contendo todos os campos que serão atualizados no cadastro de Curso;

O **XML** deve conter a tabela ***SCURSO***com os campos ***CODCOLIGADA e******CODCURSO*** como informações da chave para a atualização do cadastro de curso.

xmlExemplo de XML para alteração de informações do Cursotrue

EduCursoData



1
3-13
ENGENHARIA PRODUÇÃO
 
 
1

1
3-13
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1;CODSISTEMA=S
]]>xmlExemplo do retorno da alteração de Cursotrue1;3-13
]]>

Caso a alteração seja realizada com sucesso, será mostrado o código da coligada e o código no item **SaveRecordResult.**

## Método DeleteRecord

Este método realiza a exclusão de um Curso. Algumas informações são obrigatórias e devem ser informadas: o código da coligada, o codigo do curso e os outros campos que estão configurados como obrigatórios no sistema.

O sistema irá realizar a exclusão de um Curso caso encontre o registro.

### **Exclusão de Curso**

Para realizar exclusão de um  Curso, deve ser utilizado a operação de **DeleteRecord**.

Deve ser passado um XML contendo todos os campos que fazem parte do registro de Curso.

O **XML** deve conter a tabela ***SCURSO***com os campos ***CODCOLIGADA e CODCURSO*** como informações da chave para o cadastro de Curso e, também os campos obrigatórios para seu cadastro.

xmlExemplo de XML para exclusão de um Cursotrue

EduCursoData



1
3-4
1
1
VET\_01(Excluir)\_AUTOMAÇÃO
VETERINARIA\_NOTURNO
555
1
666
1
P
1
#####

1
3-4
]]]]>
]]>xmlExemplo do retorno de exclusão de CursotrueExclusão de registro(s) realizado com sucesso
]]>

Para mais informações segue o link da documentação padrão de uso de DataServers utilizando WebService:

<http://tdn.totvs.com/x/XYlpCw>
