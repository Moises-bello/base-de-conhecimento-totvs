---
content_hash: 9fb2a627171dbf78cd5f9f7b2c36daae7959a518fc71fec1e6d43e63e675349a
fetched_at: '2026-06-29T00:06:16.406535+00:00'
page_id: '212897529'
product: rm
source: tdn-rm
title: TTLHY6_DT_Aproveitar_Contrato_Mudanca_Turma
type: documentation
url: https://tdn.totvs.com/display/LRM/TTLHY6_DT_Aproveitar_Contrato_Mudanca_Turma
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Educacional* |
| **Módulo:** | *Classis.NET* |
| **Função:** | *Mudança de Turma* |
| **Situação/Requisito:** | *Mudança de Turma* |
| **Solução/Implementação:** | Foi retirado um ajuste realizado no processo de Mudança de Turma onde foi alterado o comportamento do sistema para não exibir a etapa de Datas de Cancelamento do contrato durante o processo, e consequentemente cancelar o contrato em situações que o contrato realmente deveria ser cancelado mesmo marcando a opção “Aproveitar contrato na mudança de turma”.  Para que o contrato seja aproveitado, as seguintes premissas devem ser obedecidas:      1. Plano de pagamento das matrizes de origem e destino devem ser o mesmo. 2. O status da matrícula de origem deve estar configurado para não cancelar o contrato. 3. Centro de custo das matrizes de origem e destino devem ser o mesmo. 4. Default contábil das matrizes de origem e destino devem ser o mesmo.   Se alguma destas premissas não for atendida, será apresentado uma informação com o item que não está atendendo a estas condições e perguntando se o usuário deseja continuar com a execução do processo. Se o usuário continuar a execução, o contrato do aluno será cancelado mesmo tendo marcado este parâmetro. |
| **Conversores e Parâmetros:** | *Marcar a opção "Aproveitar Contrato" durante o processo de Mudança de Turma.* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.9* |
| **Versão Corrigida:** | *12.1.9* |
| **Versão Expedida:** | *12.1.9* |

divs
