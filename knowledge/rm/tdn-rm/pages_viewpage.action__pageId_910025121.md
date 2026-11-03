---
content_hash: 72d08576c210918826029febb7f5a991d32ee2c186e6c51e335ac1fdb1392b6d
fetched_at: '2026-06-29T00:12:03.442549+00:00'
page_id: '910025121'
product: rm
source: tdn-rm
title: 'Função de Fórmula: TR'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=910025121
version: 22
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Função de fórmula que retorna o valor de IRRF considerando o valor passado como parâmetro. Nesta função é considerado os valores fixos dedutíveis quando for o caso, como dedução por dependente, dedução maior de 65 anos, dedução de IR Simplificado.

Sintaxe: TR (Valor)

A partir da publicação da MP 1171/2023, houve uma mudança importante na legislação tributária que impacta no cálculo do Imposto de Renda. O que mudou é que, conforme a MP, o cálculo de IR passou a exigir a aplicação da dedução mais benéfica para o contribuinte, ou seja, a dedução que resultar em menor imposto a ser pago deve ser escolhida.

No caso da Função de fórmula TR, não leva em consideração deduções como **INSS**, **pensão alimentícia**, pois elas dependem de serem calculadas podendo ter valores variados. Assim, o sistema acaba não conseguindo realizar a comparação correta entre as deduções legais e a **dedução do IR Simplificado**, podendo resultar em uma comparação de um valor menor com o valor de IR Simplificado registrado na tabela de valores fixos.

Isso faz com que o valor do **IR Simplificado**  seja **deduzido** do valor passado na função TR, considerando somente as deduções conhecidas o que poderiam não reduzir o imposto devido.

Desta forma é necessário fazer customização a fórmula utilizando outras funções/formulas complementares para incluir na base de cálculo informada na função TR caso o mesmo não queira que a dedução seja feita.

Atenção

Para considerar o valor de dedução por dependente é verificado o cadastro de dependente, além da marcação de incidência em IRRF, se os mesmo está dentro da regra da legislação para ser considerado como dependente de IR. Não é verificado o histórico de dependente.

## **02. EXEMPLO DE UTILIZAÇÃO**

Tabela de Cálculo de IRRF dentro da Vigência:

Tabela de valores fixos tem o registro com a finalidade 'Valor a deduzir no IRRF Simplificado' dentro da vigência com o valor de R$ 546,00:

Considerando o salário mensal do Colaborador é R$ 6751,65

E o colaborador tem um dependente de IR:

Retorno da Fórmula

Usuário cadastrou a Fórmula informando como parâmetro a Função RC, que retorna o salario cadastrado para o colaborador de contexto:

Como o colaborador possui somente 1 dependente, internamente é feito a comparação entre o valor dedutível por dependente (189,00) e o Valor dedução IR Simplificado (564,00). Como o valor de dedução de IR Simplificado é mais benéfico para o contribuinte, ele é deduzido da base passada na função de fórmula:

valor do salário retornado pela função RC - Valor dedução IR Simplificado = 6751,65 - 564,00 =  6187,65

Na tabela de IRRF atingiu a alíquota 27,5% com a dedução de R$ 896,00

Então o Cálculo será: (6187,65 \* 27,5/100) - 896,00  = 805,60

Colaborador com parâmetro 'Desconsiderar Desconto Simplificado do IRRF' marcado

No cadastro do Colaborador está marcado o parâmetro 'Desconsiderar Desconto Simplificado do IRRF'. Neste cenário no cálculo de IRRF não é considerado o valor da Dedução Simplificado, considerando somente as deduções legais:

Ao executar a fórmula, foi considerado o valor dedutível por dependente e não foi considerado o valor do simplificado, não fazendo assim a comparação:

Como o colaborador possui somente 1 dependente, internamente é feito considerado o valor dedutível por dependente (189,00) e deduzido da base passada na função de fórmula:

valor do salário retornado pela função RC - valor dedutível por dependente = 6751,65 - 189,00 =  6562,65

Na tabela de IRRF atingiu a alíquota 27,5% com a dedução de R$ 896,00

Então o Cálculo será: (6562,65 \* 27,5/100) - 896,00  = 908,57

Exemplo de cálculo com redutor do IRRF

Considerando um valor de R$6500,00

Iniciando execução de fórmula   
Chamando função                                   TR(6500)  
Retorno da função TR                              622,38  
Retorno                                           Folha.CallFunction ( "TR" , "ValorIrrf" , 6500 )   
Retorno                                           TR ( "TR" , "ValorIrrf" , 6500 )   
Retorno                                           622,38  
Terminando execução de fórmula

Como foi calculado esse valor:

* VALOR PASSADO EM FÓRMULA - SIMPLIFICADO = BASEIRRF PARA CÁLCULO DA TR
  + 6500 - 607,20 = 5892,80
  + Valor do IRRF: Base(5892,80) \* 27,5000% - 884,96 =735,56 (USANDO A TABELA DE IRRF CADASTRADA NA BASE DE TESTE)
* Rendimentos dentro da faixa de Redução do imposto
  + Valor da Redução: 978,62 - (0,133145 \* 6500,00) = 113,17750000 (CONSIDERA 6500 PORQUE SIMPLIFICADO É DEDUÇÁO NÃO CONSIDERADA PARA O REDUTOR)
  + IRRF com a Redução: 735,56 - 113,17750000 = 622,38
  + Valor do evento: **622,38**

## **03. TABELAS UTILIZADAS**

GFORMULAS

PVALFIX
