---
content_hash: bdf4a5d7c5779a9b4aab29504a3dd08260d15d2790feea93989ce8d548341753
fetched_at: '2026-06-29T00:06:15.330824+00:00'
page_id: '210052525'
product: rm
source: tdn-rm
title: TTAUBU_DT_Copia_Turmas_Entre_Periodos_Letivos_Com_Erro_Referencia_Objeto
type: documentation
url: https://tdn.totvs.com/display/LRM/TTAUBU_DT_Copia_Turmas_Entre_Periodos_Letivos_Com_Erro_Referencia_Objeto
version: 1
---

# COPIA DE TURMAS ENTRE PERIODOS LETIVOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Educacional.* |
| **Módulo:** | *TOTVS Gestão Educacional.* |
| **Função:** | *Cópia de turmas entre períodos letivos.* |
| **Situação/Requisito:** | *Erro de referência de objeto na seleção (no grid) da turma a ser copiada para outro período letivo, que ocorre no método lkpMatrizAplicadaAfterLookupTurno*   *devido a tentativa de acessar em um* *loop as* *rows do data source do grid que ainda não foi preenchido.* |
| **Solução/Implementação:** | *Incluir validação antes do loop não permitindo acessar as rows do data source do grid sem o mesmo estar preenchido.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *12.1.8.* |
| **Versão Corrigida:** | *12.1.7.* |
| **Versão Expedida:** | *12.1.7.112.* |

divs
