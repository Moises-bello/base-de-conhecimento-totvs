---
content_hash: 604e651854e84a58f59cb3d8d159959bb18be7b5c4788e9cb93aed7e56b4731b
fetched_at: '2026-07-02T19:24:27.712417+00:00'
page_id: '678572237'
product: protheus
source: tdn-tec
title: AdjFontsize4
type: documentation
url: https://tdn.totvs.com/display/tec/AdjFontsize4
version: 2
---

## AdjFontsize4

Redefine o tamanho da fonte ao imprimir um relatório com a função "**SetPrint**" no tamanho "**P**" (Esse tamanho define automaticamente a orientação para "**Retrato**").  
Caso esse parâmetro não seja informado é usado o padrão de 11.

ATENÇÃO

A função **SetPrint** foi **descontinuada** e não deve mais ser usada. E se possível, recomendamos que atualize o fonte do relatório que ainda a use.

| Abrangência |
| --- |
| ERP 10 e 11 |

### Exemplo

[Config]  
**AdjFontsize4=8**  
LastMainProg=sigaadv  
EnvServer=environment  
Language=1  
BrowserEnabled=1
