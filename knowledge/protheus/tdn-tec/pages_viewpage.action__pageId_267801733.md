---
content_hash: e8f41414251b7445b97b0d6024bcd5bc1d0b4b854820c26dbbbf2d0713a84e26
fetched_at: '2026-07-02T19:24:21.474788+00:00'
page_id: '267801733'
product: protheus
source: tdn-tec
title: Correção - Perda de foco dos componentes travando smartclient
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267801733
version: 1
---

|  |  |
| --- | --- |
| Situação | Em algumas telas do ERP Logix, ao perder foco de um componente, ocorria o travamento do Smartclient |
| Ocorrência | Problema acontece quando uma segunda thread criada no Smartclient que apresentava uma MessageBox, ao clicar fechar essa segunda thread, ocorria o "travamento". |
| Correção | Correção feita para não permitir que a ação de fechar o MessageBox cause o travamento. |
| Informações adicionais | * Referente ao chamado: TVHEHO e TVR630 * Referente à ocorrência: TEC-7431 * Disponível em builds superiores a 7.00.131227A-20160921 |
