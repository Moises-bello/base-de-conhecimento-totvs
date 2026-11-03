---
content_hash: 93b523c55ce9c3e67230bb69401a106256c07b0c3751624b2cdf9067d76db3dc
fetched_at: '2026-06-29T00:09:17.785202+00:00'
page_id: '421388648'
product: rm
source: tdn-rm
title: Baixar e informar o valor da diferença em um campo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388648
version: 8
---

Utilizando os parâmetros "Se diferença A Maior" e "Se diferença A Menor" é possível selecionar o nome de um campo para ser preenchido com o valor da diferença e desta forma permitir a "baixa" do lançamento.  
Os campos disponíveis são:

Se diferença A Maior

Valor Juros  Valor Multa  Valores Opcionais

Se diferença A Menor

Valor Desconto  Valores Opcionais

**Se diferença A Maior**

Foi selecionado no parâmetro "Se diferença A Maior" o campo "Valor Juros". No sistema existe um lançamento com o valor líquido de R$200,00 (duzentos reais). Ao realizar a importação do arquivo de retorno de cobrança o sistema verifica que o valor líquido deste lançamento no arquivo é de R$300,00 (trezentos reais), sendo assim, existe uma diferença de R$100,00 (cem reais). O sistema realiza o seguinte processo: -Verifica a parametrização do sistema; -Preenche automaticamente o campo "Juros" do lançamento com o valor da diferença, ou seja, R$100,00; -Baixa o lançamento com o valor líquido informado no arquivo bancário, ou seja, R$300,00.

**Se diferença A Menor**

Foi selecionado no parâmetro "Se diferença A Menor" o campo "Valor Desconto". No sistema existe um lançamento com o valor líquido de R$200,00 (duzentos reais). Ao realizar a importação do arquivo de retorno de cobrança o sistema verifica que o valor líquido deste lançamento no arquivo é de R$100,00 (cem reais), sendo assim, existe uma diferença de R$100,00 (cem reais). O sistema realiza o seguinte processo: -Verifica a parametrização do sistema; -Preenche automaticamente o campo "Desconto" do lançamento com o valor da diferença, ou seja, R$100,00; -Baixa o lançamento com o valor líquido informado no arquivo bancário, ou seja, R$100,00.

**Observações**

1 - Os Valores Opcionais serão apresentados de acordo com a parametrização dos mesmos (Assistente de Implantação de Processos | etapa Valores Opcionais do Lançamento Financeiro).

2 - Os Valores de Integração do Educacional também afetam as configurações dos parâmetros "Se diferença A Maior" e "Se diferença A Menor". Caso sejam configurados no módulo Educacional os valores nesses campos serão gravados nos Valores de Integração respectivos, sobrepondo a parametrização feita no processo de retorno de cobrança, exceto para os campos "Juros", "Multa", "Desconto" e "Não baixar" que se selecionados matém o comportamento do processo. Para saber mais detalhes da configuração no Educacional consulte .

**Exemplos**  
Os nomes dos valores apresentados dependerão dos nomes informados nos parâmetros. Os campos onde eles serão apresentados dependerão da sua "Ação". Ação = Nada, o nome do valor opcional não será apresentado para seleção. Ação = Acrescentar, o nome do valor opcional será apresentado apenas no campo "Se diferença A Maior". Ação = Descontar, o nome do valor opcional será apresentado apenas no campo "Se diferença A Menor".

Antes de realizar este processo o sistema verifica os valores dos parâmetros "Diferença de valor para Geração de Baixa Parcial" e "Diferença de valor para Geração de Lançamentos de Adiantamento". O processo "Baixar e informar o valor da diferença em um campo" só será realizado se o valor da diferença for menor ou igual ao valor informado nos parâmetros.
