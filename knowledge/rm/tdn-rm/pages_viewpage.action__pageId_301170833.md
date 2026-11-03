---
content_hash: c9e1a44cd4a7065d71572b589c9d7ae2e1d97527df772d37dc9a1c3852e04991
fetched_at: '2026-06-29T00:08:42.886423+00:00'
page_id: '301170833'
product: rm
source: tdn-rm
title: CONTROLADORIA01-537 DT Gerador de Saída
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=301170833
version: 94
---

# Gerador de saída

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Gerador de saída |
| **Situação/Requisito:** | Por motivos de compatibilização com o legado foi necessário fazer alguns ajustes em relação ao desacoplamento do Gerador de Saídas. Para acertar as quebras de build será necessário adicionar as novas referências das DLLs do TNF e alterar a classe RuntimeModule para RMSRuntimeModule. |
| **Solução/Implementação:** | Em função do desacoplamento do gerador de saídas foi necessário adicionar as referencias das DLLs do TNF (TNF.Gen.Engine e TFN.Gen.Runtime). Esta alteração foi solicitada pela equipe de framework. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados**: | N/A |
| **Requisito (informe o requisito relacionado):** | N/A |

divs
