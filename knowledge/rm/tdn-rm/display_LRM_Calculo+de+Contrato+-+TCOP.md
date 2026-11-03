---
content_hash: 3f93fc0390b1866e56935b30c911981ea38109f4ac8088120b8e7db6a2e9a908
fetched_at: '2026-06-29T00:11:17.450759+00:00'
page_id: '680260198'
product: rm
source: tdn-rm
title: Calculo de Contrato - TCOP
type: documentation
url: https://tdn.totvs.com/display/LRM/Calculo+de+Contrato+-+TCOP
version: 3
---

Este documento tem como objetivo explicar a identificação do calculo de contrato de forma mais rápida, com conferência dos campos: Contratado Inicial, Aditivos, Contrato, Saldo Contratual, Total Medido.

**Contratado Inicial:** Esse campo é calculado baseado na Quantidade x Valor dos itens no momento da associação de itens/objetos ao contrato.  
Esse valor pode ser verificado pelo SELECT na tabela MITMCNT, verificando o campo QUANTIDADEINICIAL x VALORINICIAL de cada item.

**Aditivo:** A soma dos valores dos aditivos criados no contrato. Visualizado no anexo de aditivos:

Pode ser verificado pelo SELECT nas tabelas:  
**MITMQTDADITIVO** → Que armazena as **ALTERAÇÕES** de QUANTIDADE realizadas via aditivo. Usa-se (QTDEATUAL - QTDEANTERIOR) \* VALOR.  
**MITMCNTADITIVO →** Que armazena as (Contratações) INCLUSÕES de novos itens ao aditivo. Usa-se QUANTIDADE x VALORATUAL.

**Contrato:** Contratado Inicial + Aditivo

**Total Medido:** Soma do total medido dos Períodos, pode verificar pela visão de Períodos.  
Exemplo:

***Obs.: Períodos de ESTORNO subtraem do valor total medido.***

**Saldo Contratual:** Contrato - Total Medido

O total medido, tem que ser verificado através da tabela MTRFMED.  
Acontecem muitos problemas com diferenças de SALDO, quando há medições com quantidades pequenas em relação ao valor contratado, ou valor pequeno em relação a quantidade contratada, ocasionando pequena precisão nas casas decimais. Por isso, deve verificar na MTRFMED o campo **CAMPOMEDIDO.**

**Se o CAMPOMEDIDO for = V (Valor)** → O VALOR gravado é realmente o valor considerado para calculo.   
**Se o CAMPOMEDIDO for = Q (Quantidade)** → O valor gravado pode ser inconsistente, pois pode ter sido gravado com pouca precisão de casas decimais pelo processo de Medição.   
Por isso, a conta considerada para calculo do total medido deve ser **QUANTIDADEMEDIDA x PRECOLIBERADO**.

**Parâmetros e Processos que podem influenciar no Calculo do Valor do Contrato:**

### **Reajuste PI + R**

Quando esse parâmetro estiver marcado, o Calculo do Contrato sempre será feito: **QUANTIDADEINICIAL x VALORINICIA**L de cada item. Pois todos os reajustes realizados, **não** alteram o Valor Unitário do Item, somente gera saldo de reajuste para ser medido.

Com esse cenário, o **TOTAL MEDIDO** será: **VALORMEDIDOPI + VALORMEDIDOREAJUSTE (Tabela MTRFMED).**

### **Reajuste SEM PI+R**

Quando o parâmetro estiver **DESMARCADO**, o processo de REAJUSTE irá **alterar** o Valor Unitário do Item, dessa forma, consequentemente o **VALORCONTRATO.**

Dessa forma, o Valor Contratado na visão de contratos, será calculado da seguinte forma: **TABELA MITMCNT → QUANTIDADE \* VALORATUAL.***Obs.: Nessa tabela, temos os campos QUANTIDADEINICIAL e VALORINICIAL, que pode ser usado como histórico para saber qual era o valor contratado do item no momento da associação ao contrato.*

### **Reajuste SEM PI+R em Itens Incluídos por Aditivos**

Quando é utilizado o reajuste em itens que são de provenientes de Aditivos, é verificado se parte desse item já foi medido em algum período.

Caso não tenha sido medido: O valor do aditivo é alterado, pois o reajuste altera o valor unitário e consequentemente o valor do aditivo.

Caso já tenha parte do item medido: O Aditivo mudará a sua visualização do item, pois é gerado um novo registro no aditivo, contabilizando a alteração de preço proveniente do reajuste, somente no saldo que ainda não foi medido.

O **Calculo do Aditivo**, fica da seguinte forma:

Item 001.01.04 tinha Quantidade Contratada = 5 a um preço de 200,00 - Total 2.000,00.

Item 001.01.04 tinha total medido de 1 a um preço de 200,00.

Reajuste aplicado de 25%.

O reajuste aplicado, atualizará o Valor Unitário, alterando de 200,00 para 250,00 o unitário do item. Mas, somente sobre o saldo não utilizado ainda, ou seja, 4 x 250,00.

Dessa forma, o total do aditivo será 4 x 250,00 = 1000,00 + 1 x 200 = 1200,00.
