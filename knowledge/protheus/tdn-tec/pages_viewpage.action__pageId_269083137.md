---
content_hash: 8b1ae0afcffca58ce88e872910350f00bcba67bf20561dc4fd3948b9dd997e23
fetched_at: '2026-07-02T19:24:22.228235+00:00'
page_id: '269083137'
product: protheus
source: tdn-tec
title: Correção - Métodos SetSelectedRow e RemoveColumn (TGrid) não funcionam corretamente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269083137
version: 2
---

|  |  |
| --- | --- |
| Situação | Método SetSelectedRow selecionava a linha porém ao mudar a linha atual (com o mouse ou teclado) não mostrava corretamente as linhas. Método RemoveColumns estava retirando também o cabeçalho. |
| Ocorrência | Para o método SetSelectedRow, estava faltando atualizar o valor atual selecionado do TGrid no Appserver, portanto ao mudar a linha selecionada ocorria uma repintura da linha antes de mudar a seleção. O método RemoveColumns estava informando que todas as colunas seriam removidas, causando o cabeçalho ser removido também. |
| Correção | O método SetSelectedRow agora atualiza corretamente o valor do item atual no AppServer e o método RemoveColumn apenas informa qual coluna será realmente removida. |
| Informações adicionais | * Referente à ocorrência: TEC-6652 * Disponível no Label 7.00.131227A, release SmartClient 2.3.3 |
