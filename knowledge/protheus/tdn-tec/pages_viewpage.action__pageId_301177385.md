---
content_hash: 048e32ecde25db8b0b6e326cc302ee39c93518a3c57e80552308bb3b1795ff83
fetched_at: '2026-07-02T19:24:23.250698+00:00'
page_id: '301177385'
product: protheus
source: tdn-tec
title: Correção - Cliques rápidos na tela de informações do fim do ciclo de vida da
  P11 gera erro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=301177385
version: 1
---

|  |  |
| --- | --- |
| Situação | Ao carregar a tela de informações do fim do ciclo de vida da P11 a clicar rapidamente (mais de uma vez) no botão "Ok, Entendi", gera o erro:  THREAD ERROR ([11324], renato.machado, SPOD3259) 05/09/2017 18:40:13 variable is not an object on {|THIS|OBACKGROUND:HIDE(),OBACKGROUND:=NIL} (APLIB050.PRW) 07/07/2017 14:28:15 line : 3376 |
| Ocorrência | Erro ocorre devido ao SmartClient tratar mais de um clique no botão enquanto está carregando o resto da tela. Nesta situação o bloco de código relacionado ao botão esconde o próprio botão, portanto não poderia tratar um segundo clique. |
| Correção | Correção feita para não deixar disparar um clique em um objeto que não esteja visível. |
| Informações adicionais | * Referente ao chamado: 1299862 * Referente à ocorrência: MTEC-616 * Disponível em builds iguais ou superiores a 7.00.131227A - 13.2.3.22 |
