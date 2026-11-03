---
content_hash: 81cdd2bcf6e56f66072415b5843f39a0ade47d861bbd7b3fadcaf4ce8d37df51
fetched_at: '2026-06-29T00:08:44.833918+00:00'
page_id: '309403384'
product: rm
source: tdn-rm
title: Cópia de 1350934 EDUCACIONAL01-2419 DT Planos de Aula Duplicados na Turma Gerenciada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=309403384
version: 96
---

# PLANOS DE AULA DUPLICADOS NA TURMA GERENCIADA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Turma Gerencial/Gerenciada |
| **Situação/Requisito:** | Ao tentar gerar um plano de aula através da tela Gerenciamento de Aula na turma gerencial, o sistema estava gerando o plano de aula duplicado na turma gerenciada.  Isso acontecia porque já existia um horário para aquele dia gerado e quando tentava gerar para outro horário do mesmo dia, o sistema não conseguia identificar qual o horário que era para gerar na turma gerenciada e gerava de todos os horários existentes nesse dia. |
| **Solução/Implementação:** | Gerenciamento de Aula corrigido para não gerar plano de aula duplicado em turmas gerenciadas quando já houver plano de aula gerado para a mesma data que está sendo gerado no momento.  Para corrigir os planos de aula que foram gerados duplicados, a solução é:  1. filtrar os planos de aula pelo dia que deu o problema;  2. excluir todos os planos da turma gerencial desse dia;  3. verificar se ficou algum plano na turma gerenciada para esse dia e se sim, excluir também;  4. gerar novamente os planos de aula para todos os horários desse dia que estava com problema. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | [EDUCACIONAL01-2680](http://jiraproducao.totvs.com.br/browse/EDUCACIONAL01-2680) |
| **Requisito:** | N/A |

divs
