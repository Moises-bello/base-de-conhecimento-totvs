---
content_hash: 03615bbba66f312b1e5ee18607e696fcefb7307a987b263c99bd12bef6372282
fetched_at: '2026-06-29T00:10:09.433428+00:00'
page_id: '452719666'
product: rm
source: tdn-rm
title: Código de Cálculo 5 - Salário Família
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719666
version: 22
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Informações complementares**

## **01. VISÃO GERAL**

Este Código de Cáclulo deve ser informado em um evento do Tipo Provento e Valor.

O processo verifica o número de dependentes de Salário Família cadastrado no histórico de dependentes do funcionário e multiplica pelo valor do Salário Família vigente cadastrado na tabela de valores fixos.

Para encontrar o valor da Base para o cálculo do Salário Família é verificado os (eventos que incidem em Salário Família -  eventos que estornam Salário Familia). Caso o parâmetro 'Usa salario Nominal' esteja marcado, será somando o Salário nominal do funcionário para a Base de Cálculo. Feito isto, é comparada com as tabelas fixas de finalidades 'Limite Salário Família' e 'Teto para pagamento do Salário Familia' dentro da vigencia da competência do Cálculo para identificar se o funcionario tem direito ao recebimento do benefício.

Observação

* Os Funcionários com vínculo RAIS **7 - Diretor sem vínculo empregatício**, não recebem salário Família, mesmo se possuir dependentes elegíveis. É retornado a informação no log de Cálculo
* Para os funcionários afastados pela Previdência (T, P, O) durante a competência do cálculo, também não é pago o Salário Família. Mesmo lançando dias de atestado na competência atual é considerado como afastamento, ou seja, é necessário que o funcionário tenha que ter pelo menos 1 dia de trabalho durante a competência para que o sistema lance o evento automaticamente. Caso queira forçar o lançamento do benefício para os funcionários afastados, o Parâmetro 'Paga p/afastados Previdência' deve está marcado.
* Sempre é verificado a data de Mudança do Histórico de Depedentes para considerar a número de dependentes para pagamento de Salário Família.
* Quando a Base de Cálculo para o Salário Família é 0 (Zero), não é lançado o benefício para o funcionário.

## **02. EXEMPLO DE UTILIZAÇÃO**

Dependentes Cadastrados:

Histórico de Dependente:

Tabelas Fixas  que são consideradas para o cálculo do Salário Família:

Cálculo - Sem Afastamento, Cálculo - Afastamento integral, Cálculo - Inicio de Afastamento, Cálculo - Retorno de afastamento, Cálculo - Vínculo RAIS = 7passo1,passo2,passo3,passo4,passo5yespasso1

**Caso 01**: Com o parâmetro 'usa salário nominal' desmarcado, foi considerado somente o evento de dias trabalhados lançado para o Funcionário para Base de Cálculo:

**Caso 02**: Com o Parâmetro 'usa salário nominal' marcado. Como foi somado o valor do evento de CC 2 com o Salário nominal do funcionário, a base de Cálculo para o Salário Família é R$ 1900,76, ficando acima do teto para pagamento:

**Caso 03**: Com o Parâmetro 'usa salário nominal' marcado e evento que estorna na base de Cáclulo de Salário Família. Como foi subtraído do valor do evento de CC 2 o valor do evento de falta (CC8) e posteiormente somando com o Salário nominal do funcionário, a base de Cálculo para o Salário Família passa a ser R$ 1583,97:

nopasso2

Funcionário afastado durante o mês de Fevereiro

**Caso 01**: O parâmetro 'Paga p/ afastados previdência' está desmarcado:

No log retorna que não será pago o valor do Salário Família, devido a parametrização, mesmo o funcionário possuindo base de cálculo abaixo do teto:

**Caso 02**: O parâmetro 'Paga p/ afastados previdência' está marcado:

nopasso3

Funcionário iniciando o afatamento no dia 02/02/2023:

Neste caso, o parâmetro 'Paga p/ afastado previdência' não interfere e será lançado o Salário família para o funcionário caso ele atenda os requisitos:

nopasso4

Funcionário finalizado o afastamento no dia 24/02/2023:

**Caso 01**: Neste caso, o parâmetro 'Paga p/ afastado previdência' não interfere e será lançado o Salário família para o funcionário caso ele atenda os requisitos, pois o mesmo teve dias trabalhados no mês.

**Caso 02**: Foi lançado evento de Falta para o funcionário com referencia de 3 dias e desmarcado o parâmetro 'Usa salário nominal'. Neste caso não lançou o benefício, pois a Base de Cáclulo é 0 (Zero). Mesmo marcando o parâmetro 'Paga p/ afastados previdência' não é feito:

nopasso5

Lançamento do Salário família para um funcionário de vínculo RAIS **7 - Diretor sem vínculo empregatício**

Caso 01: Funcionário sem afastamento: O mesmo não foi realizado e informou no log a mensagem referente ao vínculo RAIS.

Caso 02: Funcionário afastado no mês e parâmetro 'Paga p/ afastados previdência' marcado: O mesmo não foi realizado e informou no log a mensagem referente ao vínculo RAIS.

## **03.** **INFORMAÇÕES COMPLEMENTARES**

As regras e os tipos de dependentes elegíveis para o pagamento do Salário Família estão relacionados nos Links abaixo:

[Cadastro de Dependentes](https://tdn.totvs.com/display/LRM/Dependentes), no Titulo 'Salário Família'.
