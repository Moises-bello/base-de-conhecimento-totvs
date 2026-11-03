---
content_hash: b04b8d5bdf4303debcfca19df67786de96113b0c847765ac871dab495bfbb426
fetched_at: '2026-06-29T00:08:27.425904+00:00'
page_id: '271411823'
product: rm
source: tdn-rm
title: 420214 MEDU-2264 DT  Cadastro de Turma-disciplina/Avaliações com código de
  prova zero
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271411823
version: 110
---

# AVALIAÇÕES

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Função:** | *Avaliações* |
| **Situação/Requisito:** | No cadastro de Turma/Disciplina, anexo Avaliações, o sistema não está permitindo inserir código de prova igual a zero. |
| **Solução/Implementação:** | Otimizado validação do cadastro de Avaliações para permitir que o código da prova permita digitar zero.  *Caso algum cliente queira especificamente bloquear o valor zero para o campo código da prova, deverá utilizar uma fórmula visual para emitir a mensagem de erro.*  A alteração afetará o cadastro de avaliações na Turma/Disciplina e no Período Letivo/ Modelo de avaliações por período letivo. |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |

divs
