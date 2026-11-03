---
content_hash: 294c5c50b9bfc1d90df66e34b303567533d5517cc2cad7cdec7d210a06ec42c6
fetched_at: '2026-06-29T00:08:46.642575+00:00'
page_id: '317308239'
product: rm
source: tdn-rm
title: 1506432 CONTROLADORIA01-669 DT Preferências Relatórios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=317308239
version: 95
---

# Preferência dos relatórios contábeis

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Relatórios contábeis |
| **Situação/Requisito:** | Foi identificado que nas preferências do relatório Balancete está ocorrendo a seguinte inconsistência: Seleciona-se uma preferência com informações pré-definidas de filtro de contas e gera-se o relatório. O sistema apresenta um determinado valor para as contas de Ativo, em seguida altera-se o filtro de contas para contas do Passivo. Salva-se uma nova preferência, após gera o relatório novamente, será apresentado um outro valor para o passivo (até aí tudo correto). Ao selecionar a preferência anterior com filtros de contas do Ativo, e gerar o relatório, o sistema mantem os valores apresentados para as contas do Passivo, ou seja, o sistema não gerar os dados do relatório de acordo com os filtros salvos na preferência selecionada. |
| **Solução/Implementação:** | As contas contábeis, existentes nos relatórios do RM Saldus, estavam sendo carregadas incorretamente após a alteração da preferência. Esta situação só ocorria se o usuário executasse o relatório com a aba Filtros selecionada e, em seguida, alterasse a preferência na aba de Execução Concluída. Ao clicar no botão voltar e executar o relatório novamente era aplicado o filtro de contas da preferência anterior. Vale ressaltar que os relatórios sofreram algumas alterações para que esta situação não se repita. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados**: | N/A |
| **Requisito (informe o requisito relacionado):** | N/A |

divs
