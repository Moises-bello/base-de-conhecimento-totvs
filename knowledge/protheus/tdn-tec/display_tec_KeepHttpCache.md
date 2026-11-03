---
content_hash: ade2e35fe9397f1f6ac49efd5927b5fdf6bb2720c043c0f349810e0d89047e20
fetched_at: '2026-07-02T19:24:29.398023+00:00'
page_id: '867153217'
product: protheus
source: tdn-tec
title: KeepHttpCache
type: documentation
url: https://tdn.totvs.com/display/tec/KeepHttpCache
version: 1
---

# KeepHttpCache

Chave de configuração da seção [CONFIG] que configura se o cache das páginas web embutidas (Como por exemplo aplicações em PO-UI) serão mantidas ou não ao iniciar um TEebEngine.

Importante

A chave **KeepHttpCache** está disponível apenas para **versão 20.3.2.7** do SmartClient ou superior.

### Valores válidos

| Valor | Descrição |
| --- | --- |
| 0 (padrão) | Desabilita. |
| 1 | Faz com que o cache do navegador embutido seja mantido. |

Exemplo

```
[Config]  
LastMainProg=sigaadv  
EnvServer=environment  
KeepHttpCache=1
```
