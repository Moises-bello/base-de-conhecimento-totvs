---
content_hash: bfbfbcccb199fdb457e619635fb3855e8a060140ac8d96e53a7f2e192738412f
fetched_at: '2026-07-02T19:24:19.628257+00:00'
page_id: '243634174'
product: protheus
source: tdn-tec
title: SSLConfigure - TryProtocols
type: documentation
url: https://tdn.totvs.com/display/tec/SSLConfigure+-+TryProtocols
version: 2
---

INLINE

TryProtocols

Chave de configuração da sessão [SSLConfigure] que permite habilitar um procedimento interno da aplicação que realiza reconexões alternando as diferentes versões habilitadas do protocolo SSL/TLS (SSL2, SSL3 e TLS1) em comunicações que envolvam conexões criptografadas, por exemplo, HTTPS.

Deprecated

Chave sinalizada como **deprecated** a partir da versão  e .

Esta chave não tem mais funcionalidade na aplicação.

### Valores válidos

| Valor | Descrição |
| --- | --- |
| 1 | Habilita a reconexão SSL |
| 0 (**Padrão**) | Não habilita a reconexão SSL |

### Exemplos

Eclipsefalse

### Abrangência

A partir da build **7.00.131227A-20160630**.
