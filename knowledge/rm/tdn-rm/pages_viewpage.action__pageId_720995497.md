---
content_hash: 5736dc68935fd2e5c018a407ae3eba2f7bc0bd46020815f02d70c7abc511e25f
fetched_at: '2026-06-29T00:11:26.844079+00:00'
page_id: '720995497'
product: rm
source: tdn-rm
title: Comissão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=720995497
version: 6
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela Comissão**
   1. **Outras Ações / Ações relacionadas**
4. **Tela Lançamento Global de Comissão**
   1. **Principais Campos e Parâmetros**
5. **Tela Lançar Comissão para Folha**
   1. **Principais Campos e Parâmetros**
6. **Tela Recalcular Comissão**
   1. **Principais Campos e Parâmetros**
7. **Tela Períodos da Comissão**
   1. **Principais Campos e Parâmetros**
8. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Nesse processo, o usuário terá a possibilidade de efetuar o pagamento de uma comissão por determinado trabalho aos funcionários, a comissão que será paga ao funcionário irá se basear em uma tabela de cálculo que deverá ser associada dentro do parametrizador. Um exemplo de aplicação da implementação citada acima, seria uma empresa onde os empregados cuja a função do tipo “Saqueiro” deverá receber um determinado valor de acordo com a quantidade de sacos carregados.

## **02. EXEMPLO DE UTILIZAÇÃO**

## **Parametrização**

### 1. Tabela de Cálculo

A criação de uma tabela de cálculo é essencial para o funcionamento da rotina, podendo ser criada através do caminho Administração de Pessoal | Cálculos | Tabela de Cálculo.

Para maiores detalhes de como o sistema irá se comportar em relação a tabela de cálculo, veja explicações sobre faixas na 4ª observação do tópico **"Comissão"****.**

### 2. Configurações Gerais

A utilização das rotinas de comissão aos funcionários apenas é possível quando for feito vinculação de um campo complementar ao cadastro do funcionário, onde será usado para filtrar quem irá receber comissões calculadas ou não. O campo complementar que será vinculado, deverá ser preenchido com "SIM", "S" ou "1".

Sabendo do que é dito anteriormente, o sistema irá atuar em cima desse campo, apenas quando for feita a sua vinculação também ao parametrizador (Configurações | Parametrizador) na etapa Folha Agrária | Configurações Gerais.

Ainda no parametrizador, na Etapa 2 - Parâmetros da Filial, deve-se fazer o preenchimento de alguns parâmetros na aba “Comissão” que se tornam essenciais.

Caminho: Configurações | Parametrizador | Folha Agrária | Etapa – Parâmetros da Filial.

1. Preenchimento do período disponível para o lançamento das comissões dos funcionários.
2. O cálculo utilizado para resultar na comissão do funcionário, conforme tópico "**Comissão**",  irá utilizar a tabela de cálculo vinculada neste campo.  
   Observação:
   * Será apresentado apenas as tabelas de cálculo sem finalidade específica.
3. Deverá ser preenchido com o código e descrição do evento que será apresentado no envelope do funcionário quando for feito o lançamento da comissão.

## Cadastros/Processos

### 1. Comissão

Deverá acessar o menu Folha Agrária | Agrupador Comissão | Comissão.

No menu em questão será listada todas as Comissões pagas ou pendentes de pagamento para o funcionário.

Poderá ser feito o lançamento da Comissão manualmente através do botão “Incluir”, onde será solicitado o preenchimento dos campos conforme print abaixo:

Observações:

1. O campo" Data da comissão" terá que estar compreendido no período informado dentro dos parâmetros da filial (Configurações | Parametrizador | Parâmetros da Filial | Aba Comissão).
2. Será possível fazer o lançamento apenas para os funcionários que na “Data da comissão”, não se encontre nos cenários:  
   * Afastado ou Férias;
   * **Seja jornada de “Descanso” ou “Compensado” de acordo com o quadro de horário, mesmo que não utilize RM Chronus.**
   * Superior ao desligamento.
3. Os campos “Mês / Ano Pgto” será preenchido automaticamente quando for feito o seu lançamento para o envelope do funcionário.
4. O campo “Valor” será calculado conforme regra abaixo:

Para o cálculo, utilizaremos como exemplo a tabela a seguir:

| Número de Faixa | Limite superior | Percentual |
| --- | --- | --- |
| 1 | 300 | 0 |
| 2 | 450 | 2,7437 |
| 3 | 650 | 4,1157 |
| 4 | 999999999 | 5,4876 |

A tabela é utilizada para calcular o valor a ser pago ao funcionário em cima da quantidade de sacas (Açúcar, Feijão, Café e etc.) carregadas em determinado dia. Existem duas colunas relevantes na tabela, sendo elas:

* **Limite Superior** – Quantidade de sacas carregadas.
* **Percentual** – Valor a ser pago para o funcionário em reais (R$),   
  Obs.: Será considerado na operação o percentual dividido por 100.

O cálculo irá levar em consideração todas as faixas ultrapassadas pelo funcionário, ou seja, caso o mesmo se enquadre na faixa 3, deverá ser pago os valores da faixa 1, 2 e 3.

Exemplos

* **Calculo 1**

**Quantidade de sacas carregadas:** 250.

**Faixa em que se enquadra:** Faixa 1.

**Percentual:** Conforme tabela, faixa 1 possui percentual 0.

**Valor Calculado:**

Valor = Quantidade de Sacas \* (Percentual / 100)

Valor = 250 \* (0 / 100)

Valor = 0

Ou seja, de acordo com a tabela, para as primeiras 300 sacas será pago uma comissão de 0 reais.

* **Calculo 2**

**Quantidade de sacas carregadas:** 770

**Faixa em que se enquadra:** Faixa 4.

**Percentual:** O cálculo do percentual não se dá apenas na identificação de qual faixa o funcionário irá se enquadrar, deverá ser feito a distribuição do pagamento passando por cada faixa, como por exemplo

1. As primeiras 300 sacas serão pagas R$ 0,00.

De 770 sacas carregadas, as 300 primeiras não serão pagas nenhuma comissão, pois o percentual na tabela é 0.

| Número da Faixa | Limite superior | Percentual |
| --- | --- | --- |
| 1 | 300 | 0 |

Existira ainda 470 sacas (770 – 300) para distribuir nas faixas.

2. Como já foram pagas 300 sacas e lembrando que a faixa 2 são 450, ainda nos restará realizar o pagamento de 150 sacas. (450 – 300)

| Número da Faixa | Limite superior | Percentual |
| --- | --- | --- |
| 2 | 450 | 2,7437 |

Ou seja, as próximas 150 sacas, serão pagas R$ 0,027437 por saca.

Temos então, de um total de 770 sacas, distribuímos em duas faixas 450 sacas(300 + 150), restando assim 320 sacas a serem distribuídas/pagas.

3. De acordo com a faixa 3, onde seguindo a lógica imposta nos itens acima, será de 200 sacas pagas R$ 0,041157 por saco. (650 – 450)

| Número da Faixa | Limite superior | Percentual |
| --- | --- | --- |
| 3 | 650 | 4,1157 |

Ou seja, sabendo que já foram feitos o pagamento de 450 sacas, faltará apenas 200 para complementar o limite faixa 3 (450 + 200 = 650).

4. As próximas 120 sacas restantes (770 – 650), serão pagas com o percentual da 4 faixa, sendo R$ 0,05876 por saca.

| Número da Faixa | Limite superior | Percentual |
| --- | --- | --- |
| 4 | 999999999 | 5,4876 |

Analisando a distribuição acima, foi feito a montagem da tabela abaixo para entendermos melhor ainda a distribuição feita.

|  | **Quantidade** | **Percentual** | **Valor Calculado** |
| --- | --- | --- | --- |
| **1****º Calculo** | 300 | 0 | R$ 0,00 |
| **2****º Calculo** | 150 | 0,027437 | R$ 4,11 |
| **3****º Calculo** | 200 | 0,041157 | R$ 8,23 |
| **4****º Calculo** | 120 | 0,05876 | R$ 7,05 |
| **Somatório** | **770** |  | **R$ 19,39** |

### 2. Lançamento Global de Comissão

Existirá a opção de realizar o lançamento de comissão globalmente, através do Menu Folha Agrária | Lançamento Global de Comissão.

No processo de lançamento global, será necessário selecionar os funcionários que serão considerados para determinado lançamento de comissão, junto com a data de tal comissão e a quantidade.

O processo irá disponibilizar também duas possibilidades de “Ação na comissão”, sendo elas:

* **Sobrepor –** Ao se optar por esta flag, será sobreposto algum lançamento já existente no dia, um exemplo de utilização desse parâmetro seria em um cenário onde foi feito um lançamento incorreto de uma comissão, passando assim a possuir a necessidade de sobrepor (Criar novamente) a comissão com os dados corretos.
* **Ignorar –** Apenas será ignorado o lançamento atual da comissão para o funcionário (Processo), caso já exista alguma cadastrada para o dia.

Também poderá optar por duas possibilidades de apresentação do Log, onde:

* **Simples –** O log será apresentado com uma quantidade inferior de informações e em sequência, conforme print abaixo.
* **Detalhada –** Caso seja optado por esse parâmetro, o Log irá conter algumas informações adicionais e passarão a ser separadas por uma quebra de linha.

### 3. Recalcular Comissão

Caso seja feito alguma alteração na tabela de cálculo ou algum processo similar, será necessário efetuar o recalculo da comissão, para que o sistema atualize as comissões a serem pagas aos funcionários, considerando as novas informações.

O processo “Recalculo das Comissões dos funcionários” se encontrará disponível para ser executado no menu Folha Agrária | Comissão | Recalcular Comissão.

Ao acessar o processo em questão, será apresentado a tela abaixo e deverá ser preenchido com as seguintes informações:

1) Selecionar os funcionários que serão considerados para lançamento.

2) Preencher com um intervalo de datas que deverá ser levado em consideração para a execução.  
Observações:

* Os campos “Competência, Período e Data Pagamento, será preenchido automaticamente de acordo com a sua competência atual.
* Poderá ser lançado tal movimentação (Comissões do período selecionado) para o próximo mês.

3) Optar pela forma de atuação para a “Ação no lançamento” e “Forma de exibição do Log”, conforme já explicado no tópico **Lançamento**

**Campo complementar de funcionários que recebem comissão** será utilizado para identificação dos funcionários que recebem comissão. Por exemplo, funcionário saqueiro que é o que carrega sacas para abastecer caminhões, armazéns e outros.

### Comissão

**Período de liberação para digitação das comissões**definirá a data de início e fim para o lançamento de comissões assim como a competência a ser considerada como pagamento.

A informação da **Tabela de cálculo para comissão de saqueiro** será utilizada para definir a tabela de cálculo informando às faixas para o cálculo da remuneração por quantidade de sacos transportados.

A informação do **Evento para pagamento de comissão de saqueiro**será utilizada para lançar na folha de pagamento o evento contendo o valor a pagar das comissões

## **03. TELA Comissão**

**Outras Ações / Ações relacionadas**

| Ação | Descrição |
| --- | --- |
| Incluir | Inclui os dados informados na tela 'Comissões de Funcionários' |
| Editar | Edita os dados existentes na tela 'Comissões de Funcionários' |
| Excluir | Exclui os dados existentes na tela 'Comissões de Funcionários' |

## **04. TELA Lançamento Global de Comissão**

****Principais Campos e Parâmetros****

| Campo | Descrição |
| --- | --- |
| Código de Quebra | Selecione a quebra |
| Seleção de funcionários | Selecione os funcionários |
| Data da comissão | Informe da data para pagamento da comissão |
| Quantidade | Informe a quantidade de comissões a serem lançadas na data informada |
| Ação na comissão | Ignorar / Sobrepor |
| Forma de exibição do log | Simples / Detalhado |

## **05. TELA Lançar Comissão para a Folha**

**Principais Campos e Parâmetros**

| Campo | Descrição |
| --- | --- |
| Código de Quebra | Selecione a quebra |
| Seleção de funcionários | Selecione os funcionários |
| Período de comissão | Informe a data de início e fim para lançamento da comissão |
| Competência | Mês e Ano da Competência para lançamento da comissão para a folha |
| Período | Período para lançamento da comissão para a folha |
| Data Pagamento | Data de Pagamento para o lançamento da comissão para a folha |
| Ação no Lançamento | Ignorar / Sobrepor |
| Forma de exibição do log | Simples / Detalhado |

## **06. TELA Recálculo da Comissão**

**Principais Campos e Parâmetros**

| Campo | Descrição |
| --- | --- |
| Código de Quebra | Selecione a quebra |
| Seleção de funcionários | Selecione os funcionários |
| Período de comissão | Informe a data de início e fim do período da comissão |
| Período para recálculo da comissão | Informe a data de início e fim para recálculo da comissão |
| Forma de exibição do log | Simples / Detalhado |

## **07. TELA Períodos da Comissão**

**Outras Ações / Ações relacionadas**

| Ação | Descrição |
| --- | --- |
| Incluir | Inclui os dados informados na tela 'Comissões de Funcionários' |
| Editar | Edita os dados existentes na tela 'Comissões de Funcionários' |
| Excluir | Exclui os dados existentes na tela 'Comissões de Funcionários' |

## **08. TABELAS UTILIZADAS**

* PFUNC
* PPARAMADICIONAIS
* PPARAMFILIAL
* PCOMISSAO
* PRGRCALCTAREFAAGRARIA
* PPRODUCAOAGRÁRIA
* PFFINANC
