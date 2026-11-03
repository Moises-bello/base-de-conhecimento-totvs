---
content_hash: 6a3e208b485bd2fcdfb1c0024f565f201b86de78fb54826c043b8d742fb63c5c
fetched_at: '2026-06-29T00:06:25.500165+00:00'
page_id: '224398081'
product: rm
source: tdn-rm
title: TUBDGP_DT_HomologNet_VRBaseCalculo
type: documentation
url: https://tdn.totvs.com/display/LRM/TUBDGP_DT_HomologNet_VRBaseCalculo
version: 122
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
| **Chamados relacionados:** | TUBDGP |

divs
