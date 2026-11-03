---
content_hash: e07bcb5243d96e1b9846f5b4702669834c08a32af9a4212038e4ec089eb0d022
fetched_at: '2026-06-29T00:08:18.843711+00:00'
page_id: '266970900'
product: rm
source: tdn-rm
title: TVQTIX_DT_Turma_Gerencial_Gerenciada
type: documentation
url: https://tdn.totvs.com/display/LRM/TVQTIX_DT_Turma_Gerencial_Gerenciada
version: 111
---

# CADASTRO DE TURMAS/DISCIPLINAS GERENCIADAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Função:** | *Cadastro de turmas/disciplinas gerenciadas* |
| **Situação/Requisito:** | *Ao realizar um cadastro de uma turma/disciplina gerenciada o sistema estava apresentando mensagem de validação de igualdade de campos incorretamente.* |
| **Solução/Implementação:** | *Foi identificado que ao cadastrar uma etapa de uma turma/disciplina, o campo Etapa Final era gravado com o valor Nulo, quando não alterado.*  *Isso gerava um validação incorreta ao cadastrar uma turma gerenciada.*  *Um valor padrão foi definido ao campo e um acerto foi realizado na validação para considerar o valor nulo do campo de etapa final.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |

divs
