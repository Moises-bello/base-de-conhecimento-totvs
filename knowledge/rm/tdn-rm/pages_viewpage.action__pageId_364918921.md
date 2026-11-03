---
content_hash: 92109926669fe20c256a5e9affde4e07c50efa548cd5c5b4ddcc3b721bd89081
fetched_at: '2026-06-29T00:09:00.112680+00:00'
page_id: '364918921'
product: rm
source: tdn-rm
title: 2950230 RMSAU-4007 DT Emissão de NF do RM para o Nucleus
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364918921
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Controle de  Solicitação p/ Emissão de Nota Fiscal / Recibos |
| **Situação/Requisito:** | Ao realizar um atendimento originário de um agendamento com atividade que possua item de débito configurado com a restrição "Exige Liberação do convênio", o sistema lança a parte do honorário corretamente para o convênio e a parte do particular também. Porém ao tentar solicitar a emissão da NF pela funcionalidade de "Controle de  Solicitação p/ Emissão de Nota Fiscal / Recibos", ocorre a mensagem de que '' não é um inteiro válido |
| **Solução/Implementação:** | Foi realizado o juste na rotina de lançamento do item de débito originário da atividade da agenda e consequentemente a mensagem originária. |
