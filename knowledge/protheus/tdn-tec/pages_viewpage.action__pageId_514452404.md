---
content_hash: f70990f66b08c6ee48cc5d97506f60dd85ff9f75c16414f92991b72c6054762a
fetched_at: '2026-07-02T19:24:25.895641+00:00'
page_id: '514452404'
product: protheus
source: tdn-tec
title: TWSDLManager não apaga arquivos temporários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=514452404
version: 1
---

|  |  |
| --- | --- |
| Ocorrência | TWSDLManager não apaga arquivos temporários após várias chamadas do método ParseURL(). |
| Correção | Corrigido para que a cada novo Parser os arquivos anteriores sejam apagados. |
| Informações adicionais | * Referente ao chamado: MTEC-2957 * Disponível em builds iguais ou superiores a [13.1.3.45](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.1.3.45) e [13.2.3.45](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.2.3.45). |
