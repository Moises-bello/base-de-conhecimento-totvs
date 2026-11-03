---
content_hash: 8d08364014adce29258790ff6c784b6f51eabd50c5d10cf38dfd932f6d25e91e
fetched_at: '2026-06-29T00:09:09.775558+00:00'
page_id: '394201719'
product: rm
source: tdn-rm
title: 3589712 DEDUINTEGRACOES-3119 DT Cálculo de créditos para equivalências múltiplas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=394201719
version: 84
---

# GERAÇÃO DE LANÇAMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional. |
| **Função:** | Geração de lançamentos |
| **Situação/Requisito:** | Ao calcular os créditos financeiros com valores de crédito da matriz curricular do aluno, em caso de equivalência múltipla (mais de uma matrícula equivalendo a uma disciplina da grade), o sistema faz o cálculo apenas para a primeira disciplina equivalente matriculada, de forma que o sistema cobre como se a matrícula fosse na disciplina da grade, evitando assim, cobrar duas ou mais vezes. Porém, entendeu-se que existem cenários onde a necessidade que o aluno pague pelas duas disciplinas matriculadas, mesmo que o valor dos créditos venha da disciplina equivalente da matriz curricular do aluno. Assim, passou a existir um novo parâmetro que faz com que o sistema use o total de créditos financeiro da disciplina da matriz curricular do aluno em caso de equivalência múltipla. |
| **Solução/Implementação:** | Foi feita evolução da rotina que calcula créditos financeiros do processo de geração de lançamentos, permitindo ao sistema, através de parametrização, utilizar o número de créditos da matriz curricular do aluno em caso de equivalências, assim como utilizar o valor total de créditos financeiro da disciplina da matriz curricular do aluno em caso de equivalência múltipla.  Para tanto, foram criados dois novos parâmetros para permitir ao sistema se comportar de diferentes formas:  1 - Usar número de créditos da matriz curricular do aluno       Com essa parametrização o sistema poderá utilizar o número de créditos que consta na disciplina da matriz curricular do aluno. Assim, combinando parâmetros, será possível utilizar o valor do crédito da disciplina matriculada com o número de créditos da matriz curricular do aluno.  2 - Usar total de créditos financeiros da matriz curricular do aluno em caso de equivalência múltipla      Com essa parametrização o valor da disciplina da matriz do aluno substituirá o valor da disciplinas equivalentes matriculadas. Assim, em caso de equivalência múltipla, o sistema não processará o valor do crédito da disciplina da matriz curricular do aluno n vezes, conforme o número de disciplinas equivalentes matriculadas. Será assim, utilizado o valor total equivalente. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A. |

divs
