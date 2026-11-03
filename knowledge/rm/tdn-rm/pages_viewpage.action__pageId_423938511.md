---
content_hash: 24af236d07fabd2bad16e84890fb4e7d0cc3cf5b5da0236728bed0de24dd5098
fetched_at: '2026-06-29T00:09:27.391465+00:00'
page_id: '423938511'
product: rm
source: tdn-rm
title: Rateio por centro de custo transitório
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938511
version: 2
---

A distribuição por centro de custo transitório é utilizada em operações onde não é possível definir o critério de distribuição no momento do registro da mesma tais como Energia Elétrica, Aluguel, Treinamento, etc.

Ao incluir a Nota Fiscal, a distribuição gerencial é registrada em uma conta gerencial transitória, posteriormente o processo de distribuição é realizado na contabilidade para que as despesas e receitas registradas em contas gerenciais transitórias sejam apropriadas nas devidas contas gerenciais.

Este processo faz a redistribuição seguindo critérios de rateio pré-definidos. Ao executar o processo o mesmo irá selecionar a movimentação das contas no lote zero (lote oficial da contabilidade) e irá gerar um lançamento com dois grupos de partidas. O primeiro grupo contendo partidas inversas às partidas originais que foram selecionadas no lote zero, o segundo grupo contendo partidas com a nova distribuição.

O exemplo abaixo contempla despesas realizadas com Treinamento. No momento do registro das despesas não foi possível determinar a distribuição gerencial real, registrando-as então em uma gerencial transitória. Em um segundo momento, a empresa conferiu a lista de participantes e conseguiu determinar qual o custo a ser distribuído para cada conta gerencial. Ao executar o processo de distribuição, foi gerado um lançamento contendo dois grupos de partidas, o primeiro contendo partidas inversas às originais para zerar os valores lançados provisoriamente, uma partida inversa para zerar o saldo devedor apurado e outra para zerar o saldo credor apurado na origem e o segundo grupo contendo partidas com a nova distribuição nas devidas contas gerenciais.  
   
   
[
