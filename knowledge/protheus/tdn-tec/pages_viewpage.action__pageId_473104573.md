---
content_hash: 34d111d55be6bf77b42ceaad6c5df1459bbad1d9e4c19ed6f860e6926bd7d550
fetched_at: '2026-07-02T19:24:24.264039+00:00'
page_id: '473104573'
product: protheus
source: tdn-tec
title: Crescimento do uso de memória do Appserver ao aplicar patch
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=473104573
version: 2
---

|  |  |
| --- | --- |
| Ocorrência | Ao utilizar a opção "Aceito somente os fontes atualizados", a memoria do server cresce exponencialmente ao aplicar patch. |
| Correção | Correção para excluir listas internas do Appserver ao término de cada arquivo do patch aplicado. Obs: Essa correção não modifica o funcionamento da aplicação de patch. |
| Informações adicionais | * Referente ao chamado: TTEC-3039 * Disponível em builds iguais ou superiores a [13.1.3.42](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.1.3.42) e [13.2.3.42](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.2.3.42). |
