---
content_hash: b4a281e837c5a45fadaa1b1f8986c18f8a57384e9a670d3a499aeae55de15529
fetched_at: '2026-06-29T00:09:28.579947+00:00'
page_id: '423938716'
product: rm
source: tdn-rm
title: Desfazer Agrupamento de Lançamentos Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938716
version: 9
---

O processo de Desfazer Agrupamento de Lançamentos tem como objetivo realizar o processo inverso ao agrupamento de lançamentos, uma vez que tenha sido realizado o agrupamento e por algum motivo deseja-se desfazer tal procedimento.

O processo pode ser realizado para lançamentos que estão em lote, ou para lançamentos que já foram integrados e estão no lote oficial da contabilidade (Lote 0).

É possível desfazer o agrupamento para mais de um lote simultaneamente. Basta que na tela de lotes, sejam selecionados todos os lotes desejados, ou na tela de execução do processo, sejam adicionados os lotes que terão seus agrupamentos desfeitos.

No caso de lotes que já foram integrados ao lote oficial da contabilidade (Lote 0), basta que na visão de lançamentos sejam selecionados todos os lançamentos/partidas que terão o agrupamento desfeito.

Pode ser selecionado um período específico para desfazer o agrupamento dos lançamentos, para isto deve-se marcar a opção "Considerar período" e informar uma data inicial e data final, restringindo assim as partidas/lançamentos a serem consideradas para o processo. Se nenhuma faixa de datas for informada, todas as partidas/lançamentos existentes no lote serão automaticamente consideradas para desfazer o agrupamento.

Se desejar que o processo de desfazer agrupamento seja aplicado a uma determinada Filial, basta marcar a opção "Ativar filtro" e selecionar as Filiais desejadas. Caso a opção não seja marcada, o processo será aplicado para todas as filiais utilizadas.

Opção: **Analisar o desagrupamento avaliando todo o Lançamento Contábil**.

Ao marcar esta opção o sistema irá validar todos as partidas do lançamento referente a partida selecionada na visão de lançamentos/partidas, ou seja: Na visão de lançamento foi marcada a partida (que está agrupada) com ID igual a 100; Essa partida pertence ao lançamento 123 que por sua vez possuí outras partidas que também estão agrupadas; Se o parâmetro "Analisar o desagrupamento avaliando todo o Lançamento Contábil" estiver marcado o sistema verificará todas as partidas do lançamento, inclusive a 100.

Essa opção foi criado para contemplar a situação onde, por exemplo, foi realizado o agrupamento de débitos e crédito em uma única partida. Com isso o sistema garantirá que todas as partidas e não somente a selecionada na visão sejam analisadas durante o desagrupamento.

**Atenção** Somente poderão ser desagrupados os lançamentos que foram originados em módulos externos e lançamentos que foram gerados no novo modelo de BackOffice.

* Após execução do processo, o lançamento retornará à sua forma original, tendo suas partidas e/ou lançamentos da mesma forma que estavam antes da realização do agrupamento de lançamentos.
