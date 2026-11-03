---
content_hash: de3600ebf2db8e0c6551ed95d91554ceacd672e925ed7fd18b3cce3a7182d80b
fetched_at: '2026-06-29T00:11:43.493625+00:00'
page_id: '807221160'
product: rm
source: tdn-rm
title: Rescisão por Transferência - Desconsiderar o período da ficha financeira no
  Informe de Rendimentos / DIRF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=807221160
version: 17
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tela Período da Ficha Financeira e Período da Ficha Financeira Complementar**
5. **Tela Parâmetros da Transferência**
6. **Tabelas utilizada**

## **01. VERSÕES**

false

**A partir dos patches:**

* 12.1..2302.245
* 12.1.2306.194
* 12.1..2310.126
* 12.1.2402 e Superiores

## **02. VISÃO GERAL**

Ao efetuar a transferência de funcionários, o movimento da ficha financeira ficava duplicado em algumas situações na chapa ativa e demitida do funcionário. Quando isso acontecia, causava uma inconsistência na movimentação do Informe de Rendimentos / DIRF e devido a não temos orientações específicas na legislação em qual registro do funcionário deverá ser enviada a moviimentação.

Para tratamento desta situação,  foi criado no período da ficha financeira o campo **DESCONSIDERAMESTRANSFDIRFINF** e oparâmetro **Desconsiderar o período da ficha financeira quando a data de pagamento for igual a data de demissão**na tela de rescisão por transferência.

Com esse **NOVO** parâmetro, ao efetuar a rescisão por transferência, será indicado no período da ficha financeira em qual registro do funcionário (Ativo/Demitido) a movimentação será considerada na geração do Informe de Rendimentos / DIRF no momento da transferência do funcionário.

Quando o usuário marcar/desmarcar o parâmetro **Desconsiderar o período da ficha financeira quando a data de pagamento for igual a data de demissão** o **NOVO** campo **DESCONSIDERAMESTRANSFDIRFINF** do período da ficha financeira irá assumir o valores conforme as situações:

1) Quando a **Data de Pagamento** da rescisão por transferência for **ANTERIOR** a **Data de Demissão**:

a. Para a chapa **DEMITIDA**, o valor do campo será **1**;

b. Para a chapa **ATIVA**, o valor do campo será **0**.

2) Quando a **Data de Pagamento** da rescisão por transferência for **POSTERIOR** a **Data de Demissão**:

a. Para a chapa **DEMITIDA**, o valor do campo será **1**;

b. Para a chapa **ATIVA**, o valor do campo será **0**.

3) Quando a **Data de Pagamento** da rescisão por transferência for **IGUAL** a **Data de Demissão**:

a. Com o parãmetro **Desconsiderar o período da ficha financeira quando a data de pagamento for igual a data de demissão**, **desmarcado:**

I. Para a chapa **DEMITIDA**, o valor do campo será **1**;

II. Para a chapa **ATIVA**, o valor do campo será **0**;

b. Com o parãmetro **Desconsiderar o período da ficha financeira quando a data de pagamento for igual a data de demissão**,**marcado:**

I. Para a chapa **DEMITIDA**, o valor do campo será **0**;

II. Para a chapa **ATIVA**, o valor do campo será **1**;

**OBSERVAÇÕES:**

**01 -** O novo parâmetro criado estará disponível somente quando o parâmetro '****Considera a data de transferência igual a data de demissão na transferência sem ônus****', existente em RH | Folha de Pagamento | Configurações | Parametrizador | Rescisão | Transferência estiver **marcado**, pois quando o parâmetro está **desmarcado**, será considerado automaticamente na ficha financeira a data de pagamento igual a data de demissão.

**02 -** Será apresentado no Debug da transferência  o log de atualização do campo "Desconsidera Mês da Transferência na DIRF e Informe de Rendimento" do Período da Ficha Financeira, contento o período e o status do campo, podendo ser 1 ou 0.

## **03. EXEMPLO DE UTILIZAÇÃO**

Nos nossos exemplos, vamos considerar o cálculo da rescisão individual **Tipo 5 - Transferência sem ônus p/ Cedente** para o funcionários com a movimentação na Ficha Financeira:

1) Quando a **Data de Pagamento** da rescisão por transferência for **ANTERIOR** a **Data de Demissão**:

a. Para a chapa **DEMITIDA**, o valor do campo será **1**;

b. Para a chapa **ATIVA**, o valor do campo será **0**.

2) Quando a **Data de Pagamento** da rescisão por transferência for **POSTERIOR** a **Data de Demissão**:

a. Para a chapa **DEMITIDA**, o valor do campo será **1**;

b. Para a chapa **ATIVA**, o valor do campo será **0**.

3) Quando a **Data de Pagamento** da rescisão por transferência for **IGUAL** a **Data de Demissão**:

a) Com o parãmetro **Desconsiderar o período da ficha financeira quando a data de pagamento for igual a data de demissão**, **desmarcado**:

I. Para a chapa **DEMITIDA**, o valor do campo será **1**;

II. Para a chapa **ATIVA**, o valor do campo será **0**;

b) Com o parãmetro **Desconsiderar o período da ficha financeira quando a data de pagamento for igual a data de demissão**,**marcado:**

I. Para a chapa **DEMITIDA**, o valor do campo será **0**;

II. Para a chapa **ATIVA**, o valor do campo será **1**;

## **04.** **TELA Período da Ficha Financeira e Período da Ficha Financeira Complementar**

**Período da Ficha Financeira**

****Período da Ficha Financeira Complementar****

## **05.** **TELA Parâmetros da Transferência**

**06. TABELAS UTILIZADAS**

* PFUNC
* PDADOSRESCISAO
* PFPERFF
* PFPERFFCOMPL
