---
article_id: 360025996033
category: ADVPL - Ponto de Entrada
content_hash: f5b4407a9ea8ca3a9025805034da7a0cf1b79e9eaa8202b0b439ba7107f15759
fetched_at: '2026-06-28T22:40:12.809746+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Pontos de entrada
  MVC
type: support-article
updated_at: '2021-12-21T19:53:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025996033-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Pontos-de-entrada-MVC
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Como identificar o modelo de dados de rotinas com pontos de entrada MVC?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Não Temos ainda uma Lista completa de Pontos de entrada na P12, mas esse documento estará sempre em atualização informando algumas rotina com ponto de entrada No Padrão MVC

|  |  |
| --- | --- |
| **Rotina** | **Modelos de dados** |
| WMSA391 | WMSA391B |
| MATA131 | MATA131 |
| MATA311 | MATA311 |
| FATA300 | FATA300 |
| FATA600 | FATA600 |
| OMSA010 | OMSA010 |
| CNTA300 | CNTA300 |
| MATA094 | MATA094 |
| TECA440 | TECA440 |
| MATA010 | ITEM |
| MATA020 | CUSTOMERVENDOR |
| FINM010 | FINM010 |
| GPEA020 | GPEA020 |
| ATFA10 | ATFA012 |
| MATA014 | MATA014 |
| FISA010 | FISA010 |
| GPEA240 | GPEA240 |
| TECA930 | TECA930 |
| EECAT140 | EXPP013 |
| TECA890 | TECA890 |
| MATA960 | MATA960MOD |
| FINA460 | FINA460A |
| JURA109 | JURA109 |
| MNTA080 | MNTA080 |
| ATFA030 | ATFA036 |
| TMKA260 | TMKA260 |
| GPEA040 | GPEA040 |
| CTBA020 | CTBA020 |
| ESSIS400 | ESSIS400 |
| MATA632 | MATA632 |
| LOJA070 | LOJA070 |

Outros modelos já definidos poderão ser encontrados na documentação abaixo.

[**Fontes em MVC**](http://tdn.totvs.com/display/public/PROT/Fontes+em+MVC)

```
Obs.:  
Todos os pontos de entrada terão seu legado mantido, salvo pontos que consideramos como pontos padrões como validação após a gravação e botões que serão substituídos, os pontos que trazem conteúdo do sistema por paramixb esses serão mantidos com sua particularidades.  
Obs.: Ao escrever um fonte em MVC que será uma User Function, cuidado ao atribuir o nome ao fonte, pois ele não poderá ter o mesmo nome do Modelo de Dados (Model). Se o ID do Modelo de Dados (Model) tiver o nome FONT001 o fonte não pode ter o nome FONT001.
```

**Saiba Mais**[Ponto de Entrada Padrão do MVC](http://tdn.totvs.com/pages/releaseview.action?pageId=208345968)
