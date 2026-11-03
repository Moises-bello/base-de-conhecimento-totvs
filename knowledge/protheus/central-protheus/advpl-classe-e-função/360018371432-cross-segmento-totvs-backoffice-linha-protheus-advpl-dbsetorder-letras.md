---
article_id: 360018371432
category: ADVPL - Classe e Função
content_hash: e3ac2b3951208862427356f26a2074200b560b9d9a1a827b1a95f936413b7831
fetched_at: '2026-06-28T22:40:14.139058+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Dbsetorder letras
type: support-article
updated_at: '2021-05-06T19:37:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018371432-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Dbsetorder-letras
---

**Dúvida**Como utilizar o **Dbsetorder** quando o índice é letra?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL– Todas versões  
  
**Solução**Ao utilizar o Dbsetorder quando no deparamos a necessidade de utilizar índice que no configurador está como letra, deve utilizar a sequencia lógica do numeral ( pois a função espera um número como parâmetro).

**Exemplos**

|  |  |
| --- | --- |
| A | 10 |
| B | 11 |
| C | 12 |
| D | 13 |
| E | 14 |

```
DBSelectArea('SB1')  
DBsetorder(11)
```

**Saiba mais**[DBSetOrder](http://tdn.totvs.com/display/tec/DBSetOrder)
