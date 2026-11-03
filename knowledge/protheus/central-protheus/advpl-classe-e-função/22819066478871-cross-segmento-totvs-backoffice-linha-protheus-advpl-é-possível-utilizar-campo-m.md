---
article_id: 22819066478871
category: ADVPL - Classe e Função
content_hash: 5b6114a67ed9e0a0cc46df24348de659f7f5d5577272b706d586b08b50f5a1ff
fetched_at: '2026-06-28T22:40:20.704966+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - É possível utilizar
  campo memo em query em ADVPL?
type: support-article
updated_at: '2024-04-15T17:45:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22819066478871-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-%C3%89-poss%C3%ADvel-utilizar-campo-memo-em-query-em-ADVPL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22819066463895) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**É possível utilizar campo memo em query em ADVPL?  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**

Para o retorno de campos MEMO em uma QUERY, desde que a Query seja codificada no fonte AdvPL usando o EMBEDDED SQL , e o(s) campo(s) MEMO seja(m) o(s) último(s) campo(s) da QUERY.

**Exemplo**

```
BeginSql alias cAlias  
  SELECT A1_COD,A1_NOME,A1_VEND,A1_MEN6 //Campo Memo como último no retorno da query  
  FROM %table:SA1% SA1  
  WHERE A1_COD = '000000'  
EndSql
```

**Saiba Mais**

[Embedded SQL](https://tdn.totvs.com/display/public/framework/Embedded+SQL)

[Perguntas frequentes Dbacess](https://tdn.totvs.com/display/tec/DBAccess+-+Perguntas+frequentes#DBAccessPerguntasfrequentes-dbfaq)
