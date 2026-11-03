---
content_hash: d1dfe0fb3a5ae1aa929ab8c7ef7c6fb4188ba2ac9a348463e451be590ce8ba02
fetched_at: '2026-06-29T00:10:46.198653+00:00'
page_id: '554636481'
product: rm
source: tdn-rm
title: Ressarcimento MG - Registro H030
type: documentation
url: https://tdn.totvs.com/display/LRM/Ressarcimento+MG+-+Registro+H030
version: 5
---

## **Conteúdo**



## **01. Sobre1**

**INFORMAÇÕES COMPLEMENTARES DO INVENTÁRIO DAS MERCADORIAS SUJEITAS AO REGIME DE SUBSTITUIÇÃO TRIBUTÁRIA.**  
Este registro é obrigatório quando o campo MOT\_INV do registro H005 for igual “06”, conforme legislação definida pela UF de domicílio do contribuinte. Para os demais motivos, não deve ser informado.

## **02. Consistências para Geração do Registro2**

* **H005** será gerado automaticamente com a **Data de Inventário** de 1 dia anterior ao da Data da rotina. Exemplo: Sped gerado com data 01/01/2020 a 31/01/2020 a data de Inventário será 31/12/2019. Para geração do Registro H005 com motivo "06" e filhos, automaticamente, é necessário que a rotina gere os registros **C180**, **C185** e **C870** previamente.

Para gerar os dados de Ressarcimento ST, na pasta Personalização deverá ser marcada a opção "Gerar ressarcimento/Complemento ICMS ST":

* **H010** será gerado somente para os produtos que foram gerados nos registros "C180", "C185" e "C870".

Observação: No registro H010 é necessário informar a conta contábil do estoque e esta deve ser informada em Parâmetros do Sped Fiscal, aba Dados Inventário no campo "Código da Conta Contábil do Estoque".

* **H030** Serão selecionados os itens dos lançamentos fiscais de Entrada e a quantidade e valores de tributos serão selecionados até atender a quantidade em Estoque, no período menor ou igual a data do inventário.   
    
  Os lançamentos de saída com os itens que possuem referência de itens dos lançamentos de entrada não terão seus valores de ICMS e ICMS -ST totalizados como se estivessem no estoque. No registro H030 serão demonstrados os valores unitários ou seja **Valor do Imposto** divido pela **Quantidade** informada no H010.

Importante

**Associação de lançamentos:**  
Para o que o cálculo seja realizado corretamente é necessário associar lançamento de Saída ao Lançamento de Entrada, para isso existe o processo de associação de lançamentos de Saída, segue no documento abaixo todos os detalhes:  
 [Associação Lançamentos de Saída](https://tdn.totvs.com/pages/viewpage.action?pageId=438273534)

## **03. Registros H010 e H030 com valores zerados:3**

Quando ocorrer uma movimentação de estoque onde a quantidade total do produto, que possui lançamentos de entrada, tiver lançamentos de saída no mesmo mês, os registros H010 e H030 serão gerados no arquivo SPED Fiscal com valores zerados, uma vez que não há valor em estoque no encerramento do período. Segue exemplo abaixo:  
  
**Exemplo:**Produto **01.10** possui lançamento de entrada com quantidade 50 no mês 01/2023:  
  
  
  
O mesmo produto **01.10** possui a mesma quantidade de entrada em um lançamento de saída, zerando assim o estoque:  
  
  
  
Ao gerar a rotina SPED Fiscal no período 01/2023 é apresentado os registros **H010** e **H030** zerados:

## **04. Regerar Saldos e Custos:4**

Não é necessário executar o processo de Regerar Saldos e Custos para gerar o H030 mas caso existam produtos na base de dados que não tem suas movimentações na TRELSLD ou que realmente precisam de recálculo o processo deve ser executado.

O Processo está localizado no modulo de "Gestão de Estoque, Compras e Faturamento", pasta Estoque > Processos > Regerar Saldos e Custos

**Exemplo de Cálculo:**

Foi montando um cenário onde foi escolhido 1 produto “ABC” e feito toda sua movimentação de estoque com inclusão de movimentos que foram escriturados onde se forma o cenário abaixo do produto “ABC”.

Com a saída de 100 unidades do produto "ABC" no dia  o produto "ABC" ficou com apenas 150 unidades em estoque. Valor esperado do produto no registro registro H030 de acordo com sua movimentação até 29/02/2020 gerado na rotina de 01/03/2020 a 31/03/2020

Observação: Os valores da movimentação do dia 01/12/2018 foi proporcional a quantidade em estoque, para que os cálculos fiquem de forma correta.
