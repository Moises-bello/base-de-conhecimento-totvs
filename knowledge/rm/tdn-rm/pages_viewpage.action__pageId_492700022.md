---
content_hash: 21ad4a3fc4d3cddfeb3bfc36b404df26e8e03215317da3658ea16c8b744c1828
fetched_at: '2026-06-29T00:10:21.688067+00:00'
page_id: '492700022'
product: rm
source: tdn-rm
title: 5510501 DEDUINTEGRACOES-5076 DT Mostrar valor total original na mensagem de
  verificação de inadimplência (lentidão na matrícula)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=492700022
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | TOTVS Gestão Educacional |
| Módulo: | TOTVS Educacional |
| Função: | Verificação de inadimplência Matrícula Rematrícula |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | N/A |

## **02. SITUAÇÃO/REQUISITO**

O sistema calcula o valor líquido de todos os lançamentos vencidos do aluno e, caso o valor seja maior do que o valor máximo de tolerância para inadimplência, será emitida uma mensagem para o usuário com o valor total líquido de todos os lançamentos vencidos.

## **03. SOLUÇÃO**

Foi criado o parâmetro de Tesouraria "Mostrar valor original total na validação de inadimplência" que fará com que o valor final mostrado para o usuário na mensagem de validação de inadimplência seja o valor total original dos lançamentos vencidos.

## **DESCRIÇÃO**

Na marcação desse parâmetro, como o sistema não precisará mostrar o valor total líquido na mensagem de validação, será calculado o valor líquido de cada lançamento, somado nos cálculos anteriores e, caso esse valor seja maior ou igual ao valor do parâmetro "Valor máximo de tolerância para inadimplência", o sistema não processará o valor líquido do restante da lista de lançamentos.

O sistema continuará se comportando conforme comportamento atual se o parâmetro estiver desmarcado. Nenhuma alteração foi feita nos lançamentos mostrados, ou seja, o sistema ao detectar inadimplência do aluno, mostra sempre todos os lançamentos vencidos.

O sistema funcionará da seguinte forma para a verificação de inadimplência:

1. Parâmetro "Mostrar valor original total na validação de inadimplência" **desmarcado**. O sistema identificará os lançamentos vencidos do aluno e os mesmos terão seu respectivo valor líquido calculado. Esses lançamentos serão mostrados para o usuário e, no final da mensagem de validação, será exibido o "Valor total" que será a soma dos valores líquidos dos lançamentos vencidos.

Parâmetro "Mostrar valor original total na validação de inadimplência" **marcado**. O sistema identificará os lançamentos vencidos do aluno e será calculado o valor líquido para cada lançamento vencido. A cada cálculo de valor líquido, o valor calculado será somado com os valores líquidos calculados anteriormente e será comparado com o valor informado no parâmetro "Valor máximo de tolerância para inadimplência". Se o valor líquido total calculado for maior do que o valor máximo de tolerância para inadimplência, o sistema considerará o aluno inadimplente e mostrará os lançamentos vencidos do aluno e, no final da mensagem de validação, será exibido o "Valor total original " que será a soma dos valores originais dos lançamentos vencidos. Após a constatação de inadimplência a partir do cálculo de um lançamento, os outros lançamentos existentes não terão seu respectivo valor líquido calculado.  
  
**Exemplo**:

Aluno: ANDRE LUIZ  
Lançamentos vencidos:   
     L1 - R$ 151,80  
     L2 - R$ 151,80  
     L3 - R$ 151,80  
Valor total original: R$ 455,40  
Valor líquido de cada lançamento: R$ 160,00  
Valor máximo de tolerância para inadimplência: R$ 100,00  
  
O sistema irá calcular o valor líquido do primeiro lançamento e comparar com o valor máximo de tolerância para inadimplência. Como o valor líquido é maior, o sistema não calculará o valor líquido dos lançamentos L2 e L3 e emitirá a mensagem de validação abaixo:
