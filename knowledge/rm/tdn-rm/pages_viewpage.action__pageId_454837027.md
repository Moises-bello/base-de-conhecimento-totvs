---
content_hash: 8fdfe578924d482ff3eedf7d58ed6ff4811892147a6f36153243a02d50cf3400
fetched_at: '2026-06-29T00:10:13.145236+00:00'
page_id: '454837027'
product: rm
source: tdn-rm
title: Rematrícula - Ensino Superior
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=454837027
version: 10
---

## Visão Geral do Programa

O objetivo deste ProcessServer é possibilitar rematricular o aluno no próximo período letivo através de WebService. A matrícula do aluno poderá ser visualizadas através da visão de Matrícula no período letivo do aluno do Totvs Educacional.

Através do processServer "**EduRematriculaESuperiorData**" é possível, por meio do método **ExecuteWithXmlParams**, realizar a inclusão da matrícula do aluno.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/display/LRM/Webservices)**

### Método ExecuteWithXmlParams

Este método realizará a inclusão da matrícula do aluno no período letivo junto com as disciplinas.

Os campos chaves obrigatórios para gravação no banco de dados (PrimaryKey) são:  CODCOLIGADA; IDPERLET; IDHABILITACAOFILIAL; RA

O contexto para execução do processo e validações dos parâmetros do sistema junto ao perfil do usuário, são  $CODCOLIGADA, $CODFILIAL, $CODTIPOCURSO, $CODSISTEMA e $CODUSUARIO.

A seguir temos dois exemplos de XML um **completo,** com todas as tags, e outro **reduzido**, apenas com as tags necessárias.

xmlExemplo de XML COMPLETO para rematricula no Ensino Superiortrue

S
EduRematriculaESuperiorAction
true
false
false
mestre





$CODUNIDADEBIB
1

$CHAPAFUNCIONARIO
-1

$EXERCICIOFISCAL
1

$CODFILIAL
1

$RHTIPOUSR
-1

$CODUSUARIOSERVICO


$EDUTIPOUSR
-1

$CODLOCPRT
1

$CODUSUARIO
mestre

$CODSISTEMA
S

$CODCOLIGADA
1

$CODTIPOCURSO
3

$CODIGOEXTERNO
-1

$IDPRJ
-1
DotNet

false

7367fb31-b210-4e48-99d3-d3841c07a85a
Falha na execução do processo

false
BHN050103194
true
10.31.8.189
false


1
213000
false
BHN050103194

1000
1
guilherme.campolina
false

false
false



Rematrícula
0
true
false
2019-02-08T17:47:18.9886754-02:00
JobMonitor
false
EduRematriculaESuperiorData

RM.Edu.Interfaces.IEduRematriculaESuperior
4
RM.Edu.Interfaces.Intf, Version=12.1.24.1, Culture=neutral, PublicKeyToken=null
false
true

Processo executado com sucesso
false
true
mestre
false



0

0




1

T1VET
717
Malu Rosângela Martins
MRM2019
Sim
Sim
1
1


123
123
3
mestre
Nao
Nao




 /
 /
Nao
104
Nao
1000.0
1000.0


Nao
7
7
Nao

]]>xmlExemplo de XML REDUZIDO para rematrícula no Ensino Superiortrue




EduRematriculaESuperiorData






$CODFILIAL
1

$CODUSUARIO
mestre

$CODSISTEMA
S

$CODCOLIGADA
1

$CODTIPOCURSO
3
DotNet






0

0




1

T1VET
717
Malu Rosângela Martins
MRM2019
Sim
Sim
1
1


123
123
3
mestre
Nao
Nao




 /
 /
Nao
104
Nao
1000.0
1000.0


Nao
7
7
Nao

]]]]>
]]>xmlExemplo do retorno da rematrícula do Ensino Superiortrue


1
]]>falseTabela de referência das Tags do XML

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Tags do item EduRematriculaESuperiorParamsProc** | | | | | | |
| Tag | Obrigatório | Parâmetro  Interno | Aceita  Nulo | Tipo de  Dados | Exemplo | Descrição |
| ActionModule | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno |
| ActionName | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno |
| CanParallelize | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno |
| CanSendMail | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno |
| CanWaitSchedule | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno |
| CodUsuario | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno |
| ConnectionId | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno |
| ConnectionString | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno |
| Tags do item Context É obrigatório informar esta tag, porém com as seguintes keys: CODTIPOCURSO, CODCOLIGADA, CODSISTEMA, CODUSUARIO e CODFILIAL. Segue exemplo: falseExemplo do item Contextxml   $CODTIPOCURSO 1  $CODCOLIGADA 1  $CODSISTEMA S  $CODUSUARIO mestre  $CODFILIAL 1 DotNet ]]> | | | | | | |
| CustomData | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| DisableIsolateProcess | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| DriverType | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| ExecutionId | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| FailureMessage | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| FriendlyLogs | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| HideProgressDialog | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| HostName | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| Initialized | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| Ip | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| IsolateProcess | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| JobID | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| JobServerHostName | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| MasterActionName | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| MaximumQuantityOfPrimaryKeysPerProcess | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| MinimumQuantityOfPrimaryKeysPerProcess | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| NetworkUser | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| NotifyEmail | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| NotifyEmailList | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| NotifyFluig | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| OnlineMode | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| Tags do item PrimaryKeyList É obrigatório informar esta tag. Segue exemplo: falseExemplo do item PrimaryKeyListxml ]]> | | | | | | |
| Tags do item PrimaryKeyNames É obrigatório informar esta tag. Segue exemplo: falseExemplo do item PrimaryKeyNamexml ]]> | | | | | | |
| PrimaryKeyTableName | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| ProcessName | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| QuantityOfSplits | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| SaveLogInDatabase | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| SaveParamsExecution | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| ScheduleDateTime | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| Scheduler | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| SendMail | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| ServerName | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| ServiceInterface | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| ShouldParallelize | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| ShowReExecuteButton | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| StatusMessage | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| SuccessMessage | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| SyncExecution | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| UseJobMonitor | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| UserName | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| WaitSchedule | Não | Sim | Sim | N/A | Não é necessário informar no XML. | Parâmetro interno. |
| CodCurso | Não | Não | Sim | Booleano | Não é necessário informar no XML. | Código do curso. |
| CodGrade | Não | Não | Sim | String | Não é necessário informar no XML. | Código da matriz curricular. |
| CodHabilitacao | Não | Não | Sim | String | Não é necessário informar no XML. | Código da habilitação do aluno |
| CodStatus | Não | Não | Sim | Inteiro | Não é necessário informar no XML. | Código da situação de matrícula. |
| CodTurma | Não | Não | Sim | String | Não é necessário informar no XML. | Código da turma. |
| CodTurno | Não | Não | Sim | Inteiro | Não é necessário informar no XML. | Código do turno. |
| Tags do item ParamsRematricula Esta tag é obrigatória, segue referência de todos os itens.   | Tag | Obrigatório | Parâmetro  Interno | Aceita  Nulo | Tipo de  Dados | Exemplo | Descrição | | --- | --- | --- | --- | --- | --- | --- | | Tags do Aluno  | Tag | Obrigatório | Parâmetro  Interno | Aceita  Nulo | Tipo de  Dados | Exemplo | Descrição | | --- | --- | --- | --- | --- | --- | --- | | CodColigada | Sim | Não | Não | Inteiro | 1 | Código da coligada. | | CodPlanoPgto | Não | Não | Não | Booleano | Não é necessário informar no XML. | Código do plano de pagamento. | | CodTurma | Não | Não | Não | String | T1EB2 | Código da turma. | | IdHabilitacaoFilial | Não | Não | Não | Inteiro | 719 | Id. da matriz aplicada | | Nome | Não | Não | Não | String | Kamilly Andrea Vieira | Nome | | RA | Não | Não | Não |  | KAV2018 | Registro acadêmico do aluno. | | | | | | | | | CadastrarContrato | Não | Não | Sim | Booleano | false | Indica se é para cadastrar Contrato financeiro. | | CadastrarDisciplinas | Não | Não | Sim | Enumerado | Nao | Cadastrar disciplinas automaticamente | | CodColigada | Sim | Não | Não | Inteiro | 1 | Código da coligada | | CodFilial | Sim | Não | Não | Inteiro | 1 | Código da filial | | CodFormulaDisc | Não | Não | Sim | String | Não é necessário informar no XML. | Código da fórmula da disciplina | | CodFormulaPL | Não | Não | Sim | String | Não é necessário informar no XML. | Código da fórmula do período letivo | | CodStatusDisc | Não | Não | Sim | Inteiro | 1 | Código da situação de matrícula da disciplina | | CodStatusPL | Não | Não | Sim | Inteiro | 1 | Código da situação de matrícula do período letivo. | | CodTipoCurso | Sim | Não | Não | Inteiro | 1 | Código do nível de ensino | | CodUsuario | Não | Não | Sim | String | mestre | Código do usuário | | ConsiderarPreReqEmCurso | Não | Não | Sim | Enumerado | Nao | Indica se Considerar pré requisito em curso | | CopiarResponsavelFinanceiroContrato | Não | Não | Sim | Enumerado | Nao | Copiar responsável financeiro do contrato anterior do aluno | | CotaFinal | Não | Não | Sim | Inteiro | Não é necessário informar no XML. | Cota final. Deverá ser preenchido **obrigatoriamente** caso a situação de matrícula exigir contrato financeiro, o campo **GerarLancamento = true e o campo **TipoSelecaoParcela = Parcela**.** | | CotaInicial | Não | Não | Sim | Inteiro | Não é necessário informar no XML. | Cota inicial. Deverá ser preenchido **obrigatoriamente** caso a situação de matrícula exigir contrato financeiro, o campo **GerarLancamento = true e o campo **TipoSelecaoParcela = Parcela**.** | | DataFinalParc | Não | Não | Sim | Data | 2018-09-28 | Data final da parcela. Deverá ser preenchido **obrigatoriamente** caso a situação de matrícula exigir contrato financeiro, o campo **GerarLancamento = true** e o campo T**ipoSelecaoParcela = Data**. | | DataInicialParc | Não | Não | Sim | Data | 2018-09-11 | Data inicial da parcela. Deverá ser preenchido **obrigatoriamente** caso a situação de matrícula exigir contrato financeiro, o campo **GerarLancamento = true** e o campo T**ipoSelecaoParcela = Data**. | | DtCompetenciaFinal | Não | Não | Não | String | 06/2018 | Data de competência final | | DtCompetenciaInicial | Não | Não | Sim | String | 01/2018 | Data de competência inicial. | | GerarLancamento | Não | Não | Sim | Booleano | false | Indica se é para gerar lançamento.  Somente irá gerar lançamento se a situação de matrícula exigir contrato financeiro e o obedecer os critérios abaixo:   * Preencher o campo **CodPlanoPgto;** * Preencher o campo **TipoSelecaoParcela**, ver valores permitidos pertinentes a este campo. | | IdPerLet | Sim | Não | Não | Inteiro | 21 | Id. do período letivo. | | ManterVencimentos | Não | Não | Sim | Enumerado | Nao | Indica se é para Copiar vencimento diferenciado do contrato anterior do aluno | | MaxCreditos | Não | Não | **Sim** | Decimal | Não é necessário informar no XML. | Número máximo de créditos | | MaxCreditosOutroTurno | Não | Não | Sim | Decimal | Não é necessário informar no XML. | Número máximo de créditos outro turno | | ParcelaFinal | Sim | Não | Não | Inteiro | 1 | Parcela final. | | ParcelaInicial | Não | Não | Sim | Inteiro | 1 | Parcela inicial. Deverá ser preenchido **obrigatoriamente** caso a situação de matrícula exigir contrato financeiro, o campo **GerarLancamento = true**e ocampo **TipoSelecaoParcela = Parcela**. | | ProximaTurma | Não | Não | Sim | Enumerado | Nao | Indica se tem Preferência para a próxima turma cadastrada | | TipoMatriculaDIsc | Não | Não | **Sim** | Inteiro | Não é necessário informar no XML. | Tipo de matrícula nas disciplinas do próximo período letivo | | TipoMatriculaPL | Não | Não | **Sim** | Inteiro | Não é necessário informar no XML. | Tipo de matrícula do próximo período letivo | | TurmaAnterior | Não | Não | Sim | Enumerado | Nao | Indica se tem Preferência para a turma anterior do aluno | | | | | | | |
| RA | Não | Não | Sim | String | KAV2018 | Registro acadêmico do aluno. |

Importante

* As tags que não são obrigatórias e/ou que aceitam nulo o recomendado é **não** informar elas no XML.
