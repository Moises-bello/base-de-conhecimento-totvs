---
content_hash: 2e6a967329a8c8fd99573f70fe8cac9b25322a058f91d2912f06d986a5c10e53
fetched_at: '2026-06-29T00:08:20.052087+00:00'
page_id: '267810178'
product: rm
source: tdn-rm
title: TVUKOH_DT_Copiar_TurmasDisciplina_Nao_Copia_Campos
type: documentation
url: https://tdn.totvs.com/display/LRM/TVUKOH_DT_Copiar_TurmasDisciplina_Nao_Copia_Campos
version: 115
---

# TURMAS - COPIAR TURMAS ENTRE PERÍODO LETIVO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Turmas - copiar turmas entre período letivo* |
| **Situação/Requisito:** | *Aao executar o processo "Copiar turmas entre período letivo", as turmas/disciplinas copiadas pelo processo não tem os campos 'Nº mínimo de alunos', 'Nº máx. alunos outras mtz. aplicadas' e 'Número de aulas' copiados das turmas/disciplinas originais, mesmo estes campos estando preenchidos.* |
| **Solução/Implementação:** | *Foi identificado que ao carregar os dados para a cópia das turmas/disciplinas, os dados dos campos 'Nº mínimo de alunos', 'Nº máx. alunos outras mtz. aplicadas' e 'Número de aulas' não eram carregados das turmas/disciplinas originais, e por conseqüência não eram copiados. Foi feito o ajuste na função que carrega os dados das turmas/disciplinas disciplinas de origem para que carregue os dados que estão faltando, assim ao finalizar o processo todos os dados são copiados com sucesso.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
