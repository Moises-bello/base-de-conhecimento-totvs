---
content_hash: ba954b158e195efa0c0511fdac0060a34283884535998ba1797fc6961019961f
fetched_at: '2026-06-29T00:09:09.881419+00:00'
page_id: '394211720'
product: rm
source: tdn-rm
title: Como realizar o processo de Integridade RM x TAF?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=394211720
version: 4
---

Este processo consulta o status atual do evento no TAF e compara com o status da [Fila de Eventos](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.FilaEventos.aspx). Ele retorna a relação de eventos não encontrados e diferenças de status. 

Pre-requisito: instalação das versões 12.1.19.362 – 12.1.20.360 -12.1.21.107 ou acima.

 Observações:

* + A Quebra de Seção e Seleção de funcionários na tela principal, apenas serão habilitados caso seja marcado algum evento que relacione funcionários ou [Eventos Periódicos](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.EventosPeriodicos.aspx).
  + O Período de Apuração será obrigatório caso selecione algum dos [Eventos Periódicos](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.EventosPeriodicos.aspx).
  + Marcando o parâmetro "Período" será habilitado um campo para digitação de data. Esse intervalo será utilizado como filtro para seleção dos [Eventos de Tabelas](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.EventosDeTabelas.aspx) e os [Eventos Não Periódicos](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.EventosNaoPeriodicos.aspx), considerando a data do evento.

Para realizar o processo de consulta do status dos eventos do eSocial RM x TAF (TOTVS Automação Fiscal), o usuário pode executar os seguintes processos:

1. Acessar o menu eSocial, clique em outros processos e após acesse Integridade RM x TAF

                                              

Informe os parâmetros desejados, avance.

                                             

Selecione a coligada desejada;

                                             

Após a execução, caso o sistema inconsistência, ele  irá retornar as diferenças e os eventos não encontrados no TAF no log.
