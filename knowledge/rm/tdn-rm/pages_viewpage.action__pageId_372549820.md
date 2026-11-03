---
content_hash: 855cd100c06ae92c80567b47cf93e8c5d1857a0a1d335c8e96a8eeef4011f56b
fetched_at: '2026-06-29T00:09:01.135902+00:00'
page_id: '372549820'
product: rm
source: tdn-rm
title: 2620438 EDUCACIONAL01-5347 Atualização de usuário Pergamum tratamento do filtro
  de aluno e pessoa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=372549820
version: 1
---

# ATUALIZAR USUÁRIO PERGAMUM

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Atualizar usuário Pergamum |
| **Situação/Requisito:** | Melhorias solicitadas no processo de atualização de usuário e exportação de usuário da integração com Pergamum. Permitir escolher alunos de qualquer período letivo, ao invés de somente o corrente. Permitir filtrar todas as pessoas do contexto, mesmo que sejam alunos, professores ou funcionários. |
| **Solução/Implementação:** | Otimizações na Integração com Pergamum:  1 – Processo Atualização de usuário:  - No filtro de Alunos, foi incluído o campo “Período Letivo”, permitindo que sejam selecionados alunos matriculados em qualquer período letivo. O padrão de preenchimento deste campo será sempre o período letivo corrente, parametrizado em Parâmetros | Educacional |Secretaria | Período Letivo.  - No filtro de Pessoas, foi incluído o campo “Listar somente pessoas que não estejam vinculadas a alunos, professores e funcionários”.  O padrão é estar marcado para listar somente pessoas que não seja vinculadas. Caso seja desmarcado, serão listadas todas as pessoas existentes no contexto (mesmos as que já foram alunos, professores ou funcionários).    2 – Processo Exportação de usuário:  - No filtro de Pessoas, foi incluído o campo “Listar somente pessoas que não estejam vinculadas a alunos, professores e funcionários”.  O padrão é estar marcado para listar somente pessoas que não seja vinculadas. Caso seja desmarcado, serão listadas todas as pessoas existentes no contexto (mesmos as que já foram alunos, professores ou funcionários).   - Para melhor entendimento, os campos de período letivo foram alterados para que se digite o código do período (CODPERLET) ao invés de Id. Período (IDPERLET). |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | 2620438; 2508370 |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
