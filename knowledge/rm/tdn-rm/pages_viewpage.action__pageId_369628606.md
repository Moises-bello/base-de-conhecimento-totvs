---
content_hash: 3493c2d97ff489fb38b0e703e75a526bd8e825d258fe5d5f575c4de877ff7e78
fetched_at: '2026-06-29T00:09:00.848316+00:00'
page_id: '369628606'
product: rm
source: tdn-rm
title: 2277804 EDUCACIONAL01-4126 DT Cancelamento de Usuário do Biblios Através da
  Alteração da Situação de Matrícula
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=369628606
version: 1
---

# CANCELAMENTO DE USUÁRIO DO BIBLIOS ATRAVÉS DA ALTERAÇÃO DA SITUAÇÃO DE MATRÍCULA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Bibliotecária |
| **Função:** | Integração Educacional x Biblioteca |
| **Situação/Requisito:** | O Aluno X tem matricula nos cursos A e B e esses cursos tem matricula no período letivo Z. Ao realizar o cancelamento da matricula em apenas um dos períodos letivos, o sistema cancela o usuário da Biblioteca. |
| **Solução/Implementação:** | O sistema foi alterado para não cancelar o usuário do Biblios durante o processo de alteração da situação de matrícula se a pessoa possuir alguma matrícula em período letivo com status "ativo" e sem a opção de cancelar usuário do Biblios. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
