---
content_hash: 007fa412cd678cedabdd4926d5b93eff20f7a41b2f2699c9782fd305abbcae30
fetched_at: '2026-06-29T00:10:43.837396+00:00'
page_id: '551420239'
product: rm
source: tdn-rm
title: 1.2.1 Conta Caixa
type: documentation
url: https://tdn.totvs.com/display/LRM/1.2.1+Conta+Caixa
version: 15
---

Através da conta/caixa você pode controlar os saldos de uma conta bancária, os saldos dos caixas de uma empresa, os saldos do caixa de uma tesouraria. Os saldos são atualizados automaticamente de acordo com as movimentações realizadas no cadastro de Extratos de Caixa, ou seja, os saldos da conta/caixa são os resumos dos valores de cada registro de extrato de caixa relacionado com a conta/caixa.

Atenção

Não se aplica a integração com Protheus

Para cadastrar uma nova conta caixa, acesse: *Movimentações Bancárias | Contas Caixa*

Conta CaixaIdentificação

**Identificação**

Nesta pasta são apresentadas informações que identificam a conta/caixa.

Os campos não citados neste documento não precisam ser preenchidos.

Preencher as seguintes informações:

* **Ativa**: Marcar esta opção se a conta caixa estiver ativa para utilização.
* **Código**: Informar o código do cadastro da Conta Caixa.
* **Descrição**: Informar a Descrição da Conta Caixa.
* **Filial**: Se informada, a conta caixa só poderá ser usada para esta Filial. Se não informada, poderá ser usada por todas as Filiais da Coligada.
Dados Adicionais

**Dados Adicionais**

* **Módulo de Caixa**: “Permitir abertura de Sessão de Caixa” Marcar esta opção para permitir a utilização da Conta Caixa no módulo Sessão de Caixa.
* **Último número de Caixa Aberto**: Será apresentado o número do último caixa aberto com essa conta/caixa.
Integração Bancária

**Integração Bancária**

Ao utilizar esta conta/caixa na edição de um lançamento financeiro com a natureza a Receber, estas informações serão utilizadas na pasta Integração Bancária do Lançamento, Banco, Agência e Conta.

Além de selecionar estas opções é possível "visualizar", "incluir", "editar" e "excluir", registros destes cadastros.

* **Banco/Agência/Conta:** Informar o Banco, Agência e Conta correspondentes a esta Conta Caixa.

Caso estas informações não estejam cadastradas, é possível realizar o cadastro clicando no ícone , em seguida clicar no ícone .

Contabilidade

**Contabilidade**

Necessário informar uma conta contábil em "Defaults Contábeis"

* **Default Contábil:** Defaults Contábeis: Informar default da conta contábil que será utilizado na contabilização do lançamento/extrato de caixa (De acordo com parametrização do evento contábil).

Após cadastrar a Conta Caixa, importante cadastrar os dados do [Convênio](https://tdn.totvs.com/pages/viewpage.action?pageId=551429165). Para isso, acesse: *Anexos | Convênios*.

Cada Convênio deverá ser associado a uma Conta Caixa, Banco, Agência e Conta Corrente. A conta caixa deverá ser preenchida para o convênio cadastrado e esse convênio pode ser default, basta marcar a flag "Convênio default para a Conta Caixa". Quando definido como default, todo lançamento inserido na base carregará como default o convênio default.

Anexos


Veja Também


* [Cross Segmentos - Backoffice Linha RM - FIN - Como incluir uma Conta/Caixa](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041683914-Cross-Segmentos-Backoffice-Linha-RM-FIN-Como-incluir-uma-Conta-Caixa)
* [Como cadastrar Banco, Agência e Conta Corrente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041683254-RM-FIN-Como-cadastrar-Banco-Ag%C3%AAncia-e-Conta-Corrente)
* [RM - FIN - Conta/Caixa Global não é apresentada em coligada específica](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027565211-RM-FIN-Conta-Caixa-Global-n%C3%A3o-%C3%A9-apresentada-em-coligada-espec%C3%ADfica-)
* [Convênios](https://tdn.totvs.com/pages/viewpage.action?pageId=421388845)
