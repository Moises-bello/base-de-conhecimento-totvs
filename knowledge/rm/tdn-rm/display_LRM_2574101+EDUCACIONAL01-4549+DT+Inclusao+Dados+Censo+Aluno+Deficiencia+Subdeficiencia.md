---
content_hash: 192aeadb3fbcaded9b44f401fafdd12e12eac3904f23be88a065ade3fd1a5ea0
fetched_at: '2026-06-29T00:08:57.000607+00:00'
page_id: '351390021'
product: rm
source: tdn-rm
title: 2574101 EDUCACIONAL01-4549 DT Inclusao Dados Censo Aluno Deficiencia Subdeficiencia
type: documentation
url: https://tdn.totvs.com/display/LRM/2574101+EDUCACIONAL01-4549+DT+Inclusao+Dados+Censo+Aluno+Deficiencia+Subdeficiencia
version: 88
---

# INCLUSÃO DE DADOS DO CENSO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Inclusão de dados do Censo |
| **Situação/Requisito:** | Foi identificado uma inconsistência ao salvar os dados do censo escolar quando o aluno possui alguma deficiência informada. |
| **Solução/Implementação:** | Foi identificado uma inconsistência no método salvar do cadastro de pessoa que tenta apagar as deficiências para inserir novamente sempre que existir uma alteração, porem como a alteração é um dataset de detalhe e não no cadastro da pessoa o sistema não apaga as deficiências, porém tenta inserir novamente, sendo assim, quando ocorrer este tipo de alteração definimos o cadastro de pessoa como alterado, assim sempre que chegar ao método salvar do cadastro de pessoa o sistema irá persistir a informação corretamente. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
