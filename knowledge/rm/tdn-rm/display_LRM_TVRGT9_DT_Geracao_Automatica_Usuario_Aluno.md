---
content_hash: 1b6f2ba30d17d6dff5ff3d9b9781e9b353a618d19ae29b8dc0762e5577467da3
fetched_at: '2026-06-29T00:08:17.122613+00:00'
page_id: '253986411'
product: rm
source: tdn-rm
title: TVRGT9_DT_Geracao_Automatica_Usuario_Aluno
type: documentation
url: https://tdn.totvs.com/display/LRM/TVRGT9_DT_Geracao_Automatica_Usuario_Aluno
version: 112
---

# GERAÇÃO AUTOMÁTICA DE USUÁRIO - ALUNO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Geração Automática de Usuário - Aluno* |
| **Situação/Requisito:** | *Ao tentarmos executar o método SaveRecord do DataServer "EduFrequenciaDiariaWSData" retorna "Você não está autorizado a inserir registros!", mesmo com o usuário podendo executar tal ação pelo sistema ou pelo portal.* |
| **Solução/Implementação:** | *Ajuste para remover o parâmetro "Gerar usuários para alunos sem matrícula no período letivo" do parametrizador de geração de usuário automático para alunos. Ou seja, a geração automática de usuário para aluno será executada o aluno possuindo matrícula ou não.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
