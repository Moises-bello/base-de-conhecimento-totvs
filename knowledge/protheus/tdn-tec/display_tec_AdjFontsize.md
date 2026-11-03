---
content_hash: 066e5afd17b4a3b468f7d53a24760c3f6901aac936651a4ad30fcc6f677c45f8
fetched_at: '2026-07-02T19:24:27.701483+00:00'
page_id: '678571930'
product: protheus
source: tdn-tec
title: AdjFontsize
type: documentation
url: https://tdn.totvs.com/display/tec/AdjFontsize
version: 5
---

## AdjFontsize

Redefine o tamanho da fonte ao imprimir um relatório com a função "**SetPrint**" no tamanho "**M**" e orientação de "**Retrato**".  
Caso esse parâmetro não seja informado é usado o padrão de 6.

ATENÇÃO

A função **SetPrint** foi **descontinuada** e não deve mais ser usada. E se possível, recomendamos que atualize o fonte do relatório que ainda a use.

| Abrangência |
| --- |
| ERP 10 e 11 |

### Exemplo

[Config]  
**AdjFontsize=8**  
LastMainProg=sigaadv  
EnvServer=environment  
Language=1  
BrowserEnabled=1
