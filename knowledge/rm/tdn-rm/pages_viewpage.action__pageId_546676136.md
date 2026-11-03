---
content_hash: 47d114360161742b194e94ebaf81f576a08ddb378f9d932f6219eb867e08130d
fetched_at: '2026-06-29T00:10:41.912384+00:00'
page_id: '546676136'
product: rm
source: tdn-rm
title: Reajuste Revitalizado / Fórmulas Reajuste
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546676136
version: 28
---

Foram criadas formulas que irão flexibilizar o calculo do Reajuste. Essas formulas serão vinculadas no cadastro dos componentes de CM **(Correção Monetária)** e **Juros de Contrato**. Com isso será possível calcular um valor para taxa, um valor para base de calculo e se o reajuste pode ser executado.

Importante!

Para acessar todas as funções de fórmula do TCGI:

| **VALORBASEREAJUSTE** | Retorna o base da parcela para o cálculo do reajuste/geração de plano do contexto de juros/CM**.** |
| --- | --- |
|  | Usa como contexto o reajuste. |
| **SINTAXE** | VALORBASEREAJUSTE |

| **VALORINDICEREAJUSTE** | Retorna o índice da parcela para o cálculo do reajuste/geração de plano do contexto de juros/CM. |
| --- | --- |
| **CONTEXTO** | Usa como contexto o reajuste. |
| **SINTAXE** | VALORINDICEREAJUSTE |

| **EANIVERSARIOPERIODICIDADE** | Retorna 1 para verdadeiro e 0 para false, caso o período do reajuste é o aniversário da periodicidade para juros/CM. |
| --- | --- |
| **CONTEXTO** | Usa como contexto o reajuste. |
| **SINTAXE** | EANIVERSARIOPERIODICIDADE |

| DATAULTIMOANIVERSARIOPERIODICIDADE | Calcula a data do último aniversário em relação a data de reajuste juros/cm com periodicidade > 1 |
| --- | --- |
|  | Usa como contexto o reajuste. |
| **SINTAXE** | DATAULTIMOANIVERSARIOPERIODICIDADE |

| CALCULARJUROSCMPROPORCIONALANTECIPACAO | Retorna 1 para verdadeiro e 0 para false, caso o período do reajuste é para calcular o valor proporcional de Juros/CM para antecipação de parcela com periodicidade > 1 e não seja o aniversário da periodicidade. |
| --- | --- |
| **CONTEXTO** | Usa como contexto o reajuste. |
| **SINTAXE** | CALCULARJUROSCMPROPORCIONALANTECIPACAO |

| GETVALORCMACUMULADA | Calcula a Variação da Correção Monetária (Índice Acumulado). Primeiro argumento moeda. Segundo argumento data início correção. Terceiro argumento data fim correção. Quarto argumento defasagem do índice. |
| --- | --- |
| **CONTEXTO** | Usa como contexto o reajuste. |
| **SINTAXE** | GETVALORCMACUMULADA('IGPM', '01/01/2020', '01/09/2020', 2) |

| GETVALORCMACUMULADAPARAM | Calcula a Variação da Correção Monetária (Índice Acumulado). Primeiro argumento moeda. Segundo argumento data fim correção. Terceiro argumento defasagem do índice. Quarto argumento periodicidade que será retirado da data final para acumular o índice. Quinto argumento ignorar deflação 0 para não e 1 para sim. |
| --- | --- |
| **CONTEXTO** | Usa como contexto o reajuste. |
| **SINTAXE** | GETVALORCMACUMULADAPARAM('IGPM', '01/12/2020', 2, 12, 1) |

| GETVALORCMMENSAL | Calcula a Variação da Correção Monetária (Índice Mensal). Primeiro argumento moeda. Segundo argumento data início correção. Terceiro argumento data fim correção. Quarto argumento defasagem do índice. |
| --- | --- |
| **CONTEXTO** | Usa como contexto o reajuste. |
| **SINTAXE** | GETVALORCMMENSAL('IGPM', '01/01/2020', '01/09/2020', 2) |

| GETVALORCMMENSALPARAM | Calcula a Variação da Correção Monetária (Índice Mensal). Primeiro argumento moeda. Segundo argumento data fim correção. Terceiro argumento defasagem do índice. Quarta argumento periodicidade que será retirado da data final para acumular o índice. Quinto argumento ignorar deflação 0 para não e 1 para sim. |
| --- | --- |
| **CONTEXTO** | Usa como contexto o reajuste. |
| **SINTAXE** | GETVALORCMMENSALPARAM('IGPM', '01/12/2020', 2, 12, 1) |

| **TABREGRA** | Retorna o valor de um campo da tabela de regra da venda. Primeiro argumento nome do campo. Segundo argumento tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora) |
| --- | --- |
| **CONTEXTO** | Usa como contexto a chave da tabela "XREGRACOMPONENTEVENDA". |
| **SINTAXE** | TABREGRA('CampoReferencia','TipoDeRetorno') |

| **GETTABPARCELANUMPARCELA** | Retorna o valor de um campo da tabela de parcela para um número da parcela dentro do grupo da venda do contexto. Primeiro argumento número da parcela,  segundo argumento nome do campo e terceiro argumento tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora) |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XPARCELAPAGAMENTO" |
| **SINTAXE** | GETTABPARCELANUMPARCELA(10, 'NUN\_VENDA', 'S'); |

| **SETRESIDUODISTRIBUIDOLIMPA** | Limpa os campos de código do grupo do resíduo e a data de distribuição do resíduo. Tabela XVendaParcela |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XPARCELAPAGAMENTO" e do reajuste |
| **SINTAXE** | SETRESIDUODISTRIBUIDOLIMPA(10); |

| **SETRESIDUODISTRIBUIDOMARCAR** | Marca os campos de código do grupo do resíduo e a data de distribuição do resíduo com os dados do grupo do contexto da parcela e o período do reajuste.  Tabela XVendaParcela |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XPARCELAPAGAMENTO" e do reajuste |
| **SINTAXE** | SETRESIDUODISTRIBUIDOMARCAR(10); |

| **SETVALORRESIDUO, SETVALORRESIDUOCMANTES, SETVALORRESIDUOCMAPOS,****SETVALORRESIDUOJUROSANTES, SETVALORRESIDUOJUROSAPOS** | Armazena o valor calculado no campo Valor Resíduo. Tabela XVendaParcela |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XPARCELAPAGAMENTO" e do reajuste |
| **SINTAXE** | SETVALORRESIDUO(100.01); |

| **REAJUSTARCOMPONENTEREGRAPERIODOREAJUSTE** | Retorna 1 para verdadeiro e 0 para false, caso o período do reajuste em relação a database e a data do reajuste é para reajustar Juros/CM |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XPARCELAPAGAMENTO" e do reajuste |
| **SINTAXE** | SE REAJUSTARCOMPONENTEREGRAPERIODOR = 1 ENTAO ... FIMSE |

| **REAJUSTARCOMPONENTEREGRAVENCIMENTO** | Retorna 1 para verdadeiro e 0 para false, caso o período do reajuste em relação ao vencimento é para reajustar Juros/CM. |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XPARCELAPAGAMENTO" e do reajuste |
| **SINTAXE** | SE REAJUSTARCOMPONENTEREGRAVENCIMENTO= 1 ENTAO ... FIMSE |

| **GETSALDODEVEDORTEORICOREGRARESIDUO** | Retorna o valor do saldo devedor téorico do componente principal do valor financiado da regra até o vencimento do contexto da parcela atual. Valor do Financiamento do grupo da parcela do contexto +(mais) valor sumarizado do campo Valor Resíduo somente da parcelas que tenham o vencimento até a data do reajuste - (menos) os valores sumarizados dos campos de valor original mais CM mais juros que tenham o vencimento até a data do reajuste. |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XPARCELAPAGAMENTO" e do reajuste |
| **SINTAXE** | GETSALDODEVEDORTEORICOREGRARESIDUO |

| GETSALDODEVEDORTEORICOVENDARESIDUO | Retorna o valor do saldo devedor teórico da venda até o vencimento do contexto da parcela atual. Valor do Financiamento do grupo da parcela do contexto +(mais) valor sumarizado do campo Valor Resíduo somente da parcelas que tenham o vencimento até a data do reajuste - (menos) os valores sumarizados dos campos de valor original mais CM mais juros que tenham o vencimento até a data do reajuste. |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XPARCELAPAGAMENTO" e do reajuste |
| **SINTAXE** | GETSALDODEVEDORTEORICOVENDARESIDUO |

| **GETNUMPARCELAMESANIVERSARIOREAJUSTE** | Retorna o numero da parcela que tenha o vencimento que fez aniversário no mesmo mês da data do reajuste.  Através desta parcela será definido o limite entre o período do reajuste anual anterior e o novo período. |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XPARCELAPAGAMENTO" e do reajuste |
| **SINTAXE** | GETNUMPARCELAMESANIVERSARIOREAJUSTE |

| **GETNUMPARCELAPORDATAVENCIMENTO** | Retorna o numero da parcela que tenha o vencimento que fez aniversário no mesmo mês da data do reajuste. O primeiro argumeto é a data pesquisada e o segudo é 1 para a data exata pesquisada ou 0 para o mês/ano pesquisado  Através desta parcela será definido o limite entre o período do reajuste anual anterior e o novo período. |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XPARCELAPAGAMENTO" e do reajuste |
| **SINTAXE** | GETNUMPARCELAPORDATAVENCIMENTO('01/01/2020', 1) |

| ADICIONADIASPRORATA | Adiciona número de dias Pro-Rata a uma data passada por parâmetro. Ou Seja, não deixa a data mudar de mês. |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XVENDA" |
| **SINTAXE** | ADICIONADIASPRORATA('01/01/2022', 30) |

| DIADOCONTRATO | Retorna o dia do aniversário do contrato (Data da Venda) |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XVENDA" |
| **SINTAXE** | DIADOCONTRATO |

| DATACONTRATOREAJUSTE | Retorna a data do reajuste com base no dia do aniversário do contrato e a defasagem para Correção Monetária com moeda diária. |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XPARCELAPAGAMENTO" e do reajuste |
| **SINTAXE** | DATACONTRATOREAJUSTE |

| GETTIPOCALCULOJUROSCMREAJUSTE | Retorna o tipo de cálculo do juros sobre o CM e o oposto também. Retorno (0 = Principal 1 = Principal + Mês Anterior (CM ou Juros), 2 = Principal + Atual (CM ou Juros)) |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XPARCELAPAGAMENTO" e do reajuste |
| **SINTAXE** | GETTIPOCALCULOJUROSCMREAJUSTE |

| GETPROXIMOANIVERSARIO | Retorna a data do próximo aniversario para o cálculo do reajuste de juros/CM. |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XPARCELAPAGAMENTO" e do reajuste |
| **SINTAXE** | GETPROXIMOANIVERSARIO |

| DATAPERIODOATUALREAJUSTE | Retorna a data do loop do período do reajuste/geração do plano da parcela do contexto. |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XPARCELAPAGAMENTO" e do reajuste |
| **SINTAXE** | DATAPERIODOATUALREAJUSTE |

| VALORBASEREAJUSTE | Retorna o base da parcela para o cálculo do reajuste/geração de plano do contexto de juros/CM |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XPARCELAPAGAMENTO" e do reajuste |
| **SINTAXE** | VALORBASEREAJUSTE |

| VALORCOMPONENTEREAJUSTE | Retorna o valor do reajuste da parcela para o cálculo do reajuste/geração de plano do contexto de juros/CM |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XPARCELAPAGAMENTO" e do reajuste |
| **SINTAXE** | VALORCOMPONENTEREAJUSTE |

| VALORINDICEREAJUSTE | Retorna o índice da parcela para o cálculo do reajuste/geração de plano do contexto de juros/CM |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XPARCELAPAGAMENTO" e do reajuste |
| **SINTAXE** | VALORINDICEREAJUSTE |

| SETAPLICARVALORFORMULAFINANCEIRO | Define se é para enviar o valor para o financeiro ou não. Primeiro argumento 1 ou 0. |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XPARCELAPAGAMENTO" e do reajuste |
| **SINTAXE** | SETAPLICARVALORFORMULAFINANCEIRO(0) |

| GETPROXIMOANIVERSARIOPERIODOATUAL | Retorna a data do próximo aniversario em relação ao período atual para o cálculo do reajuste de juros/CM |
| --- | --- |
| **CONTEXTO** | Usa o contexto da "XPARCELAPAGAMENTO" e do reajuste |
| **SINTAXE** | GETPROXIMOANIVERSARIOPERIODOATUAL |

**Exemplo**

## TABREGRA('VR\_TX\_PER','V')

| Exemplo de fórmula que que irá validar se o Reajuste pode ou não executar o calculo em determinado mês.  SE  NUMVENDA = 123 OU NUMVENDA = 456 ENTAO        EANIVERSARIOPERIODICIDADE SENAO        SE DATREAJUSTE <> CONVERTDATE('01/03/2018') ENTAO               1        SENAO               0        FIMSE FIMSE |
| --- |

| Exemplo de fórmula para calcular o índice de Juros ou CM.  SE NUMVENDA = 4445 ENTAO       SE CODCOMPN = 3 ENTAO              VALORINDICEREAJUSTE \* 12       SENAO            VALORINDICEREAJUSTE       FIMSE SENAO        SE DATREAJUSTE = CONVERTDATE('01/05/2018') ENTAO              ARREDONDA(VALORINDICEREAJUSTE\*1.1,9)        SENAO               VALORINDICEREAJUSTE        FIMSE FIMSE |
| --- |

| Exemplo de fórmula para calcular o valor Base de incidência de Juros ou CM  SE NUMVENDA = 123 ENTAO       VALORBASEREAJUSTE SENAO       SE DATREAJUSTE = CONVERTDATE('01/04/2018') ENTAO              VALORBASEREAJUSTE/2        SENAO              VALORBASEREAJUSTE        FIMSE FIMSE |
| --- |
