---
content_hash: 8ac9b097c7e68935d27cae2c6bb988bc20bef4d95e769aad93dd6bbb13326a76
fetched_at: '2026-06-29T00:09:07.128697+00:00'
page_id: '384567240'
product: rm
source: tdn-rm
title: 3300521 DSAUGHFATF-1319 DT - Não permite geração de NF quando Parcial 2 ou
  maior for Particular
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=384567240
version: 1
---

# Não permite geração de NF quando Parcial 2 ou maior for Particular

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde. |
| **Módulo:** | TOTVS Gestão Hospitalar. |
| **Função:** | Controle de Solicitação p/ Emissão de Nota Fiscal / Recibos. |
| **Situação/Requisito:** | No controle de tipo de faturamento não estava ficando habilitado a opção Nota Fiscal para a parcial 2 que estava configurada para Particular e, no cadastro geral estava já configurado para convênio Particular emitir nota fiscal |
| **Solução/Implementação:** | Modificado consulta para pegar código do convênio da parcial ao invés do código de convênio do atendimento |
| **Tickets relacionados:** | <https://totvssuporte.zendesk.com/agent/tickets/3300521> |
