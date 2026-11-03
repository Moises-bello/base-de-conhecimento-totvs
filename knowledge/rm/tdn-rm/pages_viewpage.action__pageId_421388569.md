---
content_hash: 13aaacaa0c87584639e1b58f9ea3a902ee3a2e9075886774395e53b98a5fc2eb
fetched_at: '2026-06-29T00:09:17.057698+00:00'
page_id: '421388569'
product: rm
source: tdn-rm
title: Não Baixar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388569
version: 3
---

Selecionando a opção "Não Baixar" (parâmetros "Se diferença A Maior" e "Se diferença A Menor") os lançamentos que estiverem com a diferença não serão baixados.

**Se diferença A Maior**

Foi selecionado no parâmetro "Se diferença A Maior" a opção "Não Baixar". No sistema existe um lançamento com o valor líquido de R$200,00 (duzentos reais). Ao realizar a importação do arquivo de retorno de cobrança o sistema verifica que o valor líquido deste lançamento no arquivo é de R$300,00 (trezentos reais), sendo assim, existe uma diferença de R$100,00 (cem reais). O sistema realiza o seguinte processo: -Verifica a parametrização do sistema; -Não Baixa o lançamento e informa que a baixa não foi realizada devido a uma diferença nos valores líquidos.

**Observação**

Antes de realizar este processo o sistema verifica os valores dos parâmetros "Diferença de valor para Geração de Baixa Parcial" e "Diferença de valor para Geração de Lançamentos de Adiantamento". O processo "Não Baixar" só será realizado se o valor da diferença for menor ou igual ao valor informado nos parâmetros.
