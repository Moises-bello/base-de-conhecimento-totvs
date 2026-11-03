---
content_hash: 2b7377d0cfa5b11d2cec429f6f7cdfde5e519f4aa3d170f79546e0a09d2ef17c
fetched_at: '2026-06-29T00:08:22.687298+00:00'
page_id: '269437001'
product: rm
source: tdn-rm
title: 122833_DT_Solicitações_Via_Exe_Parcela_Extra_Data_Competência_Contabilização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269437001
version: 115
---

# Solicitações Aluno (Exe)

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Solicitações do aluno gerando parcela extra |
| **Situação/Requisito:** | A inclusão de uma solicitação via exe está exibindo a mensagem de erro abaixo:  Erro na criação do lançamento. Mensagem: Não foi possível setar a data de contabilização do lançamento de acordo com a data de competência da parcela |
| **Solução/Implementação:** | Realizamos um ajuste na geração da parcela proveniente das solicitações via exe para que o tipo contábil da parcela seja setado de acordo com os parâmetros de integração com o financeiro (geração de lançamentos) e data de competência da parcela seja preenchida conforme a data de vencimento.  Isto somente irá acontecer se o serviço vinculado a parcela for do tipo contábil e o educacional estiver parametrizado para considerar a data da competência como data de contabilização. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | MEDU-1055 |

divs
