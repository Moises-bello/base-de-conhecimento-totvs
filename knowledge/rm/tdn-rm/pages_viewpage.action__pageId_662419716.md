---
content_hash: 515d7caa87be33191ca4a2f5b9ca1e8c6580130168bd71c29aae0807b9e5791f
fetched_at: '2026-06-29T00:11:16.128674+00:00'
page_id: '662419716'
product: rm
source: tdn-rm
title: TPI - Base para criar evento contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=662419716
version: 12
---

**VISÃO GERAL**

Este documento é um **exemplo** de evento contábil base para apoiar as instituições na construção de um evento.

IMPORTANTE

Ressaltamos que este exemplo não contempla as particularidades de cada instituição e por isso, não recomendamos a cópia fiel para o sistema. Se necessário, solicite auxilio de sua consultoria contábil para adicionar as necessidades legais de sua instituição.

**PROCESSO DE BAIXA E CONTABILIZAÇÃO NO EXTRATO DE CAIXA**

No processo de recebimento com PIX, além do extrato da baixa, é gerado um extrato de saque manual referente a taxa.

Na conciliação financeira são gerados extratos de transferência da conta transitória para a conta caixa banco. É gerado um extrato contábil para saque e um extrato de depósito não contábil. A contabilidade da transferência é feita no extrato de saque.

Na parametrização é informado apenas um evento contábil que será utilizado para contabilizar tanto a taxa quanto a transferência.

**1 - Inclusão do Evento Contábil**

***BackOffice > Gestão Financeira > Cadastros > Evento Contábil***

O evento precisa ser criado para o Processo de Extrato de caixa, com o valor calculado a partir de Formula.

Acesse a guia Itens do Evento para inclusão dos Itens de eventos de debito e credito.

**DÉBITO**

Nos itens de debito será necessário incluir dois itens, um corresponderá a taxa acordada pela prestação do serviço e um para calcular o valor do extrato que corresponde ao valor pago, utilizamos fórmulas para verificar a natureza do extrato, ou seja, para saber se é o de Taxa (Saque Manual) ou de transferência (depósito) e utilizar a conta apropriada para cada caso. Deverá ser criada uma linha para contabilizar a taxa e outra para a transferência.

Débito taxa:

A descrição é livre, recomentamos a utilização de D - tx Extrato para identificar no extrato é um item de debito referente a taxa.

Informar Aplicar Extrato de caixa, Debito e Informamos a conta contábil responsável pela contabilização das taxas.

**OBS:** **Se a conta contábil for obtida em algum local, como por exemplo nos defaults da conta caixa, é importante ressaltar que será necessário associar a conta contábil nos defaults da conta caixa transitória e também na conta caixa referente a taxa.**

**Caso utilize uma conta caixa específica somente para contabilização da taxa, o default contábil deverá se obtido da mesma.**

**Criação da fórmula para contabilização**

**FÓRMULA 1 – Taxa PIX**

**/\*VERIFICA VALOR NO EXTRATO TIPO 1 - TAXA PIX\*/**

**SE TABEXTRATO('TIPO','I') = 1 /\*Saque Manual\*/**

**ENTAO** **ABS(TABEXTRATO('VALOR','V'))**

**SENAO 0**

**FIMSE**

Débito Extrato - Valor da Transferencia

A descrição é livre, recomentamos a utilização de D-Extrato Caixa para identificar o valor transferido para a conta banco da instituição.

Informar Aplicar Extrato de caixa, Debito e Origem da Conta Tabela Default  Conta Caixa de Destino

**Criação da fórmula para contabilização**

**FÓRMULA 2 – Valor Transferencia**

**/\*VERIFICA VALOR NO EXTRATO TIPO 3 - SAQUE TRANSFERENCIA\*/**

**SE TABEXTRATO('TIPO','I') = 3 /\***Saque Transferência\***/**

**ENTAO ABS(TABEXTRATO('VALOR','V'))**

**SENAO 0**

**FIMSE**

**CRÉDITO**

Criação do item de credito para a Conta caixa transitória - Conta caixa do extrato:

Aplicar no Extrato de Caixa, Lançar como Crédito, Origem da conta Tabela default.

Buscar default em Conta/caixa oubeuter default de credito Credito

**FÓRMULA 3 – C- CONTA TRANSITÓRIA EXTRATO**

**/\*FÓRMULA 3 – C- CONTA TRANSITÓRIA EXTRATO\*/**

**ABS(TABEXTRATO('VALOR','V'))**

**2 - Informar nos parâmetros o evento criado**

***Ambiente > Parâmetros > TOTVS Gestão Financeira >  Contas a Receber > TOTVS Pagamento Digital > Aba Baixa/Conciliação***

**3 - Parâmetros de tipo contábil de extrato**

***Ambiente > Parâmetros > TOTVS Gestão Financeira > Controle Bancário > Contab. Extrato***

Informar o Default Contábil no Extrato como Contábil
