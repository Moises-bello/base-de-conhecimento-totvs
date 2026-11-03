---
content_hash: 3ab5e1ce050775c7136d29b4c6980fb643a5953c62b8ce98113d8b94e108fb8a
fetched_at: '2026-07-02T19:24:27.704608+00:00'
page_id: '678572196'
product: protheus
source: tdn-tec
title: AdjFontsize2
type: documentation
url: https://tdn.totvs.com/display/tec/AdjFontsize2
version: 3
---

## AdjFontsize2

Redefine o tamanho da fonte ao imprimir um relatório com a função "**SetPrint**" no tamanho "**G**" (Esse tamanho define automaticamente a orientação para "**Paisagem**").  
Caso esse parâmetro não seja informado é usado o padrão de 7.

ATENÇÃO

A função **SetPrint** foi **descontinuada** e não deve mais ser usada. E se possível, recomendamos que atualize o fonte do relatório que ainda a use.

| Abrangência |
| --- |
| ERP 10 e 11 |

### Exemplo

[Config]  
**AdjFontsize2=8**  
LastMainProg=sigaadv  
EnvServer=environment  
Language=1  
BrowserEnabled=1
