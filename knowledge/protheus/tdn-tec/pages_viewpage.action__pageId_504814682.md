---
content_hash: de30c8a2de3008c9b768e8cb731b1b478b46669d016fc60cdabf58b104e13e09
fetched_at: '2026-07-02T19:24:25.697007+00:00'
page_id: '504814682'
product: protheus
source: tdn-tec
title: Refatorado Método GetServerIp
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=504814682
version: 3
---

|  |  |
| --- | --- |
| Ocorrência | Função GetServerIP retornava em alguns cenários IP vazio. |
| Correção | Alterado forma de buscar IP no Linux, agora usa interfaces de rede ao inves do GetHostByName que é sucetivel a falha dependendo da configuração do arquivo de hosts |
| Informações adicionais | * Referente ao chamado: MTEC-2781 * Disponível em builds iguais ou superiores a [13.1.3.45](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.1.3.45) e [13.2.3.45](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.2.3.45). |
