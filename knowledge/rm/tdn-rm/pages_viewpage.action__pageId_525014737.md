---
content_hash: 57970c73adc132568ae04ed9474a3e887ec047be966e21c2bd1b1cf30bb8b815
fetched_at: '2026-06-29T00:10:32.007339+00:00'
page_id: '525014737'
product: rm
source: tdn-rm
title: Controle e aprovação de dados referente a folha de pagamento.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=525014737
version: 9
---

## Visão Geral do Programa

O objetivo deste ProcessServer é possibilitar a aprovação ou reprovação dos dados referente ao professor em função da folha de pagamento.

Informações:

- Professores associados a Turma/Disciplina

- Atividade extra vinculada no anexo de Professor

- Professores vinculados ao cadastro de atividade ofertada

Para utilizar este recurso é necessário habilitar o parâmetro do sistema conforme a imagem abaixo.

Através do processServer " **EduControleDadosFolhaPagData**" é possível, por meio do método **ExecuteWithXmlParams**, realizar a aprovação ou reprovação mudando o status da informação.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/display/LRM/Webservices)**

### Método ExecuteWithXmlParams

O contexto para execução do processo e validações dos parâmetros do sistema junto ao perfil do usuário, são  $CODCOLIGADA, $CODFILIAL, $CODTIPOCURSO, $CODSISTEMA e $CODUSUARIO.

A seguir temos o exemplo de XML do processo.

xmlExemplo do XML para execução do EduControleDadosFolhaPagDatatrue

S
EduControleDadosFolhaPagAction
mestre



$EXERCICIOFISCAL
2

$CODLOCPRT
12

$CODTIPOCURSO
2

$EDUTIPOUSR
-1

$CODUNIDADEBIB
1

$CODCOLIGADA
1

$RHTIPOUSR
-1

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
-1

$CODFILIAL
1
DotNet


1
5561

CODCOLIGADA
IDATIVIDADEPROF
1
AtividadeExtraProfessor
1
1
1

]]>xmlExemplo do retorno da execução do EduControleDadosFolhaPagDatatrue


1
]]>falseTabela de referência das Tags do XML

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Tags do item EduMatriculaParamsProc** | | | | | | |
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
| Tags do item PrimaryKeyList É obrigatório informar esta tag. Segue exemplo: falseExemplo do item PrimaryKeyListxml   1  5561 ]]> | | | | | | |
| Tags do item PrimaryKeyNames É obrigatório informar esta tag. Segue exemplo: falseExemplo do item PrimaryKeyNamexml CODCOLIGADA  IDATIVIDADEPROF ]]> | | | | | | |
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
| Demais informações da Tag EduControleDadosFolhaPagParamsProc As informações das tags abaixo são obrigatórias. Segue exemplo: falseExemploxml 1  ProfessorTurmaDisciplina 1 1 1]]> | | | | | | |

Importante

* As tags que não são obrigatórias e/ou que aceitam nulo o recomendado é **não** informa-las no XML.

**EduControleDadosFolhaPagData**
