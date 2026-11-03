---
article_id: 23920950834071
category: Comércio Exterior - Easy Import Control - Cadastros
content_hash: 76868c8cd045087c707e92bad61ce84ac8492b0a3e5c982ada1d2e9799fe9a8f
fetched_at: '2026-06-28T22:39:52.197611+00:00'
product: protheus
section_id: 1500001549382
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Erro no Parâmetro
  FWFormViewStruct: O erro no método SETPROPERTY: Campo EVI_DEMERC não encontrado.'
type: support-article
updated_at: '2024-10-03T13:55:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23920950834071-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Erro-no-Par%C3%A2metro-FWFormViewStruct-O-erro-no-m%C3%A9todo-SETPROPERTY-Campo-EVI-DEMERC-n%C3%A3o-encontrado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23920954594071) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Ao efetuar a integração da **DUIMP (EICDU100)** ocorre um erro:

```
erro no parâmetro FWFormViewStruct: O erro no método SETPROPERTY: Campo EVI_DEMERC não encontrado. on FWFORMVIEWSTRUCT:SETPROPERTY(FWFORMVIEWSTRUCT.PRW) 20/10/2023 14:24:23 line : 549
```

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – *Easy Import Control* – a partir da versão 12.1.27  
  
**Solução**A inconsistência é apresentada devido à ausência do campo **EVI\_DEMERC (DE Mercosul)**. Este campo deve estar presente no banco de dados. Informamos que verifique se este campo está na SX3 ou no configurador. Se não houver, recomendamos acessar o configurador e inserir o campo manualmente. Segue abaixo um print do campo para ser usado como referência.

![EVI_DEMERC 1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23920954599831)![EVI_DEMERC 2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23920950808215)![EVI_DEMERC 3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23920950808727)![EVI_DEMERC 4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23920950811927)

**Saiba Mais**

[Integração DUIMP](https://tdn.totvs.com/pages/viewpage.action?pageId=674907489)
