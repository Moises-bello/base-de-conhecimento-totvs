---
content_hash: 67c940d2f839800111f576dba7e904e716d636b0fe4a9296798a9a73be31f374
fetched_at: '2026-06-29T00:09:28.082710+00:00'
page_id: '423938654'
product: rm
source: tdn-rm
title: 'Agrupamento de Lançamentos - Opção: Agrupar Lançamentos'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938654
version: 7
---

***Atenção!***  
  
Esta funcionalidade só está disponível para as bases já migradas para o Novo Modelo do BackOffice.  
   
Esta opção permite agrupar em um único Lançamento, todas as partidas comuns encontradas dentro de um determinado lote. Serão verificadas no lote selecionado todas as partidas comuns e as mesmas, independente de estarem em um mesmo lançamento ou não, serão agrupadas em uma única partida em um lançamento podendo, de acordo com a forma de agrupamento selecionada Agrupar débitos com créditos em uma única partida ou Agrupar partidas a débito ou ainda Agrupar partidas a crédito.

**Agrupar Débitos com Créditos em uma única partida:** para que duas partidas possam ser agrupadas em uma única partida, elas têm que estar dentro das regras para o agrupamento e pode ocorrer de duas formas:

**A-** Uma partida que tenha a conta a débito preenchida e a conta a crédito em branco e a outra partida ao contrário, tenha a conta a débito em branco e a conta crédito preenchida, onde o valor da partida a débito tem que necessariamente ser igual ao valor da partida a crédito: Neste primeiro momento os valores das partidas comuns têm que ser iguais, pois eles não serão somados, serão apenas agrupados o débito e o crédito comum em uma única partida. Depois deste momento, dentro do lote pode passar a ter várias partidas comuns, resultante deste primeiro agrupamento, com as mesmas contas no débito e no crédito, podendo ter valores iguais ou não. Neste caso ocorrerá entre as partidas comuns um novo agrupamento onde agora os valores de uma partida serão somados aos valores de outra partida agrupando-as em uma única partida em um Lançamento.

**B-** Uma partida que originalmente tenha a conta a débito e a conta a crédito preenchidas, idêntica à outra partida também originalmente preenchida com o débito e com o crédito, podendo os valores destas partidas ser iguais ou não: Neste caso todas as partidas comuns serão agrupadas em uma única partida em um Lançamento.

Esta segunda forma de agrupamento distingui-se da anterior pelo fato das partidas já virem originalmente preenchidas com o débito e com o crédito, não sendo, portanto resultantes de um agrupamento de débitos e créditos comuns em uma única partida.   
Neste tipo de do agrupamento não será levada em consideração a contrapartida, pois a partida agrupada ficará sempre com a contrapartida vazia.

**Agrupar partidas a Débito** em uma única partida e também **Agrupar partidas a Crédito** em uma única partida: O sistema percorrerá o lote e selecionará todas as partidas comuns de todos os lançamentos que estiverem dentro das regras para o agrupamento e somará seus valores e 2º valores, gerando uma única partida com a soma de todos os Débitos ou então uma única partida com a soma de todos os Créditos.

Conforme opção selecionada, o agrupamento das partidas a Débito agrupará somente as partidas a débito idênticas e que tiverem a conta a crédito vazia, independente de estarem no mesmo lançamento ou não. O agrupamento das partidas a Crédito agrupará somente as partidas a crédito idênticas e que tiverem a conta a débito vazia, independente de estarem no mesmo lançamento ou não.

Veja também

* Regras e exemplos de Agrupamentos
