---
content_hash: 6f4f569c0bae16579672bf4d02016b01927590adfa0b43841a9204a4c51cee0a
fetched_at: '2026-06-29T00:09:49.481108+00:00'
page_id: '435105298'
product: rm
source: tdn-rm
title: Contrato de Locação - Dados Gerais - Dados Reajuste
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105298
version: 26
---

#FF9000Período de Reajuste

* **Periodicidade:** Determina qual a quantidade de meses que o processo de Reajuste será aplicado, repetidamente, a partir de uma Data Base do Reajuste;
* **Data Base do Reajuste:**Determina qual será a Data base para do Reajuste, onde a partir dessa data somada a periodicidade, será calculado a Data do Próximo Reajuste que será realizado. Possui as seguintes opções:

  #FF9000
  + **Data Início Vigência Contrato:** Ao marcar esta opção o cálculo de reajuste deve considerar a data inicial do período de reajuste como a "data de início da vigência do contrato". Segue um exemplo de reajuste com essa opção:
  + **Data Início Locação:** Ao marcar esta opção o cálculo de reajuste deve considerar a data inicial do período de reajuste como a "data de início da Locação". Segue um exemplo de reajuste com essa opção:
  + **Data do Contrato:** Ao marcar esta opção o cálculo de reajuste deve considerar a data inicial do período de reajuste como a "data do Contrato". Segue um exemplo de reajuste com essa opção:
  + **Primeiro Vencimento:** Ao marcar esta opção o cálculo de reajuste deve considerar a data inicial do período de reajuste como a "data da primeira parcela".
* **Data do Próximo Reajuste:** Este campo exibe a data do próximo reajuste. No caso do reajuste ainda não realizado, é exibido o resultado da soma do valor do campo "Periodicidade" e "Data Base" definida. No caso de reajuste do já realizado, é exibido o resultado da soma do valor do campo "Periodicidade" e a data do último reajuste.
* **Considerar valor reajustado quando:** Indica como o valor reajustado será considerado para a geração de lançamentos
  + **Reajuste ocorrer até o início do período de locação:** O valor reajustado só será considerado para geração do lançamento se o reajuste ocorrer até a data de início do período de locação deste lançamento
  + **Reajuste ocorrer até o final do período de locação:** O valor reajustado será considerado para geração do lançamento se o reajuste ocorrer até a data de final do período de locação deste lançamento
#FF9000Reajuste por Índice

Os campos abaixo permitem definir como será realizado o Reajuste por Índice. Por padrão os campos vem habilitados, porém se o campo "Fórmula de reajuste" for preenchido, os campos serão desabilitados. Pois é permitido somente um tipo de reajuste por Contrato, através de Índice ou Fórmula.

* **Índice:** Determina qual Índice será utilizado no Reajuste. Exibe todos os registros cadastrados em Moedas e Índices do módulo Gestão Financeira;
* **Defasagem Cotação:** Nesse campo é possível determinar em quantos meses será a defasagem da cotação do Índice determinado do Contrato de Locação.  Segue um exemplo de utilização desse campo:

* + - Defasagem = 2: Significa que no reajuste, os contratos serão corrigidos com a variação do índice referente a 2 meses anterior a da data do reajuste.

* **Deflação:** Nesse campo é possível determinar como será o tratamento do Contrato de Locação quando acontecer deflação no período do Reajuste:

* + **Permite Deflação:** Aplica o reajuste mesmo que tenha a deflação em seu cálculo;

* + - * **Observação:** Este parâmetro irá trabalhar em conjunto com o parâmetro da coligada "**Não permitir que a deflação altere o valor da Parcela para menos que o valor original**", detalhado logo abaixo neste documento;

* + **Ignora Deflação por Período**: Se este parâmetro estiver marcado, quando o reajuste detectar deflação a correção do período não deverá ser calculada. Dessa forma o valor do reajuste será zerado, mantendo o atual valor de Locação.  
    Foi criado também um parâmetro por coligada no seguinte caminho: Parâmetros TOTVS Incorporação >> Aluguel >> Contrato de Locação>> "**Não permitir que a deflação alterar o valor da Locação para menos que o valor original**" e se marcado, ao reajustar a correção monetárias e a mesma houver uma deflação, o sistema não permitirá que o valor da parcela fique menor que o valor original.

* + **Valor do índice informado nas cotações:** Nesse campo permite definir qual o tipo de Índice está sendo utilizado no Contrato de Locação. Possui as seguintes opções:
    - **Índice Mensal:** Marcando esta opção o usuário deve informar o índice mensal no cadastro de cotações do Índice. Segue um exemplo de cotação com índice mensal

|  |  |
| --- | --- |
| **Mês** | **Índice Mensal** |
| jun/13 | 0,75 |
| jul/13 | 0,26 |
| ago/13 | 0,15 |
| set/13 | 1,5 |
| out/13 | 0,86 |
| nov/13 | 0,29 |
| dez/13 | 0,6 |
| jan/14 | 0,48 |
| fev/14 | 0,38 |
| mar/14 | 1,67 |
| abr/14 | 0,78 |
| mai/14 | -0,13 |

* + - **Índice****Acumulado:** Marcando esta opção o usuário deve informar o índice acumulado mensalmente no cadastro de cotações da moeda. Segue um exemplo de cotação com índice acumulado:

|  |  |
| --- | --- |
| **Mês** | **Índice Mensal** |
| jun/13 | 1.240,03 |
| jul/13 | 1.249,33 |
| ago/13 | 1.252,58 |
| set/13 | 1.254,46 |
| out/13 | 1.273,27 |
| nov/13 | 1.284,22 |
| dez/13 | 1.287,95 |
| jan/14 | 1.295,68 |
| fev/14 | 1.301,90 |
| mar/14 | 1.306,84 |
| abr/14 | 1.328,67 |
| mai/14 | 1.339,03 |

* **Cálculo Pró-rata Dia:** Ao marcar esse parâmetro, o contrato passará a utilizar o cálculo Pro-Rata Dia assim como será habilitado os parâmetros para definir como será aplicado o reajuste e as alterações de valor causadas por aditivos. Para ver exemplos do cálculo Pro Rata para Aditivos . Seguem as opções:

* + **Rateio de Índice:** Nesse campo é possível definir como será realizado o rateio do períodos, utilizando as seguintes opções:

* + - Valor: Mês Civil
    - Valor: Mês Comercial

* + **Aplicação de Índice:** Nesse campo é possível definir como será realizado a multiplicação do valor rateado do período, utilizando as seguintes opções:

* + - Valor: Mês Civil
    - Valor: Mês Comercial

* + **Qual a diferença entre Mês Civil e Mês Comercial?**

* + - **Mês Civil:** Expressão existente no mercado financeiro e administrativo que considera todos os dias do mês, da forma real mesmo. Por exemplo, em fevereiro teremos 28 ou 29 dias. Sendo assim, o **Ano Civil** é considerado com 365 dias.
    - **Mês Comercial:** Considera que todos os meses tenham 30 dias, com isso, o **Ano Comercial** é considerado com 360 dias.

* + **Exemplos de cálculos Pró-rata Dia**

* + - Rateio de Índice: Mês Civil e Aplicação de Índice: Mês Civil
    - Rateio de Índice: Mês Comercial e Aplicação de Índice: Mês Comercial
    - Rateio de Índice: Mês Comercial e Aplicação de Índice: Mês Civil

* + **Capitalizado (Correção sobre Correção):** Ao marcar esse parâmetro o Reajuste calcula a correção acumulada "multiplicando" os índices mensais (correção sobre correção semelhante aos juros compostos).
#FF9000Reajuste por Fórmula

* **Fórmula do Reajuste:** Nesse campo é possível informar uma fórmula para que seja utilizada no cálculo do Reajuste. Ao preencher esse campo, os campos do Reajuste por Índice são desabilitados, pois só é permitido um tipo de Reajuste por Contrato de Locação, por Índice ou Fórmula. O cálculo do reajuste é realizado para cada imóvel e então o valor do contrato é a soma dos valores de cada imóvel. Portanto o valor da fórmula será aplicado individualmente para cada imóvel. Para o desenvolvimento da fórmula sugerimos utilizar a função de fórmula [ALGCONTEXTO](https://tdn.totvs.com/pages/viewpage.action?pageId=435105346#Gestão-FunçõesdeFórmulas-Aluguel-algcontexto) que retorna campos importantes para realizar o cálculo. Para mais informações sobre esta função, [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=435105346#Gestão-FunçõesdeFórmulas-Aluguel-algcontexto).

Exemplo de fórmula: *ALGCONTEXTO('VALORBASE') \* 1.05*

#FF9000Outros Reajustes

A aba Outros Reajustes está disponível a partir da versão 12.1.2209.

Este cadastro visa agrupar os reajustes de **fundo promocional** e de **condomínio**, permitindo ao usuário utilizar parâmetros diferentes de reajuste para estas cobranças.

Todo o cadastro, tanto quando para fundo quanto para condomínio, segue a mesma lógica dos dados de reajuste do contrato, ou seja, temos os mesmos campos porém com cadastros diferentes, que irão atuar nos cálculos de reajuste de forma isolada quando disparado através destes processos.

#FF9000Importante

A partir da versão **12.1.2209**, foram modificados os comportamentos dos processos:

* Processo de reajuste
* Processo de desfazer reajuste

Os processos irão gerar novos lançamentos com os valores reajustados ou não no caso de desfazer e os lançamentos anteriores não serão excluídos da base de dados eles passam a ter o status cancelados.

Isto deve-se ao fato de permitir uma melhor rastreabilidade destes lançamentos com status cancelados, possibilitando uma posterior consulta ao mesmos.
