---
content_hash: 57b3228703a59784dfc360a1e816442b27cb9ea406a734a35c9bb4d220ff03a4
fetched_at: '2026-06-29T00:09:11.438681+00:00'
page_id: '403750087'
product: rm
source: tdn-rm
title: 3742862 DEDUINTEGRACOES-3314 DT Valor de multa negativo na geração de lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=403750087
version: 82
---

# GERAÇÃO DE LANÇAMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional. |
| **Função:** | Geração de lançamentos |
| **Situação/Requisito:** | Ao gerar lançamento com bolsa 100% cascateada com desconto concedido diretamente na parcela, caso o  desconto seja um valor arredondado para mais, o valor da bolsa será calculada com 1 centavo a mais do que o valor disponível. com isso, ao calcular o valor de multa desconsiderando o valor de bolsa e desconto, um valor negativo próximo de zero será encontrado fazendo com que o sistema valide a impossibilidade de gerar um lançamento com valor de multa negativo. |
| **Solução/Implementação:** | Foi realizada otimização do processo de geração de lançamentos, de forma que o sistema, ao calcular o valor de uma bolsa em cascata com um desconto, considere o valor de desconto arredondado para a formação do valor base para a aplicação da bolsa. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A. |

divs
