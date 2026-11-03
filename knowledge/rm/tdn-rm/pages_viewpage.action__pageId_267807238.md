---
content_hash: 13ec0abdc3efb45bbf32ac6779419a8515ec4505f7906b4e51c495cbf4dad690
fetched_at: '2026-06-29T00:08:20.004712+00:00'
page_id: '267807238'
product: rm
source: tdn-rm
title: TVXMU2_DT_Baixa_Lançamento_Com_Bolsa_Condicional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267807238
version: 113
---

# Serviço de Validação Baixa de Lançamento do Educacional

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Validação dos valores de bolsa do educacional na baixa do lançamento no financeiro |
| **Situação/Requisito:** | Ao realizar a baixa de um lançamento proveniente do TOTVS Educacional que possui Bolsa Condicional,  a mensagem abaixo está sendo exibida, impedindo a conclusão da operação:  O valor da bolsa condicional calculado na baixa do lançamento está maior que o valor calculado para esta bolsa quando o lançamento foi gerado.  Valor da bolsa na geração: 18,27 Valor da bolsa na baixa: 54,07  Recomendamos que o lançamento seja regerado no Educacional para que o valor das bolsas condicionais seja atualizado no lançamento.  Caso esta mensagem seja apresentada novamente e o valor de bolsa condicional esteja sendo processado por fórmula favor revisar a mesma.    O sistema não deveria considerar o valor apresentado na mensagem e sim o valor preenchido no campo Bolsas Condicionais. |
| **Solução/Implementação:** | Melhoria na validação da baixa de um lançamento financeiro que possui bolsa condicional.  É validado se o valor da bolsa condicional da baixa está conforme o valor da bolsa condicional identificado na geração do lançamento. Esta validação não estava considerando o valor opcional de bolsa condicional parametrizado no educacional. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | TVXMU2 |
| **Requisito (ISSUE):** | *N/A* |

divs
