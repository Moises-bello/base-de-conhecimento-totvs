---
content_hash: c06880b4e924102498b0671c78e9528c252e429647adea78f9f2c6440a248c91
fetched_at: '2026-06-29T00:09:03.671549+00:00'
page_id: '382537382'
product: rm
source: tdn-rm
title: Avaliação da Etapa da Turma Disciplina
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=382537382
version: 6
---

# Visão Geral dos processos WebSevices de Avaliações

O objetivo deste DataServer é possibilitar a busca, inclusão, alteração e exclusão de Avaliação da Etapa da Turma Disciplina  através de WebService. Tudo o que for realizado, poderá ser visualizado no cadastro de uma Avaliação no TOTVS Gestão Educacional.

Através do DataServer "**EduprovasData**" e por meio dos métodos **ReadRecord, SaveRecord e DeleteRecord**, é possível realizar busca, inclusão, manutenção e exclusão das informações das Avaliações no TOTVS Gestão Educacional.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/display/LRM/Webservices)**

Índice

2

## Método ReadRecord

Este método realiza a consulta de uma Avaliação. Algumas informações são obrigatórias e devem ser informadas: o código da Coligada,  o código da Turma Disciplina, o código da Etapa e o código da Prova.

O sistema irá realizar a consulta de uma Avaliação da Etapa da Turma Disciplina caso as informações passadas estejam de acordo com alguma Avaliação já existente no sistema.

### **Consulta de uma Avaliação**

Para realizar a consulta de uma Avaliação, deve ser utilizado a operação de **ReadRecord**.

Deve ser passado um XML contendo todos os campos de chave primária.

Caso a chave informada não retorne registro, o resultado será o nome do DataSet. Caso contrário, o mesmo terá suas informações exibidas através de um XML.

O **XML** deve conter os campos ***CODCOLIGADA , IDTURMADISC, CODETAPA, TIPOETAPA e CODPROVA***como informações da chave para busca de Avaliação da Etapa da Turma Disciplina.

xmlExemplo de XML para consulta de uma Avaliaçãotrue

Eduprovasdata

1;4385;1;N;1

CODCOLIGADA=1;CODSISTEMA=S;CODUSUARIO=MESTRE
]]>xmlExemplo do retorno de consulta de uma Avaliaçãotrue


1
4385
1
N
1
Prova
90
2018-05-03T00:00:00
2018-05-03T00:00:00
50
1
Notas
N
S
N

1
4385
1
N
1
]]]]>]]>xmlExemplo do retorno sem registrostrue<EduprovasData />
]]>

## Método SaveRecord

Este método realiza a inclusão ou alteração de uma Avaliação da Etapa da Turma Disciplina. Algumas informações são obrigatórias e devem ser informadas:  o código da Coligada,  o código da Turma Disciplina, o código da Etapa e o código da Prova, além dos outros campos que estão configurados como obrigatórios no sistema.

O sistema irá realizar a inclusão de uma Avaliação, caso o código informado não exista na base.

Se o código da Avaliação existir na coligada informada, essa terá as informações alteradas de acordo com o que será passado no arquivo XML.

***Observação***: Caso sejam passadas para o DataServer informações para **campos complementares**, devem ser utilizados os mesmos códigos obrigatórios para que o sistema consiga entender que se referem a Avaliação que se deseja alterar.

### **Inclusão de uma Avaliação da Etapa da Turma Disciplina**

Para realizar inclusão de um Avaliação, deve ser utilizado a operação de **SaveRecord**.

Deve ser passado um XML contendo todos os campos que serão cadastrados, como informação para a Avaliação.

Caso o código da Avaliação informado não exista, será incluído uma nova Avaliação. Caso contrário, o mesmo terá suas informações atualizadas.

O **XML** deve conter a tabela ***SPROVAS***com os campos ***CODCOLIGADA , IDTURMADISC, CODETAPA, TIPOETAPA e CODPROVA***como informações da chave para o cadastro da Avaliação da Etapa da Turma Disciplina, também os campos obrigatórios para seu cadastro.

xmlExemplo de XML para inclusão de uma Avaliaçãotrue

Eduprovasdata



1
4385
1
N
5
Prova
90
2018-05-03T00:00:00
2018-05-03T00:00:00
50
1
Notas
N
S
N

1
4385
1
N
5
]]]]>

CODCOLIGADA=1;CODSISTEMA=S;CODUSUARIO=MESTRE;CODTIPOCURSO=1;CODFILIAL=1
]]>xmlExemplo do retorno da inclusão de uma Avaliaçãotrue1;4385;1;N;5
]]>

Caso a inclusão seja realizada com sucesso, será mostrado o código da coligada, o código da Turma Disciplina, o código da Etapa, tipo da Etapa e o código da Prova da Avaliação inserido no item ***SaveRecordResult.***

### **Alteração de uma Avaliação**

Para realizar alteração de uma Avaliação, deve ser utilizado a operação de **SaveRecord**.

Deve ser passado um XML contendo todos os campos que serão atualizados no cadastro de Avalição;

O **XML** deve conter a tabela ***SPROVAS***com os campos ***CODCOLIGADA , IDTURMADISC, CODETAPA, TIPOETAPA e CODPROVA***como informações da chave para a atualização do cadastro de uma avaliação.

xmlExemplo de XML para alteração de informações de uma Avaliaçãotrue

Eduprovasdata



1
4385
1
N
5
Prova
100
2018-05-03T00:00:00
2018-05-03T00:00:00
50
1
Notas
N
S
N

1
4385
1
N
5
]]]]>

CODCOLIGADA=1;CODSISTEMA=S;CODUSUARIO=MESTRE;CODTIPOCURSO=1;CODFILIAL=1
]]>xmlExemplo do retorno da alteração de uma Avaliaçãotrue1;4385;1;N;1
]]>

Caso a alteração seja realizada com sucesso, será mostrado o código da coligada e o código no item **SaveRecordResult.**

## Método DeleteRecord

Este método realiza a exclusão de uma Avaliação. Algumas informações são obrigatórias e devem ser informadas:  o código da coligada, o código da Turma Disciplina, o código da Etapa, tipo da Etapa e o código da Prova da Avaliação e os outros campos que estão configurados como obrigatórios no sistema.

O sistema irá realizar a exclusão da Avaliação caso encontre o registro.

### **Exclusão da Avaliação**

Para realizar exclusão de uma Avaliação, deve ser utilizado a operação de **DeleteRecord**.

Deve ser passado um XML contendo todos os campos que fazem parte do registro de uma Avaliação.

O **XML** deve conter a tabela ***SPROVAS***com os campos ***CODCOLIGADA , IDTURMADISC, CODETAPA, TIPOETAPA e CODPROVA***como informações da chave para a atualização do cadastro de avaliação.

xmlExemplo de XML para exclusão de uma Avaliaçãotrue

EduprovasData



1
4390
1
N
1
Avaliação
100
70
Notas
N
N
N

1
4390
1
N
1
]]]]>
]]>xmlExemplo do retorno de exclusão de uma AvaliaçãotrueExclusão de registro(s) realizado com sucesso
]]>

Para mais informações segue o link da documentação padrão de uso de DataServers utilizando WebService:

<http://tdn.totvs.com/x/XYlpCw>
