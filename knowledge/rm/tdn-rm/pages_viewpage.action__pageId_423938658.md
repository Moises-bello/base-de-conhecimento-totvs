---
content_hash: 4b1660518c617e02d6dfff7c600c781e8ba6f87063c67ac0746458c8e29460af
fetched_at: '2026-06-29T00:09:28.113970+00:00'
page_id: '423938658'
product: rm
source: tdn-rm
title: Execução da Distribuição Gerencial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938658
version: 4
---

Através deste processo é possível modificar a distribuição gerencial de determinados lançamentos de forma global tendo como opção os itens relatados a seguir. Inicialmente temos que informar os parâmetros para que o sistema altere a distribuição conforme desejado.  
   
**1ª Etapa: Informar Parâmetros**  
   
Para executar o processo de Distribuição Gerencial é obrigatório informar pelo menos um lote contábil, que pode ser o lote 0 ou lote N e não pode estar bloqueado. Caso o lote esteja bloqueado, o sistema estará informando que não será possível alterar os lançamentos do lote selecionado.   
   
Ao selecionar o lote contábil, o período é alterado conforme o intervalo de datas dos lançamentos contábeis que se encontram nos lotes selecionados. Este período pode ser alterado conforme desejado. Mas o processo estará verificando o período conforme as seguintes condições:  
   
Período Contábil informado nos parâmetros do sistema Data de Fechamento informado nos parâmetros do sistema Período de digitação de lançamentos do usuário no sistema   
   
Caso o processo viole qualquer uma destas condições, o processo não será executado.   
   
No filtro de **Faixa de Contas** estaremos informando quais contas contábeis serão afetados pelo processo de distribuição selecionado. Se este filtro não for selecionado, o processo será executado para todas as contas do lote contábil selecionado.  
   
Podemos selecionar quais filiais terão os seus lançamentos afetados pelo processo de distribuição selecionado através do filtro. Se este filtro não for selecionado, o processo será executado para todas as filiais que estão informados nos lançamentos disponíveis no lote selecionado.  
   
É possível também filtrar os lançamentos que serão alterados pelo processo de distribuição gerencial através do centro de custo informado nestes lançamentos. Desta forma apenas os lançamentos que possuem os centros de custos informados como parâmetros deste processo terão a sua distribuição gerencial alterada através deste processo.   
   
Já no filtro genérico podemos buscar algumas informações que ajudarão a selecionar os lançamentos que serão alterados através do processo de distribuição gerencial. Desta forma como exemplo, podemos filtrar os lançamentos pelo o ID do Lançamento e ID da Partida, entre outras.

**2ª Etapa: Selecionar Forma de Distribuição Gerencial**  
   
Através deste processo será possível modificar a distribuição gerencial de determinados lançamentos de forma global tendo como opção os itens relatados a seguir.  
   
***Observação**: A distribuição a ser aplicada será feita individualmente para cada lançamento conforme os parâmetros informados na 1ª etapa.*

**Distribuição Gerencial do Plano de Contas**

Com esta opção selecionada a distribuição será refeita conforme a distribuição gerencial definida no cadastro do Plano de Contas. Nesta opção não é possível selecionar uma estrutura e serão alteradas as distribuições gerenciais dos lançamentos que possuem em suas contas contábeis, a débito ou a crédito, contas gerenciais informadas como default.

**Informar Distribuição Gerencial**

Com esta opção selecionada a distribuição gerencial será alterada conforme a distribuição a ser informada pelo usuário. Nesta opção poderemos executar o processo de duas formas: Por meio de uma estrutura pré-gravada ou informando a distribuição manualmente.

Se utilizar neste processo uma estrutura pré-gravada, temos que ter cadastrado inicialmente uma estrutura da forma desejada com as devidas distribuições gerenciais cadastrados nos moldes.  
  
**Atenção:** Se a estrutura informada possuir o parâmetro "Usar Contas Contábeis" habilitado, apenas os lançamentos que estiverem de acordo com os parâmetros informados na 1ª etapa e possuírem estas contas contábeis informadas nos moldes desta estrutura terão as suas distribuições gerenciais alteradas. Caso o parâmetro "Usar Contas Contábeis" estiver desabilitado, todos os lançamentos que estiverem de acordo com os parâmetros informados na 1ª etapa terão a sua distribuição gerencial alterada.  
  
Caso a estrutura selecionada esteja com o parâmetro "Usar Contas Contábeis" habilitado, no campo "Conta Contábil" é possível selecionar uma conta e verificar a distribuição que se encontra no molde que possui esta conta. Mas este campo não possibilita que seja escolhido um molde para a execução do processo. Desta forma este campo é apenas informativo para esta consulta.  
  
Se a distribuição for informada manualmente, será necessário informar as contas gerenciais desejadas com os respectivos percentuais. Desta forma todos os lançamentos que estiverem de acordo com os parâmetros informados na 1ª etapa terão a sua distribuição gerencial alterada.  
  
***Observação*:** A distribuição gerencial informada manualmente deve fechar em 100%. Caso esta distribuição gerencial esteja diferente de 100%, o processo não poderá ser executado.

**Troca de Contas Gerenciais**

Com esta opção selecionada é possível definir qual conta gerencial será trocada e qual conta irá substituir a mesma. Desta forma é possível informar na lista vários tipos de trocas ou trocar varias contas para apenas uma conta gerencial.   
  
Exemplo 1:

No lote 1 informado no parâmetro do processo, existia a o seguinte lançamento:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Lançamento | Partida | Conta Contábil | Valor | Conta Gerencial | Percentual |
| 1 | 1 | 1.1.1.1.001 | 500 | **5.01** | 100% |

Estaremos trocando a distribuição das partidas do lote 1 da seguinte forma:  
  
Conta Origem: 5.01               Conta Destino: 5.05  
  
Assim esta partida foi alterada da seguinte forma:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Lançamento | Partida | Conta Contábil | Valor | Conta Gerencial | Percentual |
| 1 | 1 | 1.1.1.1.001 | 500 | **5.05** | 100% |

**Exemplo 2:**  
  
Vamos informar na lista duas contas gerenciais que serão trocadas:  
  
Conta Origem: 5.01               Conta Destino: 5.05  
Conta Origem: 5.02               Conta Destino: 5.10  
  
Desta forma no lote que informamos nos parâmetros do processo, existem dois lançamentos, com as partidas da seguinte forma:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Lançamento | Partida | Conta Contábil | Valor | Conta Gerencial | Percentual |
| 1 | 1 | 1.1.1.1.001 | 500 | **5.01** | 50% |
|  |  |  |  | **5.03** | 50% |
| 2 | 1 | 1.1.1.1.005 | 1000,00 | **5.02** | 100% |

Após a execução deste processo, os lançamentos estarão da seguinte forma:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Lançamento | Partida | Conta Contábil | Valor | Conta Gerencial | Percentual |
| 1 | 1 | 1.1.1.1.001 | 500 | **5.05** | 50% |
|  |  |  |  | **5.03** | 50% |
| 2 | 1 | 1.1.1.1.005 | 1000,00 | **5.10** | 100% |

**Exemplo 3:**

Vamos informar na lista duas contas gerenciais que serão trocadas:

Conta Origem: 5.01               Conta Destino: 5.05  
Conta Origem: 5.02               Conta Destino: 5.05  
  
Desta forma no lote que informamos nos parâmetros do processo, existe um lançamento, com a partida da seguinte forma:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Lançamento | Partida | Conta Contábil | Valor | Conta Gerencial | Percentual |
| 1 | 1 | 1.1.1.1.001 | 500 | **5.01** | 50% |
|  |  |  |  | **5.02** | 50% |

Após a execução deste processo, os lançamentos estarão da seguinte forma:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Lançamento | Partida | Conta Contábil | Valor | Conta Gerencial | Percentual |
| 1 | 1 | 1.1.1.1.001 | 500 | **5.05** | 100% |

**Redistribuir uma Conta Gerencial**

Com esta opção selecionada é possível redistribuir os valores de uma conta gerencial para outras contas gerenciais. Neste processo é possível informar a distribuição manualmente ou utilizar uma estrutura pré-gravada cadastrada inicialmente.

É preciso informar inicialmente a conta que será redistribuída e depois selecionar a forma de redistribuição. Se utilizar neste processo uma estrutura pré-gravada, temos que ter cadastrado inicialmente uma estrutura com moldes que pode possuir uma ou mais contas gerenciais com os seus respectivos percentuais para a distribuição.

Quando a estrutura selecionada possui o parâmetro "Usar Contas Contábeis", no campo "Conta Contábil" é possível selecionar a uma conta e verificar a distribuição que se encontra no molde que possui esta conta. Mas este campo não possibilita que seja escolhido um molde para a execução do processo. Desta forma este campo é apenas informativo para esta consulta.

***Atenção*:** Se a estrutura informada possuir o parâmetro "Usar Contas Contábeis" habilitado, apenas os lançamentos que estiverem de acordo com os parâmetros informados na 1ª etapa e possuírem estas contas contábeis informadas nos moldes desta estrutura terão as suas distribuições gerenciais alteradas.  Caso o parâmetro "Usar Contas Contábeis" estiver desabilitado, todos os lançamentos que estiverem de acordo com os parâmetros informados na 1ª etapa terão a sua distribuição gerencial alterada.  
  
Se a distribuição for informada manualmente, será necessário informar as contas gerenciais desejadas com os respectivos percentuais. Desta forma todos os lançamentos que estiverem de acordo com os parâmetros informados na 1ª etapa terão a sua distribuição gerencial alterada.  
  
***Observação***: A distribuição gerencial informada manualmente deve fechar em 100%. Caso esta distribuição gerencial esteja diferente de 100%, o processo não poderá ser executado.  
  
Abaixo estão mais exemplos para explicar o processo:

**Exemplo 1:**

No lote que informamos nos parâmetros do processo, existe um lançamento, com a partida da seguinte forma:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Lançamento | Partida | Conta Contábil | Valor | Conta Gerencial | Percentual |
| 1 | 1 | 1.1.1.1.001 | 500 | **5.01** | 100% |

Desta forma foi informada manualmente a seguinte distribuição:  
Conta Gerencial: 5.01  
Distribuição gerencial:

|  |  |
| --- | --- |
| Conta Gerencial | Percentual |
| 5.02 | 25% |
| 5.03 | 50% |
| 5.04 | 25% |

Após a execução deste processo, os lançamentos estarão da seguinte forma:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Lançamento | Partida | Conta Contábil | Valor | Conta Gerencial | Percentual |
| 1 | 1 | 1.1.1.1.001 | 500 | **5.02** | 25% |
|  |  |  |  | **5.03** | 50% |
|  |  |  |  | **5.04** | 25% |

**Exemplo 2:**

No lote que informamos nos parâmetros do processo, existe um lançamento, com a partida da seguinte forma:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Lançamento | Partida | Conta Contábil | Valor | Conta Gerencial | Percentual |
| 1 | 1 | 1.1.1.1.001 | 500 | **5.01** | 50% |
|  |  |  |  | **5.02** | 50% |

Desta forma foi informada manualmente a seguinte distribuição:  
Conta Gerencial: 5.02  
Distribuição gerencial:

|  |  |
| --- | --- |
| Conta Gerencial | Percentual |
| 5.02 | 25% |
| 5.03 | 50% |
| 5.04 | 25% |

Após a execução deste processo, os lançamentos estarão da seguinte forma:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Lançamento | Partida | Conta Contábil | Valor | Conta Gerencial | Percentual |
| 1 | 1 | 1.1.1.1.001 | 500 | **5.01** | 50% |
|  |  |  |  | **5.02** | 12,5% |
|  |  |  |  | **5.03** | 25% |
|  |  |  |  | **5.04** | 12,5% |

Percebe-se que a conta 5.02 foi redistribuída, conforme informado na distribuição gerencial.

**Exemplo 3:**

No lote que informamos nos parâmetros do processo, existe um lançamento, com a partida da seguinte forma:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Lançamento | Partida | Conta Contábil | Valor | Conta Gerencial | Percentual |
| 1 | 1 | 1.1.1.1.001 | 500 | **5.01** | 50% |
|  |  |  |  | **5.02** | 50% |

Desta forma foi informada manualmente a seguinte distribuição:  
Conta Gerencial: 5.02  
Distribuição gerencial:

|  |  |
| --- | --- |
| Conta Gerencial | Percentual |
| 5.03 | 25% |
| 5.04 | 50% |
| 5.05 | 25% |

Após a execução deste processo, os lançamentos estarão da seguinte forma:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Lançamento | Partida | Conta Contábil | Valor | Conta Gerencial | Percentual |
| 1 | 1 | 1.1.1.1.001 | 500 | **5.01** | 50% |
|  |  |  |  | **5.03** | 12,5% |
|  |  |  |  | **5.04** | 25% |
|  |  |  |  | **5.05** | 12,5% |

Desta forma percebe-se que a conta gerencial 5.02 foi redistribuída para as contas 5.03, 5.04 e 5.05.

**3ª Etapa: Execução do Processo**

Após a indicação dos dados para o processo que estará alterando a distribuição gerencial, estaremos executando o processo propriamente dito. Se a execução ocorrer com sucesso, o sistema estará mostrando um log informando quais lançamentos e partidas tiveram as distribuições gerenciais alteradas.

Caso na primeira etapa tenha sido informado algum filtro e o sistema não localize lançamentos e partidas que atendam as condições informadas, o processo estará informando que não foi encontrado nenhum registro para que a distribuição gerencial seja alterada.  
  
Desta forma ao verificar a pasta de rateio dos lançamentos mostrados no log do processo, veremos que as informações estarão alteradas conforme a distribuição gerencial executada.
