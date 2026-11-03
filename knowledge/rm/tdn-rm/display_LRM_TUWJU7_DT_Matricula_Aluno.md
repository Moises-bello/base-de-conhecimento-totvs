---
content_hash: a8045e4084132c7d578c2018272c9d72b8d7a9984c0ed214ddf7f460a41f04ca
fetched_at: '2026-06-29T00:08:07.158244+00:00'
page_id: '237372340'
product: rm
source: tdn-rm
title: TUWJU7_DT_Matricula_Aluno
type: documentation
url: https://tdn.totvs.com/display/LRM/TUWJU7_DT_Matricula_Aluno
version: 113
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Função:** | *Matrícula de alunos pelo sistema* |
| **Situação/Requisito:** | No processo de matrícula pelo sistema, se o usuário marcar a opção "Imprimir contrato" ou "Imprimir boleto" mas não houver um relatório de contrato ou de boleto parametrizado, ocorre um erro (o sistema tenta passa como parâmetro para a função SetLookupValues o valor “rel.value” porém, “rel” é nulo) e o sistema permite que o usuário avance para a próxima etapa gerando outro erro na execução do processo. |
| **Solução/Implementação:** | Foi alterada a validação para que sejam validados todos os parâmetros passados para a função SetLookupValues quando o checkbox "Imprimir contrato" ou "Imprimir boleto" estiverem marcados, e caso não exista um relatório padrão parametrizado no sistema, o usuário não podeá avançar a menos que defina no processo qual será o relatório utilizado para os casos citados. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | N/A |

divs
