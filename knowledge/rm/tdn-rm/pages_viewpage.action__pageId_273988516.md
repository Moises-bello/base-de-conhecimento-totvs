---
content_hash: 8dc24974a7ffc0004692853c5b13267360e98686cb1d3caa4f7501a316abcafa
fetched_at: '2026-06-29T00:08:32.471828+00:00'
page_id: '273988516'
product: rm
source: tdn-rm
title: 691270 EDUCACIONAL01-242 DT Contabilização com valores de diferenças inferiores
  a 0,01
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273988516
version: 106
---

# Contabilização

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Contabilização |
| **Situação/Requisito:** | Ao executar o processo de contabilização esta apresentando a mensagem abaixo.  Não foi possível gerar a contabilização para o contrato 123383. Não foi possível carregar as partidas contábeis do evento de cancelamento de contrato 138  A parametrização dos eventos contábeis estão corretas |
| **Solução/Implementação:** | O processo de contabilização do novo modelo contabiliza as diferenças que podem ocorrer no contrato (aumento ou redução) e em função de arredondamento o processo estava identificando um valor de diferença muito baixo, exemplo, -0,00120, e neste caso o sistema estava acionando o evento contábil para processar a redução no contrato.  O módulo contábil trabalha com duas casas decimais e neste caso após aplicar o arredondamento no valor de -0,00120 teremos 0,00, portando o evento contábil não vai processar nenhum valor.  Realizado uma melhoria para que seja processado valor maior ou igual a 0,01. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | 691270 |
| **Requisito:** | N/A |

divs
