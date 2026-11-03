---
content_hash: f1d442db1778e47839aa5fe1760f82340bea45b5618b3364347719b43ecfb8dd
fetched_at: '2026-06-29T00:12:14.025894+00:00'
page_id: '963024323'
product: rm
source: tdn-rm
title: Cálculo de Férias - Provisionamento nas Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=963024323
version: 4
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Exemplo de Empréstimo Crédito do Trabalhador referente a Cálculo de Férias com Provisionamento nas Férias.

## **02. EXEMPLO DE UTILIZAÇÃO**

Dados Fictícios

Dica:

Para o lançamento da provisão do empréstimo na modalidade Crédito do Trabalhador veja a parametrização no link Lançamento de provisão nas férias acima em Passos para utilização.

No cadastro de empréstimos existe o seguinte cadastro

IMPORTANTE:

**É imprescindível ter importado o arquivo do emprega Brasil para ter o valor da parcela no cadastro de empréstimos. Se esse valor estiver zerado não lançará a provisão.**

Parâmetro no parametrizador marcado

Cálculo das férias

Observação:

Essa provisão não vai zerar o valor no cadastro de empréstimos da modalidade Crédito do Trabalhador. O cadastro de empréstimo será atualizado no momento o lançamento do grupo de eventos.

No LOG estará informado a proporcionalização do empréstimo

Lançamento das férias

Dica:

Veja que foi lançado o evento de provento de provisão do primeiro mês para ajudar no abatimento do desconto do empréstimo. E o provento de provisão do segundo mês será lançado ao finalizar as férias no próximo mês.

Os eventos do envelope de férias foram lançados para o envelope de pagamento, por isso foi lançado o valor do desconto integral da provisão de férias. Ou seja somando o primeiro e segundo mês no desconto de provisão no envelope.  Inclusive o evento com o líquido de férias também foi lançado no envelope de pagamento. Esses eventos devem ser lançados assim para zerar o valor já pago no envelope de férias.

Após lançamento do grupo de eventos com o empréstimo na modalidade Crédito do trabalhador

**Somente** após lançar o grupo de eventos o cadastro de empréstimo será atualizado

**Como exemplo:** Fazendo a finalização das férias para o próximo mês será lançada a provisão do segundo mês no envelope para ajudar no desconto do empréstimo do próximo mês

IMPORTANTE:

* Somente será lançado o evento de provisionamento nas férias caso **não** exista o evento de provisionamento ou empréstimo lançado em algum período da competência.
* O provisionamento será lançado proporcionalizando de acordo com dias de férias calculadas em cada mês. No caso de férias partidas, por exemplo, se no 1º mês tiver 10 dias de férias e do 2º  mês tiver 20 dias, será lançado o provisionamento de 10 dias da parcela do empréstimo no 1º mês e 20 dias da parcela do empréstimo no 2º mês.
* Independente da quantidade de dias pagos no mês será proporcionalizado, por exemplo em um caso que haja 1 dia de férias em um dos meses será feito o cálculo proporcional a esse dia.
* Dias de abono pecuniário não entram nesse cálculo de proporcionalização, serão considerados somente dias pagos como férias.
* O provisionamento somente lançará para a modalidade de empréstimo Crédito do trabalhador eSocial.
* Não será feita nenhuma tratativa para lançar o provisionamento dentro da margem consignável, mesmo se estiver parametrizado. 
  + Se não tiver líquido suficiente para desconto, deve lançar até o líquido disponível, não gerando evento de arredondamento/insuficiência de saldo.

* O cadastro de empréstimo não será atualizado quando lançar o provisionamento nas férias, somente será atualizado após lançar o grupo de eventos.

## **03.** **TABELAS UTILIZADAS**

* PFFINANC
* PFEMPRT
* PFDESCEMPRT
