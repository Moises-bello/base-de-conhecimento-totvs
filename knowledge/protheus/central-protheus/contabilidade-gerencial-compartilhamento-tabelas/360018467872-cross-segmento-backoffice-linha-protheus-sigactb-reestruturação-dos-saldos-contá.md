---
article_id: 360018467872
category: Contabilidade Gerencial - Compartilhamento Tabelas
content_hash: f32eed02d398651c62bb9f86ba35beed7fb8da1c406bd9186624d1868e7307c6
fetched_at: '2026-06-28T22:40:57.861068+00:00'
product: protheus
section_id: 1500001537461
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB: Reestruturação dos Saldos
  Contábeis'
type: support-article
updated_at: '2024-03-12T23:34:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018467872-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Reestrutura%C3%A7%C3%A3o-dos-Saldos-Cont%C3%A1beis
---

**Dúvida**Reestruturação dos Saldos Contábeis

**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
  
**Solução**

Os saldos contábeis foram reinscrito, pois,  as rotinas de saldo com lançamento retroativo de um grande período demandavam muito processamento e tempo do sistema.

Exemplo  : Se tivéssemos que fazer um lançamento retroativo pela versão Protheus 11 o tempo de processamento  é bem maior que na versão Protheus 12.

Conforme pode ser visto na tela abaixo na versão 11 tínhamos 11 tabelas 8 campos como saldo atual, saldo anterior, movimento e movimento por período que totalizavam 88 operações distintas isto para cada transição.

Na Versão 12,   não tem  saldo a cada dia, passou  a ter 2 tabelas que são  : (4 tabelas mensais e 4 quatro tabelas diárias) para as quatro entidades, gravando dois valores Debito e Crédito.

A reestruturação das tabelas de saldo possui os seguintes objetivos:

* Composição de saldos de forma mais simples;
  + Tabelas normalizadas;
  + Ganho de desempenho para leitura/escrita nos bancos;
  + Diminuição do tempo de inclusão de lançamentos contábeis.

### **A premissa para essa reestruturação é a versão 12 que não terá mais tratamento para bancos não relacionais (Codebase).**

                Na versão  P11 do produto Microsiga Protheus, o ambiente Contabilidade Gerencial possui as seguintes tabelas para gravação e consulta de saldos contábeis:

* Abaixo encontra-se detalhado  a estrutura das tabelas na Versão P11, e em seguida estão as estruturas das tabelas na versão P12

# **Versão P11 -****Estrutura de tabelas**

|  |  |  |
| --- | --- | --- |
| **TABELA DE SALDOS BÁSICOS** | | |
| **Tabela** | **Versão** | **Descrição** |
| CT2 | **P11** | Lançamentos Contabeis |
| CT3 | **P11** | Saldos de Centro de Custos |
| CT4 | **P11** | Saldos de Item contábil |
| CT6 | **P11** | Totais de Lotes |
| CT7 | **P11** | Saldos de Planos de Contas |
| CTI | **P11** | Saldos da Classe de Valores |
| CTC | **P11** | Saldos do Documento |

|  |  |  |
| --- | --- | --- |
| **TABELA DE SALDOS COMPOSTOS** | | |
| **Tabela** | **Versão** | **Descrição** |
| CTU | **P11** | Grupos Contábeis |
| CTV | **P11** | Saldo Itens X Centro de Custo |
| CTW | **P11** | Saldos Cl Valor X Centro de Custo |
| CTX | **P11** | Saldos Cl Valor X Item |
| CTY | **P11** | Saldos Ccusto X Item X Cl Valor |

|  |  |  |
| --- | --- | --- |
| **TABELA DE SALDOS DAS NOVAS ENTIDADES CONTÁBEIS** | | |
| **Tabela** | **Versão** | **Descrição** |
| CVX | **P11** | Saldos Diários |
| CVY | **P11** | Saldos Mensais |

Todas as tabelas de saldo possuem os seguintes conceitos em suas estruturas:

* Registro do saldo diário.
* Quando não tiver movimento no dia, não é gravada a informação saldo.
* Em todas as linhas de registros constam os seguintes valores:
  + Saldo Débito (D): Soma dos valores de débito no dia para a entidade.

* Saldo Crédito (C): Soma dos valores de crédito no dia para a entidade.
* Saldo Atual Débito(D): Soma de todos os valores de débitos até o dia (inclusive o dia) para a entidade.
* Saldo Atual Crédito(C): Soma de todos os valores de crédito até o dia (inclusive o dia) para a entidade.
* Saldo Anterior a Débito(D): Soma de todos os valores de débito até o dia anterior para a entidade.  
  + Saldo Anterior a Crédito(C): Soma de todos os valores de crédito até o dia anterior para a entidade.  
    
    
    
    
    
  Em uma situação aonde o usuário incluiria um lançamento no dia 26/01 o sistema processa o cálculo de **6** campos de valores para incluir um novo registro na tabela de saldo por conta.Nessa situação de gravação de lançamento o sistema precisa realizar mais 8 operações totalizando 14 operações.Se adicionarmos as outras entidades contábeis e em um lançamento retroativo de 90 dias temos a seguinte quantidade de operações:
  + Atualização 11 tabelas
  + 6 campos por tabelas
  + 90 dias
  + Total aproximando de **5940** operações.  
  perda de desempenho e serialização da gravação no banco de dados (no caso de múltiplos usuários estarem gravando ao mesmo tempo).
* Em uma realidade de milhares de registros de lançamento contábeis, verificamos que a estrutura atual não é escalável, provocando
* Em outra situação que o usuário precise incluir um lançamento retroativo no dia 03/01/2013, o sistema precisa realizar o mesmo cálculo de 6 campos para incluir o registro do saldo nesse dia. Porém ele precisa recalcular e atualizar os registros de saldos dos dias 15/01 e 25/01, pois os campos de saldo atual D/C e saldo anterior D/C estarão desatualizados.
* |  |  |  |  |  |  |  |  |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | **Data** | **Conta** | **Saldo a Débito** | **Saldo a Crédito** | **Saldo Atual Débito** | **Saldo Atual Crédito** | **Saldo Anterior Débito** | **Saldo Anterior Crédito** |
  | **01/01/2013** | 11001 | 100.000,00 | 0 | 100.000,00 | 0 | 0 | 0 |
  | **02/01/2013** | 11001 | 0 | 10.000,00 | 100.000,00 | 10.000,00 | 100.000,00 | 0 |
  | **15/01/2013** | 11001 | 0 | 5.000,00 | 100.000,00 | 15.000,00 | 100.000,00 | 10.000,00 |
  | **25/01/2013** | 11001 | 50.000,00 | 0 | 150.000,00 | 15.000,00 | 100.000,00 | 15.000,00 |
* O sistema irá calcular os saldos das contas e os registrará na tabela CT7 - Saldos por conta. O registro da conta Caixa (11001) ficará conforme o quadro a seguir:
* DATA

  CONTA DEBITO

  CONTA CREDITO

  VALOR

  HISTORICO

  | 01/01/2013 | 11001 | 23001 | 100.000,00 | Constituição da Empresa |
  | 02/01/2013 | 12001 | 11001 | 10.000,00 | Compra de Imobilizado para Operações |
  | 15/01/2013 | 31003 | 11001 | 5.000,00 | Pagamento de Conta de Luz |
  | 25/01/2013 | 11001 | 41002 | 50.000,00 | Prestação de Serviços |
* Uma empresa possui os seguintes lançamentos contábeis no sistema:
* Um exemplo dessa situação:
* A estrutura atual foi concebida com o objetivo de priorizar a consulta das informações utilizando os métodos de pesquisa codebase que consiste da pesquisa direta do registro utilizando a sua chave de busca (comando dbseek), porém, essa estrutura colocava a maior carga de processamento na operação de gravação, principalmente no processamento dos campos de saldo atual D/C e saldo anterior D/C.

# **Versão P12 -****Estrutura de tabelas**

Ao  alterar a estrutura atual da  P11  de saldos contábeis tem  como o objetivo  diminuir a quantidade de operações na gravação de saldos contábeis, e consequente anormalização das tabelas, garantindo uma melhor utilização dos recursos dos bancos de dados relacionais. Com a evolução do sistema na versão 12, não teremos  mais a codificação para bases codebase.

Sendo assim simplificaremos  os códigos fontes atuais de consulta e gravação de saldos e utilizando melhor os recurso dos banco de dados relacionais.

Abaixo  a estrutura das tabelas na versão P12

|  |  |  |
| --- | --- | --- |
| **TABELAS DE SALDOS BÁSICOS** | | |
| **Tabela** | **Versão** | **Descrição** |
| CQ1 | **P12** | Saldo por Conta no Dia |
| CQ0 | **P12** | Saldo por Conta no Mês |
| CQ3 | **P12** | Saldo por Centro de Custo no Dia |
| CQ2 | **P12** | Saldo por Centro de Custo no Mês |
| CQ5 | **P12** | Saldo Item Contábil no Dia |
| CQ4 | **P12** | Saldo Item Contábil no Mês |
| CQ6 | **P12** | Saldo Classe de Valor no Mês |
| CQ7 | **P12** | Saldo Classe de Valor no Dia |

|  |  |  |
| --- | --- | --- |
| **TABELAS DE SALDOS COMPOSTOS** | | |
| **Tabela** | **Versão** | **Descrição** |
| CQ9 | **P12** | Saldo por Entidade no Dia |
| CQ8 | **P12** | Saldos por Entidade no Mês |

|  |  |  |
| --- | --- | --- |
| **TABELA PROCESSAMENTO EM FILA** | | |
| **Tabela** | **Versão** | **Descrição** |
| CQA | **P12** | Fila de Saldos |

**Importante :** A partir da versão 12 as  tabelas abaixo  serão descontinuadas:

Tabela de Saldos Básicos

|  |  |
| --- | --- |
| **Tabela** | **Descrição** |
| CT7 | Saldo por Conta |
| CT3 | Saldo por Centro de Custo |
| CT4 | Saldo por Item Contábil |
| CTI | Saldo por Classe de Valor |
| CT6 | Saldo por Lote |

Tabela de Saldos Compostos

|  |  |
| --- | --- |
| **Tabela** | **Descrição** |
| CTU | Saldo por Entidade Gerencial |
| CTV | Saldo Item + Centro de Custo |
| CTW | Saldo Classe Valor + Centro de Custo |
| CTX | Saldo Classe de Valor + Item Contábil |
| CTY | Saldo Centro de Custo + Item Contábil + Classe de Valor |

Tabela para processamento em Fila

|  |  |
| --- | --- |
| **Tabela** | **Descrição** |
| CVO | Fila de Saldos |

A tabela de saldos por documento contábil será mantida e terá o papel de tabela de cabeçalho do lançamento contábil (CT2).

As tabelas de saldos das Novas Entidades Contábeis serão mantidas e não terão alteração na sua gravação/consulta.

As novas tabelas de saldos terão os seguintes conceitos na sua estrutura :

* Registro do saldo diário nas tabelas de saldos diários
* Registro do saldo mensal nas tabelas de saldos mensais, somando os valores dos saldos diários no período.
  + Para facilitar na montagem das queries e procedures, as tabelas de saldos mensais terão o campo que identifica o período com o tipo data e terá como conteúdo sempre o primeiro dia do mês.

* Quando não tiver movimento no dia, não será gravada a informação de saldo no dia.
* Em todas as linhas de registros constarão os seguintes valores:
  + Saldo Débito (D): Soma dos valores de débito no dia para a entidade.
  + Saldo Crédito (C): Soma dos valores de crédito no dia para a entidade.

Para ilustrar o ganho com essa nova estrutura, vamos utilizar o exemplo anterior:

Uma empresa possui os seguintes lançamentos contábeis no sistema:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Data** | **Conta Débito** | **Conta Crédito** | **Valor** | **Histórico** |
| **01/01/2013** | 11001 | 23001 | 100.000,00 | Constituição da empresa |
| **02/01/2013** | 12001 | 11001 | 10.000,00 | Compra de Imobilizado para operações |
| **15/01/2013** | 31003 | 11001 | 5.000,00 | Pagamento de conta de Luz |
| **25/01/2013** | 11001 | 41002 | 50.000,00 | Prestação de serviços |

O sistema irá calcular os saldos das contas e os registrará na tabela CQ0 - Saldo por conta no Mês e CQ1 – Saldo por Conta No Dia. O registro da conta Caixa (11001) ficará conforme os quadros a seguir:

|  |  |  |  |
| --- | --- | --- | --- |
| **CQ0 - Saldo por conta no Mês** | | | |
| **Data** | Conta | Saldo a Débito | Saldo a Crédito |
| **01/01/2013** | 11001 | 150.000,00 | 15.000,00 |

|  |  |  |  |
| --- | --- | --- | --- |
| **CQ1 – Saldo por Conta No Dia** | | | |
| **Data** | Conta | Saldo a Débito | Saldo a Crédito |
| **01/01/2013** | 11001 | 100.000,00 | - |
| **02/01/2013** | 11001 | - | 10.000,00 |
| **15/01/2013** | 11001 | - | 5.000,00 |
| **25/01/2013** | 11001 | 50.000,00 | - |

Em uma situação aonde o usuário incluiria um lançamento no dia 26/01 o sistema irá processar o cálculo de **4** campos de valores para incluir um novo registro na tabela de saldo por conta no Dia e no Mês.

**Em outra situação que o usuário precise incluir um lançamento retroativo no dia 03/01/2013, o sistema realizará o mesmo cálculo**

de 4 campos para incluir os registros do saldo nesse dia. Com a estrutura proposta o sistema **não** precisará realizar o cálculo ou atualização de **nenhum** outro dia.

Se adicionarmos as outras entidades contábeis e em um lançamento retroativo de 90 dias temos a seguinte quantidade de operações:

* Atualização 10 tabelas
* 2 campos por tabelas
* 90 dias

* Total de **20** operações, pois será necessário atualizar o saldo somente do dia e do mês que foi incluído o registro.

Na estrutura proposta, independentemente da quantidade de dias para o lançamento retrocedente, a quantidade de operações se manterá a mesma.

A lógica para consulta de saldos nessa nova estrutura deverá ser alterada utilizando query para retornar os valores de saldo de uma conta.

1. Será realizada uma query utilizando a função SUM para trazer a soma de todos os saldos **mensais** até o mês anterior do saldo que se deseja a consulta.
2. Será realizada uma query utilizando a função SUM para trazer a soma dos saldos diários do primeiro dia do período até o dia do saldo que se deseja a consulta.

3. O **saldo atual D/C** será a soma do resultado do passo 1 com o passo 2

4. Será realizada uma query utilizando a função SUM para trazer a soma dos saldos diários do primeiro dia do período até o dia**anterior** do saldo que se deseja a consulta.
5. O **saldo anterior D/C** será a soma do resultado do passo 1 com o passo 4

Utilizando os dados do exemplo anterior, para a consulta do saldo da conta no dia 15/01/13, o sistema irá realizar os seguintes procedimentos:

* Soma dos saldos mensais até o mês de dezembro de 2012

**Importante :**Na nova estrutura proposta, apenas teremos como tabelas de saldos compostos a CQ8 e CQ9 que corresponde na estrutura antiga à tabela CTU - Saldo por Entidade Gerencial.

* Total de **20** operações, pois será necessário atualizar o saldo somente do dia e do mês que foi incluído o registro.

Na estrutura proposta, independentemente da quantidade de dias para o lançamento retrocedente, a quantidade de operações se manterá a mesma.
