---
article_id: 360041906193
category: ADVPL - Classe e Função
content_hash: 3afe3c6c9a2ee35c1e15dc1eb49c2e171150410aa4eeeb2c1700bfefb13fe284
fetched_at: '2026-06-28T22:40:18.249135+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL -Erro ao utilizar
  o método put da classe FwRest
type: support-article
updated_at: '2022-06-14T17:41:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041906193-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-ao-utilizar-o-m%C3%A9todo-put-da-classe-FwRest
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Ao utilizar o método **PUT**() da classe **FwRest**() o sistema retorna o seguinte erro:

```
type mismatch on + on FWREST:PUT(FWREST.PRW)
```

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12  
  
**Causa**Esse incidente ocorre, pois falta definir o *path* na classe **fwrest**()  
  
**Solução**

```
User Function tstFwRestTest()  
 Local oRestClient := FWRest():New("http://code.google.com")//)  
    
  oRestClient:setPath("/p/json-path/")  
    
  If oRestClient:Get()  
   ConOut(oRestClient:GetResult())  
  Else  
   conout(oRestClient:GetLastError())  
  Endif  
  
Return
```

**Saiba mais  
[FWRest](https://tdn.totvs.com/display/framework/FWRest)**
