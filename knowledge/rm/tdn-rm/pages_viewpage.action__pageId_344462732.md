---
content_hash: aabc8630b7d49c3540e9b40fe2a20fe118793e3a4b6f5ff0ffaab865a241e3fb
fetched_at: '2026-06-29T00:08:53.207913+00:00'
page_id: '344462732'
product: rm
source: tdn-rm
title: Turmas (WebService)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=344462732
version: 29
---

# Visão Geral dos processos WebSevices da Turma

O objetivo deste DataServer é possibilitar a busca, inclusão, alteração e exclusão de turmas através de WebService. Tudo o que for realizado, poderá ser visualizado no cadastro de turma no TOTVS Gestão Educacional.

Através do dataserver "**EduTurmaData**" e por meio dos métodos **ReadRecord, SaveRecord e DeleteRecord**, é possível realizar busca, inclusão, manutenção e exclusão das informações das Turmas no TOTVS Gestão Educacional.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/display/LRM/Webservices)**

Índice

2

## Método ReadRecord

Este método realiza a consulta de uma turma. Algumas informações são obrigatórias e devem ser informadas: o código da coligada, o código da filial, o id do período letivo, o código da turma.

O sistema irá realizar a consulta de uma turma caso as informações passadas estejam de acordo com alguma turma já existente no sistema.

### **Consulta da turma**

Para realizar a consulta de uma turma, deve ser utilizado a operação de **ReadRecord**.

Deve ser passado um XML contendo todos os campos de chave primária.

Caso a chave informada não retorne registro, o resultado será o nome do DataSet. Caso contrário, a mesma terá suas informações exibidas através de um XML.

O **XML** deve conter os campos ***CODCOLIGADA**,****CODFILIAL, IDPERLET e CODTURMA*** como informações da chave para busca da turma.

xmlExemplo de XML para consulta de uma Turmatrue

EduTurmaData

1;1;98;Turma B

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=3;CODSISTEMA=S;
]]>xmlExemplo do retorno de consulta da Turmatrue

1
1
98
Turma B
403
ADS-A
Análise e Desenvolvimento de Sofware - Turma A
100
2018-01-01T00:00:00
2018-12-31T00:00:00
3
ADS
1
1
2018/01
2017-01-01T00:00:00
Análise e Desenvolvimento de Software
Bacharelado
Tecnologia da Informação
Matutino
0

1
1
98
Turma B
]]]]>
]]>xmlExemplo do retorno sem registrostrue<EduTurma />
]]>

## Método SaveRecord

Este método realiza a inclusão ou alteração de uma turma. Algumas informações são obrigatórias e devem ser informadas: o código da coligada, o código da filial, o id do período letivo, o código da turma, além dos outros campos que estão configurados como obrigatórios no sistema.

O sistema irá realizar a inclusão de uma turma, caso o código informado não exista na base.

Se o código da turma existir na coligada informada, essa terá as informações alteradas de acordo com o que será passado no arquivo XML.

***Observação***: Caso sejam passadas para o dataserver informações para **campos complementares**, devem ser utilizados os mesmos códigos obrigatórios para que o sistema consiga entender que se referem à turma que se deseja alterar.

### **Inclusão da turma**

Para realizar inclusão de uma turma, deve ser utilizado a operação de **SaveRecord**.

Deve ser passado um XML contendo todos os campos que serão cadastrados, como informação, para a turma.

Caso o código e turma informada não exista, será incluída uma nova turma. Caso contrário, a mesma terá suas informações atualizadas.

O **XML** deve conter a tabela ***STURMA***com os campos ***CODCOLIGADA**,****CODFILIAL, IDPERLET e CODTURMA*** como informações da chave para o cadastro da turma e, também, os campos obrigatórios para seu cadastro.

xmlExemplo de XML para inclusão de uma Turmatrue

EduTurmaData



1
1
98
Turma B
403
ADS-A
Análise e Desenvolvimento de Sofware - Turma A
100
2018-01-01T00:00:00
2018-12-31T00:00:00
3
ADS
1
1
2018/01
2017-01-01T00:00:00
Análise e Desenvolvimento de Software
Bacharelado
Tecnologia da Informação
Matutino
0

1
1
98
Turma B
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=3;CODSISTEMA=S;
]]>xmlExemplo do retorno da inclusão da Turmatrue1;1;98;Turma B]]>

Caso a inclusão seja realizada com sucesso, será mostrado o código da coligada, o código da filial, o id do período letivo e o código da turma inserido no item ***SaveRecordResult.***

### **Alteração de Turmas**

Para realizar alteração de uma turma, deve ser utilizado a operação de **SaveRecord**.

Deve ser passado um XML contendo todos os campos que serão atualizados no cadastro da turma.

O **XML** deve conter a tabela ***STURMA***com os campos ***CODCOLIGADA**,****CODFILIAL, IDPERLET e CODTURMA*** como informações da chave para a atualização do cadastro da turma.

xmlExemplo de XML para alteração de informações da Turmatrue

EduTurmaData



1
1
98
Turma B
403
ADS-A
Análise e Desenvolvimento de Sofware - Turma A
99
2018-01-01T00:00:00
2018-12-31T00:00:00
3
ADS
1
1
2018/01
2017-01-01T00:00:00
Análise e Desenvolvimento de Software
Bacharelado
Tecnologia da Informação
Matutino
0

1
1
98
Turma B
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=3;CODSISTEMA=S;
]]>xmlExemplo do retorno da alteração do cadastro da Turmatrue1;1;98;Turma B]]>

Caso a alteração seja realizada com sucesso, será mostrado o código da coligada e o código do professor no item **SaveRecordResult.**

## Método DeleteRecord

Este método realiza a exclusão de uma turma. Algumas informações são obrigatórias e devem ser informadas: o código da coligada, o código da filial, o id do período letivo, o código da turma, além dos outros campos que estão configurados como obrigatórios no sistema.

O sistema irá realizar a exclusão de uma turma caso encontre o registro.

### **Exclusão da turma**

Para realizar exclusão de uma turma, deve ser utilizado a operação de **DeleteRecord**.

Deve ser passado um XML contendo todos os campos que fazem parte do registro da turma.

O **XML** deve conter a tabela ***STURMA***com os campos ***CODCOLIGADA**,****CODFILIAL, IDPERLET e CODTURMA*** como informações da chave para o cadastro da turma e, também, os campos obrigatórios para seu cadastro.

xmlExemplo de XML para exclusão de uma Turmatrue

EduTurmaData



1
1
98
Turma B
403
ADS-A
Análise e Desenvolvimento de Sofware - Turma A
100
2018-01-01T00:00:00
2018-12-31T00:00:00
3
ADS
1
1
2018/01
2017-01-01T00:00:00
Análise e Desenvolvimento de Software
Bacharelado
Tecnologia da Informação
Matutino
0

1
1
98
Turma B
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=3;CODSISTEMA=S;
]]>xmlExemplo do retorno de exclusão da TurmatrueExclusão de registro(s) realizado com sucesso]]>

Para mais informações segue o link da documentação padrão de uso de DataServers utilizando WebService:

<http://tdn.totvs.com/x/XYlpCw>
