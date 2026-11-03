---
content_hash: 970f3dd948f8f0433763e5cfef35828e5f53c345a62a40a80c73107e721e2841
fetched_at: '2026-06-29T00:10:41.724348+00:00'
page_id: '546264605'
product: rm
source: tdn-rm
title: Aumento e Cancelamento de disciplinas - Cobrança por crédito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546264605
version: 106
---

---

O parâmetro “**Dividir valor de créditos financeiros das disciplinas matriculadas entre as parcelas do contrato"** impacta no comportamento do aumento ou cancelamento, por esse motivo abaixo iremos descrever os comportamentos considerando o parâmetro marcado e desmarcado.

Parâmetros localizado em: Configurações | Parâmetros | Integração | Financeiro / Fin – Geral 1/4

Parâmetro Marcado

Quando o TOTVS Educacional está com o paramétrio “**Dividir valor de créditos financeiros das disciplinas matriculadas entre as parcelas do contrato**” marcado o valor calculado para disciplina será dividido pela quantidade de parcelas, este valor será cobrado ou devolvido integralmente (aumento ou cancelamento total e parcial) respeitando as parametrizações.

Na matricula do aluno no período letivo pode ocorrer ao longo do ano alterações como por exemplo, adição de novas disciplinas ou cancelamento de disciplinas

Vamos descrever um exemplo onde o aluno já está matriculado no período letivo 2020/1 em 5 disciplinas  

Neste exemplo, o aluno tem 5 disciplinas cadastradas com os mesmos números e valores de créditos e deverá pagar um total de R$ 2.500, para cursar as 5 disciplinas do 1º período.

O contrato com um plano de pagamento que terá um valor total de R$ 2.500, deverá ser divido entre 6 parcelas, que foram cadastrados no plano de pagamento.

**5 (Nº de Créditos por disciplina) x R$100 x 5 (disciplinas) =****RS2.500 / 6 (parcelas) = R$ 416,67**

| **Disciplina** | **Nº Crédito x Valor do Crédito** |  | **Parcelas** | **Vencimento** | **Valor de cada parcela** |
| --- | --- | --- | --- | --- | --- |
| Introdução a Ciência do Direito | 5  \*  100 = 500 | 1 | 15/01/2020 | R$2.500 / 6 = R$416,67 |
| Direito Civil I (Parte Geral I) | 5  \*  100 = 500 | 2 | 15/02/2020 | R$2.500 / 6 = R$416,67 |
| Ciência Política | 5  \*  100 = 500 | 3 | 15/03/2020 | R$2.500 / 6 = R$416,67 |
| Direito Penal I (Parte Geral I) | 5  \*  100 = 500 | 4 | 15/04/2020 | R$2.500 / 6 = R$416,67 |
| Teoria Do Estado E Da Constituição | 5  \*  100 = 500 | 5 | 20/05/2020 | R$2.500 / 6 = R$416,67 |
| **Total do contrato** | **R$2.500** | 6 | 20/06/2020 | R$2.500 / 6 = R$416,67 |

Aumento de disciplinas na matrícula do aluno

No dia o aluno inclui a disciplina "Direito Tributário" na sua matricula que possui **3 (Nº de créditos) x R$100 (valor do crédito)**, mas o seu contrato já existe quatro parcelas geradas e quitadas com data inferior a data da inclusão da nova disciplina.

Aumento Total - Cobrança em todas as parcelas do contrato

Quando o parâmetro **"Considerar no cálculo de cobrança somente para parcelas com vencimento igual ou posterior a data da matrícula"** da  estiver desmarcado, temos um aumento total de disciplina, nesse caso a disciplina incluída na matricula do aluno será cobrada em todas as parcelas do contrato. 

- Então a disciplina "Direito Tributário" para esse cenário será cobrada em todas as parcelas do contrato do aluno, porem como as quatro primeiras parcelas já estão quitadas o valor será dividido para as parcelas ainda em aberto.

Ficando assim:

**- Valor da disciplina Direito Tributário (3 x 150) =  RS450**

**-O valor de RS450 (valor total da disciplina) / 2 (parcelas)= R$225**

| **Disciplina** | **Nº Crédito x Valor do Crédito** |  | **Parcelas** | **Vencimento** | **Valor de cada parcela** |
| --- | --- | --- | --- | --- | --- |
| Introdução a Ciência do Direito | 5 x 100 = 500 | 1 | 15/01/2020 | R$416,67 (quitada) |
| Direito Civil I (Parte Geral I) | 5 x 100 = 500 | 2 | 15/02/2020 | R$416,67 (quitada) |
| Ciência Política | 5 x 100 = 500 | 3 | 15/03/2020 | R$416,67 (quitada) |
| Direito Penal I (Parte Geral I) | 5 x 100 = 500 | 4 | 15/04/2020 | R$416,67 (quitada) |
| Teoria do Estado e da Constituição | 5 x 100 = 500 | 5 | 20/05/2020 | R$416,67 + **R$225** = R$641,67 (gerada em aberto) |
| **Direito Tributário** | **3 x 150 = 450** | 6 | 20/06/2020 | R$416,67 + **R$225** = R$641,66 |

Aumento Parcial - Cobrança apenas das parcelas com vencimento igual ou posterior a data de matrícula

Quando o parâmetro **"Considerar no cálculo de cobrança somente para parcelas com vencimento igual ou posterior a data da matrícula"** da  estiver marcado, temos um aumento parcial de disciplina, nesse caso a disciplina incluída na matricula do aluno só será cobrada daquele momento em diante.

- A disciplina "Direito Tributário" para esse cenário será cobrada o valor proporcional somente nas duas últimas parcelas do contrato do aluno.

Para cada parcela em aberto com data de vencimento posterior a data de inclusão da disciplina, será cobrado o valor de R$75,00 pela disciplina.

Ficando assim:

**- Valor da disciplina Direito Tributário (3 x 150) =  RS450**

**- O valor de RS450 (valor total da disciplina) / 6 (parcelas)= R$75.** 

| **Disciplina** | **Nº Crédito x Valor do Crédito** |  | **Parcelas** | **Vencimento** | **Valor de cada parcela** |
| --- | --- | --- | --- | --- | --- |
| Introdução a Ciência do Direito | 5 x 100 = 500 | 1 | 15/01/2020 | R$416,67 (quitada) |
| Direito Civil I (Parte Geral I) | 5 x 100 = 500 | 2 | 15/02/2020 | R$416,67 (quitada) |
| Ciência Política | 5 x 100 = 500 | 3 | 15/03/2020 | R$416,67 (quitada) |
| Direito Penal I (Parte Geral I) | 5 x 100 = 500 | 4 | 15/04/2020 | R$416,67 (quitada) |
| Teoria do Estado e da Constituição | 5 x 100 = 500 | 5 | 20/05/2020 | R$416,67 + **R$75** = R$491,67 |
| **Direito Tributário** | **3 x 150 = 450** | 6 | 20/06/2020 | R$416,67 + **R$75** = R$491,67 |

- Se no contrato já existir parcela com lançamento gerado e vencimento depois da inclusão da disciplina, a próxima parcela em aberto terá uma **Cobrança Retroativa.**   
A cobrança ficará assim **RS450 (valor total da disciplina)****/ 6 (parcelas)= R$75.** Para cada parcela em aberto com data de vencimento posterior a data de inclusão da disciplina, será cobrado o valor de R$75,00 pela disciplina.  
  
Nesse cenário a parcela de n° 6, será cobrado o valor das disciplinas já matriculadas anteriormente + valor da disciplina que foi adicionada + o valor da cobrança retroativa da disciplina não cobrada na parcela anterior.

| **Disciplina** | **Nº Crédito x Valor do Crédito** |  | **Parcelas** | **Vencimento** | **Valor de cada parcela** |
| --- | --- | --- | --- | --- | --- |
| Introdução a Ciência do Direito | 5 x 100 = 500 | 1 | 15/01/2020 | R$416,67 (quitada) |
| Direito Civil I (Parte Geral I) | 5 x 100 = 500 | 2 | 15/02/2020 | R$416,67 (quitada) |
| Ciência Política | 5 x 100 = 500 | 3 | 15/03/2020 | R$416,67 (quitada) |
| Direito Penal I (Parte Geral I) | 5 x 100 = 500 | 4 | 15/04/2020 | R$416,67 (quitada) |
| Teoria do Estado e da Constituição | 5 x 100 = 500 | 5 | 20/05/2020 | R$416,67 (gerada em aberto) |
| **Direito Tributário** | **3 x 150 = 450** | 6 | 20/06/2020 | R$416,67 + **R$75 + R$75**= R$566,66 |

Nesse cenário se a parcela de n° 5 não foi baixada, poderá ser regerada para que o valor da cobrança seja feito nela, assim não seria gerado a cobrança retroativa para próxima parcela.

Cancelamento de disciplinas na matrícula do aluno

No dia o aluno cancelou a disciplina "X" da sua matricula, mas o seu contrato já existe quatro parcelas geradas e quitadas com data inferior a data de alteração.

Cancelamento Total - Abater em todas as parcelas

Quando altero a  da disciplina para "Cancelamento Total" e o parâmetro "**Abater valor da disciplina somente para parcelas com vencimento igual ou posterior a data de alteração da situação de matricula"**e "**Conta créditos financeiros (cobrança por crédito)"**estiver desmarcado na aba , nesse caso a disciplina na matricula do aluno terá o seu cancelamento total.

- A disciplina "Introdução a Ciência do Direito" para esse cenário foi cobrada da primeira á quarta parcela, porem foi alterado o status da disciplina para "Cancelamento total", como já existe cobranças anteriores ao cancelamento será gerado um crédito em função desse cancelamento e também não será cobrada nas parcelas em aberto.

Ficando assim:

**- Valor da disciplina Introdução a Ciência do Direito (5 x 100) =  RS500**

**- O valor de** **RS500 (valor total da disciplina) / 6 (parcelas) = R$83,33 x 4 (parcelas quitadas) = R$333,33 / 2 (parcelas em aberto) = R$166,67**.

Para as quatro parcelas quitadas foi cobrando o total de R$333,33 que é a soma do valor da disciplina, esse valor deve ser divido entre as parcelas em aberto gerando assim o crédito.

| **Disciplina** | **Nº Crédito x Valor do Crédito** |  | **Parcelas** | **Vencimento** | **Valor de cada parcela** |
| --- | --- | --- | --- | --- | --- |
| **Introdução a Ciência do Direito** | **5 x 100 = 500** | 1 | 15/01/2020 | R$416,67 (quitada) |
| Direito Civil I (Parte Geral I) | 5 x 100 = 500 | 2 | 15/02/2020 | R$416,67 (quitada) |
| Ciência Política | 5 x 100 = 500 | 3 | 15/03/2020 | R$416,67 (quitada) |
| Direito Penal I (Parte Geral I) | 5 x 100 = 500 | 4 | 15/04/2020 | R$416,67 (quitada) |
| Teoria do Estado e da Constituição | 5 x 100 = 500 | 5 | 20/05/2020 | (R$2.000 / 6) - **R$166,67**= R$166,67 |
| **Total do contrato após cancelamento da disciplina** | **R$2.000** | 6 | 20/06/2020 | (R$2.000 / 6) - **R$166,67**= R$166,67 |

Cancelamento Parcial - Abater apenas das parcelas em aberto com data posterior a data de alteração não terá a cobrança dessa disciplina

Quando altero a  da disciplina para "Cancelamento Total"e o parâmetro "**Abater valor da disciplina somente para parcelas com vencimento igual ou posterior a data de alteração da situação de matricula"**estiver marcado na aba , nesse caso a disciplina na matricula do aluno terá o seu cancelamento parcial.

- Então a disciplina "Introdução a Ciência do Direito" para esse cenário foi cobrada da primeira a quarta parcela, como o cancelamento da disciplina é parcial para as parcelas em aberto com data posterior a data de alteração não terá a cobrança dessa disciplina.

Ficando assim:

**- O valor de RS2.500 (valor total do contrato) - R$500 (valor da disciplina cancelada) = R$2.000 x 6 (parcelas) = R$333,33.** 

Para as parcelas em aberto será feito a cobrança somente das disciplinas que o aluno está cursando, desconsiderando o valor da disciplina cancelada.

| **Disciplina** | **Nº Crédito x Valor do Crédito** |  | **Parcelas** | **Vencimento** | **Valor de cada parcela** |
| --- | --- | --- | --- | --- | --- |
| **Introdução a Ciência do Direito** | **5 x 100 = 500** | 1 | 15/01/2020 | R$416,67 (quitada) |
| Direito Civil I (Parte Geral I) | 5 x 100 = 500 | 2 | 15/02/2020 | R$416,67 (quitada) |
| Ciência Política | 5 x 100 = 500 | 3 | 15/03/2020 | R$416,67 (quitada) |
| Direito Penal I (Parte Geral I) | 5 x 100 = 500 | 4 | 15/04/2020 | R$416,67 (quitada) |
| Teoria do Estado e da Constituição | 5 x 100 = 500 | 5 | 20/05/2020 | (R$2.000 / 6)= R$333,33 |
| **Total do contrato após cancelamento da disciplina** | **R$2.000** | 6 | 20/06/2020 | (R$2.000 / 6) = R$333,33 |

Exclusão de disciplinas na matrícula do aluno

No dia o aluno excluiu a disciplina "X" da sua matricula, mas o seu contrato já existe quatro parcelas geradas e quitadas com data inferior a data de alteração.

- A disciplina "Introdução a Ciência do Direito" para esse cenário foi cobrada da primeira á quarta parcela,  porem a disciplina foi excluída da matricula , como já existe cobranças anteriores a exclusão será gerado um crédito em função desse cancelamento e também não será cobrada nas parcelas em aberto.

Ficando assim:

**-O valor de RS500 (valor total da disciplina) / 6 (parcelas) = R$83,33 x 4 (parcelas quitadas) = R$333,33 / 2 (parcelas em aberto) = R$166,67**.

Para as quatro parcelas quitadas foi cobrando o total de R$333,33 que é a soma do valor da disciplina, esse valor deve ser divido entre as parcelas em aberto gerando assim o crédito.

| **Disciplina** | **Nº Crédito x Valor do Crédito** |  | **Parcelas** | **Vencimento** | **Valor de cada parcela** |
| --- | --- | --- | --- | --- | --- |
| **Introdução a Ciência do Direito** | **5 x 100 = 500** | 1 | 15/01/2020 | R$416,67 (quitada) |
| Direito Civil I (Parte Geral I) | 5 x 100 = 500 | 2 | 15/02/2020 | R$416,67 (quitada) |
| Ciência Política | 5 x 100 = 500 | 3 | 15/03/2020 | R$416,67 (quitada) |
| Direito Penal I (Parte Geral I) | 5 x 100 = 500 | 4 | 15/04/2020 | R$416,67 (quitada) |
| Teoria do Estado e da Constituição | 5 x 100 = 500 | 5 | 20/05/2020 | (R$2.000 / 6) - **R$166,67**= R$166,67 |
| **Total do contrato após cancelamento da disciplina** | **R$2.000** | 6 | 20/06/2020 | (R$2.000 / 6) - **R$166,67**= R$166,67 |

Parâmetro Desmarcado

Quando o TOTVS Educacional está com o paramétrio “**Dividir valor de créditos financeiros das disciplinas matriculadas entre as parcelas do contrato**” desmarcado tem o mesmo comportamento que abordamos anteriormente com o parâmetro marcado, no entanto o valor calculado para disciplina não será dividido pela quantidade de parcelas, este valor será cobrado ou devolvido integralmente (aumento ou cancelamento total) respeitando as parametrizações.

Na matricula do aluno no período letivo pode ocorrer ao longo do ano alterações como por exemplo, adição de novas disciplinas ou cancelamento de disciplinas

Vamos descrever um exemplo onde o aluno já está matriculado no período letivo 2020/1 em 5 disciplinas

Neste exemplo, o aluno tem 5 disciplinas cadastradas com os mesmos números e valores de créditos e deverá pagar um total de R$ 15.000, para cursar as 5 disciplinas do 1º período.

O contrato com um plano de pagamento que terá um valor total de R$ 2.500 em cada parcela conforme valor da disciplina.

**5 (Nº de Créditos por disciplina) x R$100 x 5 (disciplinas) =****RS2.500**

| **Disciplina** | **Nº Crédito x Valor do Crédito** |  | **Parcelas** | **Vencimento** | **Valor de cada parcela** |
| --- | --- | --- | --- | --- | --- |
| Introdução a Ciência do Direito | 5  \*  100 = 500 | 1 | 15/01/2020 | R$2.500 |
| Direito Civil I (Parte Geral I) | 5  \*  100 = 500 | 2 | 15/02/2020 | R$2.500 |
| Ciência Política | 5  \*  100 = 500 | 3 | 15/03/2020 | R$2.500 |
| Direito Penal I (Parte Geral I) | 5  \*  100 = 500 | 4 | 15/04/2020 | R$2.500 |
| Teoria Do Estado E Da Constituição | 5  \*  100 = 500 | 5 | 20/05/2020 | R$2.500 |
| **Total do contrato** | **R$2.500** | 6 | 20/06/2020 | R$2.500 |

Aumento de disciplinas na matrícula do aluno

No dia o aluno inclui a disciplina "Direito Tributário" na sua matricula que possui 3 (Nº de créditos) x R$150 (valor do crédito), mas o seu contrato já existe quatro parcelas geradas e quitadas com data inferior a data da inclusão da nova disciplina.

Aumento Total - Cobrança em todas as parcelas do contrato

Quando o parâmetro **"Considerar no cálculo de cobrança somente para parcelas com vencimento igual ou posterior a data da matrícula"** da [Matrícula na disciplina](https://tdn.totvs.com/pages/viewpage.action?pageId=425459150) estiver desmarcado.

- A disciplina "Direito Tributário" para esse cenário será cobrada em todas as parcelas do contrato do aluno, porem como as quatro primeiras parcelas já estão quitadas, a partir da parcela 5 o valor da disciplina correspondente a parcela de 1 a 4 será cobrado (o valor total a ser cobrado será dividido pela quantidade de parcelas restantes no contrato).

Ficando assim:  
**- Valor da disciplina Direito Tributário (3 x 150) =** **RS450****- Da parcela 1 a 4  a disciplina " Direito Tributário " não foi cobrada (  RS450 x 4  = R$1800 )****O valor de R$1.800 deverá ser cobrado, neste caso o TOTVS Educacional divide entre as parcelas ainda não geradas, no caso parcela 5 e 6 ( R$1.800 / 2 = R$900)**

| **Disciplina** | **Nº Crédito x Valor do Crédito** |  | **Parcelas** | **Vencimento** | **Valor de cada parcela** |
| --- | --- | --- | --- | --- | --- |
| Introdução a Ciência do Direito | 5 x 100 = 500 | 1 | 15/01/2020 | R$2.500(quitada) |
| Direito Civil I (Parte Geral I) | 5 x 100 = 500 | 2 | 15/02/2020 | R$2.500(quitada) |
| Ciência Política | 5 x 100 = 500 | 3 | 15/03/2020 | R$2.500(quitada) |
| Direito Penal I (Parte Geral I) | 5 x 100 = 500 | 4 | 15/04/2020 | R$2.500(quitada) |
| Teoria do Estado e da Constituição | 5 x 100 = 500 | 5 | 20/05/2020 | R$2.500 + **R$450 +R$900**= R$3.850 |
| **Direito Tributário** | **3 x 150 = 450** | 6 | 20/06/2020 | R$2.500 + **R$450 +R$900**= R$3.850 |

Aumento Parcial - Cobrança apenas das parcelas com vencimento igual ou posterior a data de matrícula

Quando o parâmetro **"Considerar no cálculo de cobrança somente para parcelas com vencimento igual ou posterior a data da matrícula"** da [Matrícula na disciplina](https://tdn.totvs.com/pages/viewpage.action?pageId=425459150) estiver marcado, temos um aumento parcial de disciplina, nesse caso a disciplina incluída na matricula do aluno só será cobrada daquele momento em diante.

- A disciplina "Direito Tributário" para esse cenário será cobrada o valor somente nas duas últimas parcelas do contrato do aluno, ficando assim **RS450 (valor total da disciplina)**por parcela em aberto.Para cada parcela em aberto com data de vencimento posterior a data de inclusão da disciplina, será cobrado o valor de R$450,00 pela disciplina.

Ficando assim:

**- Valor da disciplina Direito Tributário (3 x 150) =** **RS450****- O valor de  R$450 deverá ser cobrado para cada parcela em aberto com data de vencimento posterior a data de inclusão da disciplina, no caso parcela 5 e 6.**

| **Disciplina** | **Nº Crédito x Valor do Crédito** |  | **Parcelas** | **Vencimento** | **Valor de cada parcela** |
| --- | --- | --- | --- | --- | --- |
| Introdução a Ciência do Direito | 5 x 100 = 500 | 1 | 15/01/2020 | R$2.500(quitada) |
| Direito Civil I (Parte Geral I) | 5 x 100 = 500 | 2 | 15/02/2020 | R$2.500(quitada) |
| Ciência Política | 5 x 100 = 500 | 3 | 15/03/2020 | R$2.500(quitada) |
| Direito Penal I (Parte Geral I) | 5 x 100 = 500 | 4 | 15/04/2020 | R$2.500(quitada) |
| Teoria do Estado e da Constituição | 5 x 100 = 500 | 5 | 20/05/2020 | R$2.500 + **R$450** = R$2.950 |
| **Direito Tributário** | **3 x 150 = 450** | 6 | 20/06/2020 | R$2.500 + **R$450** = R$2.950 |

Cancelamento de disciplinas na matrícula do aluno

No dia o aluno cancelou a disciplina "X" da sua matricula, mas o seu contrato já existe quatro parcelas geradas e quitadas com data inferior a data de alteração.

Cancelamento Total - Abater em todas as parcelas

Quando na Situação de Matrícula a opção "**Abater valor da disciplina somente para parcelas com vencimento igual ou posterior a data de alteração da situação de matricula"** e "**Conta créditos financeiros (cobrança por crédito)"**estiver desmarcado.

A disciplina "**Introdução a Ciência do Direito**" para esse cenário foi cobrada da primeira á quarta parcela, porem foi alterado o status da disciplina para "Cancelamento total", como já existe cobranças anteriores ao cancelamento será gerado um crédito em função desse cancelamento e também não será cobrada nas parcelas em aberto.

Ficando assim:   
**- Valor da disciplina "Introdução a Ciência do Direito" é de RS500****- Valor total já cobrado no contrato RS500 x 4 (parcelas quitadas) = R$2.000****O valor de R$2.000 já cobrado pela disciplina será devolvido, neste caso o TOTVS Educacional divide o saldo entre as parcela não geradas ( R$2.000 / 2 = R$1.000).**

| **Disciplina** | **Nº Crédito x Valor do Crédito** |  | **Parcelas** | **Vencimento** | **Valor de cada parcela** |
| --- | --- | --- | --- | --- | --- |
| **Introdução a Ciência do Direito** | **5 x 100 = 500** | 1 | 15/01/2020 | R$2.500(quitada) |
| Direito Civil I (Parte Geral I) | 5 x 100 = 500 | 2 | 15/02/2020 | R$2.500(quitada) |
| Ciência Política | 5 x 100 = 500 | 3 | 15/03/2020 | R$2.500(quitada) |
| Direito Penal I (Parte Geral I) | 5 x 100 = 500 | 4 | 15/04/2020 | R$2.500(quitada) |
| Teoria do Estado e da Constituição | 5 x 100 = 500 | 5 | 20/05/2020 | R$2.000 - **R$1000**= R$1000 |
|  |  | 6 | 20/06/2020 | R$2.000 - **R$1000**= R$1000 |

Cancelamento Parcial - Abater apenas das parcelas em aberto com data posterior a data de alteração não terá a cobrança dessa disciplina

Quando altero a  [Situação de Matrícula](https://tdn.totvs.com/pages/viewpage.action?pageId=425458318)da disciplina para "Cancelamento Total"e o parâmetro "**Abater valor da disciplina somente para parcelas com vencimento igual ou posterior a data de alteração da situação de matricula"**estiver marcado na aba [Status na Disciplina](https://tdn.totvs.com/display/LRM/Status+na+Disciplina), nesse caso a disciplina na matricula do aluno terá o seu cancelamento parcial.

Então a disciplina "Introdução a Ciência do Direito" para esse cenário foi cobrada da primeira a quarta parcela, como o cancelamento da disciplina é parcial para as parcelas em aberto com data de vencimento posterior a data de cancelamento da disciplina não terá a cobrança dessa disciplina.

Para as parcelas em aberto será feito a cobrança somente das disciplinas que o aluno está cursando, desconsiderando o valor da disciplina cancelada.

Ficando assim 

**- Valor da disciplina "Introdução a Ciência do Direito" é de RS500**

**- O valor de  R$500 deverá ser desconsiderado para cada parcela em aberto com data vencimento posterior a data de cancelamento da disciplina, no caso parcela 5 e 6.**

| **Disciplina** | **Nº Crédito x Valor do Crédito** |  | **Parcelas** | **Vencimento** | **Valor de cada parcela** |
| --- | --- | --- | --- | --- | --- |
| **Introdução a Ciência do Direito** | **5 x 100 = 500** | 1 | 15/01/2020 | R$2.500(quitada) |
| Direito Civil I (Parte Geral I) | 5 x 100 = 500 | 2 | 15/02/2020 | R$2.500(quitada) |
| Ciência Política | 5 x 100 = 500 | 3 | 15/03/2020 | R$2.500(quitada) |
| Direito Penal I (Parte Geral I) | 5 x 100 = 500 | 4 | 15/04/2020 | R$2.500(quitada) |
| Teoria do Estado e da Constituição | 5 x 100 = 500 | 5 | 20/05/2020 | R$2.000 - **R$500**= R$1.500 |
|  |  | 6 | 20/06/2020 | R$2.000 - **R$500**= R$1.500 |

Exclusão de disciplinas na matrícula do aluno

No dia o aluno exclui a disciplina "X" da sua matricula, mas o seu contrato já existe quatro parcelas geradas e quitadas com data inferior a data de alteração.  
  
A disciplina "**Introdução a Ciência do Direito**" para esse cenário foi cobrada da primeira á quarta parcela, porem a disciplina foi excluída da matricula", como já existe cobranças anteriores a exclusão será gerado um crédito em função dessa exclusão e também não será cobrada nas parcelas em aberto.  
  
Ficando assim:   
**- Valor da disciplina "Introdução a Ciência do Direito" é de RS500****- Valor total já cobrado no contrato RS500 x 4 (parcelas quitadas) = R$2.000****O valor de R$2.000 já cobrado pela disciplina será devolvido, neste caso o TOTVS Educacional divide o saldo entre as parcela não geradas ( R$2.000 / 2 = R$1.000).**

| **Disciplina** | **Nº Crédito x Valor do Crédito** |  | **Parcelas** | **Vencimento** | **Valor de cada parcela** |
| --- | --- | --- | --- | --- | --- |
| **Introdução a Ciência do Direito** | **5 x 100 = 500** | 1 | 15/01/2020 | R$2.500(quitada) |
| Direito Civil I (Parte Geral I) | 5 x 100 = 500 | 2 | 15/02/2020 | R$2.500(quitada) |
| Ciência Política | 5 x 100 = 500 | 3 | 15/03/2020 | R$2.500(quitada) |
| Direito Penal I (Parte Geral I) | 5 x 100 = 500 | 4 | 15/04/2020 | R$2.500(quitada) |
| Teoria do Estado e da Constituição | 5 x 100 = 500 | 5 | 20/05/2020 | R$2.000 - **R$1.000**= R$1.000 |
|  |  | 6 | 20/06/2020 | R$2.000 - **R$1.000**= R$1.000 |

Mudança de turma/disciplina

No caso de o aluno mudar de turma e continuar matriculado na mesma disciplina, podemos ter as situações abaixo:

Cancelamento Total

Matrícula na disciplina **Ciência Política** da **TURMA A** e alteração do status dessa disciplina para **CANCELAMENTO TOTAL** ou mesmo a exclusão da disciplina.

* Inclusão da mesma disciplina **Ciência Política**da **TURMA B**que possui os mesmos valores de crédito. Nesta não foi marcada a opção de "Considerar no cálculo de cobrança somente para parcelas com vencimento igual ou posterior a data da matrícula"  sendo considerado como **AUMENTO TOTAL**

Nesse cenário, se existir parcelas já geradas que tiveram cobrança indevida ou deveriam ter o aumento da disciplina, seus respectivos créditos serão utilizados nas próximas parcelas e, ao mesmo tempo, gerado o aumento. Como não houve mudança de valor da disciplina nem no número de créditos, o valor do contrato permanece o mesmo.

* Inclusão da mesma disciplina **Ciência Política**da **TURMA B**que possui os mesmos valores de crédito. Nesta foi marcada a opção de "Considerar no cálculo de cobrança somente para parcelas com vencimento igual ou posterior a data da matrícula"  sendo considerado como **AUMENTO PARCIAL**

Nesse cenário, se existir parcelas já geradas que tiveram cobrança indevida, seus respectivos créditos serão utilizados nas próximas parcelas e, ao mesmo tempo, gerado o aumento. Para essa situação como o aumento é parcial e o cancelamento é total o valor do contrato não será o mesmo, pois teremos a devolução integral da disciplina cancelada e o aumento dependerá da data de vencimento e inclusão da disciplina.

Cancelamento Parcial

Matrícula na disciplina **Ciência Política** da **TURMA A** e alteração do status dessa disciplina para **CANCELAMENTO PARCIAL**.

* Inclusão da mesma disciplina **Ciência Política**da **TURMA B**que possui os mesmos valores de crédito. Nesta não foi marcada a opção de "Considerar no cálculo de cobrança somente para parcelas com vencimento igual ou posterior a data da matrícula" sendo considerado como **AUMENTO TOTAL**

Nesse cenário, se existir parcelas já geradas que deveriam ser considerados o aumento da disciplina, seus respectivos valores serão considerados nas próximas parcelas e, ao mesmo tempo, gerado o aumento. Para essa situação como o aumento é total o cancelamento é parcial o valor do contrato não será o mesmo, pois teremos a cobrança integral da disciplina e o cancelamento dependerá da data de vencimento e alteração de status da disciplina.

* Inclusão da mesma disciplina **Ciência Política**da **TURMA B**que possui os mesmos valores de crédito. Nesta não foi marcada a opção de "Considerar no cálculo de cobrança somente para parcelas com vencimento igual ou posterior a data da matrícula" sendo considerado como **AUMENTO PARCIAL**

Neste cenário, como o aumento é parcial  é parcial o valor do contrato poderá não será o mesmo, pois teremos a cobrança da disciplina e o cancelamento dependerá da data de vencimento e alteração de status da disciplina.

É através do detalhamento de cálculo da parcela que o TOTVS Educacional identifica se a disciplina foi cobrada ou não é qual valor já processado para a mesma.

No entanto dependendo de quando o lançamento foi gerado (versões mais antigas) as parcelas podem não possuir detalhamento, neste caso estas parcelas não serão consideradas na analise do sistema em caso de aumento, cancelamento e exclusão, ou seja, não é possível saber se a disciplina já foi cobrada.
