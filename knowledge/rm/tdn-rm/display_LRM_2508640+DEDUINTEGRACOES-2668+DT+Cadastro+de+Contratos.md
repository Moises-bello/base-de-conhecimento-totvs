---
content_hash: df7384fa36ffab16d020ed3ce770c4e133b181260b10da17efe0bafe10d173fe
fetched_at: '2026-06-29T00:09:04.140253+00:00'
page_id: '382552668'
product: rm
source: tdn-rm
title: 2508640 DEDUINTEGRACOES-2668 DT Cadastro de Contratos
type: documentation
url: https://tdn.totvs.com/display/LRM/2508640+DEDUINTEGRACOES-2668+DT+Cadastro+de+Contratos
version: 83
---

# CADASTRO DE CONTRATOS - EDIÇÃO DE ALUNO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | Cadastro de Contratos |
| **Situação/Requisito:** | Através do cadastro do Contrato é possível editar o cadastro do Aluno, entretanto, se acessarmos o contrato do aluno através do anexo, na matrícula do período letivo o link não funciona. |
| **Solução/Implementação:** | Havia um tratamento para desabilitar o campo de RA do contrato a partir da central do aluno, porém esse tratamento acabou desabilitando o lookup de aluno no contrato sempre que a action de contratos fosse uma action de detalhe.  Foi feito um ajuste para que somente quando o contrato for editado na central do aluno que o campo de Registro Acadêmico ("RA") será desabilitado. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
