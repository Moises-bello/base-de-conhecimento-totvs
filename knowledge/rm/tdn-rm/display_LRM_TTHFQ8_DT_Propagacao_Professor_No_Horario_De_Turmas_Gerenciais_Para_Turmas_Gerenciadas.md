---
content_hash: b883bb4d0f2ad9bfa5ff906e222c22ee9fdbc610529093b20f67b89d59aa19ec
fetched_at: '2026-06-29T00:06:14.461369+00:00'
page_id: '210045946'
product: rm
source: tdn-rm
title: TTHFQ8_DT_Propagacao_Professor_No_Horario_De_Turmas_Gerenciais_Para_Turmas_Gerenciadas
type: documentation
url: https://tdn.totvs.com/display/LRM/TTHFQ8_DT_Propagacao_Professor_No_Horario_De_Turmas_Gerenciais_Para_Turmas_Gerenciadas
version: 1
---

# PROFESSOR DO HORARIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Educacional.* |
| **Módulo:** | *TOTVS Gestão Educacional.* |
| **Função:** | *Professor do horário.* |
| **Situação/Requisito:** | *Na replicação de professores de horários para turmas disciplinas gerenciadas, as queries que recuperam os dados do professor e do horário não*  *levam* *em consideração a coligada, fazendo com que recuperem dados inconsistentes, causando erro de violação de chave estrangeira na inserção*  *dos mesmos.* |
| **Solução/Implementação:** | *Inclusão de filtro pela coligada nas queries que recuperam os dados do professor e do horário para a inserção correta.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *11.82.42.* |
| **Versão Corrigida:** | *11.82.41.* |
| **Versão Expedida:** | *11.82.41.* |

divs
