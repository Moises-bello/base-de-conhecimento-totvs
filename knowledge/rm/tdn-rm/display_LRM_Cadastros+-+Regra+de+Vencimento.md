---
content_hash: 3e5fa9e3360837a028b779fa24792f3a96ce7eb4ee82f7e3808fa4a4159569f8
fetched_at: '2026-06-29T00:09:49.324993+00:00'
page_id: '435105281'
product: rm
source: tdn-rm
title: Cadastros - Regra de Vencimento
type: documentation
url: https://tdn.totvs.com/display/LRM/Cadastros+-+Regra+de+Vencimento
version: 7
---

As regras de Vencimento são responsáveis por definir a data de vencimento dos lançamentos Financeiros  gerados  a partir das parcelas de aluguel. De acordo com as configurações  da Regra de vencimento  vinculada ao contrato de locação, os lançamentos terão seus devidos comportamentos alterados.

O cadastro de Regra de Vencimento, será utilizado pelos cadastros do [Modelo de Contrato de Locação](http://tdn.totvs.com/pages/viewpage.action?pageId=435105135) e [Contrato de Locação](http://tdn.totvs.com/pages/viewpage.action?pageId=435105265)

**Incluindo uma Regra de Vencimento**

* **Passo 1 -** Acesse: TOTVS Incorporação/ Aluguel/ Cadastros de Aluguel-Cadastros/ Regra de Vencimento
* **Passo 2 -** Clique em [Incluir] . O formulário será exibido
* **Passo 3 -** Preencha os campos e clique no botão [Salvar]. Os campo são:

**Figura 1 - Tela de cadastro da Regra de Vencimento**

* **Código da Regra de Vencimento:** Campo gerado automaticamente pelo sistema para identificar a Regra de Vencimento
* **Descrição:** Descrição  da regra de vencimento a cadastrar.
* **Ação de Divergência de Vencimento:**Esse campo determina como será o comportamento do sistema, quando um período possuir menos dias que um mês comercial. Segue as opções do campo:

* + **Considera Valor do Contrato:** Ao selecionar essa opção, o lançamento irá sempre considerar o Valor do Contrato de Locação, mesmo que o período de locação seja menor que um mês comercial;
  + **Fraciona / Acumula:** Ao selecionar essa opção , o lançamento irá realizar uma proporcionalização do Valor de locação, conforme a quantidade de dias no período;

* **Quantidade de vencimento no mês:** Esse campo determina quantos vencimentos terá em um período de locação. Tem a opção de 1 ou 2. Caso a opção selecionada seja 2, será exibido novos campos de "Dia de Vencimento" e "Contagem segundo vencimento" para que seja parametrizado o segundo vencimento. Ao parametrizar a regra de vencimento com 2 vencimentos, o Contrato de Locação irá criar 2 lançamentos financeiros com o mesmo valor, assim o valor de locação será dividido por 2;

* + **Observações:** Os dois vencimentos em um mesmo período é aplicado somente na geração de lançamentos do Contrato de Locação. Nos casos de Aluguel Complementar, multa rescisória e etc não será aplicado essa funcionalidade.

* **Dia de Vencimento:** Valor numérico que definirá os dias de vencimento  de acordo com o campo **[Contagem]** **Contagem:** Define o padrão de contagem de vencimento  em conjunto com o campo **[Dia de Vencimento].** Possui as seguintes opções:

* + **Fixo:** Os vencimentos dos lançamentos do Contrato de Locação, sempre serão nesse dia;
  + **Útil:** Os vencimento dos lançamentos do Contrato de Locação irá considerar somente dias úteis;

* **Dia de Vencimento:** Valor numérico que definirá os dias de vencimento do Segundo vencimento de acordo com o campo **[Contagem].** Esse campo será exibido somente se no campo "Quantidade de vencimento no mês" for selecionada a opção 2; **Contagem segundo vencimento:** Define o padrão de contagem de vencimento  em conjunto com o campo **[Dia de Vencimento].**Esse campo será exibido somente se no campo "Quantidade de vencimento no mês" for selecionada a opção 2. Possui as seguintes opções:

* + **Fixo**: Os vencimentos dos lançamentos do Contrato de Locação, sempre serão nesse dia;
  + **Útil**: Os vencimento dos lançamentos do Contrato de Locação irá considerar somente dias úteis.
