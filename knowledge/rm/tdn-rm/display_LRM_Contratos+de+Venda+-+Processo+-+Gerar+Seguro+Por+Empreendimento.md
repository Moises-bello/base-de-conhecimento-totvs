---
content_hash: 65dec6aa9f1330de7ef3defcf453a659199578e59b301d691e7c7a7741d4f55b
fetched_at: '2026-06-29T00:09:46.399897+00:00'
page_id: '435104774'
product: rm
source: tdn-rm
title: Contratos de Venda - Processo - Gerar Seguro Por Empreendimento
type: documentation
url: https://tdn.totvs.com/display/LRM/Contratos+de+Venda+-+Processo+-+Gerar+Seguro+Por+Empreendimento
version: 12
---

O processo gerar seguro por empreendimento tem o objetivo de agrupar nas parcelas dos lançamentos financeiros de uma venda  o valor de seguro. Para Que o seguro seja gerado é necessário possuir um contrato de venda  com a situação "Efetivado" e que tenha também os lançamentos financeiros desbloqueados.

**Pré-condições**

* Ter incluído um Empreendimento
* Ter efetivado uma Venda em que o seu plano de financiamento tenha o componente
* Ter gerado os lançamentos financeiros da Venda.

**Entrada**

* Selecione a venda e acesse o processo [Gerar Seguro por Empreendimento];
* Informe a data do cálculo e se desejar marque o checkbox "Cálculo sem juros de atraso das parcelas vencidas". Ao desmarcar este parâmetro o sistema irá executar a função de cálculo do valor líquido para retornar os valores de juros e multa para parcelas em atraso além de executar o reajuste on-line para cálculo do valor atualizado.
* Foi criado um novo parâmetro na tela do processo, para escolher se deseja lançar o seguro somente na parcela com vencimento na competência da data de cálculo. Ou seja, o componente de Seguro por empreendimento será inserido na parcela de acordo com a data definida no momento da execução do processo;
* Caso marque o checkbox "Desfazer o valor calculado do seguro", o processo irá zerar o valor do componente "Seguro por Empreendimento" para a parcela que for localizada pela data informada no processo;
* Caso o componente Seguro por Empreendimento esteja com o Tipo base calculo seguro parametrizado da forma abaixo, o sistema irá: 
  + **Seguro sobre o saldo devedor do grupo:** o cálculo será feito considerando o saldo devedor de cada grupo que tenha este componente em sua composição, tratando todas as parcelas em aberto (vencidas e vincendas) que tenham a data de vencimento maior ou igual à data informada no processo. Assim cada grupo com este tipo de componente, terá o seu próprio valor do seguro de acordo com o saldo devedor do grupo ao qual ela pertence; ou
  + **Seguro sobre o saldo devedor de todos os grupos:** o cálculo será feito considerando o saldo devedor de todas as parcelas em aberto (vencidas e vincendas), que tenham a data de vencimento maior ou igual à data informada no processo, independentemente do grupo destas parcelas. Ao utilizar este tipo de parametrização, não é necessário se colocar um componente de seguro para cada grupo, uma vez que o valor será calculado sobre todas as parcelas em aberto. O valor do seguro calculado, será inserido na próxima parcela em aberto imediatamente após data informada no processo; ou
  + **Seguro sobre o saldo devedor do grupo de parcelas vincendas:** o cálculo será feito considerando o saldo devedor de cada grupo que tenha este componente em sua composição, tratando todas as parcelas vincendas que tenham a data de vencimento maior ou igual à data informada no processo. Assim cada grupo com este tipo de componente, terá o seu próprio valor do seguro de acordo com o saldo devedor do grupo ao qual ela pertence; ou
  + **Seguro sobre o saldo devedor de todos os grupos de parcelas vincendas:** o cálculo será feito considerando o saldo devedor de todas as parcelas vincendas, que tenham a data de vencimento maior ou igual à data informada no processo, independentemente do grupo destas parcelas. Ao utilizar este tipo de parametrização, não é necessário se colocar um componente de seguro para cada grupo, uma vez que o valor será calculado sobre todas as parcelas em aberto. O valor do seguro calculado, será inserido na próxima parcela em aberto imediatamente após data informada no processo;
* O sistema exibirá a mensagem informando que o seguro foi gerado com sucesso.
* Para visualizar as parcelas de seguro, acesse  [Anexos/ Plano de financiamento]

Importante!

A partir do Release 12.1.2306, para executar o este processo basta dar Permissão de Acesso no Perfil do Usuário, ao Menu ***[01.01.01.49] - Contratos Gerar Seguro Por Empreendimento***:
