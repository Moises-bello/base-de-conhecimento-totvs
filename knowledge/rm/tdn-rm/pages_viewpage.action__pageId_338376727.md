---
content_hash: 5a71f6a976431ecf181053566d83e22623fa8a88666a481f285faf2103cbf5cb
fetched_at: '2026-06-29T00:08:52.296629+00:00'
page_id: '338376727'
product: rm
source: tdn-rm
title: Geração de lançamentos por Parcela
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=338376727
version: 4
---

## Visão Geral do Programa

O objetivo deste ProcessServer é possibilitar a inclusão / alteração de lançamento para uma parcela de um contrato do aluno através de WebService. Os lançamentos incluídos poderão ser visualizados através da visão de lançamentos do Totvs Gestão Financeira ou através da edição da parcela considerada na geração.

Através do processServer "**EduGerarLancFromParcelaData**" é possível, por meio do método **ExecuteWithXmlParams**, realizar a inclusão ou alteração de um lançamento de uma determinada parcela.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/display/LRM/Webservices)**

### Método ExecuteWithXmlParams

Este método realizará a inclusão ou alteração de um lançamento. Deve ser informando o código da coligada e o id da parcela, além das outras informações que compõem o contexto de execução como $CODCOLIGADA, $CODFILIAL, $CODTIPOCURSO, $CODSISTEMA e $CODUSUARIO. O sistema irá realizar uma inclusão de lançamento caso não a parcela não possua vínculo com lançamento gerado (registro na SLAN). Se já existir um vínculo entre um lançamento e a parcela, o respectivo lançamento da parcela será alterado (regerado).

#### **Utilização do WebService**

**Inclusão ou alteração de lançamento da parcela**

Para realizar inclusão ou alteração de um lançamento para a parcela, deve ser utilizado a operação de ExecuteWithXmlParams. Deve ser passado um XML contendo basicamente a identificação da parcela (CODCOLIGADA, IDPARCELA) e os campos do contexto de execução com os valores como se o usuário estivesse logado no sistema.

Campos obrigatórios: CODCOLIGADA, IDPARCELA, $CODCOLIGADA, $CODFILIAL, $CODTIPOCURSO, $CODSISTEMA, $CODUSUARIO

### Exemplo de XML para inclusão / alteração de lançamentos

xmlGeração da parcela 48169




EduGerarLancFromParcelaData



S
EduGerarLancFromParcela
mestre



$EXERCICIOFISCAL
22

$CODLOCPRT
12

$CODTIPOCURSO
1

$EDUTIPOUSR
A

$CODUNIDADEBIB
5

$CODCOLIGADA
1

$RHTIPOUSR
01

$CODIGOEXTERNO
-1

$CODSISTEMA
S

$CODUSUARIOSERVICO


$CODUSUARIO
mestre

$IDPRJ
-1

$CHAPAFUNCIONARIO
00027

$CODFILIAL
1
DotNet


1
48169

CODCOLIGADA
IDPARCELA






0









0



1
0





1







1


mestre











0001-01-01T00:00:00

Inclusao
false
false
false


















true




IdParcela
0
0

false
Nenhum

]]]]>
]]>

### Exemplo do retorno da inclusão / alteração de lançamento

xml


1
]]>
