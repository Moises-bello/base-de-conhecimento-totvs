---
article_id: 360041301114
category: ADVPL - Classe e Função
content_hash: 78e857a0d0a0f332a9b52b564a8515f7fef0ba48da552abad83d161e69ea7b98
fetched_at: '2026-06-28T22:40:15.494066+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Como Ativar a função
  FWLogMsg.
type: support-article
updated_at: '2022-01-14T17:21:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041301114-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-Ativar-a-fun%C3%A7%C3%A3o-FWLogMsg
---

**Dúvida**Como ativar a função **FWLogMsg**()  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - A partir da versão 12.1.17  
  
**Solução**Esta API refere-se a padronização da linha Microsiga Protheus sobre a  
implementação da API **LogMsg** da Virtual Machine.Para isso é necessário habilitar a chave **FWLOGMSG\_DEBUG**= 1 no appserver.ini.

```
Exemplo:  
FwLogMsg("INFO", /*cTransactionId*/, "REST", FunName(), "", "01", "JSON successfully parsed to Object", 0, (nStart - Seconds()), {}) // nStart é declarada no inicio da função
```

**Console:**  
![2020-01-13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055038134/2020-01-13.png)

**Saiba Mais**  
**[FWLogMsg](https://tdn.totvs.com/display/framework/FWLogMsg)**
