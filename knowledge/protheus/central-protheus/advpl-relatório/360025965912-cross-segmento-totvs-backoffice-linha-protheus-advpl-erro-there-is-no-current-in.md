---
article_id: 360025965912
category: ADVPL - Relatório
content_hash: 09384905c00cab3dc34c2c46a475e7e39eb780b2f66d54520d0b287195aea398
fetched_at: '2026-06-28T22:40:22.830090+00:00'
product: protheus
section_id: 1500001549062
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Erro There is no
  current index. on TRPOSITION:EXECUTE
type: support-article
updated_at: '2021-12-30T16:50:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025965912-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-There-is-no-current-index-on-TRPOSITION-EXECUTE
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:00 min*** **Ocorrência**

Sistema apresenta erro ao criar relatório com TOTVS Report.

```
THREAD ERROR ([XXXX], XXXX, XXXXXx) xx/xx/xxxx  
AFN010: There is no current index. on TRPOSITION:EXECUTE(REPORT05.PRW)  
  
Called from TRPOSITION:EXECUTE(REPORT05.PRW)   
Called from TRSECTION:EVALPOSITION(REPORT02.PRW) 
```

Tabela principal é a SD1, tabelas relacionadas SC7 e AFN.   
O relacionamento com a tabela SC7 já é o padrão.   
Criado relacionamento com a tabela AFN, campos D1\_DOC+D1\_ITEM+D1\_COD com os campos AFN\_DOC+AFN\_ITEM+AFN\_COD.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025413252/mceclip2.png)**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 11.80  
  
**Causa**Erro ocorre pois a tabela não tem o índice correspondente ao criado no relacionamento   
  
**Solução**

Para criação do Índice no Configurador -> Banco de dados -> Tabela

- click no Ícone de Edição ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025428531/mceclip4.png)

- Opção *Índice* e click criar novo índice ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025414292/mceclip5.png), correspondente ao seu relacionamento.

- Salvar ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025429071/mceclip6.png) em ambiente exclusivo.

Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025412872/mceclip0.png)
