---
content_hash: 499a8ee93015429702140d25b7cdc55e5e74048e392d1764843f62c6e7721669
fetched_at: '2026-06-29T00:06:14.481682+00:00'
page_id: '210046454'
product: rm
source: tdn-rm
title: TTNAG7_DT_Propagacao_Professor_No_Horario_De_Turmas_Gerenciais_Para_Turmas_Gerenciadas
type: documentation
url: https://tdn.totvs.com/display/LRM/TTNAG7_DT_Propagacao_Professor_No_Horario_De_Turmas_Gerenciais_Para_Turmas_Gerenciadas
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
| **Versões/Release:** | *12.1.8.* |
| **Versão Corrigida:** | *12.1.8.* |
| **Versão Expedida:** | *12.1.8.* |

divs
