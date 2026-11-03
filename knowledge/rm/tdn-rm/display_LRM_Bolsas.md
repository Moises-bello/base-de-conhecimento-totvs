---
content_hash: f297b04b5ff79f25b886c7a3cfcc9e5469c7e85495a2d54f28120051149e5d0f
fetched_at: '2026-06-29T00:08:58.858530+00:00'
page_id: '361444403'
product: rm
source: tdn-rm
title: Bolsas
type: documentation
url: https://tdn.totvs.com/display/LRM/Bolsas
version: 9
---

# Visão Geral dos processos WebServices de Bolsas

O objetivo deste DataServer é possibilitar a busca, inclusão, alteração e exclusão de bolsas através de WebService. Tudo o que for realizado, poderá ser visualizado no cadastro de bolsas no TOTVS Gestão Educacional.

Através do dataserver "**EduBolsaData**" e por meio dos métodos **ReadRecord, SaveRecord e DeleteRecord**, é possível realizar busca, inclusão, manutenção e exclusão das informações de bolsas no TOTVS Gestão Educacional.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/display/LRM/Webservices)**

Índice

2

## Método ReadRecord

Este método realiza a consulta de uma bolsa. Algumas informações são obrigatórias e devem ser informadas: o código da coligada e o código da bolsa.

O sistema irá realizar a consulta de bolsa, caso as informações passadas estejam de acordo com alguma bolsa já existente no sistema.

### **Consulta de bolsa**

Para realizar a consulta de uma bolsa, deve ser utilizado a operação de **ReadRecord**.

Deve ser passado um XML contendo todos os campos de chave primária.

Caso a chave informada não retorne registro, o resultado será o nome do DataSet. Caso contrário, a mesma terá suas informações exibidas através de um XML.

O **XML** deve conter os campos ***CODCOLIGADA******e CODBOLSA*** como informações da chave para busca da bolsa.

xmlExemplo de XML para consulta de uma Bolsatrue

EduBolsaData

1;69

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1
]]>xmlExemplo do retorno de consulta de Bolsatrue

1
69
Teste Automatizado T
15.0000
1
1
0
N
S
P
S
S
S
A
N

1
69
Teste
]]]]>
]]>xmlExemplo do retorno sem registrostrue<EduBolsa />
]]>

## Método SaveRecord

Este método realiza a inclusão ou alteração de uma bolsa. Algumas informações são obrigatórias e devem ser informadas: o código da coligada e o código da bolsa, além dos outros campos que estão configurados como obrigatórios no sistema.

O sistema irá realizar a inclusão de uma bolsa, caso o código da bolsa informado no XML não exista no sistema. O valor do código da bolsa presente no XML serve apenas para identificar a bolsa dentro do próprio XML. O sistema irá criar um código para a bolsa inserida.

Se o código da bolsa existir na coligada informada, essa terá as informações alteradas de acordo com o que será passado no arquivo XML.

***Observação:*** Caso sejam passadas para o dataserver informações para **campos complementares**, devem ser utilizados os mesmos códigos obrigatórios para que o sistema consiga entender que se referem à bolsa que se deseja alterar.

### **Inclusão de bolsa**

Para realizar inclusão de uma bolsa, deve ser utilizado a operação de **SaveRecord**.

Deve ser passado um XML contendo todos os campos que serão cadastrados, como informação, para a bolsa.

Caso o Código da Bolsa informado exista as informações serão atualizadas.

O **XML** deve conter a tabela ***SBOLSA*** com os campos ***CODCOLIGADA******e CODBOLSA*** como informações da chave para o cadastro de bolsa e, também, os campos obrigatórios para seu cadastro.

xmlExemplo de XML para inclusão de uma Bolsatrue

EduBolsaData



1
68

Teste Automatizado T
15
1



1

0
N
S
P
S


S
S



A
N

1
68
Teste
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1
]]>xmlExemplo do retorno da inclusão de Bolsatrue1;78]]>

Caso a inclusão seja realizada com sucesso, será mostrado o código da coligada e o código da bolsa inserido no item ***SaveRecordResult.***

### **Alteração de bolsa**

Para realizar alteração de uma bolsa, deve ser utilizado a operação de **SaveRecord**.

Deve ser passado um XML contendo todos os campos que serão atualizados no cadastro de bolsa.

O **XML** deve conter a tabela ***SBOLSA*** com os campos ***CODCOLIGADA******e CODBOLSA*** como informações da chave para a atualização do cadastro de bolsa.

xmlExemplo de XML para alteração de informações de Bolsatrue

EduBolsaData



1
78

Teste Automatizado
20
1



1

0
N
S
P
S


S
S



A
N

1
78
Teste
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1
]]>xmlExemplo do retorno da alteração do cadastro de Bolsatrue1;78
]]>

Caso a alteração seja realizada com sucesso, será mostrado o código da coligada e o código da bolsa no item **SaveRecordResult.**

## Método DeleteRecord

Este método realiza a exclusão de uma bolsa. Algumas informações são obrigatórias e devem ser informadas: o código da coligada e o código da bolsa, além dos outros campos que estão configurados como obrigatórios no sistema.

O sistema irá realizar a exclusão de uma bolsa caso encontre o registro.

### **Exclusão de bolsa**

Para realizar exclusão de uma bolsa, deve ser utilizado a operação de **DeleteRecord**.

Deve ser passado um XML contendo todos os campos que fazem parte do registro de bolsa.

O **XML** deve conter a tabela ***SBOLSA*** com os campos ***CODCOLIGADA******e CODBOLSA*** como informações da chave para o cadastro de bolsa e, também, os campos obrigatórios para seu cadastro.

xmlExemplo de XML para exclusão de uma Bolsatrue

EduBolsaData




1
78

Teste Automatizado T
15
1



1

0
N
S
P
S


S
S



A
N
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1
]]>xmlExemplo do retorno de exclusão de BolsatrueExclusão de registro(s) realizado com sucesso]]>

Para mais informações segue o link da documentação padrão de uso de DataServers utilizando WebService:

<http://tdn.totvs.com/x/XYlpCw>
