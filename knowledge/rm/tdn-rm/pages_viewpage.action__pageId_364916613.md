---
content_hash: fe17d4dce83627e3fc48be69fe933bc172f0e525e67606e186219a831f719bfc
fetched_at: '2026-06-29T00:08:59.807757+00:00'
page_id: '364916613'
product: rm
source: tdn-rm
title: 2487201 EDUCACIONAL01-4383 DT Desenturmação com movimentação (Notas/Faltas
  ou Frequência)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364916613
version: 3
---

# DESENTURMAÇÃO COM MOVIMENTAÇÃO (NOTAS/FALTAS E FREQUÊNCIA)

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Desenturmação com movimentação (Notas/Faltas ou Frequência) |
| **Situação/Requisito:** | Ao realizar o processo de Desenturmação o sistema avisa que todas as notas e faltas serão perdidas e se o usuário deseja continuar. O usuário informa que sim, porém o sistema ainda sim emite o erro dizendo que não é possível a desenturmação pelo fato de existirem notas e faltas digitadas. |
| **Solução/Implementação:** | Ajuste na mensagem quando executa-se uma desenturmação, para que quando se tem permissão especial em excluir matrícula com movimentação (notas/faltas) a seguinte mensagem será exibida: "Todas as notas, faltas, conceitos e frequência do(s) aluno(s) serão perdidos. Deseja continuar?". Caso não tenha permissão a seguinte mensagem será exibida: "Alunos que possuam notas, faltas, conceitos ou frequência não serão desenturmados. Os que não se enquadram nesta situação serão desenturmados. Deseja continuar?". |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
