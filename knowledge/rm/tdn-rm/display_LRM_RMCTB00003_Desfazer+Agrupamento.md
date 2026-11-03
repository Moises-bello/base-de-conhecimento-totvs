---
content_hash: acdcc208104fa8c09d76947331c09ef80867fead2a81075aadbba6133810ddc2
fetched_at: '2026-06-29T00:08:41.757015+00:00'
page_id: '286747768'
product: rm
source: tdn-rm
title: RMCTB00003_Desfazer Agrupamento
type: documentation
url: https://tdn.totvs.com/display/LRM/RMCTB00003_Desfazer+Agrupamento
version: 6
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS - Gestão Contábil |
| **Versões:** | 12.1.18 |
| **Ocorrência:** | Desfazer Agrupamento de Lançamentos |
| **Ambiente:** | Novo Modelo BackOffice |
| **Passo a passo:** | **Definição do processo**  O processo de Desfazer Agrupamento de Lançamentos tem como objetivo realizar o processo inverso ao agrupamento de lançamentos, uma vez que tenha sido realizado o agrupamento e por algum motivo deseja-se desfazer tal procedimento.  O processo pode ser realizado para lançamentos que estão em lote, ou para lançamentos que já foram integrados e estão no lote oficial da contabilidade (Lote 0).  **Regras Gerais**  Não há regras pré-definidas, sendo necessário apenas selecionar o lote a ser desagrupado e informar algum filtro se necessário.  No caso de lotes que já foram integrados ao lote oficial da contabilidade (Lote 0), basta que na visão de lançamentos sejam selecionados todos os lançamentos/partidas que terão o agrupamento desfeito.  Disponível através da visão de lançamentos dos lotes no **Menu Escrituração Contábil | Lotes | Selecione o lote | Processos | Desfazer Agrupamento.**  Ou diretamente pela visão do lote zero no **Menu Escrituração Contábil | Lançamento | Selecione o respectivo lançamento | Processos Desfazer Agrupamento.** **Parametrização Necessária**  1 - Selecione o lote a ser desagrupado e acesse a opção Processos / Desfazer Agrupamento:      2 - Após selecionado o lote o mesmo já aparece na tela de seleção, sendo possível adicionar mais lotes, conforme necessidade:      3 - No item seguinte podemos aplicar filtro de datas ou de filiais:      **Importante** Caso selecione alguma partida específica para Desfazer o Agrupamento, será apresentada a opção '**Analisar o desagrupamento avaliando todo o Lançamento Contábil**' que poderá ser selecionada durante a execução do processo:      Ao marcar esta opção o sistema irá validar todos as partidas do lançamento referente a partida selecionada na visão de lançamentos/partidas.  Exemplo:  Na visão de lançamento foi marcada a partida (que está agrupada) com ID igual a 100; Essa partida pertence ao lançamento 123 que por sua vez possuí outras partidas que também estão agrupadas; Se o parâmetro "Analisar o desagrupamento avaliando todo o Lançamento Contábil" estiver marcado o sistema verificará todas as partidas do lançamento, inclusive a 100.  Essa opção foi criado para contemplar a situação onde, por exemplo, foi realizado o agrupamento de débitos e crédito em uma única partida. Com isso o sistema garantirá que todas as partidas e não somente a selecionada na visão sejam analisadas durante o desagrupamento.  4 - Sempre verifique o log gerado: |
| **Observações:** | Somente poderão ser desagrupados os lançamentos que foram originados em módulos externos e lançamentos que foram gerados no novo modelo de BackOffice.Após execução do processo, o lançamento retornará à sua forma original, tendo suas partidas e/ou lançamentos da mesma forma que estavam antes da realização do agrupamento de lançamentos. Para mais informações acesse . |
