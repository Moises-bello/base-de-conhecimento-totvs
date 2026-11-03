---
content_hash: 45cbeab7bfee4724a6cdf0e97e78ac8d045b8887b2adb0dd897de09cbf5c499e
fetched_at: '2026-06-29T00:09:11.613040+00:00'
page_id: '412884170'
product: rm
source: tdn-rm
title: Avaliação Descritiva (WebService)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=412884170
version: 2
---

# Visão Geral dos processos WebSevices de Alunos

O objetivo deste DataServer é possibilitar a busca e exclusão de alunos através de WebService. Tudo o que for realizado, poderá ser visualizado no cadastro de avaliações descritivas no TOTVS Gestão Educacional.

Através do dataserver "**EduExecAvalDescritivaData**" e por meio dos métodos **ReadRecord e DeleteRecord**, é possível realizar busca e exclusão das informações de avaliações descritivas cadastradas no TOTVS Gestão Educacional.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/display/LRM/Webservices)**

Índice

2

## Método ReadRecord

Este método realiza a consulta de uma avaliação descritiva. Algumas informações são obrigatórias e devem ser informadas: o código da coligada, o id da turma disciplina, o código da etapa, o tipo da etapa, o código da prova, o id interno da prova e o código pessoa do aluno.

O sistema irá realizar a consulta da avaliação descritiva, caso as informações passadas estejam de acordo com alguma avaliação já existente no sistema.

### **Consulta de aluno**

Para realizar a consulta de uma avaliação descritiva, deve ser utilizado a operação de **ReadRecord**.

Deve ser passado um XML contendo todos os campos de chave primária.

Caso a chave informada não retorne registro, o resultado será o nome do DataSet. Caso contrário, a mesma terá suas informações exibidas através de um XML.

O **XML** deve conter os campos ***CODCOLIGADA, IDTURMADISC, CODETAPA, TIPOETAPA, CODPROVA, ID e CODPESSOA***como informações da chave para busca da avaliação.

xmlExemplo de XML para consulta de uma Avaliação Descritivatrue

EduExecAvalDescritivaData

1;4632;1;N;1;23358;45871

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1;CODSISTEMA=S
]]>xmlExemplo do retorno de consulta de uma Avaliação Descritivatrue

1
4632
1
N
1
AD
23358
45871
S
]]]]>
]]>xmlExemplo do retorno sem registrostrue<EduExecAvalDescritivaData />
]]>

## Método DeleteRecord

Este método realiza a exclusão de uma avaliação descritiva. Algumas informações são obrigatórias e devem ser informadas: o código da coligada, o id da turma disciplina, o código da etapa, o tipo da etapa, o código da prova, o id interno da prova e o código pessoa do aluno.

O sistema irá realizar a exclusão de uma avaliação caso encontre o registro.

### **Exclusão de aluno**

Para realizar exclusão de uma avaliação, deve ser utilizada a operação de **DeleteRecord**.

Deve ser passado um XML contendo todos os campos que fazem parte do registro de avaliação descritiva.

O **XML** deve conter a tabela ***SEXECAVALDESCRITIVA***com os campos ***CODCOLIGADA, IDTURMADISC, CODETAPA, TIPOETAPA, CODPROVA, ID e CODPESSOA*** como informações da chave para o cadastro de avaliação descritiva e, também, os campos obrigatórios para seu cadastro.

xmlExemplo de XML para exclusão de uma Avaliação Descritivatrue

EduExecAvalDescritivaData



1
4632
1
N
1
AD
23359
45871
S
]]]]>

CODCOLIGADA=1;CODFILIAL=1;CODTIPOCURSO=1;CODSISTEMA=S
]]>xmlExemplo do retorno de exclusão de uma Avaliação DescritivatrueExclusão de registro(s) realizado com sucesso]]>

Para mais informações segue o link da documentação padrão de uso de DataServers utilizando WebService:

<http://tdn.totvs.com/x/XYlpCw>
