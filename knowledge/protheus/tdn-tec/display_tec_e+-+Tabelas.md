---
content_hash: e3a5f7f66e8d1a606ee4307eab8de7fe10cfc059191b8a5ae35cd65e72189ff0
fetched_at: '2026-07-02T19:24:27.572191+00:00'
page_id: '656073821'
product: protheus
source: tdn-tec
title: e - Tabelas
type: documentation
url: https://tdn.totvs.com/display/tec/e+-+Tabelas
version: 3
---

Todas as execuções de testes são armazenados em um Banco de dados, dessa forma, é possível comparar e consultar resultados antigos caso seja necessário alguma análise retroativa.

Vamos à tabelas disponíveis com dados dos resultados:

## **Testes**

##### [PROBAT\_TEST\_EXECUTION]

Tabela principal da execução dos testes contendo dados principais.

| Campo | Tipo Dado | Descrição |
| --- | --- | --- |
| CODE\_EXEC | C | Código de Execução |
| DATE | D | Data da Execução |
| TIME | C | Hora da Execução |
| START | C | Time Início dos Testes (suites) |
| FINISH | C | Time Fim dos Testes (suites) |
| CALLSTACK | C | Main Function de entrada ao PROBAT utilizada para solicitar a execução |
| TYPE | C | "Type" informado nos parâmetros |
| PARAMS | C | Parâmetros passados para main function de entrada |
| CUSTOM | C | Identificador customizado |

##### [PROBAT\_TEST\_RESULTS]

Resultados totalizados entre todos os testes, agrupados conforme parâmetros enviados à função de entrada.

| Campo | Tipo Dado | Descrição |
| --- | --- | --- |
| CODE | C | Código de controle interno |
| CODE\_EXEC | C | Código execução |
| TYPE | C | Agrupamento dos types enviados nos parâmetros |
| START | C | Time Inicio dos Testes (grupos) |
| FINISH | C | Time Fim dos Testes (grupos) |
| TOTAL | N | Total de Testes registrados |
| OK | N | Qtde de Testes com Sucesso |
| ERROR | N | Qtde de Testes com Erro |
| NOTEXECUTE | N | Qtde de Testes Pulados "Skip" |

##### [PROBAT\_TEST\_TESTS]

Resultado de cada registro de teste, gerado por cada assert executado.

| Campo | Tipo Dado | Descrição |
| --- | --- | --- |
| CODE | C | Código controle Interno |
| START | C | Time Início Teste |
| FINISH | C | Time Fim Teste |
| RESULT\_FROM | C | Indica quem é o gerador dessa linha de testes ( T = Test |
| CODE\_ROUTINE | N | Código da rotina de teste (cadastro interno) |
| TYPE\_ROUTINE | C | Tipo da Rotina que gerou resultado ( TST = Teste |
| ANNOTATION | M | Descrição capturada pela annotation |
| ROUTINE | C | Nome Fonte |
| FOLDER | C | Diretório do fonte |
| TYPE | C | Tipo rotina ( C = Class |
| NAMEFUNCTION | C | Nome da Function |
| NAMECLASS | C | Nome da Class |
| NAMEMETHOD | C | Nome do Method |
| SEQUENCE | C | Sequencia do assert dentro do mesma função/método |
| TARGET | C | Rotina algo do teste |
| ERROR | M | Mensagem de erro, quando houver |
| DESCRIPTION | M | Descrição enviada pelo assert |
| SOURCE\_CALL | C | Fonte que chamou o assert |
| LINE\_CALL | N | Linha do fonte onde chamou o assert |
| ASSERT | C | Função de Assert Usada |
| RESULT | C | Resultado gerado pelo teste |
| EXPECTED | C | Valor esperado para o teste |
| OK | N | Resultado ( 0 = Erro |

##### [PROBAT\_TEST\_ERRORS]

Tabela contendo todas as mensagems de erros capturas pelo **PROBAT**

| Campo | Tipo Dado | Descrição |
| --- | --- | --- |
| CODE\_EXEC | C | Código execução |
| CODE\_SRC | N | Código cadastro de fontes do projeto |
| CODE\_TST | N | Código cadastro do fonte de teste |
| NAMESPACE | C | Namespace usada no fonte |
| SOURCE | C | Fonte |
| CODE | C | Código erro |
| ERROR | M | Mensagem de erro |

##### [PROBAT\_TEST\_WARNING]

Tabela contendo todas as mensagens de aviso geradas pelo assertWarning().

| Campo | Tipo Dado | Descrição |
| --- | --- | --- |
| CODE\_EXEC | C | Código de execução |
| WARNING | C | Mensagem de aviso |
| SOURCE\_CALL | C | Fonte que executou o assert |
| LINE\_CALL | N | Linha do fonte que executou o assert |

---

## **Cobertura de Códigos**

Dados relacionados à cobertura de código

##### [PROBAT\_CODECOVERAGE\_TOTAL]

Percentual Total de cobertura sumarizado por todos os fontes

| Campo | Tipo Dado | Descrição |
| --- | --- | --- |
| CODE\_EXEC | C | Código execução |
| SOURCES | N | Qtde de fontes apurados |
| LINES | N | Qtde de linhas apuradas |
| COVERAGE | N | % total de cobertura ( todos os fontes ) |
| COVERAGE\_FRAME | N | % total de cobertura de fontes oficiais do projeto |
| COVERAGE\_TEST | N | % total de cobertura dos fontes de testes |

##### [PROBAT\_CODECOVERAGE\_SOURCES]

Percentual Total de cobertura por fonte

| Campo | Tipo Dado | Descrição |
| --- | --- | --- |
| CODE\_EXEC | C | Código execução |
| RUN | C | Indica se esse fonte foi executado ( 0 = Não |
| CODE\_SRC | N | Código cadastro de fontes do projeto |
| CODE\_TST | N | Código cadastro do fonte de teste |
| SOURCE | C | Nome fonte |
| LINES | N | Qtde linhas do fontes |
| COVERAGE | N | % cobertura de código para esse fonte |

##### [PROBAT\_CODECOVERAGE\_LINES]

Informação linha a linha por fonte sobre a cobertura

| Campo | Tipo Dado | Descrição |
| --- | --- | --- |
| CODE\_EXEC | C | Código execução |
| CODE\_SRC | N | Código cadastro de fontes do projeto |
| CODE\_TST | N | Código cadastro do fonte de teste |
| SOURCE | C | Nome fonte |
| LINE | C | Número da linha do fonte |
| COVERAGE | N | Informação de cobertura da linha ( -1 = Não Debugável |
| CHANGE | C | Indica que houve troca entre -1 e 0 |
