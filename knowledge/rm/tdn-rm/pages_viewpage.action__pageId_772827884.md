---
content_hash: 05814ce454d515dbeb3bba0ad76f4aec05a244b01acbcab367a98f967e3604db
fetched_at: '2026-06-29T00:11:36.519847+00:00'
page_id: '772827884'
product: rm
source: tdn-rm
title: Recesso de Estágio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=772827884
version: 30
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Recesso Estagiário |
| País: | Brasil |

## **02. SITUAÇÃO/REQUISITO**

De acordo com a Lei nº 11.788, de 25 de setembro de 2008, os estagiários têm direito a recesso conforme descrito no artigo 13 da referida lei:  
Art. 13. É assegurado ao estagiário, sempre que o estágio tenha duração igual ou superior a 1 (um) ano, período de recesso de 30 (trinta) dias, a ser gozado preferencialmente durante suas férias escolares.  
§ 1o O recesso de que trata este artigo deverá ser remunerado quando o estagiário receber bolsa ou outra forma de contraprestação.  
§ 2o Os dias de recesso previstos neste artigo serão concedidos de maneira proporcional, nos casos de o estágio ter duração inferior a 1 (um) ano.

## **03. SOLUÇÃO**

Para contemplar a administração dos dias de direito de recesso e efetivar os cálculos relativos, o módulo de férias do TOTVS Folha de Pagamento foi adequado a esta lei.

11ParametrizaçãoParametrizaçãoImportante!

O controle de períodos aquisitivos para o recesso tem funcionamento semelhante ao já existente para férias de funcionários normais, onde a cada período de 12 meses o estagiário terá direito a 30 dias de recesso e também o recesso poderá ser dividido em mais de um período de gozo. A executação do processo Geração do Histórico de Provisão irá provisionar em cada mês de estágio o direito e o valor relativo a 2,5 dias de recesso.

1) Para que o TOTVS Folha de Pagamento realize a administração dos períodos aquisitivos, dias de recesso e seus cálculos, é necessário que o parâmetro '**Considera tratamento para Recesso de Estagiário**' esteja marcado. Este parâmetro está localizado em **RM / RH / Folha de Pagamento / Configurações / Parametrizador / Folha de Pagamento / Férias / Controle 1/2**, conforme imagem abaixo:

2) Para utilizar o parâmetro '**Considera tratamento para Recesso de Estagiário**', será necessário incluir os cadastros dos eventos a seguir:

[Código de Cálculo - 332 - RECESSO DE ESTÁGIO](https://tdn.totvs.com/pages/viewpage.action?pageId=452719754) Evento valor do tipo provento. Destinado ao cálculo de recesso de estagiário, sendo os descontos de acordo com as incidências parametrizadas pelo usuário.

[Código de Cálculo - 333 - RECESSO DE ESTÁGIO VENCIDO](https://tdn.totvs.com/pages/viewpage.action?pageId=452718760) Evento valor do tipo provento. Destinado ao cálculo de recesso de estagiário vencido, sendo os descontos de acordo com as incidências parametrizadas pelo usuário.

[Código de Cálculo - 334 - RECESSO DE ESTÁGIO PROPORCIONAL](https://tdn.totvs.com/pages/viewpage.action?pageId=452718761) Evento valor do tipo provento. Destinado ao cálculo de recesso de estagiário proporcional, sendo os descontos de acordo com as incidências parametrizadas pelo usuário.

[Código de Cálculo - 356 - DIFERENÇA DE RECESSO DE ESTÁGIO](https://tdn.totvs.com/pages/viewpage.action?pageId=829293262) Evento valor do tipo provento. Destinado ao cálculo da diferença de recesso de estagiário,  recesso de estagiário vencido e recesso de estagiário proporcional, sendo os descontos de acordo com as incidências parametrizadas pelo usuário.

3) O cadastro do período de gozo do recesso estagiário será realizado na mesma interface utilizada para o cadastro de férias, através do ícone de Cadastro de Férias: 

A tela Período de Gozo será aberta.

**Observações:**

No caso do recesso de estagiário, diversos recursos da **tela de Período de Gozo** estarão desabilitados devido a não serem recursos comuns aos estagiários, conforme abaixo:

**•    Não poderá optar por 1a parcela 13º salário se for tipo T – Estagiário.**  
**•    Não poderá optar por recebimento de abono pecuniário.**  
**•    Não poderá optar por empréstimo de férias.**  
**•    Não haverá tratamento para pagamento de licença remunerada (férias coletivas).**  
**•    Não haverá consulta ao recibo de férias uma vez que os códigos de cálculo utilizados no cálculo de Férias não serão utilizados no cálculo do Recesso.**  
**•    pagamento dos dias de recesso será realizado junto ao pagamento da bolsa.**

4) Deverá ser realizado o cadastramento do período de gozo do recesso e executado o processo **Férias / Cálculo de Férias**, para que seja calculado o evento de Recesso de Estágio.

5) O cálculo do recesso de estágio será executado com base no valor nominal da bolsa estágio, constante no campo Salário, do cadastro do estagiário, somado aos eventos que incidem salário que eventualmente estejam lançados no envelope de pagamento do estagiário relativo ao mês competência atual.

6) Após o cálculo do recesso, deverá ser executado o processo **Férias / Lançamento**, ou poderá realizar este lançamento através da tela Período de Gozo, pelo botão **Lançar**.

7) Executando o lançamento do Recesso de Estágio, o evento cadastrado que possui o código de cálculo 332 - Recesso Estagiário será lançado no envelope de pagamento do mês competência que houver início do gozo do recesso, de acordo com o número total de dias de recesso, independente do fato dos dias serem compreendidos no mês atual ou no próximo mês.

**Observação:** Se for utilizado no evento de pagamento da Bolsa de Estágio com código de cálculo 2 - Dias Trabalhados, o valor deste evento será calculado proporcional ao número de dias estagiados no mês, considerando o número de dias de recesso no mês. Além disto, a situação do Estagiário será atualizada automaticamente de **A – Ativo** para **G – Recesso Remunerado de Estágio**.

8) O próximo passo será executar a Finalização do Recesso do Estagiário, para isto deverá ser executado o processo **Férias / Finaliza** ou poderá executar pelo cadastro de **Período de Gozo** através botão **Finalizar**.

O processo de Finalização sendo executado, irá atualizar o cadastro de **Período Aquisitivo de Recesso**. Além disto, a situação do funcionário será atualizada, retornado de **G – Recesso Remunerado de Estágio** para **A – Ativo.**

9) As rescisões de contrato de estagiários deverão ser efetuadas através do módulo Rescisões, da mesma forma que é feito para funcionários normais. Na rescisão do contrato de estágio, o sistema irá calcular, em hipótese do estagiário não ter gozado do recesso:

**• Recesso indenizado** no caso de haver período aquisitivo de recesso vencido. (Será lançado o evento com código de cálculo 333 - RECESSO DE ESTÁGIO VENCIDO)  
**• Recesso proporcional** para contratos rescindindo com menos 1 ano, ou com mais de 1 ano que apresentar direito a gozo proporcional. (Será lançado o evento com código de cálculo 334 - RECESSO DE ESTÁGIO PROPORCIONAL)

Verificando as seguintes condições:

**•** No **Parametrizador em Rescisão / Cálculo** o parâmetro **Recebem verbas rescisórias - Estagiário** deve estar desmarcado.

**1) Os eventos com códigos de cálculo 333 - RECESSO DE ESTÁGIO VENCIDO e 334 - RECESSO DE ESTÁGIO PROPORCIONAL devem estar cadastros, no Cadastro de Eventos. 2) Será sempre lançado o recesso vencido e o recesso proporcional, independentemente do tipo de rescisão.IMPORTANTE!**

2Cálculo de Recesso de EstagiárioCálculo de Recesso de Estagiário

**Para efetuar o cálculo do Recesso do Estagiário, vamos supor os dados abaixo:**

**Exemplo de Período de Gozo de Recesso:**

**Período aquisitivo de gozo em**  **a**

**Cálculo sendo executado na competência: 01/2022**

**Data do recesso:**  **a**

1) Realizar o cadastro do recesso em **RM / RH / Folha de Pagamento / Administração de Pessoal / Cadastros / Funcionário / Cadastro de Férias**, para que seja calculado o evento de recesso de estágio:

2) Após o cadastro do recesso, deverá ser executado o processo **RM / RH / Folha de Pagamento / Administração de Pessoal / Cadastros / Funcionário / Cadastro de Férias / Lançar**:

3) Executando o lançamento do Recesso de Estágio, o evento cadastrado que possui o código de cálculo 332 – Recesso Estagiário será lançado no envelope de pagamento do mês competência que houver início do gozo do recesso, de acordo com o número total de dias de recesso, independente do fato dos dias serem compreendidos no mês atual ou no próximo mês, conforme o Envelope de Pagamento do estagiário:

**Observação:** Se for utilizado no evento de pagamento da Bolsa de Estágio com código de cálculo 2 - Dias Trabalhados, o valor deste evento será calculado proporcional ao número de dias estagiados no mês, considerando o número de dias de recesso no mês.

4) O próximo passo será executar a Finalização do Recesso do Estagiário, para isto deverá ser executado o processo **RM / RH / Folha de Pagamento / Administração de Pessoal / Cadastros / Funcionário / Cadastro de Férias /** **Finaliza:**

**Observação:** O processo de Finalização sendo executado, irá atualizar o cadastro de **Período Aquisitivo de Recesso**. Além disto, a situação do funcionário será atualizada, retornado de **G – Recesso Remunerado de Estágio** para **A – Ativo.**

3Cálculo da diferença do Recesso de EstagiárioCálculo da diferença do Recesso de Estagiário

**Para efetuar o cálculo da Diferença do Recesso do Estagiário, vamos supor os dados abaixo:**

1) Foi pago para o estagiário no mês de janeiro/2022 - período 1, os valores do envelope abaixo:

2) Foi alterado o salário do estagiário para **R$1.200,00**, em **01/01/2022**:

3) Executar o processo de diferença de férias em **RM / RH / Folha de Pagamento / Férias / Processos / Diferença****:**

3) Após executar o processo de diferença de férias, será lançado no envelope o valor do evento de diferença em **RM / RH / Folha de Pagamento / Férias / Processos / Diferença****:**

**Observação**:

Antes de efetuar o cálculo da diferença de recesso estagiário, deverá ser cadastrado o evento com **Código de Cálculo 356 - DIFERENÇA DE RECESSO DE ESTÁGIO**, para que seja lançado o valor da diferença no envelope.

4Cálculo do Recesso de Estagiário lançado na RescisãoCálculo do Recesso de Estagiário lançado na Rescisão

**Para o cálculo da rescisão, contemplando os eventos de recesso de estagiário , iremos considerar os dados abaixo:**

Rescisão de contrato do estagiário em:    
Data de início do está:    
Período aquisitivo para gozo de recesso vencido: 01/01/2021 a 31/12/2021  
Período aquisitivo proporcional para gozo de recesso:  a

1) Cadastrar os dados da Rescisão em **RM / RH / Folha de Pagamento / Rescisão / Rescisão / Cadastro de Rescisão****:**

2) Clicar no botão Calcular Rescisão:

3) Após o cálculo, conferir se os eventos de com **Código de Cálculo 333 - RECESSO DE ESTÁGIO VENCIDO** e **334 - RECESSO DE ESTÁGIO PROPORCIONAL**,foram lançados no envelope:

**Observação**:

Antes de efetuar o cálculo da rescisão , considerando o recesso estagiário, deverão ser cadastrados os evento com **Código de Cálculo 333 - RECESSO DE ESTÁGIO VENCIDO** e **334 - RECESSO DE ESTÁGIO PROPORCIONAL**, para que sejam lançados os eventos na movimentação da rescisão.

## **04. TABELAS UTILIZADAS**

* PCODCALCULO
* PEVENTO
* PFFINANC
* PFUNC
* PFUFERIAS
* PFUFERIASPER
* PPARAM

## **05. ASSUNTOS RELACIONADOS**

**[Código de Cálculo 332 - RECESSO DE ESTÁGIO](https://tdn.totvs.com/pages/viewpage.action?pageId=452719754)**

**[Código de Cálculo 333 - RECESSO DE ESTÁGIO VENCIDO](https://tdn.totvs.com/pages/viewpage.action?pageId=452718760)**

**[Código de Cálculo 334 - RECESSO DE ESTÁGIO PROPORCIONAL](https://tdn.totvs.com/pages/viewpage.action?pageId=452718761)**

**[Código de Cálculo 356 - DIFERENÇA DE RECESSO DE ESTÁGIO](https://tdn.totvs.com/pages/viewpage.action?pageId=829293262)**
