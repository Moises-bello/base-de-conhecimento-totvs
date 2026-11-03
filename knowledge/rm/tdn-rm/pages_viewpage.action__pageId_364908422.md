---
content_hash: 356ab948fa806ff74680408d29c562e23789db35c2d8812afec414bc5ba2777c
fetched_at: '2026-06-29T00:08:59.592124+00:00'
page_id: '364908422'
product: rm
source: tdn-rm
title: S-2200 – Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364908422
version: 16
---

* Este evento registra a carga inicial de funcionários, admissão do empregado ou o ingresso de servidores estatutários.
* Trata-se do primeiro evento relativo a um determinado vínculo – excetuado a situação prevista para o evento “[S-2190 -Admissão de Trabalhador-Registro Preliminar](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.S2190.aspx)”, registrando as informações cadastrais e do contrato de trabalho.
* Pode ocorrer também quando o empregado é transferido de uma empresa do mesmo grupo econômico ou em decorrência de uma sucessão, fusão ou incorporação.  
    
  Para a geração do evento S-2200 o usuário  deverá seguir os seguintes passos:  
    
  1º Passo: Cadastre um funcionário através do menu Administração de Pessoal | Funcionários

Será gerado gatilho na fila de eventos  para o evento S-2200 com status 0-Pendente.

O Usuário poderá visualizá-lo no menu eSocial | Eventos de tabelas/ Não Periódicos | Fila de Eventos.

2º Passo:Gerar XML:

O usuário deverá executar o processo de Geração do  XML para que o evento fique no status 1-Gerado .

Para isso deverá selecionar o evento e clicar Gerar XML dentro da fila de eventos ou através do menu esocial | Eventos de tabelas |Não Periódicos | Gerar XML.

3º Passo: Integrar evento com o TAF:.

Para isso deverá selecionar o evento e clicar Integrar TAF.

Neste momento o status do evento será alterado para 3-Enviado para o TAF.

4º Passo:Enviar os eventos gerados na fila para o TOTVS Automação Fiscal (TAF)

* Acesse o produto Totvs Automação Fiscal (TAF)  e realize  o processamento para envio das informações do Totvs Folha de pagamento para o TAF.

5º Passo: Atualize o Status da integração TAF.

Para atualizar o status da integração do TAF Terá as seguintes opções:

* Selecionar  " Processos" |Atualizar Status integração TAF ou através do menu Processos | Atualizar Status Integração TAF.

Veja mapeamento dos campos que serão informados: <http://tdn.totvs.com/display/public/LRM/Evento+S-2200>
