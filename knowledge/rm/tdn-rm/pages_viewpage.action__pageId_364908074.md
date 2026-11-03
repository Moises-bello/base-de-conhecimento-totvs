---
content_hash: 59ef2e308d1253a25cd6bf89190976d64feea7e9049bf608453d5a510d807fea
fetched_at: '2026-06-29T00:08:59.585715+00:00'
page_id: '364908074'
product: rm
source: tdn-rm
title: S-2190 - Admissão de Trabalhador - Registro Preliminar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364908074
version: 19
---

* Este evento é opcional, e deverá ser utilizado quando não for possível enviar todas as informações do evento “[S-2200- Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.S2200.aspx)” até o final do dia imediatamente anterior ao do início da respectiva prestação do serviço.
* É imprescindível o envio posterior do evento “[S-2200- Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.S2200.aspx) .
* Deve ser enviado até o final do dia imediatamente anterior ao do início da prestação do serviço pelo trabalhador admitido. No caso de admissão de empregado na data do início da obrigatoriedade de envio dos eventos não periódicos ao eSocial, o prazo de envio  da informação de admissão é o próprio dia da admissão.

Para a geração do evento S-2190 oo usuário deverá proceder conforme abaixo:

1º Passo:Acesse o  menu Administração |Registro Preliminar  e inclua um novo Registro .

Será gerado gatilho na fila de eventos para o evento S-2190 com Status 0-Pendente.

O Usuário poderá visualizá-lo no menu eSocial | Eventos de tabelas/ Não Periódicos.

2º Passo: Gerar XML:

O usuário deverá executar o processo de Geração do  XML para que o evento fique no status 1-Gerado .

Para isso deverá selecionar o evento e clicar Gerar XML dentro da fila de eventos ou através do menu esocial | Eventos de tabelas |Não Periódicos | Gerar XML

3º Passo-Integrar evento com o TAF:

Para isso deverá selecionar o evento e clicar Integrar TAF.

Neste momento o status do evento será alterado para 3-Enviado para o TAF.

4º Passo:Enviar os eventos gerados na fila para o TOTVS Automação Fiscal (TAF)

* Acesse o produto Totvs Automação Fiscal (TAF)  e realize  o processamento para envio das informações do Totvs Folha de pagamento para o TAF.

5º Passo: Atualizar o Status da integração TAF.

Para atualizar o status da integração do TAF terá as seguintes opções:

* Selecionar  " Processos" |Atualizar Status integração TAF ou através do menu Processos | Atualizar Status Integração TAF.

Veja mapeamento dos campos que serão informados: <http://tdn.totvs.com/display/public/LRM/Evento+S-2190>
