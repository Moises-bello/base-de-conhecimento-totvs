---
content_hash: 763aa76a071d7d2102b285c10ca399eb2e8dca276eca57d304a52f09a925170f
fetched_at: '2026-06-29T00:11:50.248743+00:00'
page_id: '839304283'
product: rm
source: tdn-rm
title: Apuração do FGTS na Rescisão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=839304283
version: 19
---

## 

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tabelas utilizadas**

## **01. VERSÕES**

false

**A partir dos patches/releases:**

* 12.1.2306.252
* 12.1.2310.194
* 12.1.2402.132
* 12.1.2406 e Superiores

## **02****. VISÃO GERAL**

Para a apuração do FGTS Digital, os valores referente ao aviso prévio não devem ser considerados para descontos de eventos que estornam na base de FGTS caso o funcionário possua alguma verba que estorna a base, mesmo sendo valor menor. O mesmo ocorre para a Base de FGTS 13º Salário, onde valores que estornam a base de FGTS de 13º não podem ser descontados dos proventos referente ao 13º indenizado.

Para atender esta determinação da legislação, foram feitas as alterações abaixo no produto quando tem rescisão e verbas que estornam na apuração da Base de Cálculo do FGTS e FGTS 13º.

**Rescisão e Rescisão Complementar**

* Código de Cálculo 467 - FGTS AVISO PRÉVIO do tipo Base para calcular o Valor do FGTS de Aviso Prévio considerando como Base de FGTS do aviso prévio os eventos com os CC’s 62, 219, 99 e 140, e todos os eventos de média do grupo de Aviso Prévio do Sindicato, e se os mesmos incidirem/estornarem no FGTS Folha.
* Código de Cálculo 468 - FGTS 13º INDENIZADO do tipo Base para calcular o Valor do FGTS 13º sobre aviso prévio considerando como Base de FGTS 13º sobre aviso prévio os eventos com os CC’s  71, 220 e 98 e se os mesmos incidirem/estornarem no FGTS 13º.
* Códigos de Cálculo 26 e 73 não consideram os valores dos CC 62, 99 e 219, e todos os eventos de média do grupo de Aviso Prévio do Sindicato, na base de cálculo e se os mesmos incidirem/estornarem no FGTS Folha.
* Códigos de Cálculo 31 e 133 não consideram os valores dos CC 71, 220 e 98 na base de Cálculo e se os mesmos incidirem/estornarem no FGTS 13º.
* Código de Cálculo 28 considera os novos CC  na base cálculo para o cálculo da Multa
* Caso o valor do depósito for negativo, não irá lançar os eventos com os novos CC’s como já ocorre com os anteriores
* Na Rescisão Complementar os novos códigos de cálculo para as bases indenizadas 469 - BASE DE FGTS DIFERENÇA AVISO INDENIZADO e 470 - BASE DE FGTS DIFERENÇA 13º INDENIZADO
* Ao realizar o lançamento da rescisão do tipo 4, com a opção "Desconta Aviso Prévio" marcada, o CC 140 (com a propriedade “Incide FGTS” marcada na aba Inc. Descontos no próprio CC) fará o abatimento do valor mensal da Base Folha, do campo FGTS, na aba Incidências, do Envelope de Pagamento

IMPORTANTE

01 - Quando houver cálculo de rescisão complementar referente a rescisões processadas antes da liberação dessa implementação, os valores do FGTS não serão separados por não existirem Código de Cálculo 467 - FGTS AVISO PRÉVIO e Código de Cálculo 468 - FGTS 13º INDENIZADO na rescisão original.

02 - Quando houver atualização da base de dados os campos novos serão preenchidos com NULL. Os campos criados nas tabelas somente serão preenchidos após cálculos depois da conversão da base de dados.

**Ficha Financeira/Envelope de pagamento**

* Campos no período da Ficha Financeira para armazenar a Base de FGTS Aviso prévio e a Base FGTS 13º Sobre Aviso Prévio. Os depósitos são calculados em tela.
* Novos campos da tabela PFPERFF: BASEFGTSAVPREVIO e BASEFGTS13AVPREVIO
* Demonstração dos valores negativos será mantida
* Considera o percentual 2% ou 8% conforme o tipo de funcionário para o FGTS
* Os campos de valores são calculados, não retornando de campo da tabela
* Os campos na tela do envelope  de base devem ser calculados automaticamente quando o usuário marcar/desmarcar a incidência de FGTS

**Resilição**

* Campos na tabela PFRESILICAOENCARGOS: BASEFGTSAVPREVIO e BASEFGTS13AVPREVIO - para armazenar a Base de FGTS Aviso prévio e a Base FGTS 13º Sobre Aviso Prévio.

* Demonstração na tela do cadastro de Resilição

**Passivo Trabalhista**

* Campos na tabela PSIMULADEMISSAO: FGTSAVPREVIO e FGTS13AVPREVIO para armazenar o valor de depósito de FGTS Aviso prévio e FGTS 13º Sobre Aviso Prévio.

* Demonstração no relatório do Passivo Trabalhista

**Funções de Fórmula**

Tratamento das novas regras do FGTS / FGTS Indenizado nas funções abaixo:

  BASECALCULO -> Novos tipos FGTSINDENIZADO e FGTS13INDENIZADO

  BASEFGTS -> Irá retornar a soma dos FGTS Folha e FGTS Indenizado

  BASEFGTSFF -> -> Irá retornar a soma dos FGTS Folha e FGTS Indenizado

  BSFGTS13 -> -> Irá retornar a soma dos FGTS 13o e FGTS 13o Indenizado

  BASEFGTS13FF -> -> Irá retornar a soma dos FGTS 13o e FGTS 13o Indenizado

## **03****. EXEMPLO DE UTILIZAÇÃO**

Funções de Fórmulas

Realizada a rescisão e no cálculo foram demonstrados os seguintes valores no envelope:

BASECALCULO - FGTSINDENIZADO = 1428,05

BASECALCULO - FGTSINDENIZADO = 117,67

BASEFGTS e BASEFGTSFF = 1524,32 + 1428,05 = 2952,37

BSFGTS13 e BASEFGTS13FF = 823,67 + 117,67 = 941,34

Rescisão

Após a inclusão dos códigos de cálculo necessários para o cálculo da rescisão com FGTS Digital os valores que incidem em FGTS são:

FGTS = 1412 + 96,27 = 1508,27 \* 0,08 = 120,66

FGTS13 = 823,67 \* 0,08 = 65,89

FGTS AVISO INDENIZADO = 1412 + 16,05 = 1428,05 \* 0,08 = 114,24

FGTS 13º INDENIZADO = 117,67 \* 0,08 = 9,41

Rescisão Complementar de Rescisão SEM CCs 467 e 468

Mesmo que a rescisão original não tenha sido calculada com o FGTS Digital, será necessário a inclusão dos eventos com os códigos de cálculos novos para executar o processo da rescisão complementar.

Veja exemplo de uma rescisão calculada antes da implementação do FGTS Digital:

Após a inclusão dos códigos de cálculo necessários para o cálculo da rescisão complementar com FGTS Digital os valores que incidem em FGTS são:

FGTS = 500 + 500 = 1000 \* 0,08 = 80,00

FGTS13 = 291,66 + 41,67 = 333,33 \* 0,08 = 26,67

Mas serão inseridos os eventos com código de cálculo 469 - BASE DE FGTS DIFERENÇA AVISO INDENIZADO e código de cálculo 470 - BASE DE FGTS DIFERENÇA 13º INDENIZADO que são as bases de cálculo da rescisão complementar que não dependem do cálculo da rescisão original:

Rescisão Complementar de Rescisão COM CCs 467 e 468

Após a inclusão dos códigos de cálculo necessários para o cálculo da rescisão complementar com FGTS Digital os valores que incidem em FGTS são:

FGTS = 1000 + 68,18 = BASE 1068,18 \* 0,08 = 85,45

FGTS13 = 583,33 \* 0,08 = 46,67

FGTS AVISO INDENIZADO = 1000 + 11,36 = BASE 1011,36 \* 0,08 = 80,91

FGTS 13º INDENIZADO = 83,33 \* 0,08 = 6,67

Passivo Trabalhista

Após conversão da base de dados, importação do novo relatório e execução do processo de Passivo Trabalhista será possível a visualização do relatório com os novos campos:

Resilição

Após conversão da base de dados e execução do cálculo da resilição será possível a visualização dos novos campos:

Encargos

Após conversão da base de dados e execução do processo de Gerar Encargos, será possível visualizar no log do processo, a linha referente ao FGTS na Folha e 13º :  
  
  
  
**Folha:**  
  
- Encargo = (base FGTS + base FGTS Av. Prévio) \* % encargo / 100 =

**13º :**  
  
- Encargo = (base FGTS 13º + base FGTS 13º Av. Prévio) \* % encargo / 100 =

Abatimento do Desconto do Aviso Prévio na Base Folha do FGTS

Ao realizar a rescisão com o tipo de demissão 4 (Iniciativa Empregado sem justa causa), utilizando a data da competência corrente e independente do número de dias de aviso prévio utilizados e marcando a opção "Desconta Aviso Prévio"

Após calcular a rescisão e abrir o Envelope de Pagamento, ao localizar o lançamento “Desconto de Aviso Prévio” (lançamento referente ao CC 140, com a propriedade “Incide FGTS” marcada na aba Inc. Descontos no próprio CC), observou-se o seu valor, neste caso de R$855,54

Ao consultar a aba Incidências, observou-se que a Base Folha do FGTS incide o valor do desconto e apresenta o valor já descontado de R$7.183,18 (R$8.038,72 da Base Folha do INSS - R$855,54 do CC 140, no formato de "Desconto de Aviso Prévio" no Envelope de Pagamento)

**04. TABELAS UTILIZADAS**

* PFPERFF
* PFFINANC
* PSIMULADEMISSAO
* PFRESILICAOENCARGOS
