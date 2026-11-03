---
article_id: 22016757290263
category: Gestão de Frotas
content_hash: b7451f3f84975b48e34c4c30a8be18557293ac6a43257f4fb26bcb1bcaa12241
fetched_at: '2026-06-28T22:42:39.297081+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Atualização de custos dos Abastecimeto
  ao realizar o Custo Médio no SIGAEST
type: support-article
updated_at: '2024-03-13T12:58:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22016757290263-Manufatura-Linha-Protheus-MNT-Atualiza%C3%A7%C3%A3o-de-custos-dos-Abastecimeto-ao-realizar-o-Custo-M%C3%A9dio-no-SIGAEST
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22016757273367)***Tempo aproximado para leitura: **00:03:30 min**  
**Dúvida**Ao realicar o processo de **Custo Médio - MATA330**, os custos do abastecimento são atualizados?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas (SIGAGFR) - Versão 12  
  
**Solução**No contexto de realizar o processo de **Recálculo do Custo Médio** as movimentações de entrada e saída de estoque podem receber alterações em seu custo. Devido a integração entre os módulos pelo parâmetro **MV\_NGMNTES - Integracao Manutencao - SIGAMNT** com **Estoque - SIGAEST**, igual a **S - Sim** e a relação do abastecimento realizado em um **Posto Interno** **juntamente com o processo de movimentação do estoque** com a utilização do parâmetro **MV\_ESTHOME - Indica o momento que o estoque sera debitado**, igual a **S - Abastecimento** ou **C - Conciliacao**. O processo precisa equalizar os valores entre os módulos, visto a relação e integração.  
Então sempre que o **Recálculo do Custo Médio** for realizado, as movimentações que possuirem vínculo com um abastecimento, vão ter o **Valor Total do abastecimento - TQN\_VALTOT** e o **Valor Unitário - TQN\_VALUNI** do abastecimento atualizados conforme a atualização do custo da movimentação do estoque.  
O vínculo entre o abastecimento e a movimentação de estoque pode ser consultada relacionando o campo de **Sequencial - TQN\_NUMSEQ** na tabela de abastecimento e o campo de **Sequencial**- **D3\_NUMSEQ**na tabela de movimentações do estoque.
