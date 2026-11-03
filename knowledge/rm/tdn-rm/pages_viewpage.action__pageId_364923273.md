---
content_hash: d39e21ac2c8eb7b9cbe092e9b90a62bacc063ca6806e69c0ec04f1110d540ec8
fetched_at: '2026-06-29T00:09:00.175992+00:00'
page_id: '364923273'
product: rm
source: tdn-rm
title: Processo Seletivo Terceirizado (WebService)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364923273
version: 4
---

# Visão Geral dos processos WebSevices de Processo Seletivo Terceirizado

O objetivo deste DataServer é possibilitar a busca, inclusão e alteração candidatos através de WebService no Processo Seletivo Terceirizado. Tudo o que for realizado, poderá ser visualizado na visão de candidatos e matrículas do processo seletivo terceirizado no TOTVS Gestão Educacional.

Através do dataserver "**EduCandidatoProcSelData**" e por meio dos métodos **ReadView,****ReadRecord e SaveRecord** , é possível realizar busca, inclusão e manutenção das informações de candidatos no TOTVS Gestão Educacional.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/display/LRM/Webservices)**

Índice

2

## Método ReadView

Este método realiza a consulta de uma lista de candidatos. Algumas informações são obrigatórias e devem ser informadas: o código da coligada e o código do processo selecido.

O sistema irá realizar a consulta da lista de candidatos.

**Consulta de uma lista de candidatos**

Para realizar a consulta de uma lista de candidatos, deve ser utilizado a operação de **ReadView**.

Deve ser passado um XML contendo todos os campos de filtro.

O **XML** deve conter os campos ***SCANDIDATOPROCSEL.CODCOLIGADA******e SCANDIDATOPROCSEL.IDPROCSEL*** como informações da filtro para busca da lista.

xmlExemplo de XML para consulta de uma lista de candidatostrue

EduCandidatoProcSelData

SCANDIDATOPROCSEL.CODCOLIGADA = 1 AND SCANDIDATOPROCSEL.IDPROCSEL = 8

CODCOLIGADA=1;CODFILIAL=1;CODSISTEMA=S;CODTIPOCURSO=1
]]>xmlExemplo de retorno da lista de candidatostrue

1
8
1
Aluno Proc Terceirizado Um
1987-07-30T00:00:00
Belo Horizonte
MG
Pai Proc Terceirizado Um
Mãe Proc Terceirizado Um
ES-00213
2018-04-04T00:00:00
1951-07-30T00:00:00
1951-07-30T00:00:00
Belo Horizonte
Belo Horizonte
MG
MG

1
8
2
Aluno Proc Terceirizado Dois
1987-07-29T00:00:00
Belo Horizonte
MG
Pai Proc Terceirizado Dois
Mãe Proc Terceirizado Dois
ES-00212
2018-04-04T00:00:00
1951-07-30T00:00:00
1951-07-30T00:00:00
Belo Horizonte
Belo Horizonte
MG
MG

1
8
1
23
1
1
100.0000
1
9
Teste
ProcTeste0001
2018/1
S

1
8
2
23
1
1
100.0000
2
9
Teste
ProcTeste0001
2018/1
S
]]]]>
]]>

## Método ReadRecord

Este método realiza a consulta de um candidato. Algumas informações são obrigatórias e devem ser informadas: o código da coligada, o código do processo seletivo e o número da inscrição.

O sistema irá realizar a consulta de candidato, caso as informações passadas estejam de acordo com algum candidato já existente no sistema.

**Consulta de Candidatos**

Para realizar a consulta de um candidato, deve ser utilizado a operação de **ReadRecord**.

Deve ser passado um XML contendo todos os campos de chave primária.

Caso a chave informada não retorne registro, o resultado será o nome do DataSet. Caso contrário, a mesma terá suas informações exibidas através de um XML.

O **XML** deve conter os campos ***CODCOLIGADA,******IDPROCSEL e o NUMEROINSCPROCSEL***como informações da chave para busca do candidato.

xmlExemplo de XML para consulta de um Candidatotrue

EduCandidatoProcSelData

1;8;1

CODCOLIGADA=1;CODFILIAL=1;CODSISTEMA=S;CODTIPOCURSO=1
]]>xmlExemplo do retorno de consulta de um Candidatotrue

1
8
1
Aluno Proc Terceirizado Um
1987-07-30T00:00:00
Belo Horizonte
MG
Pai Proc Terceirizado Um
Mãe Proc Terceirizado Um
ES-00213
2018-04-04T00:00:00
1951-07-30T00:00:00
1951-07-30T00:00:00
Belo Horizonte
Belo Horizonte
MG
MG

1
23
8
1
1
1
100.0000
1
9
Teste
ProcTeste0001
2018/1
S
]]]]>
]]>xmlExemplo do retorno sem registrostrue<EduCandidatoProcSel />
]]>

## Método SaveRecord

Este método realiza a inclusão ou alteração de um candidato.

O sistema irá realizar a inclusão de um candidato, caso o código informado não exista na base.

### **Inclusão de Candidato**

Para realizar inclusão de um candidato, deve ser utilizado a operação de **SaveRecord**.

Deve ser passado um XML contendo todos os campos que serão cadastrados, como informação, para o candidato.

Caso os dados informados não existam, será incluído um novo candidato. Caso contrário, o mesmo terá suas informações atualizadas.

O **XML** deve conter a tabela ***SCANDIDATOPROCSEL**  e **SOPCAOCANDIDATO***com os campos ***CODCOLIGADA, IDPROCSEL******e NUMEROINSCPROCSEL*** como informações da chave para o cadastro de candidatos.

xmlExemplo de XML para inclusão de um Candidatotrue

EduCandidatoProcSelData



1
8
3
Aluno Proc Terceirizado Três
1987-07-30T00:00:00
Belo Horizonte
MG
Pai Proc Terceirizado Três
Mãe Proc Terceirizado Três
1951-07-30T00:00:00
1951-07-30T00:00:00
Belo Horizonte
Belo Horizonte
MG
MG

1
23
8
3
1
1
100.0000
1
9
Teste
ProcTeste0001
2018/1
S
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODSISTEMA=S
]]>xmlExemplo do retorno da inclusão de um Candidatotrue1;8;3]]>

Caso a inclusão seja realizada com sucesso, será mostrado o código da coligada, o código do processo seletivo e o número de inscrição inserido no item ***SaveRecordResult.***

### **Alteração de um Candidato**

Para realizar alteração de um candidato, deve ser utilizado a operação de **SaveRecord**.

Deve ser passado um XML contendo todos os campos que serão atualizados no cadastro de candidatos.

O **XML** deve conter a tabela ***SCANDIDATOPROCSEL**  e **SOPCAOCANDIDATO***com os campos ***CODCOLIGADA, IDPROCSEL******e NUMEROINSCPROCSEL*** como informações da chave para o cadastro de candidatos.

xmlExemplo de XML para alteração de informações de um Candidatotrue

EduCandidatoProcSelData



1
8
3
Aluno Proc Terceirizado Três
1987-07-30T00:00:00
Belo Horizonte
MG
Pai Proc Terceirizado Três
Mãe Proc Terceirizado Três
1951-07-30T00:00:00
1951-07-30T00:00:00
Belo Horizonte
Belo Horizonte
MG
MG

1
23
8
3
1
1
100.0000
1
9
Teste
ProcTeste0001
2018/1
S
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODSISTEMA=S
]]>xmlExemplo do retorno da alteração do cadastro de um Candidatotrue1;8;3
]]>

Caso a inclusão seja realizada com sucesso, será mostrado o código da coligada, o código do processo seletivo e o número de inscrição inserido no item ***SaveRecordResult.***
