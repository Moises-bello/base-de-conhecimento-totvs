---
content_hash: 5db6f48eca2a021217235850eb4d4930647827e7a45a212fec4487555a6496cc
fetched_at: '2026-06-29T00:08:30.182162+00:00'
page_id: '272408728'
product: rm
source: tdn-rm
title: 511039 MRH-8047 DT Codigo_Pagamento_GPS
type: documentation
url: https://tdn.totvs.com/display/LRM/511039+MRH-8047+DT+Codigo_Pagamento_GPS
version: 108
---

# CÓDIGO DE PAGAMENTO GPS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projeto |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Guia de INSS. |
| **Situação/Requisito:** | Ao gerar a Guia de INSS por Tomador, o produto deveria levar o Código de Pagamento que for preenchido no parâmetro código de pagamento para o Administrativo e o Código de Pagamento cadastrado dentro do cadastro do cliente/fornecedor para o Tomador Obra CEI porém o sistema estava levando o código de pagamento preenchido para todos os tomadores. |
| **Solução/Implementação:** | Foi ajustado o sistema para para que no momento em que o parâmetro de código de pagamento for preenchido e o tomador for o administrativo o sistema respeite o parâmetro preenchido porém para os demais tomadores o sistema respeite o cadastro de cliente/fornecedor. |
| **Tickets relacionados:** | * 511039 |

divs
