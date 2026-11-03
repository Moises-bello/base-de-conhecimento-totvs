---
article_id: 37677808178967
category: Financeiro - Contabilização
content_hash: 8d4266aa7c1bd33015eca550eb9c9532fef0c114551e51c718d3bf1363ed2599
fetched_at: '2026-06-28T22:38:05.178841+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: Cross Segmento - Backofficce Linha Protheus - FINA450 -  Como contabilizar
  a compensação entre carteiras?
type: support-article
updated_at: '2026-02-09T20:45:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37677808178967-Cross-Segmento-Backofficce-Linha-Protheus-FINA450-Como-contabilizar-a-compensa%C3%A7%C3%A3o-entre-carteiras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37677828520599) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Como contabilizar a compensação entre carteiras?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA450 - Todas as versões.  
  
**Solução**

Para realizar o cadastro do **Lançamento Padrão (LP)**, acesse o menu:  
**Atualizações → Cadastros → Lançamento Padrão**.

Para o **LP 594**, devem ser criados **dois registros distintos**, sendo:

* um referente ao **débito**;
* Outro referente ao **crédito**.

**Débito**  
No campo **VAL MOEDA 1**, configure a seguinte expressão:

```
If(SE1->(EOF()), VALOR, 0)
```

**Crédito**  
No campo **VAL MOEDA 1**, configure a seguinte expressão:

```
If(SE2->(EOF()), VALOR, 0)
```

Exemplo cadastro LP 594

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37677828521751)

É possível validar que a contabilização será apresentada respeitando as sequências cadastradas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37678006515991)

O **estorno da compensação** entre carteiras é efetuado por meio da **LP 535**. Para garantir a correta reversão do lançamento contábil, deve-se utilizar a mesma expressão aplicada na contabilização original, conforme a expressão anteriormente informada.
