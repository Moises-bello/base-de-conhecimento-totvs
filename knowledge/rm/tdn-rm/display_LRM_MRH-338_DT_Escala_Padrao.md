---
content_hash: a168d35aa20b7ae99cbf6a7311b040a0bd741880cb4f2ea61b35dfaa69d8973b
fetched_at: '2026-06-29T00:08:23.399763+00:00'
page_id: '270084556'
product: rm
source: tdn-rm
title: MRH-338_DT_Escala_Padrao
type: documentation
url: https://tdn.totvs.com/display/LRM/MRH-338_DT_Escala_Padrao
version: 110
---

# ESCALA PADRÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Pessoas |
| **Função:** | Escala Padrão |
| **Situação/Requisito:** | Ao tentar cadastrar uma nova escala padrão, o sistema apresentava uma mensagem informando que o campo "Cód Definição Escala" não poderia ser nulo, mas este campo não estava visível para preenchimento. |
| **Solução/Implementação:** | Foi verificado que esta tela (Escalas) na verdade se trata de um anexo, e o campo "Cód Definição Escala" se refere ao registro da tela principal (Escala Padrão). O erro ocorria pois o sistema estava permitindo abrir o anexo sem abrir a tela principal. Foi feita implementação para abrir o anexo somente após abrir a tela principal. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | MRH-338 |
| **Requisito (ISSUE):** |  |

divs
