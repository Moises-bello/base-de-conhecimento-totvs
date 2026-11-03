---
content_hash: f24521fc66afed7dcd3a413286a0d8483461659c42999776edf27d3bb3242b2f
fetched_at: '2026-06-29T00:08:59.595676+00:00'
page_id: '364908430'
product: rm
source: tdn-rm
title: S-2205 - Alteração de Dados Cadastrais do Trabalhado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364908430
version: 13
---

* Este evento registra as alterações de dados cadastrais do trabalhador, tais como: documentação pessoal, endereço, escolaridade, estado civil, contato, etc.
* Deve ser utilizado tanto para empregados/servidores, inseridos através do evento [S-2200](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.S2200.aspx), quanto para outros trabalhadores sem vínculo de emprego cuja informação foi enviada originalmente através do evento específico de “[S-2300 -Trabalhados sem vinculo de emprego/Estatutário-inicio](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.S2300.aspx)”.

Segue procedimentos para geração do evento S-2205-Alteração de Dados Cadastrais .

1º Passo-Quando o usuário realizar alguma alteração no cadastro do funcionário será  gerado gatilho na Fila de eventos  com status 0-Pendente.

O Usuário poderá visualizá-lo no menu eSocial | Eventos de tabelas/ Não Periódicos.

2º Passo-Gerar XML:

O usuário deverá executar o processo de Geração do  XML para que o evento fique no status 1-Gerado .

Para isso deverá selecionar o evento e clicar Gerar XML dentro da fila de eventos ou através do menu esocial | Eventos de tabelas |Não Periódicos | Gerar XML.

3º Passo- Integrar evento com o TAF :

Para isso deverá selecionar o evento e clicar Integrar TAF.

Neste momento o status do evento será alterado para 3-Enviado para o TAF.

4º Passo: Enviar os eventos gerados na fila para o TOTVS Automação Fiscal (TAF):

* Acessar o produto Totvs Automação Fiscal (TAF)  e realize  o processamento para envio das informações do Totvs Folha de pagamento para o TAF.

5º Passo:Atualizar o Status da integração TAF

Para atualizar o status da integração do TAF terá as seguintes opções:

* Na fila de eventos selecionar  " Processos" |Atualizar Status integração TAF ou através do menu Processos | Atualizar Status Integração TAF.  
    
    
  Veja mapeamento dos campos que serão informados:
