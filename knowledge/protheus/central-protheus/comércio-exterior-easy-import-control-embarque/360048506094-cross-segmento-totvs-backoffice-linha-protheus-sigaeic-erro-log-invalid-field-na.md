---
article_id: 360048506094
category: Comércio Exterior - Easy Import Control - Embarque
content_hash: 17e5e6fcb3b66403db942e7b5ea7afa0d2879fa43f9f9859b8855cf6d285d448
fetched_at: '2026-06-28T22:39:48.716255+00:00'
product: protheus
section_id: 1500001538381
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Erro log: invalid
  field name in Alias TRB->WI_KILO1 on TC210VALID'
type: support-article
updated_at: '2022-05-02T14:54:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048506094-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Erro-log-invalid-field-name-in-Alias-TRB-WI-KILO1-on-TC210VALID
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Correção para o erro log:

```
invalid field name in Alias TRB->WI_KILO1 on TC210VALID
```

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – *Easy Import Control* – A partir da versão 12.1.17  
  
**Solução**

1 .Acesse o Configurador - Base de Dados - Dicionário - Base de Dados

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043574094/mceclip0.png)

2. Em Dicionário de dados selecione a ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043462814/mceclip2.png).

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044424613/mceclip1.png)

3. Procurar por **SWI** ![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043574354/mceclip3.png) e selecione ![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043574434/mceclip4.png).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071866774/mceclip0.png)

4. Posicione no campo **WI\_KILO1**e selecione ![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043575194/mceclip12.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071866974/mceclip1.png)

5. Marque o campo **WI\_KILO1** como **usado** na Aba **Uso** e utilizado para todos os módulos na Aba Módulos. 

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044425913/mceclip13.png)  
![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044425973/mceclip14.png)  
Após essas alterações realize o procedimento novamente.
