---
content_hash: 7ce3d5f9b3b129a51447a0a666d3248ae11cff35a220078543d5be822d01900d
fetched_at: '2026-06-29T00:08:14.872094+00:00'
page_id: '244719387'
product: rm
source: tdn-rm
title: TV498_DT_Aproveitar_Contrato_Não_deve_Cancelar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244719387
version: 117
---

# MUDANÇA TURMA/TURNO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Função:** | *Mudança Turma/Turno* |
| **Situação/Requisito:** | No processo de Mudança de turma/turno, no Ensino Básico, quando marcamos a opção “Aproveitar Contrato” o sistema estava incorretamente cancelando o contrato da turma original, quando o centro de custo da turma Destino era diferente da turma Origem. |
| **Solução/Implementação:** | Realizado mudança de comportamento no processo de Mudança de turma/turno, no Ensino Básico, quando marcamos a opção “Aproveitar Contrato” o sistema NÃO irá cancelar o contrato da turma original, mesmo se o centro de custo da turma Destino for diferente da Origem.  Existem outros critérios de validação que antes cancelava o contrato, mas a partir desta versão não irá mais fazer o cancelamento (centro de custo diferente, plano de pagamento diferente, default contábil diferente, ou se o status da matricula origem está marcado para cancelar contrato ).  É apresentado mensagem na tela do processo, sempre que os critérios de aproveitamento de contrato não forem atendidos, solicitando ao usuário se deseja continuar. Por exemplo:    “ Centro de custo e departamento diferentes entre as matrizes aplicadas de origem e destino.”    “ Plano de pagamento diferente entre as matrizes aplicadas de origem e destino. “    “ Default contábil diferente entre as matrizes aplicadas de origem e destino.”    “  A situação da matrícula no período letivo de origem não deve estar configurado para cancelar o contrato.” |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A.* |

divs
