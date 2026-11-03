---
article_id: 360020480231
category: ADVPL - Ponto de Entrada
content_hash: fbfb0e0783be8fae13b82712e26c825b48a1af4f1e6374ecab47dd2496595a05
fetched_at: '2026-06-28T22:40:11.661913+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Campo e5_valor em
  Fa380chv
type: support-article
updated_at: '2022-06-21T17:57:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020480231-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Campo-e5-valor-em-Fa380chv
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Ao tentar utilizar o campo E5\_VALOR no ponto de entrada FA380CHV para ordenar a chave específica, o mesmo não realiza a ordenação.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Solução**Utilizar o campo E5\_VALOR informando o tamanho padrão na função Str():

```
STR(E5_VALOR, 16, 2)
```

Obs:  Para que seja realizado corretamente a ordenação, ela precisa estar cadastrada na SIX.

![Capturar.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360016435591/Capturar.JPG)

**Saiba mais**  
[FUNÇÃO STR](http://tdn.totvs.com/display/tec/Str)  
[PONTO DE ENTRADA FA380CHV](http://tdn.totvs.com/display/PROT/FA380CHV+-+Ordena+dados)
