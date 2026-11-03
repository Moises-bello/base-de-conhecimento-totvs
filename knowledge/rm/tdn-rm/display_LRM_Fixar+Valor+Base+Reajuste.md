---
content_hash: 03d427f21074520aa10b4947792795aa64b90984e4c59712676f1198e5c4f4b9
fetched_at: '2026-06-29T00:05:51.511861+00:00'
page_id: '1050311232'
product: rm
source: tdn-rm
title: Fixar Valor Base Reajuste
type: documentation
url: https://tdn.totvs.com/display/LRM/Fixar+Valor+Base+Reajuste
version: 6
---

Novo processo na visão de venda permite que os valores reajustados até o momento possam ser utilizados como base para novos reajustes, alterando o comportamento dos valores futuros sem impactar o passado.

Esse recurso é ideal para cenários de importação de dados de contratos provenientes de sistemas concorrentes que passaram a utilizar o RM. Nesses casos, o sistema irá considerar os reajustes apenas a partir da data definida, utilizando os valores já existentes como base para os cálculos futuros. Para vendas importadas de sistemas legados, o registro será criado no RM já com o reajuste fixado na mesma data de reajuste informada durante o processo de importação.

Também pode ser utilizado em situações em que há mudança de parametrização. Por exemplo, quando anteriormente foi realizado reajuste com INCC e, posteriormente, deseja-se alterar para IPCA. Nesse caso, não é necessário realizar aditivo, basta executar esse processo antes da alteração para que o sistema “congele” os reajustes até aquela data e passe a calcular os próximos valores com base na nova configuração, sem impactar os valores já reajustados. Esse comportamento se aplica a qualquer tipo de configuração que influencie os valores de reajuste.

Importante

* O processo fixa o reajuste utilizando, por padrão, a data do último reajuste realizado. Caso não exista histórico de reajuste para a venda, será considerada a data informada na execução do processo.
* Para pro-rata, recomenda-se que tanto os valores dos componentes quanto a data de reajuste da venda importada estejam alinhados ao último dia do mês, garantindo maior consistência nos cálculos.
* É permitido escolher componentes que não serão fixado o valor, pois tem situação que o cliente deseja que o sistema reajusta desde início do contrato.
* Se marcar a opção fixar conforme periodicidade do componente, caso tem resíduo ou CM anual com juros mensal, o sistema irá respeitar o aniversário de cada componente, pois uns são mensais e outros anuais, tem reajustes em momentos diferentes, então será fixado conforme o seu aniversário

Quando o usuário tentar executar o reajuste para uma data anterior a essa fixada, o sistema mostrará isso no log.

Venda=> Processos => Reajustes => Fixar Valor Base Reajuste (Tem permissão nova para essa funcionalidade)
