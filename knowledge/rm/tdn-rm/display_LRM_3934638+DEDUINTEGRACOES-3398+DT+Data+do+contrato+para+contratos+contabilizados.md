---
content_hash: 1977af14ad69dd8fecc8207e9aa49d40f3889a12957919441e5e1af4c7bb15e2
fetched_at: '2026-06-29T00:09:12.331347+00:00'
page_id: '417694243'
product: rm
source: tdn-rm
title: 3934638 DEDUINTEGRACOES-3398 DT Data do contrato para contratos contabilizados
type: documentation
url: https://tdn.totvs.com/display/LRM/3934638+DEDUINTEGRACOES-3398+DT+Data+do+contrato+para+contratos+contabilizados
version: 82
---

# DATA DO CONTRATO PARA CONTRATOS CONTABILIZADOS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Cadastro de contratos / Geração de contabilização por competência |
| **Situação/Requisito:** | Data do contrato está habilitada para edição mesmo com o contrato já contabilizado. |
| **Solução/Implementação:** | Travamento da data do contrato para contratos com contabilizações ativas. O sistema já possuía um tratamento para travar a data de contratos já contabilizados mas a mesma estava sendo feita incorretamente considerando  um o campo IDOPERACAO da SCONTRATO, o qual não é mais preenchido.  Sistema passou a se basear na tabela SCONTRATOCONT para verificar se o contrato possui contabilizações ativas.  O contrato previamente contabilizado cuja data já foi alterada deverá ser estornado e contabilizado novamente. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
