---
content_hash: 5632d96d9c348ab75fe360f9d21a7cc569230f2e4e5ba9320125ff4039789b39
fetched_at: '2026-06-29T00:08:17.915845+00:00'
page_id: '259560084'
product: rm
source: tdn-rm
title: TVSGIX_DT_BolsaRetroativa_Sem_Par_Pag_Maior_PagMenor
type: documentation
url: https://tdn.totvs.com/display/LRM/TVSGIX_DT_BolsaRetroativa_Sem_Par_Pag_Maior_PagMenor
version: 114
---

# Bolsa Retroativa

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Bolsa Retroativa |
| **Situação/Requisito:** | Ao executar o processo de bolsa retroativa esta sendo apresentada a mensagem abaixo:  Valor que está sendo baixado para o Lançamento Coligada 1 | IdLan = 3168336  é maior que o valor líquido. Valor Baixado 1042,13 | Valor Líquido 521,07  Esta mensagem é apresentada porque o sistema não estava parametrizado para identificar os campos de valores opcionais que controlam o pagamento a maior e pagamento a menor. |
| **Solução/Implementação:** | Implementada uma evolução na inclusão da bolsa retroativa para que valide se a parametrização do campo opcional de pagamento a maior ou a menor está preenchida. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | TVSGIX |
| **Requisito (ISSUE):** | *N/A* |

divs
