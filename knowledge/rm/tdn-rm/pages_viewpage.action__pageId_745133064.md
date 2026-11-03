---
content_hash: 152eb8e23f51a98a94ee1399e1f394fa2608a97a381d14fc915c927e43a6b3b5
fetched_at: '2026-06-29T00:11:32.151415+00:00'
page_id: '745133064'
product: rm
source: tdn-rm
title: Outras Operações.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=745133064
version: 32
---

O objetivo deste menu é agrupar funcionalidades que agregam valor ao dia a dia do operador, facilitando o atendimento.

## Estorno

Utilizado nos casos onde é necessário registrar a devolução do valor pago pelo cliente em uma transação financeira anterior. O acesso a esta operação pode ser concedido através de [permissão por perfil de usuários](https://tdn.totvs.com/pages/viewpage.action?pageId=744486576).

---

## Serviços Extras

Utilizado nos casos onde é necessário registrar a devolução do valor pago pelo cliente em uma transação financeira anterior. O acesso a esta operação pode ser concedido através de [permissão por perfil de usuários](https://tdn.totvs.com/pages/viewpage.action?pageId=744486576).

Pré-requisito

Para que a opção de Serviços Extras fique disponível é necessário que exista integração do TOTVS Gestão Financeira com o módulo TOTVS Gestão Educacional.

---

## Sangria

Sangria de caixa é quando acontece a retirada não programada de um valor do caixa, ou por uma questão de segurança para evitar valores altos armazenados no caixa.

A sangria pode ocorrer das seguintes formas:

* Retirada manual de valor, onde a conta caixa destino não é informada. Nesse caso, é gerado o extrato de caixa com a operação de saque manual na conta caixa da sessão;
* Através de transferência entre contas, onde o valor será retirado da conta caixa da sessão e depositado na conta caixa de destino informada. Nesse caso, são gerados os extratos de caixa referente às operações de saque transferência e depósito transferência.

Contabilidade

O tipo contábil do extrato gerado pode ser definido nos [parâmetros gerais do caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=744486589#Configura%C3%A7%C3%B5esiniciais-Gerais).   
Quando contábil, os extratos de saque manual e saque transferência serão contabilizados usando os defaults (tabelas opcionais) da conta caixa da sessão como fonte de informação para identificar o evento contábil.

O(s) extrato(s) referente(s) à sangria serão gerados para a filial vinculada à conta/caixa e na ausência desta, serão gerados para a filial da sessão de caixa.

O acesso a essa funcionalidade pode ser concedido através da [permissão por perfil de usuários](https://tdn.totvs.com/x/sPZfL). 

---

## Suprimento

Suprimento de caixa representa uma entrada de dinheiro no caixa, geralmente para troco e pode ocorrer das seguintes formas:

* Entrada de valor manual, onde a conta caixa origem não é informada. Nesse caso, é gerado o extrato de caixa com a operação depósito manual e quando for contábil, são utilizados os defaults da conta caixa da sessão como fonte de informação para identificar o evento contábil;
* Através de transferência entre contas, onde a conta caixa de origem é informada. Nesse caso, o valor é retirado da conta caixa de origem e depositado na conta caixa da sessão, sendo gerados os extratos de caixa referentes à essas operações. O extrato contabilizado será o saque transferência e serão utilizados os defaults da conta caixa de origem como fonte de informação para identificar o evento contábil.

Contabilidade

O tipo contábil do extrato gerado pode ser definido nos [parâmetros gerais do caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=744486589#Configura%C3%A7%C3%B5esiniciais-Gerais).   
Quando contábil, os extratos de saque manual e saque transferência serão contabilizados usando os defaults (tabelas opcionais) da conta caixa da sessão como fonte de informação para identificar o evento contábil.

O(s) extrato(s) referente(s) ao suprimento serão gerados para a filial vinculada à conta/caixa e na ausência desta, serão gerados para a filial da sessão de caixa.

O acesso a essa funcionalidade pode ser concedido através da [permissão por perfil de usuários](https://tdn.totvs.com/x/sPZfL).

---

## 2ª via do cupom TEF

Este recurso permite a reimpressão do comprovante de pagamentos realizados via TEF. Para que essa funcionalidade esteja disponível, é necessário que a sessão de caixa esteja habilitada para o uso do TEF e o parâmetro *Imprime comprovante TEF* (localizado em: Ambiente | Parâmetros | Gestão Financeira | Contas a Receber | Caixa | Módulo de Caixa | TEF)esteja marcado.

A reimpressão pode ser feita de duas formas:

* **Imprimir último cupom:** reimprime o comprovante do último recebimento realizado (quando disponível no TEF);

* **Selecionar cupom para impressão:** permite localizar e selecionar os recebimentos por meio de filtros disponíveis, e imprimir a segunda via do comprovante (caso esteja disponível no TEF).

A comunicação ocorre diretamente com o pinpad, permitindo a impressão da via do cliente, da via do estabelecimento ou de ambas.

Disponibilidade

A 2ª via do cupom TEF está disponível a partir da versão 12.1.2510.

---

## Encerrar Sessão

[Clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=781216399) para saber mais detalhes o encerramento da sessão.

0solid

[Voltar para o Menu Principal](https://tdn.totvs.com/pages/viewpage.action?pageId=744486517)
