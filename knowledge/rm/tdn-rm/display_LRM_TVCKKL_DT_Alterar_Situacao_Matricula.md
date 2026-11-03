---
content_hash: 14e9afc25c67f18688c4d8ab0e2b1d4b70ae87f52b76c115b5d3e6e5d930af82
fetched_at: '2026-06-29T00:08:12.725267+00:00'
page_id: '243647458'
product: rm
source: tdn-rm
title: TVCKKL_DT_Alterar_Situacao_Matricula
type: documentation
url: https://tdn.totvs.com/display/LRM/TVCKKL_DT_Alterar_Situacao_Matricula
version: 119
---

# SITUAÇÃO DE MATRÍCULA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Educacional.* |
| **Módulo:** | *TOTVS Gestão Educacional.* |
| **Função:** | *Processo para alterar situação de matrícula na disciplina.* |
| **Situação/Requisito:** | *Quando a nova situação de matrícula do aluno estava parametrizada para bloquear a alteração da situação de matrícula o sistema emitia uma mensagem informando o usuário do bloqueio e só permitia a alteração, caso o usuário tivesse permissões especiais.* |
| **Solução/Implementação:** | *Durante o processo de alteração de situação de matrícula, o bloqueio da alteração só deve ocorre, caso a situação de matrícula atual esteja parametrizada para que realizar o bloqueio da alteração. Desta forma, este parâmetro só será avaliado na situação de matrícula atual e não na nova situação de matrícula na disciplina.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *TVEXMY.* |
| **Requisito (ISSUE):** | *N/A.* |

divs
