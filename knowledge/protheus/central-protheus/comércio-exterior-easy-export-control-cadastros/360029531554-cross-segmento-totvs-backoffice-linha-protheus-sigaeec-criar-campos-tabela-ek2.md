---
article_id: 360029531554
category: Comércio Exterior - Easy Export Control - Cadastros
content_hash: 58330c9797cb2053eaa98d5c6d10ffe21993e4866347b6e1cf916198cdbc258e
fetched_at: '2026-06-28T22:36:57.345075+00:00'
product: protheus
section_id: 1500001549302
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Criar campos tabela
  EK2
type: support-article
updated_at: '2022-06-09T19:26:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029531554-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Criar-campos-tabela-EK2
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:04:00 min  
  
Dúvida**Criação de campos na tabela EK2 referente a justificativa da DUE.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Versão 12.1.17  
  
**Solução**Para envio das informações de Justificativa da DUE, será necessária a criação dos campos na tabela EK2.  
1. Acesse o configurador SIGACFG **-** Ambiente - Base de Dados**-** Dicionário e selecione Base de Dados.

![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042834773/mceclip14.png)

2. Dicionários de Dados e selecione ![mceclip16.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042835153/mceclip16.png)

![mceclip15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041994294/mceclip15.png)

3. Procurar Por EK2 Buscar e selecione ![mceclip18.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041994454/mceclip18.png)

![mceclip17.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042835213/mceclip17.png)  
4. Posicione em Campos e selecione ![mceclip21.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041994614/mceclip21.png)e faça a inclusão dos campos abaixo.

![mceclip20.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041994554/mceclip20.png)

```
Campo EK2_JUSDUE   
TIPO 1 - Caracter  
Tamanho 100
```

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042833053/mceclip0.png)**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041992834/mceclip1.png)**

```
Campo EK2_DESTAQ  
TIPO 1 - Caracter  
Tamanho 30
```

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041992874/mceclip2.png)  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042833473/mceclip3.png)**

```
Campo EK2_SEQED3  
TIPO 1 - Carácter  
Tamanho 3 
```

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041993074/mceclip4.png)  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042833773/mceclip5.png)

```
Campo EK2_PESNCM  
TIPO 2 - Numérico  
Tamanho 16  
Decimal 3
```

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042833893/mceclip6.png)  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042833973/mceclip7.png)

```
Campo EK2_QTDNCM  
TIPO 2- Numérico  
Tamanho 15  
Decimal 3
```

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042834113/mceclip8.png)  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042834193/mceclip9.png)

```
Campo EK2_DESC  
TIPO 1 - Caracter  
Tamanho 30
```

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041993714/mceclip10.png)  
![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041993834/mceclip11.png)

```
Campo EK2_VLSCOB  
TIPO 2- Numérico  
Tamanho 16  
Decimal 2
```

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042834393/mceclip12.png)![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042834513/mceclip13.png)
