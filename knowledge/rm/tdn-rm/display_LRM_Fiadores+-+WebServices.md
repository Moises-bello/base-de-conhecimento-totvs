---
content_hash: d5f774fe9a35cf38ea59c00d9a1e2ca47de35e1a4f4d9b0a0aab5320b864e712
fetched_at: '2026-06-29T00:11:32.810670+00:00'
page_id: '749075197'
product: rm
source: tdn-rm
title: Fiadores - WebServices
type: documentation
url: https://tdn.totvs.com/display/LRM/Fiadores+-+WebServices
version: 9
---

# Visão Geral dos processos WebServices de Fiadores

O objetivo deste DataServer é possibilitar a busca, inclusão, alteração e exclusão de fiadores através de WebService. Tudo o que for realizado, poderá ser visualizado no cadastro de fiadores no TOTVS Gestão Educacional.

Através do dataserver "**EduFiadorData**" e por meio dos métodos **ReadRecord, SaveRecord e DeleteRecord**, é possível realizar busca, inclusão, manutenção e exclusão das informações de fiadores no TOTVS Gestão Educacional.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/display/LRM/Webservices)**

Índice

2

## Método ReadRecord

Este método realiza a consulta de um fiador. Algumas informações são obrigatórias e devem ser informadas: o código da coligada e o código do fiador.

O sistema irá realizar a consulta de fiador, caso as informações passadas estejam de acordo com algum fiador já existente no sistema.

### **Consulta de fiador**

Para realizar a consulta de um fiador, deve ser utilizado a operação de **ReadRecord**.

Deve ser passado um XML contendo todos os campos de chave primária.

Caso a chave informada não retorne registro, o resultado será o nome do DataSet. Caso contrário, a mesma terá suas informações exibidas através de um XML.

O **XML** deve conter os campos ***CODCOLIGADA******e IDFIADOR*** como informações da chave para busca do fiador.

xmlExemplo de XML para consulta de um Fiadortrue

EduFiadorData

1;33

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1
]]>xmlExemplo do retorno de consulta de Fiadortrue

1
33
LFS-0020
1
C01893
23
4-1
1
3
V
S
4-1-1
]]]]> ]]>xmlExemplo do retorno sem registrostrue ]]>

## Método SaveRecord

Este método realiza a inclusão ou alteração de um fiador. Algumas informações são obrigatórias e devem ser informadas: o código da coligada e o código do fiador, além dos outros campos que estão configurados como obrigatórios no sistema.

O sistema irá realizar a inclusão de um fiador, caso o código do fiador informado no XML seja igual a zero. O valor do código do fiador presente no XML serve apenas para identificar o fiador dentro do próprio XML. O sistema irá criar um código para o fiador inserido.

Se o código do fiador existir na coligada informada, essa terá as informações alteradas de acordo com o que será passado no arquivo XML.

***Observação:***

* No campo **Status** só pode receber um dos valores V - Avaliação, A - Aprovado, e R - Reprovado
* No campo **Ativo** só pode receber um dos valores S - Ativo, e N - Inativo.

### **Inclusão de fiador**

Para realizar inclusão de um fiador, deve ser utilizado a operação de **SaveRecord**.

Deve ser passado um XML contendo todos os campos que serão cadastrados, como informação, para o fiador.

Caso o Código do Fiador informado exista as informações serão atualizadas.

O **XML** deve conter a tabela ***SFIADOR***com os campos ***CODCOLIGADA*** ***e IDFIADOR*** como informações da chave para o cadastro de fiador e, também, os campos obrigatórios para seu cadastro.

xmlExemplo de XML para inclusão de um Fiadortrue

EduFiadorData


1
0
LFS-0020
Carolina Maria Souza
1
C01893
LFS Aluno 1 Agrupamento
23
4-1
ENGENHARIA DE SOFTWARE
4-1-1
TECNÓLOGO EM ANÁLISE DE SISTEMAS
1
Habilitação 2009/1
3
NOITE
V
S
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1
]]>xmlExemplo do retorno da inclusão de Fiadortrue1;33]]>

Caso a inclusão seja realizada com sucesso, será mostrado o código da coligada e o código do fiador inserido no item ***SaveRecordResult.***

### **Alteração de fiador**

Para realizar alteração de um fiador, deve ser utilizado a operação de **SaveRecord**.

Deve ser passado um XML contendo todos os campos que serão atualizados no cadastro de fiador.

O **XML** deve conter a tabela ***SFIADOR***com os campos ***CODCOLIGADA*** ***e IDFIADOR*** como informações da chave para a atualização do cadastro de fiador.

xmlExemplo de XML para alteração de informações de Fiadortrue

EduFiadorData


1
33
LFS-0020
Carolina Maria Souza
1
C01893
LFS Aluno 1 Agrupamento
23
4-1
ENGENHARIA DE SOFTWARE
4-1-1
TECNÓLOGO EM ANÁLISE DE SISTEMAS
1
Habilitação 2009/1
3
NOITE
V
N
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1
]]>xmlExemplo do retorno da alteração do cadastro de Fiadortrue1;33 ]]>

Caso a alteração seja realizada com sucesso, será mostrado o código da coligada e o código do fiador no item **SaveRecordResult.**

## Método DeleteRecord

Este método realiza a exclusão de um fiador. Algumas informações são obrigatórias e devem ser informadas: o código da coligada e o código do fiador, além dos outros campos que estão configurados como obrigatórios no sistema.

O sistema irá realizar a exclusão de um fiador caso encontre o registro.

### **Exclusão de fiador**

Para realizar exclusão de um fiador, deve ser utilizado a operação de **DeleteRecord**.

Deve ser passado um XML contendo todos os campos que fazem parte do registro de fiador.

O **XML** deve conter a tabela ***SFIADOR*** com os campos ***CODCOLIGADA*** ***e IDFIADOR*** como informações da chave para o cadastro de fiador e, também, os campos obrigatórios para seu cadastro.

xmlExemplo de XML para exclusão de um Fiadortrue

EduFiadorData


1
33
LFS-0020
Carolina Maria Souza
1
C01893
LFS Aluno 1 Agrupamento
23
4-1
ENGENHARIA DE SOFTWARE
4-1-1
TECNÓLOGO EM ANÁLISE DE SISTEMAS
1
Habilitação 2009/1
3
NOITE
V
N
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1
]]>xmlExemplo do retorno de exclusão de FiadortrueExclusão de registro(s) realizado com sucesso]]>

Para mais informações segue o link da documentação padrão de uso de DataServers utilizando WebService:

<http://tdn.totvs.com/x/XYlpCw>
