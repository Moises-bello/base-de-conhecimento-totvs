---
content_hash: 23a67ef4c60f040e8bcd3393d15a4c51591cdb8cdc90a08e02f57f800e9a3a6a
fetched_at: '2026-06-29T00:08:36.885967+00:00'
page_id: '284480543'
product: rm
source: tdn-rm
title: 95448 CONTROLADORIA01-51 DT Importação de Avaliação Patrimonial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284480543
version: 103
---

# Importação de avaliação patrimonial

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Avaliação patrimonial |
| **Situação/Requisito:** | O cliente possui bens que necessitam ser importados e possuem avaliação. |
| **Solução/Implementação:** | Para possibilitar a importação de avaliações patrimoniais foi necessário realizas as seguintes alterações no processo:  1 - As mensagens do log sofreram algumas melhorias. 2 - O botão "Executar novamente" foi removido do processo de importação de avaliações patrimoniais. 3 - Foi criada uma validação para impedir a criação de avaliações negativas. Esta situação ocorria quando o patrimônio existente no arquivo possuía um valor de mercado inferior ao valor base corrigido. 4 - Ao realizar a importação da avaliação, de patrimônios que não sofreram alteração na vida útil, estava sendo gerada uma revisão de vida útil. Foi necessário realizar algumas modificações para que revisão de vida útil seja realizada apenas quando a quantidade de meses, informada no arquivo de importação, for menor ou superior a do patrimônio existente na base de dados. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados**: | N/A |
| **Requisito (informe o requisito relacionado):** | N/A |

divs
