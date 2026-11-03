---
content_hash: f408037091ea84f93ccbe93603213291b89dbd7329df44d5d9883dd8fd691f27
fetched_at: '2026-06-29T00:09:10.811931+00:00'
page_id: '403048875'
product: rm
source: tdn-rm
title: Contratos - Medições a PI (Preço Inicial), R (Reajuste) ou PI + R (Preço Inicial
  + Reajuste)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=403048875
version: 166
---

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Obras e Projetos |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Medição/Consumo de Contrato | PrjContratoMedirItemAction / PrjContratoDeMaterialConsumirObjAction | |
| **Parâmetro(s):** | Utilizar Valor do Reajuste na Medição (PI + R) |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | TOPEXECONTROL01-4339  TOPEXECONTROL01-3815 |
| **Tabelas Utilizadas:** | MTRFMED, MOBJCNTMED |

## Objetivo

Para os contratos a receber e a pagar com as finalidades Serviços, Insumos e Extra-Histograma, o TOTVS Obras e Projetos permitir a informação dos valores medidos/consumidos do preço inicial contratado e do reajuste dos itens/objetos separadamente.

*.*

### Definição da Regra de Negócio

As medições de serviço e consumo de objetos dos Contratos de Serviços, Insumos e Extra-Histograma permitirão realizar medição/consumo em PI (Preço Inicial), R (Reajuste) ou PI+R (Preço Inicial + Reajuste).

00ParâmetrosParâmetros de Projeto

Para usar o recurso de medição/consumo é necessário parametrizar o Totvs Obras e Projetos para utilizar o valor do reajuste na medição/consumo (PI + R).

Para habilitar o parâmetro acesse o Menu Principal do Totvs Obras e Projetos em "Projeto | Construção e Projetos | Projetos (F6)".

Para os projetos que possuem contratos com o Tipo de Reajuste igual a **"Por Contrato"** e a Aplicação do Reajuste igual a **"Valor Atual"** o parâmetro de "Utiliza Valor Do Reajuste Na Medição (PI + R)" estará desabilitado para marcação.

Veja como o parâmetro fica caso existam tais contratos

Na tela de parâmetros de projeto acesse "Contratos | Geral", ative o parâmetro **“Utilizar Valor do Reajuste na Medição (PI + R) ”**.

Efeito do parâmetro ao ser ativado:

* Na tela de contratos, serão apresentados alguns campos de valores de contrato.

**Valor Calculado Reajuste**: É o valor total do reajuste calculado de todos os períodos do contrato.

**Valor Medido Reajuste**: É o valor total de reajuste medido/consumido no contrato.

**Saldo Reajuste:** É o saldo disponível para ser medido/consumido no contrato.

* Na tela de medição de contrato e consumo de objetos serão apresentados algumas colunas referentes ao Reajuste.

41

Para saber mais sobre os contratos que utilizam Medição de Itens clique aqui.

61

Para saber mais sobre os contratos que utilizam Consumo de Objetos clique aqui.

Importante

* Para os projetos em que o parâmetro não estiver marcado, o sistema irá manter seu comportamento atual.
* Com o parâmetro marcado os contratos que possuem períodos já liberados, ao realizar o processo de reajuste o sistema não irá criar períodos de reajustes. O processo de reajuste para os contratos que possuem períodos já liberados irá gerar saldo sobre o valor medido e nos períodos posteriores ao realizar a medição será possível verificar na coluna o Saldo do Reajuste o valor relativo ao período liberado.
* Vale salientar que, para projetos configurados para utilizar a medição/consumo em PI, R ou PI + R, o parâmetro “Permitir medição/consumo superior a 100%” caso definido como “Sempre Permitir” ou “Permitir com Senha”, passa a considerar o saldo do contrato apenas em valor, ou seja, não será consistido o saldo em quantidade.
* Ao marcar o parâmetro, somente será permitido a inclusão de contratos com a aplicação de reajuste à "**Valor Unitário Inicial**" e Tipo de reajuste "**Por Item Associado**".
* É necessário a execução do processo atualizar informações do contrato para liberação de reajuste e medição de contratos que já possuem medição realizada.

  01Para mais informações clique aqui.
1Ajuste Legado

Para os contratos que não possuem o reajuste discriminado por PI, R ou PI + R o ajuste da conversão será feito através do processo de **"Atualizar Valor medido Preço inicial e Valor medido Reajuste do Contrato"** desta forma é necessário habilitar o parâmetro de **Utilizar Valor do Reajuste na Medição (PI + R).**

Após habilitar o parâmetro acesse o menu **Executar** localizado no canto direito da tela, em seguida pesquise por  "**Atualizar Valor medido Preço inicial e Valor medido Reajuste do Contrato**" .

Veja como acessar a tela de Atualizar informações de Valor Medido Preço Inicial e Valor Medido Reajuste do contrato 

Na tela de "**Atualizar Valor medido Preço inicial e Valor medido Reajuste do Contrato**", serão apresentados todos os contratos que já sofreram reajustes a Preço Inicial e Valor Atual.

Para contratos que estavam configurados para que seus reajustes fossem sobre o **Valor Atual**, será feito a conversão dos percentuais para que seja calculado de forma correta o fator de reajuste considerando agora o **Valor Inicial (PI).**

Veja o exemplo

O contrato de serviço de Num. Contrato "1" e o contrato de insumo de Num. Contrato "2" são apresentados na tela de **Atualizar Informações de Valor Medido Preço Inicial e Valor Medido Reajuste do contrato**, porque possuem reajuste realizado.

Ao avançar a tela selecionando o Num. Contrato "2" é apresentado todos os períodos liberados e medidos/consumidos.

Os períodos são separados por insumo (contrato de insumo), código da tarefa (contrato de insumo e serviço) e tipo do período (estorno, complementar, normal ou período de reajuste ).

Veja o exemplo

Na etapa de **Atualizar informações do contrato**, deve-se informar os valores correspondentes ao que é **PI** e o que é **R**.

Ao informar o valor de R(campo Valor Medido Reajuste) ou PI(Campo Valor Medido Preço Inicial) automaticamente o campo Valor Medido Preço Inicial ou Valor Medido Reajuste (dependendo de qual campo foi preenchido) será calculado automaticamente com o valor da diferença.

**Por exemplo:**

O valor medido do período foi de R$ 200,00. Ao informar um Valor Medido Preço Inicial de R$ 120,00 automaticamente o campo de Valor Medido Reajuste será preenchido com a diferença entre o **Valor Medido** - **Valor Medido** Preço Inicial que é igual a R$ 80,00.

Veja o exemplo do preenchimento dos campos

**Valor Cálculo Reajuste:** (**Percentual reajuste (%)** \*  **Valor Medido Preço Inicial**)/100

**Valor Medido Preço Inicial:** Neste campo é informado o valor medido de preço inicial desejado. Ao preencher este campo, os campos Valor Cálculo Reajuste, Valor Medido Reajuste e Percentual Reajuste Medido (%) serão calculados automaticamente.

**Valor Medido Reajuste:** Neste campo é informado o valor medido de reajuste desejado. Ao preencher este campo, os campos Valor Cálculo Reajuste, Valor Medido Preço Inicial e Percentual Reajuste Medido (%) serão calculados automaticamente.

**Percentual reajuste medido (%):** Neste campo é informado o percentual de reajuste medido pago no Valor Medido Total. Ao preencher este campo, o campo Valor Medido reajuste será calculado automaticamente com base no preenchimento dos demais campos.

**Percentual reajuste (%):** É o percentual do reajuste aplicado para o período.

**Valor Medido:** É o valor total medido para uma determinada tarefa e insumo

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Contrato | Período | Insumo | Valor Medido | Código da Tarefa | Valor Cálculo Reajuste | Valor Medido Preço Inicial | Valor Medido Reajuste | Percentual reajuste medido (%) | Percentual reajuste (%) |
| 2 | 0001 | F00001 | 20 | 001.03.01 | 2,8 | 14 | 6 | 30 | 20 |
| 2 | 0001 | F00002 | 10 | 001.03.01 | 1 | 5 | 5 | 50 | 20 |
| 2 | 0001 | F00003 | 10 | 001.03.01 | 0,51378 | 2,5689 | 7,4311 | 74,311 | 20 |
| 2 | 0001 | F00004 | 2,37 | 001.03.01 | 0,4 | 2 | 0,37 | 15,61181435 | 20 |
| 2 | 0001R001 | F00001 | 3,96 | 001.03.01 | 0 | 0 | 3,96 | 100 | 20 |
| 2 | 0001R001 | F00002 | 1,96 | 001.03.01 | 0 | 0 | 1,96 | 100 | 20 |
| 2 | 0001R001 | F00003 | 2,01 | 001.03.01 | 0,202 | 1,01 | 1 | 49,75124378 | 20 |
| 2 | 0001R001 | F00004 | 0,51 | 001.03.01 | 0 | 0 | 0,51 | 100 | 20 |
| 2 | 0002 | F00004 | 20,36 | 001.03.01 | 0 | 0 | 20,36 | 100 | 10 |
| 2 | 0002 | M00001 | 23,65 | 001.03.03 | 2,36 | 23,6 | 0,05 | 0,21141649 | 10 |
| 2 | 0002 | M00002 | 13,65 | 001.03.02 | 1,365 | 13,65 | 0 | 0 | 10 |
| 2 | 0002C001 | M00001 | 3,27 | 001.03.03 | 0,3 | 3 | 0,27 | 8,256880734 | 10 |
| 2 | 0002R001 | F00004 | 4,12 | 001.03.01 | 0 | 0 | 4,12 | 100 | 10 |
| 2 | 0002R001 | M00001 | 5,39 | 001.03.03 | 0,009 | 0,09 | 5,3 | 98,33024119 | 10 |
| 2 | 0002R001 | M00002 | 2,73 | 001.03.02 | 0 | 0 | 2,73 | 100 | 10 |
| 2 | 0003 | F00004 | 282,05 | 001.03.01 | 20,005 | 200,05 | 82 | 29,07285942 | 10 |
| 2 | 0003 | M00001 | 4,64 | 001.03.03 | 0,4 | 4 | 0,64 | 13,79310345 | 10 |
| 2 | 0003C001 | F00004 | 6095,62 | 001.03.01 | 609,5 | 6095 | 0,62 | 0,010171238 | 10 |
| 2 | 0004 | F00001 | 2562,77 | 001.03.01 | 256,2 | 2562 | 0,77 | 0,030045615 | 10 |
| 2 | 0004 | M00002 | 57,74 | 001.03.02 | 5,7 | 57 | 0,74 | 1,281607205 | 10 |
| 2 | 0005 | F00003 | 172,98 | 001.03.01 | 12,036 | 120,36 | 52,62 | 30,4197017 | 10 |
| 2 | 0005 | F00004 | 1022,37 | 001.03.01 | 102,237 | 1022,37 | 0 | 0 | 10 |
| 2 | 0006 | M00001 | 495,44 | 001.03.03 | 49,2 | 492 | 3,44 | 0,694332311 | 10 |

Após a execução do processo de atualização dos valores do contrato, ao acessar os períodos e verificar o consumo os valores informados no processo serão apresentados corretamente conforme informado na tela de **Atualizar Informações de Valor Medido Preço Inicial e Valor Medido Reajuste do contrato.**

Veja um exemplo de como fica os valores após a execução do processo

O contrato de Num. Contrato: "**Exemplo**" possui reajuste de 10% para o primeiro período e 21% para o quarto período.

Os períodos 0001 ao período 0004 estão liberados e somente o período 0005 está consumido.

Ao acessar a tela de parâmetros de projetos F6 e habilitar o parâmetro **"Utilizar Valor do Reajuste na Medição (PI + R)"**, fica disponível o processo de "**Atualizar Informações de Valor Medido Preço Inicial e Valor Medido Reajuste do contrato**". Ao abrir a tela do processo, serão apresentados os contratos que podem ser convertidos para o reajuste discriminado.

Na etapa de Atualizar informações do contrato, foi informado os valores de Preço inicial e de Reajuste.

Após a execução do processo de **Atualizar Informações de Valor Medido Preço Inicial e Valor Medido Reajuste do contrato** foi acessado o período 0001 para verificar se os valores estão preenchidos corretamente conforme informado no processo de atualização.

Note que o Valor Medido (Inicial + Reajuste) está correto conforme o campo Valor medido do processo de atualizar e os Campo Valor Calculo Reajuste está igual ao campo Valor Calculado Reajuste, Campo Valor medido reajuste está igual ao Valor medido reajuste da tela de consumo de objetos e os percentuais estão corretos também conforme a tela de atualizar.

2Processo de Reajuste31Reajuste

**Reajuste**

1 - Criar um contrato, podendo ser do tipo de Serviço, Insumo ou Extra/Extra-Histograma.

2 - Definir na aba "**Reajuste**" do contrato o tipo de reajuste "**Por Item Associado**" e Aplicação do Reajuste: "**Valor Unitário Inicial"**.

3 - Realizar a associação dos itens/objetos ao contrato.

4 - Gerar os períodos para o contrato.

5 - Aplicar o reajuste para um ou mais itens associados ao contrato.

Selecione o contrato, em Processos | Reajuste do Item Associado | Reajustar Itens Associados ao Contrato.

Veja o exemplo

* + Ao abrir a tela do processo de "**Reajustar Itens Associados ao Contrato**" será apresentado no campo "**Períodos disponíveis**" o ultimo período disponível para realizar o reajuste.

Informações adicionais

Contrato de serviço, contrato de Insumo e contrato de Extra/Extra - Histograma:

* + - Ao aplicar o reajuste para os itens associados, o anexo de **itens do contrato** terá a coluna "**Valor Unitário Atual**" alterada para o novo valor unitário.
    - No anexo "**Reajuste do Item Associado**", é apresentado o valor do percentual do Reajuste aplicado (Coluna **Percentual Reajuste (%)**) para cada item associado.
    - No anexo "**Reajuste do Item Associado**", é apresentado o valor unitário anterior ao reajuste realizado (Coluna **Valor Anterior**).
2Deflação

**Deflação**

1 - Criar um contrato, podendo ser do tipo de Serviço, Insumo ou Extra/Extra-Histograma.

2 - Definir na aba "**Reajuste**" do contrato o tipo de reajuste "**Por Item Associado**" e Aplicação do Reajuste: "**Valor Unitário Inicial"**.

3 - Realizar a associação dos itens/objetos ao contrato.

4 - Gerar os períodos para o contrato.

5 - Aplicar o reajuste **negativo** para um ou mais itens associados ao contrato.

Selecione o contrato, em Processos | Reajuste do Item Associado | Reajustar Itens Associados ao Contrato.

Veja o exemplo

* + Ao abrir a tela do processo de "**Reajustar Itens Associados ao Contrato**" será apresentado no campo "**Períodos disponíveis**" o ultimo período disponível para realizar o reajuste.

Informações adicionais

Contrato de serviço, contrato de insumo, contrato de extra/extra-histograma:

* + Ao aplicar o reajuste para os itens associados, o anexo de **itens do contrato** terá a coluna "**Valor Unitário Atual**" alterada para o novo valor unitário.
  + No anexo "**Reajuste do Item Associado**", é apresentado o valor do percentual do Reajuste aplicado (Coluna **Percentual Reajuste (%)**) para cada item associado.
  + No anexo "**Reajuste do Item Associado**", é apresentado o valor unitário anterior ao reajuste realizado (Coluna **Valor Anterior**).
3Provisório 

**Provisório**

1 - Criar um contrato, podendo ser do tipo de Serviço, Fornecimento de Material, Insumo ou Extra/Extra-Histograma.

2 - Definir na aba "**Reajuste**" do contrato o tipo de reajuste "**Por Item Associado**" e Aplicação do Reajuste: "**Valor Unitário Inicial"**.

3 - Realizar a associação dos itens/objetos ao contrato.

4 - Gerar os períodos para o contrato.

5 - Aplicar o reajuste para um ou mais itens associados ao contrato marcando a opção de **Provisório**.

Selecione o contrato, em Processos | Reajuste do Item Associado | Reajustar Itens Associados ao Contrato.

Veja o exemplo

* + Ao abrir a tela do processo de "**Reajustar Itens Associados ao Contrato**" será apresentado no campo "**Períodos disponíveis**" o ultimo período disponível para realizar o reajuste.

Informações adicionais

Contrato de serviço, contrato de insumo, contrato extra/extra-histograma:

* + Ao aplicar o reajuste para os itens associados, o anexo de **itens do contrato** terá a coluna "**Valor Unitário Atual**" alterada para o novo valor unitário.
  + No anexo "**Reajuste do Item Associado**", é apresentado o valor do percentual do Reajuste aplicado (Coluna **Percentual Reajuste (%)**) para cada item associado.
  + No anexo "**Reajuste do Item Associado**", é apresentado o valor unitário anterior ao reajuste realizado (Coluna **Valor Anterior**).
  + No anexo "**Reajuste do Item Associado**", é informado na coluna **Provisório** o tipo do Reajuste se é **Provisório (marcado)** ou não **(desmarcado)** .

Não é permitido dois reajustes provisórios para o mesmo contrato. Reajuste provisório é uma previsão do fator esperado para o reajuste desta forma não é permitido adicionar novos reajustes, enquanto o fator não for efetivado.

**Efetivar Reajustes Provisórios do Item Associado**

Após realizar o reajuste provisório, realizar as medições ou não é possível efetivar o reajuste informado como Provisório.

Para efetivar este reajuste provisório é necessário selecionar o contrato | Processos | Efetivar Reajustes Provisórios do Item Associado | Selecionar os itens desejados para efetivar o reajuste em seguida executar o processo.

Obs.: Caso na tela de "Efetivar Reajustes Provisórios do Item Associado" seja informado um valor de percentual maior ou menor que o inicial a diferença será calculada e apresentada no campo de **Saldo Reajuste**.

4Cancelamento de Reajuste

**Cancelamento de Reajuste:**

Processo de cancelamento disponível no anexo de Reajustes do Item Associado e Reajustes do Objeto Associado.

Ao executar o processo de cancelamento é exibida a mensagem abaixo, sendo que o processo realizara o cancelamento do ultimo reajuste, ou seja do reajuste de maior data de vigência inicial.

Este processo realiza as seguintes etapas:

* + Valida se o projeto e contrato permitem alteração.
  + Apaga o reajuste e retorna o valor unitário do item ao valor unitário do reajuste anterior.
  + Atualiza o Saldo de Reajuste

**Restrições:** Caso o cancelamento gere um Saldo de Reajuste negativo o processo é abortado e o usuário é informado sobre o valor no qual o saldo ficaria caso o reajuste fosse cancelado.

**Exemplo da mensagem apresentada:**

Cancelamento não permitido pois o item ficara com saldo de reajuste negativo -10,0000!  
Para realizar o cancelamento do reajuste é necessário cancelar as medições que consumiram o saldo deste reajuste.

**Observações:** Não existe diferença entre o cancelamento de reajuste provisório ou efetivo.

3Contrato de Serviço41Calculo dos campos

**Calculo das colunas na tela de medição**

**Valor Unitário Inicial**: É o valor unitário do item sem reajuste.

**Valor Unitário Atual:** É o valor unitário do item com o reajuste efetivado.

**Valor Medido Preço Inicial:** É o valor inicial (**PI**) medido.

**Valor Medido Reajuste:** É o valor do campo **(Valor Medido Preço Inicial** \* **Percentual de Reajuste Período) + Valor Medido Preço Inicial.**

Exemplo:

| **Valor Medido Preço Inicial** | **Percentual de Reajuste Período** | **(Valor Medido Preço Inicial** \* **Percentual de Reajuste Período) + Valor Medido Preço Inicial** |
| --- | --- | --- |
| R$ 100,00 | 5 % | R$ 105,00 |

Obs.: Este campo e editável e é possível informado um valor de reajuste superior ou inferior, respeitando apenas o Saldo do Reajuste disponível.

**Valor Medido (Inicial + Reajuste):** É a soma da coluna Valor Medido Preço Inicial + Valor Medido Reajuste;

**Valor Calculado Reajuste:** É o valor do campo (**Valor Medido Preço Inicial \* Percentual de Reajuste Período).**

**Saldo Reajuste:** É o valor do saldo não utilizado no período anterior somado ao saldo do reajuste atual não utilizado no período vigente.

**Percentual Reajuste Período (%):** É o percentual de reajuste aplicado para o período selecionado.

**Acumulado Medição de Reajuste:**  É o valor do campo "**Valor Medido Reajuste"** do período **anterior + "**Valor Medido Reajuste"**** do período **atual.**

**Acumulado Calculado de Reajuste:** É **o** valor do campo "**Valor Calculado Reajuste**" do período **anterior** + "**Valor Calculado Reajuste"** do período **atual**.

**Valor Acumulado:** É a soma do campo "**Valor Medido Preço Inicial**" do período **anterior** + "**Valor Medido Preço Inicial**" do período **atual**.

Exemplo:

| Período | **Valor Medido Preço Inicial** | **Percentual Reajuste Período (%)** | **Valor Acumulado** |
| --- | --- | --- | --- |
| 0001 | R$ 100,00 | 10 | 100 |
| 0002 | R$ 100,00 | 10 | 200 |

**% Acumulado:** (Qtde. Medida / Qtde. Contratada ) \* 100

**Saldo (v)**: Valor Total Contratado - Valor Medido Preço Inicial

Exemplo da exibição dos valores do contrato

**Reajuste Devido:** Apresenta a soma dos valores de reajustes calculados sobre o valor medido.  
**Reajuste Previsto:** Apresenta a soma dos valores de reajuste calculados sobre o valor medido adicionando a previsão de reajuste calculado sobre o saldo do contrato a preço inicial.

2Processo51Reajuste

* + Abaixo um cenário utilizando um contrato de prestação de serviço que utiliza o reajuste **por item associado**, Período Reajuste "**mensal**" e a aplicação do reajuste feito a **valor unitário inicial**.

Veja o contrato

XXXXXXXXXXXXXXX alterar a imagem com a alteração aonde não possui o campo por contrato e valor atual

O contrato já possui períodos gerados e itens associados.

* + Realizado o processo de reajuste para os itens associados aplicando um percentual de reajuste diferente para cada item associado.

| Cod. Tarefa | Nome | Descrição | Índice de Reajuste | Valor Unit. Inicial | Qtde. Contratada | Und. | Valor Unit. contratado | Percentual Atual (%) | Vigência Anterior | Vlr Anterior | Perc. Anterior | Vlr. Reajustado | Data de Execução | Vigência Inicial | Provisório |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001 | Obra | Obra |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 001.01 | Etapa | Etapa |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 001.01.04 | Estudos Ambientais | Estudos Ambientais |  | 1 | 500,00 | UN | 1 | 5 |  |  |  | 1,05 |  |  |  |
| 001.01.05 | Transporte de Funcionários | Transporte de Funcionários |  | 1 | 500,00 | HR | 1 | 6 |  |  |  | 1,06 |  |  |  |
| 001.01.06 | Transporte de Equipamentos | Transporte de Equipamentos |  | 1 | 500,00 | H | 1 | 7 |  |  |  | 1,07 |  |  |  |

* + Após realizar o reajuste, os valores dos itens associados ao contrato serão atualizados no anexo de "**Itens do Contrato**" e no anexo de "**Reajustes do item associado**" é possível verificar o antigo valor e a porcentagem do reajuste aplicado.

### **Medição do período 0001:**

* + Informado o "Valor Medido Preço Inicial" no valor de R$ 50,00 para o item com 5% de reajuste, assim é gerado um valor de reajuste de R$ 2,50;
  + Nesta tarefa será utilizado somente R$ 1,50 do saldo gerado de reajuste, restando R$ 1,00 de Saldo de Reajuste para o próximo período.

| Cod. Tarefa | Valor unitário Inicial | Valor unitário Atual | Valor total Contratado | Qtde. Contratada | % Medido | Qtde. Medida | Valor Medido Preço Inicial | Valor Medido Reajuste | Valor Medido (Inicial + Reajuste) | Valor Calculado Reajuste | Saldo do Reajuste | Saldo(v) | Percentual Reajuste (%) | Acumulado Medição de Reajuste | Acumulado Calculado de Reajuste |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001.01.04 | 1,00 | 1,05 | 500,00 | 500,00 | 10,000 | 50,00 | 50,00 | 1,50 | 51,50 | 2,50 | 1,00 | 450,00 | 5,00 | 1,50 | 2,50 |

Resultado

* + Ao abrir a tela de medição do período 0002 para Tarefa 001.01.04 a coluna **Saldo Reajuste** irá possuir o valor de **R$ 1,00** referente ao saldo do reajuste não utilizado no período anterior.

* + Informado o "Valor Medido Preço Inicial" no valor de R$ 50,00 para o item com 6% de reajuste, assim é gerado um valor de reajuste de R$ 3,00;
  + Nesta tarefa será utilizado todo o saldo gerado de reajuste.

| Cod. Tarefa | Valor unitário Inicial | Valor unitário Atual | Valor total Contratado | Qtde. Contratada | % Medido | Qtde. Medida | Valor Medido Preço Inicial | Valor Medido Reajuste | Valor Medido (Inicial + Reajuste) | Valor Calculado Reajuste | Saldo do Reajuste | Saldo(v) | Percentual Reajuste (%) | Acumulado Medição de Reajuste | Acumulado Calculado de Reajuste |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001.01.05 | 1,00 | 1,06 | 500,00 | 500,00 | 10,000 | 50,00 | 50,00 | 3,00 | 53,00 | 3,00 | 0,00 | 450,00 | 6,00 | 3,00 | 3,00 |

Resultado

* + Ao abrir a tela de medição do período 0002 para Tarefa 001.01.05 a coluna Saldo Reajuste não terá saldo, isso porque no período 0001 foi realizado todo consumo do saldo.

* + Informado o "Valor Medido Preço Inicial" no valor de R$ 50,00 para o item com 7% de reajuste, assim é gerado um valor de reajuste de R$ 3,50;
  + Nesta não será utilizado o saldo do reajuste, restando R$ 3,50 de Saldo do Reajuste para o próximo período.

| Cod. Tarefa | Valor unitário Inicial | Valor unitário Atual | Valor total Contratado | Qtde. Contratada | % Medido | Qtde. Medida | Valor Medido Preço Inicial | Valor Medido Reajuste | Valor Medido (Inicial + Reajuste) | Valor Calculado Reajuste | Saldo do Reajuste | Saldo(v) | Percentual Reajuste (%) | Acumulado Medição de Reajuste | Acumulado Calculado de Reajuste |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001.01.06 | 1,00 | 1,07 | 500,00 | 500,00 | 10,000 | 50,00 | 50,00 | 0,00 | 50,00 | 3,50 | 3,50 | 450,00 | 7,00 | 0,00 | 3,50 |

Resultado

* + Ao abrir a tela de medição do período 0002 para Tarefa 001.01.06 a coluna **Saldo Reajuste** irá possuir o saldo de **R$ 3,50**, isso porque no período 0001 não foi consumido o saldo do reajuste.
2Deflação

* + Abaixo um cenário utilizando Deflação em um contrato de prestação de serviço que utiliza o reajuste **por item associado**, Período Reajuste "**mensal**" e a aplicação do reajuste feito a **valor unitário inicial**.
  + Realizado o processo de "**Reajustar Itens associados ao contrato"** aplicando um valor negativo de reajuste para cada item associado.

| Cod. Tarefa | Nome | Descrição | Índice de Reajuste | Valor Unitário Inicial | Qtde. Contratada | Und. | Valor Unitário contratado | Percentual Atual (%) | Vigência Anterior | Valor Anterior | Percentual Anterior | Valor Reajustado | Data de Execução | Vigência Inicial | Provisório |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001 | Obra | Obra |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 001.01 | Etapa | Etapa |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 001.01.04 | Estudos Ambientais | Estudos Ambientais |  | 1 | 500,00 | UN | 1 | -5 |  |  |  | 0,95 |  |  |  |
| 001.01.05 | Transporte de Funcionários | Transporte de Funcionários |  | 1 | 500,00 | HR | 1 | -6 |  |  |  | 0,94 |  |  |  |
| 001.01.06 | Transporte de Equipamentos | Transporte de Equipamentos |  | 1 | 500,00 | H | 1 | - 7 |  |  |  | 0,93 |  |  |  |

* + Após realizar o reajuste provisório, os valores dos itens associados ao contrato serão atualizados no anexo de "**Itens do Contrato**" e no anexo de "**Reajustes do item associado**" é possível verificar o antigo valor e a porcentagem do reajuste aplicado.

### **Medição do período 0001:**

* + Informado o "Valor Medido Preço Inicial" no valor de R$ 50,00 para o item com -5% de reajuste, assim é gerado um valor de reajuste de R$ - 2,50;

* + Nesta tarefa será utilizado somente R$ -1,00 do saldo gerado de reajuste, restando R$ -1,50 de Saldo de Reajuste para o próximo período.

| Cod. Tarefa | Valor unitário Inicial | Valor unitário Atual | Valor total Contratado | Qtde. Contratada | % Medido | Qtde. Medida | Valor Medido Preço Inicial | Valor Medido Reajuste | Valor Medido (Inicial + Reajuste) | Valor Calculado Reajuste | Saldo do Reajuste | Saldo(v) | Percentual Reajuste (%) | Acumulado Medição de Reajuste | Acumulado Calculado de Reajuste |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001.01.04 | 1,00 | 0,95 | 500,00 | 500,00 | 10,000 | 50,00 | 50,00 | -1,00 | 49,00 | -2,50 | -1,50 | 450,00 | - 5,00 | -1,00 | -2,50 |

Resultado

* + Ao abrir a tela de medição do período 0002 para Tarefa 001.01.04 a coluna **Saldo Reajuste** irá possuir o valor de **R$ -1,50** referente ao saldo do reajuste não utilizado no período anterior.

* + Informado o "Valor Medido Preço Inicial" no valor de R$ 50,00 para o item com - 6% de reajuste, assim é gerado um valor de reajuste de R$ - 3,00;
  + Nesta tarefa será utilizado todo o saldo gerado de reajuste.

| Cod. Tarefa | Valor unitário Inicial | Valor unitário Atual | Valor total Contratado | Qtde. Contratada | % Medido | Qtde. Medida | Valor Medido Preço Inicial | Valor Medido Reajuste | Valor Medido (Inicial + Reajuste) | Valor Calculado Reajuste | Saldo do Reajuste | Saldo(v) | Percentual Reajuste (%) | Acumulado Medição de Reajuste | Acumulado Calculado de Reajuste |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001.01.05 | 1,00 | 0,94 | 500,00 | 500,00 | 10,000 | 50,00 | 50,00 | -3,00 | 47,00 | -3,00 | 0,00 | 450,00 | -6,00 | -3,00 | -3,00 |

Resulado

* + Ao abrir a tela de medição do período 0002 para Tarefa 001.01.05 a coluna Saldo Reajuste não terá saldo, isso porque no período 0001 foi realizado todo consumo do saldo de deflação.

* + Informado o "Valor Medido Preço Inicial" no valor de R$ 50,00 para o item com -7% de reajuste, assim é gerado um valor de reajuste de R$ -3,50;
  + Nesta não será utilizado o saldo do reajuste, restando R$ -3,50 de Saldo do Reajuste para o próximo período.

| Cod. Tarefa | Valor unitário Inicial | Valor unitário Atual | Valor total Contratado | Qtde. Contratada | % Medido | Qtde. Medida | Valor Medido Preço Inicial | Valor Medido Reajuste | Valor Medido (Inicial + Reajuste) | Valor Calculado Reajuste | Saldo do Reajuste | Saldo(v) | Percentual Reajuste (%) | Acumulado Medição de Reajuste | Acumulado Calculado de Reajuste |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001.01.06 | 1,00 | 0,93 | 500,00 | 500,00 | 10,000 | 50,00 | 50,00 | 0,00 | 50,00 | -3,50 | -3,50 | 450,00 | -7,00 | 0,00 | -3,50 |

Resultado

* + Ao abrir a tela de medição do período 0002 para Tarefa 001.01.06 a coluna **Saldo Reajuste** irá possuir o saldo de **R$ -3,50**, isso porque no período 0001 não foi consumido o saldo do reajuste de deflação.
3Provisório

* + Abaixo um cenário utilizando Deflação em um contrato de prestação de serviço que utiliza o reajuste **por item associado**, Período Reajuste "**mensal**" e a aplicação do reajuste feito a **valor unitário inicial**.
  + Realizado o processo de "**Reajustar Itens associados ao contrato"** aplicando um valor negativo e positivo de reajuste em seguida marcado a opção de "**Provisório**" para cada item associado.

| Cod. Tarefa | Nome | Descrição | Índice de Reajuste | Valor Unitário Inicial | Qtde. Contratada | Und. | Valor Unitário contratado | Percentual Atual (%) | Vigência Anterior | Valor Anterior | Percentual Anterior | Valor Reajustado | Data de Execução | Vigência Inicial | Provisório |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001 | Obra | Obra |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 001.01 | Etapa | Etapa |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 001.01.04 | Estudos Ambientais | Estudos Ambientais |  | 1 | 500,00 | UN | 1 | 5 |  |  |  | 1,05 |  |  | X |
| 001.01.05 | Transporte de Funcionários | Transporte de Funcionários |  | 1 | 500,00 | HR | 1 | -6 |  |  |  | 0,94 |  |  | X |
| 001.01.06 | Transporte de Equipamentos | Transporte de Equipamentos |  | 1 | 500,00 | H | 1 | 7 |  |  |  | 1,07 |  |  | X |

* + Após realizar o reajuste provisório, os valores dos itens associados ao contrato serão atualizados no anexo de "**Itens do Contrato**" e no anexo de "**Reajustes do item associado**" é possível verificar o antigo valor e a porcentagem do reajuste aplicado.

### **Medição do período 0001:**

* + - Informado o "Valor Medido Preço Inicial" no valor de R$ 50,00 para o item com 5% de reajuste, assim é gerado um valor de reajuste provisório de R$ 2,50;
    - Nesta tarefa será utilizado somente R$ 1,50 do saldo gerado de reajuste, restando R$ 1,00 de Saldo de Reajuste para o próximo período.

| Cod. Tarefa | Valor unitário Inicial | Valor unitário Atual | Valor total Contratado | Qtde. Contratada | % Medido | Qtde. Medida | Valor Medido Preço Inicial | Valor Medido Reajuste | Valor Medido (Inicial + Reajuste) | Valor Calculado Reajuste | Saldo do Reajuste | Saldo(v) | Percentual Reajuste (%) | Acumulado Medição de Reajuste | Acumulado Calculado de Reajuste |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001.01.04 | 1,00 | 1,05 | 500,00 | 500,00 | 10,000 | 50,00 | 50,00 | 1,50 | 51,50 | 2,50 | 1,00 | 450,00 | 5,00 | 1,50 | 2,50 |

Resultado

* + Ao abrir a tela de medição do período 0002 para Tarefa 001.01.04 a coluna **Saldo Reajuste** irá possuir o valor de **R$ 1,00** referente ao saldo do reajuste **Provisório** não utilizado no período anterior.

* + Informado o "Valor Medido Preço Inicial" no valor de R$ 50,00 para o item com - 6% de reajuste, assim é gerado um valor de reajuste provisório de R$ - 3,00;
  + Nesta tarefa será utilizado todo o saldo gerado de reajuste.

| Cod. Tarefa | Valor unitário Inicial | Valor unitário Atual | Valor total Contratado | Qtde. Contratada | % Medido | Qtde. Medida | Valor Medido Preço Inicial | Valor Medido Reajuste | Valor Medido (Inicial + Reajuste) | Valor Calculado Reajuste | Saldo do Reajuste | Saldo(v) | Percentual Reajuste (%) | Acumulado Medição de Reajuste | Acumulado Calculado de Reajuste |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001.01.05 | 1,00 | 0,94 | 500,00 | 500,00 | 10,000 | 50,00 | 50,00 | -3,00 | 47,00 | -3,00 | 0,00 | 450,00 | -6,00 | -3,00 | -3,00 |

Resultado

* + Ao abrir a tela de medição do período 0002 para Tarefa 001.01.05 a coluna Saldo Reajuste não terá saldo, isso porque no período 0001 foi realizado todo consumo do saldo de deflação do item **Provisório**.

* + Informado o "Valor Medido Preço Inicial" no valor de R$ 50,00 para o item com 7% de reajuste, assim é gerado um valor de reajuste de R$ 3,50;
  + Nesta não será utilizado o saldo do reajuste, restando R$ 3,50 de Saldo do Reajuste para o próximo período.

| Cod. Tarefa | Valor unitário Inicial | Valor unitário Atual | Valor total Contratado | Qtde. Contratada | % Medido | Qtde. Medida | Valor Medido Preço Inicial | Valor Medido Reajuste | Valor Medido (Inicial + Reajuste) | Valor Calculado Reajuste | Saldo do Reajuste | Saldo(v) | Percentual Reajuste (%) | Acumulado Medição de Reajuste | Acumulado Calculado de Reajuste |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 001.01.06 | 1,00 | 1,07 | 500,00 | 500,00 | 10,000 | 50,00 | 50,00 | 0,00 | 50,00 | 3,50 | 3,50 | 450,00 | 7,00 | 0,00 | 3,50 |

Resultado

* + Ao abrir a tela de medição do período 0002 para Tarefa 001.01.06 a coluna **Saldo Reajuste** irá possuir o saldo de **R$ 3,50**, isso porque no período 0001 não foi consumido o saldo do reajuste .

* + Ao efetivar o valor do reajuste provisório o sistema continuará com os mesmos valores informados na medição.

4Contrato de Insumo e Extra/ Extra-histograma61Calculo dos campos

**Contrato de Extra/Extra-Histograma:**

Para saber mais sobre Contrato Extra e Contrato Extra-Histograma [clique aqui.](http://fwrm-wiki:9999/WikiHelp/PRJ/PRJ.ContratoExtraHistograma.aspx)

**Consumo de Objetos:**

**Na parte superior da tela de consumo de objetos do contrato possui alguns campos, abaixo é demonstrado como cada campo é preenchido:**

* + Os três primeiros campos da tela de Consumo de Objetos do Contrato (**Contrato,** **Valor Consumido e Saldo**) são referentes ao Preço Inicial do contrato desconsiderando o valor de reajuste.

Veja como é o preenchimento do campo

**Contrato:** Num. Contrato informado na inclusão do contrato.

**Valor consumido:** É a soma da coluna **Valor Medido Preço Inicial** do período vigente e os períodos anteriores.

**Saldo:** É a soma do Saldo valor do período vigente e os períodos anteriores.

* + Os últimos três campos da tela de Consumo de Objetos do Contrato (Período, Valor Consumido e Saldo Reajuste) são referentes ao Preço Inicial mais o valor de reajuste do contrato.

Veja como é o preenchimento do campo

**Período:** É o período atual selecionado.

**Valor consumido:** É a soma do Valor Medido (Inicial + Reajuste) do período selecionado.

**Saldo Reajuste:** É o valor do Saldo Reajuste disponível para consumo.

Objetos Associados ao Contrato

**Saldo do Reajuste:** É o valor do saldo não utilizado no período anterior somado ao saldo do reajuste atual não utilizado no período vigente.

**Saldo Valor:** É a (**Quantidade Contratada \* Valor Unitário Inicial)** - **Valor Medido Preço Inicial** do período atual e anteriores.

**Valor Medido Preço Inicial:** É a soma do **valor medido a preço inicial** dos períodos anteriores mais o período atual.

**Valor Medido (Inicial + Reajuste):** É a soma da coluna **Valor Medido Preço Inicial** + **Valor Medido Reajuste**;

**Valor Unitário Inicial:** É o valor unitário do item sem reajuste;

**Percentual Reajuste (%):** É o valor do reajuste aplicado vigente.

**Acumulado Calculado de Reajuste:** É o valor informado na aba "**Objetos consumidos no Período: 000xx** " do campo "**Valor Calculado Reajuste**" do período **anterior** + "**Valor Calculado Reajuste**" do período **atual**.

**Acumulado Medição de Reajuste:** É o valor informado na aba "**Objetos consumidos no Período: 000xx** " do campo "**Valor Medido Reajuste"** do período **anterior + "**Valor Medido Reajuste"**** do período **atual.**

Os campos somente serão atualizados para o período vigente após a execução do consumo do objeto no período atual.

Objetos a Consumir

**Valor Medido Reajuste:** É o valor a ser consumido do saldo de reajuste no período atual. Esse campo é calculado automaticamente ao informar o **Valor Medido Preço Inicial;**

**Valor Calculado Reajuste:** É o valor do campo (**Valor Medido Preço Inicial** \* **Percentual de Reajuste Período**) para o período atual.

**Valor Medido (Inicial + Reajuste)**: É a soma da coluna **Valor Medido Preço Inicial** + **Valor Medido Reajuste**;

**Saldo Reajuste:** É o saldo de reajuste disponível para ser consumido no período.

**Valor Medido Preço Inicial:** É o valor consumido no período vigente.

**Valor Unitário Inicial:** É o valor unitário do item sem reajuste;

**Percentual Reajuste (%):** É o percentual de reajuste aplicado para o período vigente.

**Acumulado Calculado de Reajuste:** É o valor informado na aba "**Objetos consumidos no Período: 000xx** " do campo "**Valor Calculado Reajuste**".

**Acumulado Medição de Reajuste:** É o valor informado na aba "**Objetos consumidos no Período: 000xx** " do campo "**Valor Medido Reajuste**".

Dica

Os campos **Valor medido Reajuste**, **Valor Medido Preço Inicial**, **Percentual Consumido (%)** e **Quantidade Consumida** da tela de consumo, possuem uma funcionalidade de calculadora para realizar cálculos diretamente no campo.

Para utilizar basta somente clicar sobre o campo e apertar **Alt + ↓** ou apertar a seta para baixo que é apresentada ao clicar no campo.

Veja exemplo51

Para realizar o processo de reajuste, deflação e provisório veja os exemplos apresentados nesta seção.

6Validações e Restrições

**Validações:**

* + - Não é possível aumentar o valor negativo do reajuste de deflação ou medir mais do que 0.

Exemplo: Na tabela abaixo, o usuário informou o "**Valor medido reajuste**" superior ao "**Valor calculado do reajuste**", neste caso o sistema não irá permitir.

| Valor Medido Preço Inicial | Valor Calculado Reajuste | Saldo Reajuste | Valor Medido Reajuste |
| --- | --- | --- | --- |
| R$ 100,00 | **R$ -5,00** | 0 | **R$ -6,00** |

* + - Para o contrato que utiliza do reajuste a preço inicial e que não tenha aplicado o reajuste para o período xxxx é apresentado uma mensagem na parte inferior da tela de medição do contrato de serviço informando que os itens estão aptos para receber um reajuste.

* + - Ao marcar o parâmetro, somente será permitido a inclusão de contratos com a aplicação de reajuste à "**Valor Unitário Inicial**" e Tipo de reajuste "**Por Item Associado**".
    - Ao tentar excluir os objetos que possuem reajuste realizado, o sistema valida se possui reajuste e não permite a exclusão dos objetos associados.
    - Ao tentar medir/consumir um período de um contrato que foi realizado o reajuste diferente do Pi+R será apresentado uma mensagem para que seja executado o processo de conversão de contratos no modelo antigo de reajuste.

**Restrições**

* + - A medição/consumo em PI, R ou PI + R não se aplicará aos contratos com a finalidade Fornecimento de Material;

# 1 - API de Medição

---

Esta API permitirá a entrada de valores da medição da quantidade dos serviços que já foram executados no período selecionado. 

**Máscara de Url: <http://localhost:8051/api/construction-projects/v1/contract-measure-input>**

Irá retornar o mesmo JSON e uma lista de avisos que não provocaram erros:

**Método de entrada:** Post

Exemplo de JSon de entrada

|  |  |
| --- | --- |
| 1 2 3 4 5 6 7 8 9 10 11 | Exemplo de API: {   "companyId": 1,   "projectId": 2,   "contractId": 33,   "period": "0002",   "cities":[       {         "stateCode": "RO",          "cityCode": "00015",          "value": 20,         "products":[             {                 "value": 20,                  "measurements":[                     {                         "companyId": 1,                         "projectId": 2,                         "contractId": 33,                         "itemId": 182,                         "value": 20,                           "tasks":[    {                                 "companyId": 1,                                 "projectId": 2,                                 "taskId": 5,                                 "value": 20                             }                            ]                     }                 ]             }         ]         },       {         "value": 10,         "products":[             {                 "value": 10,                  "measurements":[                     {                         "companyId": 1,                         "projectId": 2,                         "contractId": 33,                         "itemId": 182,                         "value": 10,                           "tasks":[    {                                 "companyId": 1,                                 "projectId": 2,                                 "taskId": 5,                                 "value": 10                             }                            ]                     }                 ]             }         ]         }     ] } |
