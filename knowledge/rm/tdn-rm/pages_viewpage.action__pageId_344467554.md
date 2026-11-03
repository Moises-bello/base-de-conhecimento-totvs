---
content_hash: b6477e3bfa50b9a2179fb812958a135f05ad452340139d88d79baf138ebc95bc
fetched_at: '2026-06-29T00:08:53.307602+00:00'
page_id: '344467554'
product: rm
source: tdn-rm
title: Curso\Habilitações (WebService)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=344467554
version: 5
---

# Visão Geral dos processos WebSevices de Curso\Habilitações

O objetivo deste DataServer é possibilitar a busca, inclusão, alteração e exclusão de Curso\Habilitação através de WebService. Tudo o que for realizado, poderá ser visualizado no cadastro de Curso\Habilitação no TOTVS Gestão Educacional.

Através do DataServer "**EduHabilitacaoData**" e por meio dos métodos **ReadRecord, SaveRecord e DeleteRecord**, é possível realizar busca, inclusão, manutenção e exclusão das informações de Curso\Habilitação no TOTVS Gestão Educacional.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/display/LRM/Webservices)**

Índice

2

## Método ReadRecord

Este método realiza a consulta de um Curso\Habilitação. Algumas informações são obrigatórias e devem ser informadas: o código da coligada, código do Curso e o Código da Habilitação.

O sistema irá realizar a consulta de um Curso\Habilitação, caso as informações passadas estejam de acordo com algum Curso\Habilitação já existente no sistema.

### **Consulta do Curso\Habilitação**

Para realizar a consulta de um Curso\Habilitação, deve ser utilizado a operação de **ReadRecord**.

Deve ser passado um XML contendo todos os campos de chave primária.

Caso a chave informada não retorne registro, o resultado será o nome do DataSet. Caso contrário, a mesma terá suas informações exibidas através de um XML.

O **XML** deve conter os campos ***CODCOLIGADA, CODCURSO e CODHABILITACAO***como informações da chave para busca de Curso\Habilitação.

xmlExemplo de XML para consulta de um Curso\Habilitaçãotrue

EduHabilitacaoData

1;3-7;1

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1
]]>xmlExemplo do retorno de consulta de Curso\Habilitaçãotrue


1
3-7
1
ENGENHARIA01\_AUTOMAÇÃO
 
 
2
0

1
3-7
1
]]]]>
]]>xmlExemplo do retorno sem registrostrue<EduHabilitacaoData />
]]>

## Método SaveRecord

Este método realiza a inclusão ou alteração de um Curso\Habilitação. Algumas informações são obrigatórias e devem ser informadas: o código da coligada, o código do Curso e o código da Habilitação, além dos outros campos que estão configurados como obrigatórios no sistema.

O sistema irá realizar a inclusão de um Curso\Habilitação, caso o código informado não exista na base.

Se o código do Curso\Habilitação existir na coligada informada, essa terá as informações alteradas de acordo com o que será passado no arquivo XML.

***Observação***: Caso sejam passadas para o DataServer informações para **campos complementares**, devem ser utilizados os mesmos códigos obrigatórios para que o sistema consiga entender que se referem ao Curso\Habilitação que se deseja alterar.

### **Inclusão de Curso\Habilitação**

Para realizar inclusão de um Curso\Habilitação, deve ser utilizado a operação de **SaveRecord**.

Deve ser passado um XML contendo todos os campos que serão cadastrados, como informação para o Curso\Habilitação.

Caso o código do Curso\Habilitaçãco informado não exista, será incluída um novo Curso\Habilitaçãoo. Caso contrário, o mesmo terá suas informações atualizadas.

O **XML** deve conter a tabela ***SHABILITACAO***com os campos ***CODCOLIGADA,******CODCURSO e o CODHABILITACAO***como informações da chave para o cadastro de Curso\Habilitação, também os campos obrigatórios para seu cadastro.

xmlExemplo de XML para inclusão de um Curso\Habilitaçãotrue

EduHabilitacaoData



1
3-7
1
ENGENHARIA01\_AUTOMAÇÃO
 
 
2
0

1
3-7
1
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1;CODSISTEMA=S
]]>xmlExemplo do retorno da inclusão de Curso\Habilitaçãotrue1;3-7;1
]]>

Caso a inclusão seja realizada com sucesso, será mostrado o código da coligada, o Código do Curso e o Código da Habilitação inserido no item ***SaveRecordResult.***

### **Alteração de Curso\Habilitação**

Para realizar alteração de um Curso\Habilitação, deve ser utilizado a operação de **SaveRecord**.

Deve ser passado um XML contendo todos os campos que serão atualizados no cadastro de Curso\Habilitação;

O **XML** deve conter a tabela ***SHABILITACAO***com os campos ***CODCOLIGADA,******CODCURSO e o CODHABILITACAO***como informações da chave para a atualização do cadastro de Curso\Habilitação.

xmlExemplo de XML para alteração de informações do Curso\Habilitaçãotrue

EduHabilitacaoData



1
3-2
1
ADM\_EMPR\_ADM01
 
 
2
0

1
3-2
1
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1;CODSISTEMA=S
]]>xmlExemplo do retorno da alteração de Curso\Habilitaçãotrue1;3-2;1
]]>

Caso a alteração seja realizada com sucesso, será mostrado o código da coligada e o código no item **SaveRecordResult.**

## Método DeleteRecord

Este método realiza a exclusão de um Curso\Habilitação. Algumas informações são obrigatórias e devem ser informadas: o código da coligada, o codigo do curso e os outros campos que estão configurados como obrigatórios no sistema.

O sistema irá realizar a exclusão de um Curso\Habilitação caso encontre o registro.

### **Exclusão de Curso\Habilitação**

Para realizar exclusão de um  Curso\Habilitação, deve ser utilizado a operação de **DeleteRecord**.

Deve ser passado um XML contendo todos os campos que fazem parte do registro de Curso\Habilitação.

O **XML** deve conter a tabela ***SHABILITACAO***com os campos ***CODCOLIGADA,******CODCURSO e o CODHABILITACAO*** como informações da chave para o cadastro de Curso\Habilitação e também os campos obrigatórios para seu cadastro.

xmlExemplo de XML para exclusão de um Curso\Habilitaçãotrue

EduHabilitacaoData



1
3-7
1
ENGENHARIA01\_AUTOMAÇÃO
 
 
2
0

1
3-7
1
]]]]>
]]>xmlExemplo do retorno de exclusão de Curso\HabilitaçãotrueExclusão de registro(s) realizado com sucesso
]]>

Para mais informações segue o link da documentação padrão de uso de DataServers utilizando WebService:

<http://tdn.totvs.com/x/XYlpCw>
