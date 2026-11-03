---
content_hash: 4cc2f36ab6ecdbf9e1677b0e2925d7606bc74887cb3ca949cbead0bb5a0745cc
fetched_at: '2026-06-29T00:08:45.826939+00:00'
page_id: '315899999'
product: rm
source: tdn-rm
title: 1352610 FINANCEIRO01-2618 Truncar histórico de cheque
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=315899999
version: 95
---

# TRUNCAR HISTÓRICO DE CHEQUE

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Emissão/Recebimento de cheque. |
| **Situação/Requisito:** | Quando sistema está parametrizado com histórico default para cheque, ao montar o mesmo de acordo com as variáveis informadas, caso o tamanho ultrapasse 255 caracteres o valor é exibido na tela e ocorre uma inconsistência ao avançar o processo impedindo sua execução. |
| **Solução/Implementação:** | Caso o histórico de cheque montado de acordo com o default parametrizado ultrapasse o tamanho máximo (255 caracteres) o valor será truncado descartando os caracteres a partir da posição 256. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | 1352610. |
| **Requisito:** | FINANCEIRO01-2618. |

divs
