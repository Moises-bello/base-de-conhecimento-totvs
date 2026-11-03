---
content_hash: d8bc4d4c55c06429a198cdf6eaba37f5a5833ec5b741919e9d6611d9dc40c9b5
fetched_at: '2026-06-29T00:09:01.590805+00:00'
page_id: '374309719'
product: rm
source: tdn-rm
title: 2989394 DSAUGHASSIST-838 DT Alteração das datas de guia autorização provenientes
  de agendamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=374309719
version: 2
---

# DSAUGHASSIST-838 Erro encerramento da conta (Alteração das datas de guia autorização provenientes de agendamento)

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | Totvs Gestão Hospitalar |
| **Função:** | Crianção de atendimento externo através de agenda de atendimentos |
| **Situação/Requisito:** | Ao agendar um atendimento solicitar autorização do procedimento via TISS, em outra data futura abrir um atendimento externo através deste agendamento. As guias do agendamento são passadas para o atendimento com a data que foram autorizadas pela TISS (data do agendamento) , porém esta data é anterior ao atendimento. Deste modo a guia, bem como o item lançado na conta, ficam fora da parcial do atendimento. |
| **Solução/Implementação:** | Ao criar um atendimento externo proveniente de agendamento, alterar as datas das guias que vieram do agendamento para a data final do atendimento. |
| **Tickets relacionados:** | 2989394 |
| **Requisito:** | DSAUGHASSIST-838 |
