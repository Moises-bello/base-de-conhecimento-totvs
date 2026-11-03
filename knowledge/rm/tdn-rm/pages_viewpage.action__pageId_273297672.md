---
content_hash: b96580d79be02c05aa373cb0d0c991f2d3ddb009a026c4c03ef9c547afb7693f
fetched_at: '2026-06-29T00:08:31.261865+00:00'
page_id: '273297672'
product: rm
source: tdn-rm
title: 717774 EDUCACIONAL01-67 DT CENSO - Professores que deveriam aparecer no arquivo
  não aparecem
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273297672
version: 112
---

# Censo Ensino Superior

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Geração do Censo - Censo da Educação Superior - Docente |
| **Situação/Requisito:** | * Alguns professores não estavam sendo geados no arquivo * O campo "Naturalidade" do cadastro do professor não estava correto na geração do arquivo |
| **Solução/Implementação:** | Ao gerar o arquivo do censo correspondente a  "Censup - Censo da Educação Superior - Docente - Registro 31 - 32", o sistema não estava gerando as informações correspondente ao professor em que  a data de término esteja sem preencher (informações do professor vinculado a turma/disciplina).  Ao gerar o arquivo do censo correspondente a  "Censup - Censo da Educação Superior - Docente - Registro 31 - 32", o sistema não estava considerando as informações do campo "Naturalidade" e sim "Cidade".  Realizamos um ajuste para considerar o campo "Naturalidade". |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** | 717774 |
| **Requisito:** |  |

divs
