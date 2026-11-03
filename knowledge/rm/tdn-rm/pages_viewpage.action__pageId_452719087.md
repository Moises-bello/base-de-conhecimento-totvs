---
content_hash: 33fb7a096c519b2e4b3e7b2525cfe325ada9d93bf3d2cfefac46512b1182709a
fetched_at: '2026-06-29T00:10:03.283793+00:00'
page_id: '452719087'
product: rm
source: tdn-rm
title: Cartão de Ponto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719087
version: 12
---

Neste módulo, será possível realizar alteração referente ao uso ou não do cartão de ponto, permitindo que os funcionários sejam considerados em todo o processo de coleta de marcações e apuração de ponto.

Através do módulo é possível controlar:

**Identificação**  
Essa tela é utilizada para identificar se: Funcionário utiliza ponto no período atual, utiliza o ponto parcialmente no período atual, ou não utiliza ponto no período atual.

Através do menu **Processos**, é possível alterar o status do funcionário no ponto,  podendo optar pelos itens de Menu:

**Utiliza Cartão de Ponto:** Abrirá uma tela para ser informada a data de quando os funcionários selecionados na visão passarão a bater ponto e ser considerado em todo o processo de apuração.

O sistema impedirá a inserção da **Data de início de utilização do cartão de Ponto,** se for **anterior à Data de Admissão**, exibindo uma mensagem de bloqueio.

**Exemplo:** Data de Admissão : 10/02/2026

                 Data de Início de Utilização de Cartão de Ponto: 09/02/2026

                 Mensagem : **Data início não pode ser menor do que a data de admissão.**

**Deixar de Utilizar Cartão de Ponto:** Abrirá uma tela para ser informada a data de quando os funcionários selecionados na visão deixarão de bater ponto e não ser mais considerados no processo de apuração.

**Observações:**

**1)** Se existe algum movimento no período anterior, não poderá fazer NENHUMA exclusão.

**2)**Validar se é necessário excluir item do histórico caso necessite utilizar em todo período atual.

**3)** O sistema passou a validar a data do histórico de utilização do cartão de ponto ao inserir batidas.

Exemplo:Funcionário possui os seguintes históricos:

Data início utiliza cartão     - 01/09/2021

Deixou de utilizar o cartão - 06/09/2011

Voltou a utilizar o cartão    - 10/09/2021

Ao tentar inserir batidas na data 06/09/2021 até 09/09/2021 o sistema irá apresentar a seguinte mensagem:  "Funcionário não utiliza cartão de ponto na data informada"  e não será permitida a inclusão.

**Anexo:** Histórico de utilização de cartão de ponto Visão que mostra os períodos em que o funcionário utilizou ou não cartão de ponto. Há uma opção de exclusão para permitir desfazer possíveis erros de lançamento.
