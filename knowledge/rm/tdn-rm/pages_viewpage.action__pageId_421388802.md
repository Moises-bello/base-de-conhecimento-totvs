---
content_hash: f82ce3b8be8a9aa6d6162e5d88af5773b17c5e71d80b67aa36393d211b02576d
fetched_at: '2026-06-29T00:09:18.861802+00:00'
page_id: '421388802'
product: rm
source: tdn-rm
title: Emissão / Recebimento de Cheques  
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388802
version: 7
---

A emissão de cheques para Lançamentos a pagar/receber será realizada pela visão de Lançamentos pelos ícones específicos e poderá ser também durante o processo de Baixa, quando utilizado o meio de pagamento "cheque".

**Emissão de Cheque com Meio de pagamento default:**

Na inclusão de cheque, pelos ícones específicos de emissão pela visão de lançamentos, poderá ser gerado cheque com o meio de pagamento default. O parâmetro foi criado para facilitar a inclusão de cheque, que quase sempre, utiliza a mesma forma de pagamento na emissão.

Para isso, é necessário informar no parâmetro *'Meio de Pagamento Default para Emissão de Cheque'* do Financeiro, o meio de pagamento default que será exibido na emissão do cheque.

**Observação**

Serão exibidos para seleção, somente aqueles do tipo "Cheque" e da coligada corrente.

**Parâmetro**

Ambiente > Parâmetros > TOTVS Gestão Financeira > Contas a Pagar -> Baixa -> Manutenção de Baixas →Cheque

Ao informar o meio de pagamento no parâmetro, a emissão do cheque deve exibir o meio de pagamento parametrizado, concluindo normalmente a inclusão do cheque.

O item de Baixa e o Extrato, deveram receber o meio de pagamento default ou não default, Informado no cheque.

O sistema deve permitir que o meio de pagamento seja alterado mesmo que esteja parametrizado no sistema.

**Observação**

Para que o sistema carregue os defaults do banco, agência e conta corrente do lançamento na emissão do cheque, basta preencher esses dados no cadastro da conta caixa usada na inclusão do lançamento, assim ao emitir o cheque esses dados serão carregados para a tela de cheque na aba "Dados Adicionais".

**Recebimento Via Cheque**

Ao incluir um cheque para mais de um lançamento a receber, através do Recebimento Via Cheque na visão de lançamentos, é exibido as opções:

**Um cheque para todos os lançamentos**

Ao marcar essa opção é emitido somente um cheque para todos os lançamentos selecionados, onde o valor do cheque será a soma dos valores líquidos dos lançamentos.

**Um cheque para cada lançamento**

Ao selecionar é exibido as opções:

* Informar dados somente uma vez – é informado os dados apenas uma vez para todos os cheques.
* Replicar Banco, Agência, Conta Corrente e Forma de Pagamento para todos os cheques – ao informar Banco, Agência e Conta Corrente na aba Dados adicionais do primeiro cheque esses dados serão replicados para os demais cheques, sempre respeitando os dados default.

**Um cheque para cada Cliente/Fornecedor**

Ao marcar essa opção é emitido um cheque para cada Cliente/Fornecedor dos lançamentos selecionados.

**Campo "Nominal a"**

Nesse campo, por default, é carregado o valor [NOM] para a pagar e [FIL] para a receber. Caso esteja configurado default nas preferências de usuário então sobrepõe a esse valor.
