---
content_hash: 99605360057b679cb5f5f04e4276f745ea86c4859c048a19cc3ecc763649df5d
fetched_at: '2026-06-29T00:11:26.125027+00:00'
page_id: '715818269'
product: rm
source: tdn-rm
title: Rendimentos Recebidos Acumuladamente (RRA)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=715818269
version: 44
---

## 

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tela Parametrizador**
   1. **Principais Campos e Parâmetros**
5. **Tabelas utilizadas**

## **01.****VERSÕES**

false

**A partir dos patches:**

* 12.1.34.258
* 12.1.2205.207
* 12.1.2209.152
* 12.1.2302
* e Superiores

IMPORTANTE:

**Alterações para contemplar base de IRRF RRA folha e férias juntas foram a partir dos patches:**

* 12.1.2410.281
* 12.1.2502.182
* 12.1.2506.124
* 12.1.2510 e Superiores

## **02. VISÃO GERAL**

Conforme o DECRETO Nº 9580, DE 22 DE NOVEMBRO DE 2018, (DOU DE 23.11.2018), SEÇÃO VI:  
DOS RENDIMENTOS RECEBIDOS ACUMULADAMENTE  
Art. 48 - Os rendimentos recebidos acumuladamente e submetidos à incidência do imposto sobre a renda com base na tabela progressiva, quando correspondentes a anos-calendário anteriores ao do recebimento, serão tributados exclusivamente na fonte, no mês do recebimento ou do crédito, separadamente dos demais rendimentos recebidos no mês, observado o disposto no art. 702 ao art. 706. (Lei nº 7713, de 1988, art. 12-A).

Deve constar o rendimento pago de forma acumulada (art. 12-A da Lei no 7.713, de 1988 **<http://www.planalto.gov.br/ccivil_03/leis/L7713.htm>****),**relativo a anos-calendário anteriores ao do pagamento, decorrentes de:

a)  aposentadoria, pensão, transferência para a reserva remunerada ou reforma, pagos pela Previdência Social da União, dos estados, do Distrito Federal e dos municípios; ou ainda

b) os provenientes do trabalho, inclusive aqueles oriundos das decisões das Justiças do Trabalho, Federal, Estaduais e do Distrito Federal, relativos a anos-calendário anteriores ao do pagamento;

c) A partir da DIRF de 2017, passou a ser obrigatório as seguintes informações referentes ao pagamento de RRA:

* + Nome e CPF/GNPJ do Advogado;
  + Valores referente Pensão Alimentícia discriminado por Dependentes.

No TOTVS Folha de Pagamento, para gerar as informações dos Rendimentos Recebidos Acumuladamente dos funcionários que receberam este tipo de verba, basta proceder da seguinte maneira:

1. Criar eventos com os novos códigos de cálculo para separar os valores de RRA.
2. Deverá existir um envelope de pagamento separado para pagamento do RRA, não poderá estar no mesmo envelope de pagamento da folha.

IMPORTANTE:

Ou seja, os períodos definidos no parametrizador para receberem as verbas referentes ao RRA não podem ser usados no momento do cálculo. Nesse momento o período definido nos parâmetros locais deve ser diferente dos períodos definidos para RRA.

1. 1. Definir período para lançamento no parametrizador (usuário irá informar, devendo ser acima de 99, igual foi feito para retificação);
   2. Esse período deve ser bloqueado pelo usuário para qualquer lançamento, se tratando de uma boa prática esse bloqueio;
   3. A diferença de Férias e Folha podem ser inseridos no mesmo período;
   4. Décimo terceiro deve ser inserido em período diferente.
   5. Para rescisão complementar entendemos que seria o período completo como RRA não precisando separar entre folha, férias e 13º salário.
   6. No período destinado ao cálculo do RRA será lançado somente eventos de diferença cujo valor refere-se a eventos originais com incidência em imposto de renda. Os demais eventos que tiverem diferenças e não estiverem marcados em nenhuma incidência de imposto de renda, até mesmo dedutível de imposto de renda, serão lançados no período atual.

      **Exemplo**: Se no envelope de pagamento referente ao ano anterior tiver um evento de desconto sem incidência em IR e com uma fórmula que referencia RC haverá cálculo de diferença e esse valor será lançado no envelope atual, como na imagem abaixo:
   7. Será inserido um período no mês dezembro com o valor do código de cálculo que irá armazenar o mês da diferença na PFVERBASDIS quando não existir o período referência em dezembro.

      **Exemplo:**Férias iniciadas em 02 de janeiro serão pagas em dezembro, mas o período de lançamento será em janeiro, então se houver reajuste salarial de anos anteriores, a diferença calculada deverá ser considerada como RRA devido o pagamento ser no ano anterior ao exercício atual. Não existirá o período de lançamento das férias em dezembro por isso será criado um período novo em dezembro para o lançamento do código de cálculo que irá armazenar o mês da diferença na PFVERBASDIS. Mas se o reajuste salarial for o ano exercício atual, o mesmo não será calculado como RRA. O mesmo vale para férias partidas que finalizam em Janeiro do ano corrente, onde o reajuste contempla somente o mês de retorno das férias.

      Quando o reajuste salarial for no ano corrente, cálculo realizado na competência de Dezembro e o caixa Janeiro, também não será considerado como RRA qualquer diferença calculada (Folha, Férias, 13º e Rescisão).

Dica:

Continuará existindo os eventos de base para não ter impactos na DIRF – referentes ao período anterior a essa implementação

* Continuará preenchendo o histórico de RRA de acordo com o mês competência, ano competência e período;
* O histórico de RRA deverá ser separado Folha/Férias e 13o. Salário (preencher os campos já existentes).

Quando for necessário recálculo de diferenças é imprescindível o cancelamento do movimento para que não haja acúmulo de valores, principalmente no histórico de RRA.

* Quando for calculada a diferença salarial, quando é realizado também o pagamento de RRA, faz-se necessário cancelar o período da diferença e também o período de RRA (automaticamente). Para que isto seja possível,  o cancelamento do período da diferença salarial deverá ser integral (conforme exemplo abaixo). Caso o cancelamento seja feito parcialmente, selecionando os eventos, o registro de RRA não será cancelado do Histórico de RRA, mesmo que seus registros sejam apagados do envelope de pagamento, inclusive.

**Exemplo:** A opção "Cancela todos os eventos" deverá estar marcada para que o cancelamento do período da diferença salarial seja integral, conforme explicado anteriormente

                   

IMPORTANTE:

Seguindo as [Orientações Consultoria de Segmentos - Apuração e tributação de rendimento recebido acumuladamente (RRA)](https://tdn.totvs.com.br/pages/viewpage.action?pageId=152801855)

01 - No cálculo do IRRF referente ao RRA não será deduzido valores de dependentes e de +65 anos, visto que no Art. 39 da IN nº 1.500/2014 é exposto que somente é dedutível para a base de RRA: Pensão Alimentícia e contribuição de INSS. 

02 - A base de cálculo do IRRF para RRA de Folha e de Férias devem ser unificadas. 

**Observação:** Mesmo o cálculo da base sendo unificado, os valores a serem descontados seguirão em eventos separados nos códigos de cálculos:

* [207 - IRRF RRA](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718702)
* [211 - IRRF RRA Férias](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719935)

Inclusive foi enviado para o eSocial para verificar a aceitação do XML pelo RET, retornou do eSocial com sucesso.

## **03. EXEMPLO DE UTILIZAÇÃO**

Parametrização

Marcar o parâmetro no Parametrizador / Folha Normal / Geral 2/2 e indicar os períodos para cada cálculo

Folha/Férias

Base configurada com alteração salarial para o mês 11/2021 sendo o período atual 02/2022 e

no período 1 foi lançado diferença de folha e diferença de férias a partir de 11/2021

 

ENVELOPE CALCULADO COM DIFERENÇA FOLHA

**Cálculo de RRA Folha / Férias**

ENVELOPE CALCULADO COM RRA FOLHA/FÉRIAS

**Cálculo de RRA Folha / Férias**

No cálculo da folha foi considerado o valor de 11/2021 de folha e no cálculo das férias foi considerada as férias pagas em 12/2021

HISTÓRICO DE RRA

VERBAS DE DISSIDIO

VALORES LANÇADOS PARA O MOVIMENTO DO DEPENDENTE

13º Salário

Pago o 13º Salário em Dezembro de 2021

APÓS ALTERAÇÃO SALARIAL FOI CALCULADA A DIFERENÇA REFERENTE AO ANO ANTERIOR

NO PERÍODO ATUAL APRESENTA O VALOR DA BASE DE FGTS

NO PERÍODO INDICADO NO PARAMETRIZADOR APRESENTA OS VALORES DO CÁLCULO DA DIFERENÇA

HISTÓRICO DE RRA

VERBAS DE DISSIDIO

VALORES LANÇADOS PARA O MOVIMENTO DO DEPENDENTE

Rescisão

Calculada a rescisão contratual em 31/10/2021

EM 08/2022 FOI ALTERADO O SALÁRIO RETROATIAVO A 10/2021 – CALCULADA A RESCISÃO COMPLEMENTAR FORAM LANÇANDOS NO ENVELOPE ATUAL

NO ENVELOPE RRA – SOMENTE EVENTOS QUE TEM INCIDÊNCIA IRRF

HISTÓRICO DE RRA

VERBAS DE DISSIDIO

VALORES LANÇADOS PARA O MOVIMENTO DO DEPENDENTE

LANÇAMENTO DO LÍQUIDO DE RESCISÃO COMPLEMENTAR

IRRF - Exemplo Cálculo RRA

Cálculos realizados em base fictícia e com valores fictícios:

**IRRF RRA Folha e IRRF RRA Férias**

Para o funcionário do cenário foram pagas diferenças de salário dos meses 10 e 11/2022. O salário de 12/2022 foi pago no dia 05/01/2023.

Primeiro foi calculado a diferença de folha e com isso o IRRF RRA FOLHA considerando os 2 meses

Depois  foi calculado a diferença de férias e com isso o IRRF RRA FÉRIAS considerando os 3 meses e a base total de folha e férias

**IRRF RRA 13º Salário**

**IRRF RRA Rescisão**

No cálculo houve o primeiro desconto de um valor referente a folha de 10/2022 e o desconto IRRF RRA Folha da rescisão considerando a base de IRRF folha do período 100 e a base do IRRF RRA Férias.

IRRF RRA Folha - considera o valor IRRF RRA Folha e a base IRRF RRA Férias

IRRF RRA Férias - considera o valor de IRRF RRA Folha

IRRF RRA 13º Salário

**Abaixo iremos exemplificar cenários onde os cálculos de diferença não são considerados RRA, mesmo o pagamento original ter ocorrido em anos-calendários anteriores:**

RRA - Reajuste salarial não retroativo a anos calendários anteriores - Rescisão

Exemplificando a situação quando o colaborador tem rescisão com aviso prévio projetando até Janeiro do ano atual da base de dados:

Colaborador foi demitido dia 20/11/2023 com 60 dias de aviso. O Pagamento foi realizado no dia 30/11/2023:

O Colaborador teve um reajuste salarial por dissídio referente ao dia 01/01/2024. O Módulo Folha de Pagamento está na competência 01/2024

Fazendo o cálculo da Rescisão complementar, o mesmo não foi calculado como RRA, pois a data de mudança salarial não é de anos calendários anteriores:

RRA - Reajuste salarial não retroativo a anos calendários anteriores - Férias

Exemplificando a situação de colaborador que tem férias iniciando em Janeiro, mas o pagamento foi em Dezembro do ano anterior:

Colaborador com férias iniciando dia 02/01/2024 e pagamento dia 29/12/2023:

Em fevereiro de 2024 foi realizado um reajuste salarial por dissídio referente a comp. 01/2024:

Ao fazer o cálculo de diferença de férias as mesmas não foram pagas como RRA, pois o pagamento referente as férias gozadas em janeiro não se trata de exercício anterior. O Pagamento em Dezembro é mera antecipação:

RRA - Reajuste salarial não retroativo a anos calendários anteriores - Férias Partidas

Exemplificando o cenário onde o colaborador teve férias iniciando em Dezembro e finalizando em Janeiro:

Colaborador com férias de 18/12/2023 a 06/01/2024 com pagamento dia 14/12/2023:

Reajuste salarial realizado em Fevereiro de 2024 retroativo a Janeiro de 2024:

Ao calcular a diferença de férias, as mesmas não foram consideradas como RRA:

RRA - Reajuste salarial em Dezembro/ Caixa Janeiro - Férias

Exemplificando o cenário onde o colaborador teve férias iniciando em Dezembro e finalizando em Janeiro, onde a alteração salarial foi processada na competência de Dezembro com pagamento em Janeiro:

Colaborador com férias de 18/12/2023 a 06/01/2024 com pagamento dia 14/12/2023:

Reajuste salarial processada na competência 12/2023 retroativa ao mês 11/2024:

Cálculo de diferença de férias realizado com pagamento para o dia 05/01/2024 não foi considerado como RRA:

RRA - Reajuste salarial em Dezembro/ Caixa Janeiro - 13º Salário

Exemplificando o cenário onde o colaborador teve pagamento de 13º Salário em Dezembro e cálculo de diferença em Dezembro, onde a alteração salarial foi processada na competência de Dezembro com pagamento em Janeiro:

Colaborador com pagamento do 13º Salário no dia 20/12/2024:

Reajuste salarial processado na competência 12/2023:

Cálculo de diferença de 13º Salário realizado com pagamento para o dia 05/01/2025 não foi considerado como RRA:

## **04.** **TELA Parametrizador**

****Principais Campos e Parâmetros****

| Campo | Descrição |
| --- | --- |
| Utiliza Cálculo RRA | Parâmetro para marcar quando utiliza o cálculo RRA |
| Período Folha/Férias | Período para lançamento da diferença de folha e/ou férias referente ao RRA e deve ser maior que 99. |
| Período 13º Salário | Período para lançamento da diferença de 13º salário referente ao RRA, deve ser maior que 99 e diferente dos outros períodos. |
| Período Rescisão | Período para lançamento da diferença de rescisão referente ao RRA, deve ser maior que 99 e diferente dos outros períodos. |

## **05. TABELAS UTILIZADAS**

* PPARAMADICIONAIS
* PEVENTO
* PFFINANC
* PFVERBASDIS
* PFVERBASDISFER
