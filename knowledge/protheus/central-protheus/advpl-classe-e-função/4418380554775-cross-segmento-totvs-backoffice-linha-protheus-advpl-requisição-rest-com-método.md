---
article_id: 4418380554775
category: ADVPL - Classe e Função
content_hash: cb137bdd340470de11b2e312d510fd177a01566d46da6999a41bf75a8450c815
fetched_at: '2026-06-28T22:40:17.149061+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Requisição REST
  com método PATCH
type: support-article
updated_at: '2022-01-07T19:36:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418380554775-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Requisi%C3%A7%C3%A3o-REST-com-m%C3%A9todo-PATCH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Estou usando a classe **FWRest** mas não estou encontrando como faço uma requisição com o método PATCH, é possível utilizar o mesmo?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**O **[FWRest](https://tdn.totvs.com/display/framework/FWRest)**tem suporte apenas para os verbos: **POST, GET, PUT e DELETE**.  
Os demais métodos não estão disponíveis no produto.  
Pode utilizar a classe **[HTTPQuote](http://tdn.totvs.com/display/tec/HTTPQuote)**onde o segundo parâmetro **cMethod recebe o verbo PATCH.**

|  |  |  |  |
| --- | --- | --- | --- |
| **cMethod** | Caracter | Define o HTTP Method que será utilizado, **permitindo outros além** de POST/GET. | X |

```
HTTPQuote ( "http://localhost:8080/api/test", "PATCH", "a=1&b=2", '{"id":1}', 120, {"Content-Type: application/json"}, @cHeaderRet )
```

Dicas sobre desenvolvimento nas plataformas **TOTVS**.  
<https://devforum.totvs.com.br/>
