---
content_hash: e699548fdba399f0d6493af218d9dbefec66f53a19426af1aa57afa45db53f59
fetched_at: '2026-06-29T00:08:50.040224+00:00'
page_id: '331857866'
product: rm
source: tdn-rm
title: 1394179 RMSAU-1263 Troca de Local de Uso
type: documentation
url: https://tdn.totvs.com/display/LRM/1394179+RMSAU-1263+Troca+de+Local+de+Uso
version: 1
---

# Elaboração de Contas - Aba MatMed

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Ajustar valor inicial do campo Local de Uso |
| **Situação:** | Ao incluir novo registro na aba MatMed, na tela de Elaboração de Contas, o campo de Local de Uso não estava mantendo o valor do registro anterior. |
| **Solução:** | Alterado o comportamento do campo para copiar o valor do último registro, e em caso de não haver um valor, buscar o valor padrão cadastrado em:  Cadastros/Faturamento/Local de Uso, Local de uso para faturamento. |
