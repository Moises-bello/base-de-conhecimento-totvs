---
content_hash: 7b8a1ce253dd3104b9c8fd03c9fd69cea88caf1c4021bfa666ec7a85250d726a
fetched_at: '2026-06-29T00:11:25.509722+00:00'
page_id: '710550011'
product: rm
source: tdn-rm
title: COCKPIT 360 - Resumo Financeiro
type: documentation
url: https://tdn.totvs.com/display/LRM/COCKPIT+360+-+Resumo+Financeiro
version: 11
---

### Resumo Financeiro

Neste agrupador o sistema exibe as informações referentes aos Contratos de **Venda** e de**Locação de Imóveis** considerando se há parcelas geradas em associadas ao Cliente em análise e apresentando os valores com base no Reajuste Monetário aplicado na base no momento da consulta.

São detalhadas as seguintes informações:

* ***Contratos:*** são considerados **todos** os Contratos de **Venda**e de**Locação de Imóveis**para os quais há parcelas geradas para o Cliente em análise sendo detalhados

+ a ***Quantidade*** de Contratos cadastrados para este Cliente. Ao clicar nessa informação, o sistema abre a visão detalhando esses Contratos; e
+ a ***Soma dos Valores*** atualizados desses Contratos, considerando a Data do último Reajuste Monetário aplicado na base e sem acréscimo de Juros e nem de Multa do módulo Financeiro.

* ***Saldo Devedor:*** dos Contratos sumarizados pelo campo acima e detalhados no card de *Contratos*, sendo apresentados

+ o ***Percentual*** de Saldo Devedor, que é calculado em relação à soma dos valores dos Contratos do Cliente. Ao clicar nessa informação, o sistema abre a visão detalhando esses Contrato; e
+ o ***Valor do Saldo Devedor*** este valor é a soma do Valor Líquido de todas as Parcelas em aberto nos Contratos deste Cliente, considerando os valores de Reajuste Monetário que estão aplicados nesses Contratos, no momento deste acesso;

* ***Boletos em Aberto:*** o sistema também apresenta um resumo dos Boletos que estão em aberto para este Cliente, levando em consideração as informações do módulo financeiro. No card sã sendo detalhados

+ a ***Quantidade*** de Boletos em aberto cujo Sacado é o Cliente em análise. Ao clicar nessa informação, o sistema abre a visão com esses Boletos; e
+ a ***Soma dos Valores*** desses Boletos gravados na tabela dessa Entidade, no módulo financeiro, no momento dessa consulta.

* ***Parcelas Em Atraso:*** são considerados os saldos das parcelas em aberto com data de vencimento anterior ao dia da consulta realizada nesta ferramenta, sendo apresentadas

+ a ***Quantidade*** das Parcelas em atraso/vencidas, com situação Em Aberto ou Parcialmente Quitada. Ao clicar nessa informação, o sistema abre a visão detalhando essas Parcelas; e
+ o seu respectivo ***Valor*** levando em consideração o último Reajuste Monetário de cada Contrato do Cliente, sem nenhum acréscimo de Juros ou Multa do módulo financeiro.

* ***Parcelas Futuras:*** aqui são consideradas as parcelas com data de vencimento posterior ao dia da consulta no cockpit, sendo apresentadas

+ a ***Quantidade*** de Parcelas vincendas. Ao clicar nessa informação, o sistema abre a visão detalhando essas Parcelas; e
+ o seu respectivo ***Valor*** que conforme o padrão, é calculado levando em consideração o último Reajuste Monetário de cada Contrato do Cliente, sem nenhum acréscimo de Juros ou Multa do módulo financeiro.

* ***Parcelas Pagas:*** o sistema apresenta as informações abaixo, considerando as parcelas com data de quitação até a data de consulta à essa ferramenta, sendo exibidas

+ a ***Quantidade*** de Parcelas quitadas. Ao clicar nessa informação, o sistema abre a visão detalhando essas Parcelas; e
+ a ***Soma dos Valores*** dessas Parcelas levando em consideração as informações do módulo financeiro;

* ***Despesas Em Atraso:*** o sistema apresenta as informações abaixo, considerando as Despesas em aberto, com data de vencimento anterior à data de consulta à essa ferramenta, sendo exibidas

+ a ***Quantidade*** de Despesas em atraso. Ao clicar nessa informação, o sistema abre a visão detalhando essas Despesas; e
+ a ***Soma dos Valores*** desses registros.

* ***Despesas Futuras:*** o sistema apresenta as informações abaixo, considerando as Despesas com data de vencimento posterior à data dessa consulta, sendo exibidas

+ a ***Quantidade*** de Despesas futuras geradas. Ao clicar nessa informação, o sistema abre a visão detalhando essas Despesas; e
+ a ***Soma dos Valores*** desses registros.

* ***Despesas Pagas:*** o sistema apresenta as informações abaixo, considerando as Despesas que estão quitadas até data da consulta realizada, sendo exibidas

+ a ***Quantidade*** de Despesas pagas. Ao clicar nessa informação, o sistema abre a visão detalhando essas Despesas; e
+ a ***Soma dos Valores*** desses registros.

Atenção!

Ao abrir a visão dos Lançamentos Financeiros dos Contratos através do Cockpit 360, são exibidos os lançamentos/parcelas de todas as Coligadas que o Cliente tem Contrato, seja de Vendas ou de Locação, porém, caso se tente gerar boletos para lançamentos de coligadas diferentes ao mesmo tempo, o sistema exibirá uma exceção, informando que *“Este processo não é permitido para múltiplas coligadas”*.

Desta forma, sugerimos que os boletos sejam gerados por Contratos que pertençam à mesma Coligada.

Saiba Mais:

[Controle de Despesa - Cadastro individual de despesas](https://tdn.totvs.com/display/LRM/Controle+de+Despesa+-+Cadastro+individual+de+despesas)

[FIN - Lançamentos](https://tdn.totvs.com/pages/viewpage.action?pageId=421388578)

[FIN - Boleto](https://tdn.totvs.com/display/LRM/FIN+-+Boleto)
