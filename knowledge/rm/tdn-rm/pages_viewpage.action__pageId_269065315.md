---
content_hash: ed92ed1430fbbf9e307926eeb18de8ae9578141e8c58b7d9988193bbadbd3785
fetched_at: '2026-06-29T00:08:21.662852+00:00'
page_id: '269065315'
product: rm
source: tdn-rm
title: 169962_AbaFinanceiro_MatriculaProcessoSeletivo_Competência_Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269065315
version: 110
---

# Matricula via processo seletivo

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacionaal |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Matricula via processo seletivo |
| **Situação/Requisito:** | O cliente informa que no momento de fazer a matrícula de um aluno aprovado via processo seletivo (Matrícula e Avaliação -> Matrícula -> Processo Seletivo RM), caso se selecione uma situação de matrícula no período letivo que exija contrato financeiro e exija que a competência contábil esteja preenchida, o botão avançar esta ficando habilitado mesmo não preenchendo a competência, isto ocorre somente se o usuário marcar a opção "Cadastrar contrato", preencher a competência contábil e depois desmarcar a opção "Cadastrar contrato". |
| **Solução/Implementação:** | Ao realizar uma matricula via processo seletivo (Matrícula e Avaliação -> Matrícula -> Processo Seletivo RM) realizamos uma melhoria para que o botão avançar não fique habilitado  indevidamente caso a competência contábil não esteja preenchida (isto se o sistema estiver parametrizado para utilizar a data da competência do contrato como data de contabilização). |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | ISSUE: MEDU-930 |
| **Requisito (ISSUE):** |  |

divs
