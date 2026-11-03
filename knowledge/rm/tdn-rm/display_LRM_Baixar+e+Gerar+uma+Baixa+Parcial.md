---
content_hash: d7bfdf63c46d5692ceb7bd3d08f65bf0fe18d1623def1f2372d3b953c75f57f0
fetched_at: '2026-06-29T00:09:18.134395+00:00'
page_id: '421388680'
product: rm
source: tdn-rm
title: Baixar e Gerar uma Baixa Parcial
type: documentation
url: https://tdn.totvs.com/display/LRM/Baixar+e+Gerar+uma+Baixa+Parcial
version: 4
---

É possível definir que o sistema realize uma "Baixa Parcial" do lançamento caso encontre uma diferença "A Menor" entre o valor líquido do lançamento e o valor líquido apresentado no arquivo bancário.  
 Antes de realizar este processo o sistema verifica o valor do parâmetro "Diferença de valor para Geração de Baixa Parcial". O processo só será realizado se o valor da diferença for maior que o valor informado no parâmetro. Se a diferença for menor, igual ou o campo estiver com o valor "0", os processos realizados serão o de Não Baixar e Baixar e informar o valor da diferença em um campo.

**Exemplo quando o valor da diferença for "menor" ou "igual" ao valor informado no parâmetro**

No parâmetro "Diferença para Geração de Baixa Parcial" foi informado o valor de "101,00". No sistema existe um lançamento com o valor líquido de R$200,00 (duzentos reais). Ao realizar a importação do arquivo de retorno de cobrança o sistema verifica que o valor líquido deste lançamento no arquivo é de R$100,00 (cem reais), sendo assim, existe uma diferença de R$100,00 (cem reais). O sistema realiza o seguinte processo: -Verifica o parâmetro; -Quando existe valor no parâmetro é apresentada uma mensagem informando sobre o processo de Baixa Parcial; -Como o valor da "diferença" é menor que o valor informado no parâmetro, o sistema passa a respeitar os parâmetros "Se diferença A Maior" e "Se diferença A Menor".

**Exemplo quando o valor da diferença for "maior" do que o valor informado no parâmetro**

No parâmetro "Diferença de valor para Geração de Baixa Parcial" foi informado o valor de "99,00". No sistema existe um lançamento com o valor líquido de R$200,00 (duzentos reais). Ao realizar a importação do arquivo de retorno de cobrança o sistema verifica que o valor líquido deste lançamento no arquivo é de R$100,00 (cem reais), sendo assim, existe uma diferença de R$100,00 (cem reais). O sistema realiza o seguinte processo: -Verifica o parâmetro; -Quando existe valor no parâmetro é apresentada uma mensagem informando sobre o processo de Baixa Parcial; -Como o valor da "diferença" é maior que o valor informado no parâmetro, o sistema baixa o lançamento com o "valor líquido" informado no arquivo (100,00) e gera outro lançamento com o valor da diferença (100,00).

**Observações**

O lançamento baixado fica relacionado com o lançamento gerado pela baixa parcial.

Mesmo não estando parametrizada a utilização de Baixa Parcial no sistema este processo será realizado.

Este processo respeita os parâmetros de Baixa Parcial.

A data de vencimento do lançamento gerado será a mesma do lançamento original.
