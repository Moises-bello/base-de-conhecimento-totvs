---
content_hash: ac2df9fc43de2f19f967893eb98cd52eb1c36b301990a714a178ce9836cb6586
fetched_at: '2026-06-29T00:08:32.657218+00:00'
page_id: '273994327'
product: rm
source: tdn-rm
title: 695885 EDUCACIONAL01-303 DT Erro ao baixar automaticamente lançamento com valor
  líquido igual a zero
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273994327
version: 105
---

# CADASTRO DE BOLSAS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional. |
| **Função:** | Cadastro de bolsas |
| **Situação/Requisito:** | Ao gerar um lançamento financeiro, o sistema ajusta os valores opcionais de bolsas do lançamento afim de evitar que a soma de todos os descontos concedidos no educacional ultrapasse o valor original do lançamento. Com isso, diferenças de frações de centavos podem existir entre a soma de todas as bolsas condicionais e o valor opcional de bolsas condicionais do lançamento financeiro. Com isso, caso o lançamento tenha valor líquido igual a zero, o sistema não consegue realizar a baixa automática se o valor total das bolsas condicionais for maior que o valor opcional de bolsas. |
| **Solução/Implementação:** | Foi realizada otimização do processo de geração de lançamentos financeiros, permitindo ao sistema, trabalhar com uma margem, em centavos, conforme a quantidade de bolsas condicionais, para poder considerar que o valor de bolsas condicionais sofreu aumento indevido, após a geração. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A. |

divs
