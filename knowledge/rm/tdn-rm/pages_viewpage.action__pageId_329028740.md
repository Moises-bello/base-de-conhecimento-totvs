---
content_hash: 39ea3e8e9714ca7956c64101049eb94b0becdaaffdfd94139772b308725924cc
fetched_at: '2026-06-29T00:08:48.893029+00:00'
page_id: '329028740'
product: rm
source: tdn-rm
title: 1844031 RMSAU-2035DT  Alteração da data inicial da parcial quando existem procedimentos
  anteriores a data informada.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=329028740
version: 1
---

# [1844031 RMSAU-2035DT](http://tdn.totvs.com/pages/viewpage.action?pageId=327326220) Alteração da data inicial da parcial quando existem procedimentos anteriores a data informada.

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Elaboração de contas |
| **Situação/Requisito:** | Ao alterar a data de uma parcial (2 ou maior) para uma data posterior a de algum item de Diagnose e Terapia, ocorre uma validação em tela que não permite alterar a data da parcial para uma data posterior a do procedimento. |
| **Solução/Implementação:** | A validação para estes casos deve considerar se a data da Diagnose e Terapia não ira se encaixar em nenhuma das parciais e não somente a que teve a data alterada. E só bloquear a alteração da data se o procedimento não se encaixar em nenhuma das parciais da conta. |
| **Tickets relacionados:** | 1844031 |
| **Requisito:** | RMSAU-2035. |
