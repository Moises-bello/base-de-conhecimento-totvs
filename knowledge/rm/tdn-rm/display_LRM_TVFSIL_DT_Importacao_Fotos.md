---
content_hash: 40b8b9866e2fcdb042939e2eb561fb65592f6d691ee7234e14d5d39c485847fb
fetched_at: '2026-06-29T00:08:16.914101+00:00'
page_id: '248582529'
product: rm
source: tdn-rm
title: TVFSIL_DT_Importacao_Fotos
type: documentation
url: https://tdn.totvs.com/display/LRM/TVFSIL_DT_Importacao_Fotos
version: 112
---

# IMPORTAÇÃO DE FOTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projeto* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Importação de Fotos* |
| **Situação/Requisito:** | Quando utiliza-se arquitetura N Camadas e mapeamento de unidade de rede como caminho das fotos no client o server não reconhece o caminho informado ocasionando erro. |
| **Solução/Implementação:** | Ajuste na rotina de alteração de fotos para casos que utiliza arquitetura N Camadas para realizar a cópia das fotos em uma pasta temporária no server. Desta forma o server independe do caminho das fotos no client. |
| **Chamados relacionados:** | TVFSIL |

divs
