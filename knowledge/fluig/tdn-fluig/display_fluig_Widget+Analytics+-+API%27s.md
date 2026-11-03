---
content_hash: 83c242cea0f25792186d29f7fb3af78f68901ac820342f4f7ef55e5657cae084
fetched_at: '2026-06-28T21:35:30.130196+00:00'
page_id: '807994945'
product: fluig
source: tdn-fluig
title: Widget Analytics - API's
type: documentation
url: https://tdn.totvs.com/display/fluig/Widget+Analytics+-+API%27s
version: 5
---

---

API's disponíveis para gerenciar as informações da URL de Dashboard do Fluig Analytics.

#f2f2f2#f2f2f2

*Lembrando que uma página pode possuir uma ou mais instâncias de Widget de Analytics.*

| API consumida | Especificação |
| --- | --- |
| {FLUIG\_URL}/portal/api/rest/wcm/iframe/analytics/url/{instanceId}  onde instanceId, é o id da instância da widget de Analytics na página | Retorna a URL para renderizar o iframe da Dashboard do Fluig Analytics:   * A URL já retorna com o redirecionamento para o Identity, onde ocorrerá a validação, e também o parâmetro **RelayState** que indica o redirecionamento para o Fluig Analytics. |
| {FLUIG\_URL}/portal/api/rest/wcm/iframe/analytics/save/{instanceId}  onde instanceId, é o id da instância da widget de Analytics na página | Atualiza a URL para renderizar o iframe da Dashboard do Fluig Analytics:   * Essa API deve ser utilizada para atualizar a URL, caso ocorra uma alteração no id do projeto ou no id da Dashboard no Fluig Analytics. |
