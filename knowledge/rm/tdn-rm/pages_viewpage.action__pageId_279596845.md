---
content_hash: 866c3dd849e75f81160b21282d83412d2c400461bfb5880b154e239185281eb1
fetched_at: '2026-06-29T00:08:35.388286+00:00'
page_id: '279596845'
product: rm
source: tdn-rm
title: 751376 EDUCACIONAL01-236 DT Exclusão de Matrícula no Período Letivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=279596845
version: 108
---

# EXCLUSÃO DE MATRÍCULA NO PERÍODO LETIVO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Exclusão de Matrícula no Período Letivo* |
| **Situação/Requisito:** | *Mesmo como a parametrização do perfil Educacional marcado para "Excluir matrícula com movimentação", o sistema impede a exclusão de matrícula em disciplinas caso exista frequência / etapa preenchida.* |
| **Solução/Implementação:** | *Alteração do nome do parâmetro de "Excluir matrícula com movimentação" para "Permitir excluir matrícula no período letivo com movimentação em notas e frequência" nos parâmetros Educacionais do perfil do usuário. Além disso, foi incluído a validação da frequência diária digitada na exclusão, ou seja, o se o aluno possuir alguma falta lançada pela frequência diária e este parâmetro não estiver marcado, seja bloqueado a exclusão. Foi incluído também a validação da frequência diária na exclusão da matrícula em disciplina no parâmetro "Bloqueia a exclusão de disciplina do aluno caso haja notas e/ou faltas digitadas" em Configurações | Parâmetros | Matrícula | Movimento 1/4.* |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
