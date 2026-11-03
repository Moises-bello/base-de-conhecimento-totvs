---
content_hash: b08b70e51855c352f4b21fefecae14628e23fca95462437d416bb041faf42c4e
fetched_at: '2026-07-02T19:24:28.688249+00:00'
page_id: '808013941'
product: protheus
source: tdn-tec
title: Correção - A propriedade MsCalend:CanMultSel não esta funcionando
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=808013941
version: 3
---

A multipla seleção de datas e pintura dos dias no componente MSCalend não estavam funcionando corretamente

|  |  |
| --- | --- |
| Situação | Tanto a pintura do dia selecionado, com fundo amarelo, e a seleção de múltiplos dias no componente MsCalend não estavam funcionando. |
| Ocorrência | O problema ocorreu por conta da mudança de assinatura de um método do QT6 |
| Correção | Alterado a assinatura do método de pintura de componente, sobrescrito do QT6 |
| Informações adicionais | * Referente ao chamado: [DTCLIENT01-4407](https://jiraproducao.totvs.com.br/browse/DTCLIENT01-4407) * Referente à ocorrência: [18515622](https://suporte.totvs.com/portal/p/10098/consulta-tickets?ticket=18515622) * Disponível em builds superiores a 20.3.2.3 |
