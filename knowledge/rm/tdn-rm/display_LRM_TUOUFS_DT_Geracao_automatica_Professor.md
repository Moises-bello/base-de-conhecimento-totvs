---
content_hash: 4ed01f961408a4ca1a687288b80ca22690aac79be42bdd557c730ddaf92eac42
fetched_at: '2026-06-29T00:08:04.755053+00:00'
page_id: '235580884'
product: rm
source: tdn-rm
title: TUOUFS_DT_Geracao_automatica_Professor
type: documentation
url: https://tdn.totvs.com/display/LRM/TUOUFS_DT_Geracao_automatica_Professor
version: 117
---

# Geração automática de usuário para professores

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Educacional* |
| **Módulo:** | *Classis.NET* |
| **Função:** | *Geração de usuários* |
| **Situação/Requisito:** | *Geração automática de usuários para profeossor* |
| **Solução/Implementação:** | *Foi realizado uma melhoria no processo de geração automática de usuários de professores em banco de dados Oracle.*  *O processo de geração de usuário automática para professores é acionado logo após a inclusão do registro de professor. Ao ser realizado a chamada do processo de geração automática de usuários, o sistema realiza novas consultas para buscar informações adicionais do usuário que será gerado. Quando é utilizado o SQL Server o sistema realiza uma "consulta suja", no qual consegue realizar a busca das informações no banco antes mesmo da transação de inclusão do Professor tenha sido concluída.*  *Isso não ocorre quando é utilizado banco de dados Oracle, onde neste caso a geração de usuários não era realizada por não ser retornado as informações necessárias.*  *Foi realizado uma melhoria para que este processo seja chamado somente após a conclusão da transação de inclusão de professor.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
