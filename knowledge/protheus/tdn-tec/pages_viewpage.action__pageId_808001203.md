---
content_hash: 05d71c86c7519e6c6a51f724bd46c59bffb578fc4d1d4247af85826e094e69e0
fetched_at: '2026-07-02T19:24:28.679318+00:00'
page_id: '808001203'
product: protheus
source: tdn-tec
title: Correção - Menu na área de trabalho Logix causa queda no SmartClient
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=808001203
version: 1
---

Ao clicar com o botão direito em um ícone na área de trabalho do ambiente Logix, após abrir uma rotina, o SmartClient cai.

|  |  |
| --- | --- |
| Situação | Queda no SmartClient ao abrir um TMenuPopup. |
| Ocorrência | O ambiente perde o componente com foco e o TMenuPopup falha em abrir ocasionando queda. |
| Correção | Foram adicionadas proteções para que o TMenuPopup não termine sem um componente de âncora. |
| Informações adicionais | * Referente ao chamado: #18207293 * Referente à ocorrência: DTCLIENT01-4404 * Disponível em builds superiores a 20.3.2.1 |
