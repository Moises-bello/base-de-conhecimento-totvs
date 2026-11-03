---
content_hash: 484ad3f89166710990d334b496c41a60d87fd56b0f66a2f858b874bda6f97566
fetched_at: '2026-07-02T19:24:21.479351+00:00'
page_id: '267801968'
product: protheus
source: tdn-tec
title: Reconexão de servidores ao abrir o TDS.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267801968
version: 1
---

|  |  |
| --- | --- |
| Situação | Ao reiniciar o TDS, não eram respeitas as configurações da página de preferencias, onde se configura quais servidores serão reconectados. |
| Ocorrência | Encontramos um problema ao reiniciar o TDS, onde todos os servidores eram reconectados, mesmo a página de preferencias configurada para não reconectar nenhum ou somente o ultimo selecionado. |
| Correção | Alteramos o processo para respeitar as configurações da página de preferencias. |
| Informações adicionais | * Referente ao chamado: TVRCOX * Referente à ocorrência: SSIM-1230 * Disponível em builds superiores a 11.3.3. |
