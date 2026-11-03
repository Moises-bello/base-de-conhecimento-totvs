---
content_hash: 776a51949c2261428ff65719f8c2444d625465f6d2404c732bc7b24ed74e39bb
fetched_at: '2026-07-02T19:24:21.445183+00:00'
page_id: '267790542'
product: protheus
source: tdn-tec
title: Necessidade de retry de SSL para versão de protocolos distintas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267790542
version: 1
---

Necessidade de retry de SSL para versão de protocolos distintas<Resumo do que foi contemplado na alteração associada a essa nota de release> 

|  |  |
| --- | --- |
| Situação | Necessidade de retry de SSL para versão de protocolos distintas |
| Ocorrência | Quando o server conectado altera o tipo de protocolo SSL. |
| Melhoria | Criado mecanismo de reconexão para site seguro (SSL), funcionando para email e HTTP. A chave TryProtocols=1, tanto na seção Mail (para emails) quanto na seção SSLConfigure (para HTTP), habilita essa funcionalidade. |
| Informações adicionais | * Referente ao chamado: Não a chamado associado * Referente à ocorrência: TTEC-723 * Disponível em builds superiores a 7.00.131227A - 1.0.3 |
