---
content_hash: e8903e34a60a4f713b004790c4d7684217d2c86312352133b5662bc9a4af4379
fetched_at: '2026-06-29T00:08:59.582663+00:00'
page_id: '364908067'
product: rm
source: tdn-rm
title: Eventos Não Periódicos - Passo a Passo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364908067
version: 8
---

Para gerar os eventos "Não Periódicos"  o usuário deverá ter realizado junto aos sistemas Totvs Folha de pagamento,Totvs Automação de Ponto, Totvs Segurança e Medicina Trabalho um dos seguintes Cadastros / Processos.

* Admissão/ingresso de um empregado/servidor
* Alteração de salário
* Alterar Função
* Desligamento
* Incluir Afastamento
* Cadastrar Férias

1-Será gerado [Gatilho](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.GerarGatilhosIniciais.aspx) na fila de eventos  .

O Usuário poderá visualizá-lo no menu eSocial | Eventos de tabelas/ Não Periódicos | Fila de Eventos.

2-Gerar XML:

O usuário deverá executar o processo de Geração do  XML para alterar o status do evento de 0-Pendente para  1-Gerado .

Para isso deverá selecionar o evento desejado  e clicar Gerar XML dentro da fila de eventos ou através do menu esocial | Eventos de tabelas |Não Periódicos | Gerar XML.

Veja que através do menu | Eventos de tabelas |Não Periódicos | Gerar XML será possível :

* Definir os tipos de eventos
* Os arquivos a serem gerados
* Status para geração

3-Integrar com TAF.

Será necessário  integrar com TAF utilzando uma das opções abaixo :

* Na Fila de eventos clicando na opção Integrar TAF ou através do processos | Integrar TAF.

 4-Atualizar status integração TAF:

* Acessar o produto Totvs Automação Fiscal (TAF)  e realize  o processamento para envio das informações do Totvs Folha de pagamento para o TAF.
* Atualizar o Status da integração TAF que poderá ser feita através das  seguintes opções:

* + Selecionar  " Processos" |Atualizar Status integração TAF. ou através do menu Processos | Atualizar Status Integração TAF.

Observação : Através do “Processos" na fila de eventos será possível : Gerar XML, integrar com TAF, Atualizar Status integração TAF e Gerar eventos de Exclusão (S-3000).
