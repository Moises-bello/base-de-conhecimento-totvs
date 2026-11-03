---
content_hash: 2971e0adfe50a0c35b62dbc4c50bb9415b8ee08fa5260500650a50ec29509003
fetched_at: '2026-06-29T00:09:28.116461+00:00'
page_id: '423938660'
product: rm
source: tdn-rm
title: 'Agrupamento de Lançamentos – Opção: Agrupar Partidas'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938660
version: 6
---

***Atenção!***  
   
Esta funcionalidade só está disponível para as bases já migradas para o Novo Modelo do BackOffice.  
    
A opção Agrupar Partidas é muito parecida com a opção Agrupar Lançamentos. O que distingue uma da outra é que em Agrupar Lançamentos, todas as partidas comuns existentes dentro do lote poderão ser agrupadas em um único lançamento, ao passo que em **Agrupar Partidas**, o agrupamento será realizado somente entre as partidas comuns de um único lançamento e poderá, conforme opção selecionada, Agrupar débitos com créditos, em uma única partida ou Agrupar partidas a débito ou ainda Agrupar partidas a crédito.

**Agrupar Débitos com Créditos em uma única partida:** para que duas partidas possam ser agrupadas em uma única partida, elas têm que estar dentro das regras para o agrupamento e pode ocorrer de duas formas:

**A-** Uma partida que tenha a conta a débito preenchida e a conta a crédito em branco e a outra partida ao contrário, tenha a conta a débito em branco e a conta crédito preenchida, onde o valor da partida a débito tem que necessariamente ser igual ao valor da partida a crédito: Neste caso as partidas serão agrupadas em uma única que terá nela mesma o débito e o crédito preenchidos.

**B-** Uma partida que originalmente tenha a conta a débito e a conta a crédito preenchidas, idêntica à outra partida também originalmente preenchida com o débito e com o crédito, podendo os valores destas partidas ser iguais ou não: Neste caso todas as partidas comuns serão agrupadas em uma única partida.

Neste tipo de agrupamento não será levada em consideração a contrapartida, a partida agrupada ficará sempre com a contrapartida vazia.

**Agrupar partidas a Débito** em uma única partida e também **Agrupar partidas a Crédito** em uma única partida: O sistema selecionará, por lançamento, as partidas comuns que estiverem dentro das regras para o agrupamento, e somará seus valores e 2º valores, gerando uma única partida com a soma de todos os Débitos ou então uma única partida com a soma de todos os Créditos.

Conforme opção selecionada, o agrupamento das partidas a Débito agrupará somente as partidas a débito idênticas e que tiverem a conta a crédito vazia. O agrupamento das partidas a Crédito agrupará somente as partidas a crédito idênticas e que tiverem a conta a débito vazia.

Neste tipo de agrupamento a Data Cotação 2ª Moeda tem que ser a mesma em todas as partidas.

Veja também

* Regras e exemplos de Agrupamentos
