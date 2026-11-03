---
content_hash: 8a5cad6ebb077f9fc4902da0cee41ceb6c5ebc2b980a47a1c84d6a1e482c335d
fetched_at: '2026-06-29T00:08:07.710530+00:00'
page_id: '237385404'
product: rm
source: tdn-rm
title: TUUQN9_DT_Avaliacao_De_Conhecimento
type: documentation
url: https://tdn.totvs.com/display/LRM/TUUQN9_DT_Avaliacao_De_Conhecimento
version: 120
---

# AVALIAÇÃO DE CONHECIMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Pessoas |
| **Função:** | Avaliação de Conhecimento |
| **Situação/Requisito:** | Ao acessar o cadastro de Turmas, no Vitae, ir em Anexo>Avaliação de Conhecimento>Anexo>Avaliados, e tentar excluir um candidato que já tenha tido inscrição para prova no RMTestis gerada, ocorre o erro: Classe não encontrada: TstExportacaoProva. |
| **Solução/Implementação:** | Realizado ajuste na Avaliação de Conhecimento de forma que a rotina de exclusão de Avaliados utilize o serviço correto do Educacional. Pois os serviços tiveram seus nomes alterados:  De: TstExportacaoProva -> Para: TstExportacaoProvaMod  De: TstProvasService -> Para: TstProvasServiceMod |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUUQN9, TUXXM9, TUZN79 |
| **Requisito (ISSUE):** |  |

divs
