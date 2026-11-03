---
content_hash: 0dba4220c0b6a33380db2d4f009344968356d1f255a787e14019599719d06440
fetched_at: '2026-06-29T00:06:01.363575+00:00'
page_id: '198937763'
product: rm
source: tdn-rm
title: TSWVET_DT_ERRO_MUDANCA_TURMA_TURNO_APROVEITANDO_CONTRATO
type: documentation
url: https://tdn.totvs.com/display/LRM/TSWVET_DT_ERRO_MUDANCA_TURMA_TURNO_APROVEITANDO_CONTRATO
version: 1
---

# MUDANÇA DE TURMA/TURNO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Função:** | *Mudança de Turma/Turno* |
| **Situação/Requisito:** | *Ao executar o processo de mudança de turma/turno com o parametro "Aproveitar contrato na mudança de turma" marcado, e as turmas de origem e destino possuírem alguma discrepância em:*  *Plano de Pagamento, Parametros da Matricula, Matriz Aplicada ou Default Contábil*  *O* *processo não está sendo executado corretamente.* |
| **Solução/Implementação:** | *Modificado a validação realizada no processo para o parametro "Aproveitar contrato na mudança de turma" marcado, para que seja exibido apenas um aviso para o cliente informando dos erros.*  *Caso o cliente deseja continuar com o processo, o contrato será reaproveitado.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.6* |
