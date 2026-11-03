---
article_id: 15484305426583
category: Gestão de Frotas
content_hash: d29d4b44e6033c46c8f35191c3560151173fde0ffebd8c530068f3c2007c7c32
fetched_at: '2026-06-28T22:42:39.615240+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Valor unitário do Combustível na Importação
  de Abastecimento
type: support-article
updated_at: '2023-10-16T20:39:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15484305426583-Manufatura-Linha-Protheus-MNT-Valor-unit%C3%A1rio-do-Combust%C3%ADvel-na-Importa%C3%A7%C3%A3o-de-Abastecimento
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15484288874263)*** Tempo aproximado para leitura: **00:02:10 min****Dúvida**Qual é a regra usada para definir de onde será pego o **Valor Unitário** do combustível ao realizar uma importação de abastecimento?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas - Todas as versões  
  
**Solução**A primeira etapa na determinação da **origem** do **Valor do Combustível** é avaliar o parâmetro **MV\_NGPRSB2 - Busca preço médio na tabela SB2**. Se esse parâmetro estiver igual a **S - Sim**, o próximo passo é confirmar se o **Abastecimento Importado** foi realizado em um **Posto Interno** e se o posto possui **Tanque** e **Bomba**. Após verificar que o posto é interno e que a importação possui tanque e bomba, o **Valor do Combustível** é **obtido** da tabela **SB2 - Saldos Físico e Financeiro**.  
  
Caso alguma das validações anteriores não seja **Verdadeira**, o valor **não é obtido da SB2**. Nesse caso, é avaliado o parâmetro **MV\_NGPRENE - Indica se permite o usuário escolher se pode a partir da inconsistência gerar preço negociado oriundo da importação**. Se ele estiver igual a **S - Sim**, o valor é obtido do **Arquivo de Importação**. Caso o campo **TR6\_VLCOMB** **- Valor do combustível** não faça parte do cadastro do layout, são selecionados os valores **TR6\_QTDCOM - Quantidade Combustível Abastecido** e **TR6\_VLTOT - Valor Total Abastecido** e caso esses campos existam o valor é **obtido** a partir do cálculo **TR6\_VLTOT / TR6\_QTDCOM**. Caso algum dos campos não exista, o valor é atribuído como **zero**.  
  
No entanto, se o segundo parâmetro estiver igual a **N - Não**, é verificado se o parâmetro **MV\_NGCONEG - Checa valor negociado com o posto?** está igual a **S - Sim** e se o abastecimento possui **Posto**, **Loja** e **Tipo de Combustível**. Caso preencha esses requisitos, o **Valor do Combustível** é selecionado na tabela **TQH - Preços dos Combustíveis**. Se algum dos campos avaliados estiver **faltando** no abastecimento ou caso o parâmetro avaliado esteja igual a **N - Não**, o **Valor do Combustível** é **atribuído** como **zero**.
