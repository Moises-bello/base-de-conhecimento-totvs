---
content_hash: 437082fa1ba564e750d781d2534ab36c78e07196bdea5ea6eabea51ae3538d49
fetched_at: '2026-06-29T00:06:25.503354+00:00'
page_id: '224398206'
product: rm
source: tdn-rm
title: TUEZGY_DT_HomologNet_VRBaseCalculo
type: documentation
url: https://tdn.totvs.com/display/LRM/TUEZGY_DT_HomologNet_VRBaseCalculo
version: 119
---

# VALOR BASE CALCULO QUANDO O TIPO DE CÓDIGO DE CÁLCULO FOR IGUAL A 22 - INSALUBRIDADE

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção* *e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Gerar o valor da tag VLBaseCalculo para o tipo de rubrica igual a 013 quando o código de cálculo for igual a 22 considerando o salário mínimo* |
| **Situação/Requisito:** | Ao lançar um evento que seja de insalubridade com rubrica 013 na rescisão do funcionário e gerar o Homolognet o sistema busca o valor do salário nominal do funcionário para preencher a base de cálculo da insalubridade desconsiderando o valor do salário mínimo conforme código de cálculo 22 que utilizada o mínimo como base para insalubridade e leva informação incorreta para o xml. |
| **Solução/Implementação:** | *Realizado a verificação quando o tipo de rubrica for igual a 013 e o código de cálculo for igual a 22 - Insalubridade, considerar o valor do salário mínimo cadastrado no sindicato para o cálculo da tag <VLBaseCalculo> do HomologNet.* |
| **Chamados relacionados:** | TUEZGY, TUBDGP |

divs
