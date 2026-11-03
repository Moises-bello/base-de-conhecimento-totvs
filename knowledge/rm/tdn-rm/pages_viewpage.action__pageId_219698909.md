---
content_hash: bc8ac07ec04ab3cea3f7eecfee9bca6ca1061647b8c84710800d057476d6833e
fetched_at: '2026-06-29T00:06:19.547504+00:00'
page_id: '219698909'
product: rm
source: tdn-rm
title: TTSML4_DT_Gerar_Contabilizacao_Contrato_100%_Estornado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=219698909
version: 1
---

# GERAR CONTABILIZACAO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Educacional.* |
| **Módulo:** | *TOTVS Gestão Educacional.* |
| **Função:** | *Gerar Contabilização.* |
| **Situação/Requisito:** | *Erro de referência de objeto ao gerar contabilização de contrato 100% estornado e que já exista contabilidade no lote zero. Isto ocorre devido ausência*  *de validação na inserção de serviços nas parcelas contábeis, que não deveria levar em consideração as parcelas estornadas.* |
| **Solução/Implementação:** | *Incluir validação do status (StatusCont == Contabilizacao) da parcela contábil ao inserir os serviços na mesma. Adicionalmente, para trazer a lista das*   *parcelas contábeis ordenadas, incluir um ORDER BY pelo campo SPARCELACONT.MESANO no método que recupera as mesmas.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *11.82.41.* |
| **Versão Corrigida:** | *11.82.41.* |
| **Versão Expedida:** | *11.82.41.* |

divs
