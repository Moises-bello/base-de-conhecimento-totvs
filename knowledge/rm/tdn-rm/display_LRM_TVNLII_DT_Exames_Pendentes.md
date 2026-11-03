---
content_hash: 2b30213919f8a95046d09d35f3fe7b4b62f891c779df2bf0e0af90927e584350
fetched_at: '2026-06-29T00:08:17.702927+00:00'
page_id: '257623269'
product: rm
source: tdn-rm
title: TVNLII_DT_Exames_Pendentes
type: documentation
url: https://tdn.totvs.com/display/LRM/TVNLII_DT_Exames_Pendentes
version: 114
---

# EXAMES PENDENTES

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Segurança e Saúde Ocupacional |
| **Função:** | Exames Pendentes |
| **Situação/Requisito:** | Ao gerar exames pendentes, o sistema está colocando a data do próximo exame, considerando a data de vinculação do perfil de exames. Se o exame é excluído e gerado novamente, é gerado com outra data. |
| **Solução/Implementação:** | Foi realizado ajuste na geração de Exames Pendentes para que ao excluirmos um exame pendente de Mudança de Função e gerá-lo novamente o mesmo seja gerado como Mudança de Função novamente e não como Periódico como ocorria. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TVNLII |
| **Requisito (ISSUE):** |  |

divs
