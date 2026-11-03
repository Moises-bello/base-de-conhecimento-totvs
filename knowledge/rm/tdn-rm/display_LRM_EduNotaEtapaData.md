---
content_hash: 046f8a7722ca41137f48cad5f29240cedff14eacf58456e3f13eab35de96d01f
fetched_at: '2026-06-29T00:08:58.807590+00:00'
page_id: '361442967'
product: rm
source: tdn-rm
title: EduNotaEtapaData
type: documentation
url: https://tdn.totvs.com/display/LRM/EduNotaEtapaData
version: 11
---

# Visão Geral dos processos WebSevices da Nota/Falta de Etapa

O objetivo deste DataServer é possibilitar a busca, inclusão e alteração de notas/faltas de etapa através de WebService. Tudo o que for realizado, poderá ser visualizado no menu de notas e faltas de etapa no TOTVS Gestão Educacional.

Através do dataserver "**EduNotaEtapaData**" e por meio dos métodos **ReadRecord e SaveRecord**, é possível realizar busca, inclusão e manutenção das informações de notas/faltas de etapa no TOTVS Gestão Educacional.

Vale lembrar que **este dataserver será descontinuado. Para isso pode-se usar o [EduAlunoEtapaData](http://tdn.totvs.com/display/LRM/EduAlunoEtapaData).**

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/display/LRM/Webservices)**

Índice

2

**Caso o usuário informado na autenticação, não possua permissão ao menu, o processo não poderá ser executado.**

O caminho da permissão, para que o usuário realize o processo, é: **Matrícula e Avaliação | Mais | Digitação por Aluno | Notas e Faltas de Etapa ou Matrícula e Avaliação | Notas e Faltas de Etapa.**

## Método ReadRecord

Este método realiza a consulta de uma nota/falta de etapa. Algumas informações são obrigatórias e devem ser informadas: o código da coligada, código da etapa, tipo da etapa, id da turma disciplina e registro acadêmico do aluno.

O sistema irá realizar a consulta da nota/falta de etapa, caso as informações passadas estejam de acordo com alguma nota/falta de etapa já existente no sistema.

### **Consulta da nota/falta de etapa**

Para realizar a consulta de uma nota/falta de etapa, deve ser utilizado a operação de **ReadRecord**.

Deve ser passado um XML contendo todos os campos de chave primária.

Caso a chave informada não retorne registro, o resultado será o nome do DataSet. Caso contrário, a mesma terá suas informações exibidas através de um XML.

O **XML** deve conter os campos ***CODCOLIGADA, CODETAPA, TIPOETAPA, IDTURMADISC e******RA*** como informações da chave para busca da nota/falta de etapa.

Para realizar a consulta de uma falta, deve-se informar o **TIPOETAPA** como "F".

xmlExemplo de XML para consulta de uma nota/falta de etapatrue

EduNotaEtapaData

1;1;N;4390;MFA2018

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1
]]>xmlExemplo do retorno de consulta da nota/falta de etapatrue

1
1
N
4390
MFA2018
80
]]]]>
]]>xmlExemplo do retorno sem registrostrue<EduNotaEtapa />
]]>

## Método SaveRecord

Este método realiza a inclusão ou alteração de uma nota/falta de etapa. Algumas informações são obrigatórias e devem ser informadas: o código da coligada, código da etapa, tipo da etapa, id da turma disciplina e registro acadêmico, além dos outros campos que estão configurados como obrigatórios no sistema.

O sistema irá realizar a inclusão de uma nota/falta de etapa, caso as informações passadas não exista na base.

Se houver um registro já existente com as informações informadas na chave, esse será alterado de acordo com os dados passados no arquivo XML.

### **Inclusão da nota/falta de etapa**

Para realizar inclusão de uma nota/falta de etapa, deve ser utilizado a operação de **SaveRecord**.

Deve ser passado um XML contendo todos os campos que serão cadastrados, como informação, para a nota/falta de etapa.

Se houver um registro já existente com as informações informadas na chave, esse será alterado de acordo com os dados passados.

O **XML** deve conter a tabela ***SNOTAETAPA***com os campos ***CODCOLIGADA, CODETAPA, TIPOETAPA, IDTURMADISC e******RA*** como informações da chave para o cadastro da nota/falta de etapa e, também, os campos obrigatórios para seu cadastro.

Para realizar a inclusão de uma falta, deve-se informar o **TIPOETAPA** como "F".

xmlExemplo de XML para inclusão de uma nota/falta de etapatrue

EduNotaEtapaData



1
1
N
4390
MFA2018
80
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1
]]>xmlExemplo do retorno da inclusão da nota/falta de etapatrue1;1;N;4390;MFA2018]]>

Caso a inclusão seja realizada com sucesso, será mostrado o código da coligada, código da etapa, o tipo da etapa, o id da turma disciplina e o registro acadêmico inserido no item ***SaveRecordResult.***

### **Alteração da nota/falta de etapa**

Para realizar alteração de uma nota/falta de etapa, deve ser utilizado a operação de **SaveRecord**.

Deve ser passado um XML contendo todos os campos que serão atualizados no cadastro da nota/falta de etapa.

O **XML** deve conter a tabela ***SNOTAETAPA***com os campos ***CODCOLIGADA, CODETAPA, TIPOETAPA, IDTURMADISC e******RA*** como informações da chave para o cadastro da nota/falta de etapa e, também, os campos obrigatórios para seu cadastro.

Para realizar a alteração de uma falta, deve-se informar o **TIPOETAPA** como "F".

xmlExemplo de XML para alteração de informações da nota/falta de etapatrue

EduNotaEtapaData



1
1
N
4390
MFA2018
70
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1
]]>xmlExemplo do retorno da alteração do cadastro da nota/falta de etapatrue1;8001408
]]>

Caso a inclusão seja realizada com sucesso, será mostrado o código da coligada, código da etapa, o tipo da etapa, o id da turma disciplina e o registro acadêmico inserido no item ***SaveRecordResult.***
