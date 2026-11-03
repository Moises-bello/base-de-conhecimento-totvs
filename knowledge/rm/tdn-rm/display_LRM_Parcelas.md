---
content_hash: 928aeb58811aaa3b44c15b177e6ada3e1894d2da6180b3df3dc8892e466a363a
fetched_at: '2026-06-29T00:09:03.994481+00:00'
page_id: '382539102'
product: rm
source: tdn-rm
title: Parcelas
type: documentation
url: https://tdn.totvs.com/display/LRM/Parcelas
version: 2
---

# Visão Geral dos processos WebSevices de Parcelas

O objetivo deste DataServer é possibilitar a busca, inclusão, alteração e exclusão de parcelas através de WebService.

Através do dataserver "**EduParcelaData**" e por meio dos métodos **ReadRecord, SaveRecord e DeleteRecord**, é possível realizar busca, inclusão, manutenção e exclusão das informações de parcelas no TOTVS Gestão Educacional.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/display/LRM/Webservices)**

Índice

2

## Método ReadRecord

Este método realiza a consulta de uma parcela. Algumas informações são obrigatórias e devem ser informadas: o código da coligada e o identificador da parcela.

O sistema irá realizar a consulta da parcela, caso as informações passadas estejam de acordo com alguma parcela já existente no sistema.

### **Consulta de parcela**

Deve ser passado um XML contendo todos os campos de chave primária.

Caso a chave informada não retorne registro, o resultado será o nome do DataSet. Caso contrário, a mesma terá suas informações exibidas através de um XML.

O **XML** deve conter os campos ***CODCOLIGADA******e IDPARCELA*** como informações da chave para busca do aluno.

xmlExemplo de XML para consulta de uma parcelatruetrue

EduParcelaData

1;49711

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=2
]]>xmlExemplo do retorno de consulta de Parcelatrue

1
49711
JR01
3651
86
1
8
1
225.0000
2018-05-10T00:00:00
P
P
N
MN
mestre
2018-07-12T14:30:43
mestre
2018-07-12T14:30:43

1
49711
1
L02552
JR01
1
86
JULIANA DATENA PEREIRA NETA
100.0000
]]]]>
]]>xmlExemplo do retorno sem registrostrue<EduParcela />
]]>

## Método SaveRecord

Este método realiza a inclusão ou alteração de uma ou várias parcelas. Algumas informações são obrigatórias: o código da coligada e o identificador da parcela, além dos outros campos que estão configurados como obrigatórios no sistema.

O sistema irá realizar a inclusão da parcela, caso o registro  informado não exista na base. Essa identificação ocorre com base na chave primária da tabela SPARCELA: CODCOLIGADA e IDPARCELA

Se o registro informado existir na base de dados ele terá as informações alteradas de acordo com o que será passado no arquivo XML.

***Observação***:

1. No caso da inclusão de parcelas, caso seja informado mais de um registro no XML a chave primária informada deve ser diferente entre os registros. Isso se faz necessário para que o processo entenda que as informações passadas através do XML correspondem a registros diferentes

   xmlExempo do XML para inclusão de várias parcelastrue

   1
   0
   JR01
   3651
   86
   1
   7
   1
   226
   2018-05-10T00:00:00
   P
   P

   1
   1
   JR01
   3651
   86
   1
   8
   1
   227
   2018-05-10T00:00:00
   P
   P

   1
   2
   JR01
   3651
   86
   1
   9
   1
   228
   2018-06-10T00:00:00
   P
   P
   ]]>

Caso a inclusão ou alteração seja realizada com sucesso, será mostrado o código da coligada e o identificador da parcela ***SaveRecordResult.***

### Método DeleteRecord

Este método realiza a exclusão de uma ou várias parcelas. Algumas informações são obrigatórias: o código da coligada e o identificador da parcela.

Deve ser passado um XML contendo a chave primária que fazem parte do registro de parcela (CODCOLIGADA e IDPARCELA).

xmlExemplo de XML para exclusão de uma parcelatrue

EduparcelaData



1
49710

1
49711

1
49712
]]]]>

codcoligada=1;codfilial=1;codtipocurso=1
]]>xmlExemplo do retorno de exclusão de AlunotrueExclusão de registro(s) realizado com sucesso]]>

Para mais informações segue o link da documentação padrão de uso de DataServers utilizando WebService:

<http://tdn.totvs.com/x/XYlpCw>
