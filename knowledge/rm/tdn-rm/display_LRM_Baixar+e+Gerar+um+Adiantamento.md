---
content_hash: 924af13fa6ef6080c341c7a0126cc2b6f0aa424786ecdd28199b2af4e81aae47
fetched_at: '2026-06-29T00:09:18.132520+00:00'
page_id: '421388679'
product: rm
source: tdn-rm
title: Baixar e Gerar um Adiantamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Baixar+e+Gerar+um+Adiantamento
version: 3
---

Caso encontre uma diferença "A Maior" entre o valor líquido do lançamento e o valor líquido apresentado no arquivo bancário, é possível definir que o sistema gere um lançamento de "Adiantamento" com o valor da diferença e baixe o lançamento com o seu valor líquido.  
 Antes de realizar este processo o sistema verifica o valor do parâmetro "Diferença de valor para Geração de Lançamentos de Adiantamento". O processo só será realizado se o valor da diferença for maior que o valor informado no parâmetro. Se a diferença for igual, menor ou o campo estiver com o valor "0", os processos realizados serão o de Não Baixar e Baixar e informar o valor da diferença em um campo.  
 Ao informar um valor no parâmetro é necessário informar um Tipo de Documento com a Classificação "Adiantamento" no parâmetro "Código do Tipo de Documento de Adiantamento (Default)".

**Exemplo quando o valor da diferença for "menor" ou "igual" ao valor informado no parâmetro**

No parâmetro "Diferença de valor para Geração de Lançamentos de Adiantamento" foi informado o valor de "101,00". No sistema existe um lançamento com o valor líquido de R$200,00 (duzentos reais). Ao realizar a importação do arquivo de retorno de cobrança o sistema verifica que o valor líquido deste lançamento no arquivo é de R$300,00 (trezentos reais), sendo assim, existe uma diferença de R$100,00 (cem reais). O sistema realiza o seguinte processo: -Verifica o parâmetro; -Quando existe valor no parâmetro é apresentada uma mensagem informando sobre o processo de Adiantamento; -Como o valor da "diferença" é menor que o valor informado no parâmetro, o sistema passa a respeitar os parâmetros "Se diferença A Maior" e "Se diferença A Menor".

**Exemplo quando o valor da diferença for "maior" do que o valor informado no parâmetro**

No parâmetro "Diferença de valor para Geração de Lançamentos de Adiantamento" foi informado o valor de "99,00". No sistema existe um lançamento com o valor líquido de R$200,00 (duzentos reais). Ao realizar a importação do arquivo de retorno de cobrança o sistema verifica que o valor líquido deste lançamento no arquivo é de R$300,00 (trezentos reais), sendo assim, existe uma diferença de R$100,00 (cem reais). O sistema realiza o seguinte processo: -Verifica o parâmetro; -Quando existe valor no parâmetro é apresentada uma mensagem informando sobre o processo de Adiantamento; -Como o valor da "diferença" é maior que o valor informado no parâmetro, o sistema baixa o lançamento com o seu "valor líquido" e gera um lançamento de adiantamento com o valor da diferença (100,00).

**Observações**

O lançamento de adiantamento é gerado já baixado.

O lançamento original não fica vinculado e nem relacionado ao lançamento gerado de adiantamento.

As informações contábeis do lançamento de adiantamento serão as mesmas do lançamento original.

Se a baixa do lançamento original for cancelada, o lançamento de adiantamento não sofrerá alteração, ou seja, ele continuará na base de dados sem alteração. Se o arquivo de retorno for importado novamente, será criado outro lançamento de adiantamento.
