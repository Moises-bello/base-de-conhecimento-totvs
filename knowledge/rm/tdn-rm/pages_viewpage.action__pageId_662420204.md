---
content_hash: d117e7e787ed8d0d565b6c5811c09ece145b3ea5411238564720b9c3c3ee29bf
fetched_at: '2026-06-29T00:11:16.135190+00:00'
page_id: '662420204'
product: rm
source: tdn-rm
title: TOTVS Pagamento Cartão - Base para criar evento contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=662420204
version: 8
---

**VISÃO GERAL**

Este documento é um **exemplo** de evento contábil base para apoiar as instituições na construção de um evento.

IMPORTANTE

Ressaltamos que este exemplo não contempla as particularidades de cada instituição e por isso, não recomendamos a cópia fiel para o sistema. Se necessário, solicite auxilio de sua consultoria contábil para adicionar as necessidades legais de sua instituição.

**PROCESSO DE BAIXA E CONTABILIZAÇÃO DO EXTRATO DO CARTÃO**

No processo de recebimento com cartão de crédito, além do extrato da baixa, é gerado um extrato de saque manual referente a taxa.

Na conciliação financeira são gerados extratos de transferência da conta transitória para a conta caixa banco. É gerado um extrato contábil para saque e um extrato de depósito não contábil. A contabilidade da transferência é feita no extrato de saque.

Na parametrização é informado apenas um evento contábil que será utilizado para contabilizar tanto a taxa quanto a transferência.

**1 - Inclusão do Evento Contábil**

***BackOffice > Gestão Financeira > Cadastros > Evento Contábil***

**DÉBITO**

Para o débito, é utilizada uma fórmula para verificar a natureza do extrato, ou seja, para saber se é o de Taxa (Saque Manual) ou de transferência (depósito) e utilizar a conta apropriada para cada caso. Deverá ser criada uma linha para contabilizar a taxa e outra para a transferência.

Débito taxa:

**OBS:** **Se a conta contábil for obtida em algum local, como por exemplo nos defaults da conta caixa, é importante ressaltar que será necessário associar a conta contábil nos defaults da conta caixa transitória e também na conta caixa referente a taxa.**

**Caso utilize uma conta caixa específica somente para contabilização da taxa, o default contábil deverá se obtido da mesma.**

**Criar fórmula para contabilização:**

**FÓRMULA 1 – D-TX EXTRATO**

**/\*VERIFICA VALOR NO EXTRATO TIPO 1 - TAXA PIX\*/**

**SE TABEXTRATO('TIPO','I') = 1 /\*Saque Manual\*/**

**ENTAO****ABS(TABEXTRATO('VALOR','V'))**

**SENAO 0**

**FIMSE**

Débito conta Banco - *Conta caixa destino do extrato*:

**Criar fórmula para contabilização:**

**/\*VERIFICA VALOR NO EXTRATO TIPO 3 - SAQUE TRANSFERENCIA\*/**

**SE TABEXTRATO('TIPO','I') = 3 /\*Saque Transferência\*/**

**ENTAO ABS(TABEXTRATO('VALOR','V'))**

**SENAO 0**

**FIMSE**

**CRÉDITO**

Criar uma linha de Crédito para Conta caixa transitória - Conta caixa do extrato:

**FÓRMULA 1 – C- CONTA TRANSITÓRIA EXTRATO**

**ABS(TABEXTRATO('VALOR','V'))**

**2 - Informar nos parâmetros os eventos criados**

***Ambiente > Parâmetros > TOTVS Gestão Financeira > Contas a Receber > Baixas > Cartão de Crédito/Débito > Conciliação***

**3 - Parâmetros de tipo contábil de extrato**

***Ambiente > Parâmetros > TOTVS Gestão Financeira > Controle Bancário > Contab. Extrato***

**4 - Cadastrar conta caixa e informar default contábil**

***Movimentações Bancárias > Contas Caixa***
