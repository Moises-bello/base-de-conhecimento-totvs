---
article_id: 7865897212439
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 9306d95c4cce29a13d347ccc52ccc26e164d60736616320f89e0dd55ea11688f
fetched_at: '2026-06-28T22:38:32.837309+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  FT300D1ST
type: support-article
updated_at: '2022-08-01T17:08:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7865897212439-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-FT300D1ST
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **FT300D1ST - Inclusão de novos status para o campo AD1\_STATUS**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

Ponto de entrada para incluir mais status para o campo AD1\_STATUS.

O campo AD1\_STATUS possui tamanho 1, e consequentemente o status a ser inserido não pode ser maior que 9.  
  
**Exemplo**

```
#Include 'Protheus.ch'  
  
User Function Ft300D1St()  
  
    Local aStatus := {}  
  
    MSGAlert("O Ponto de entrada FT300D1ST foi executado!")  
  
    aAdd(aStatus,"5=Novo Status")  
    aAdd(aStatus,"6=Outro Status")  
    aAdd(aStatus,"7=Status Final")  
  
Return aStatus
```

**Observação: Filtro no browse** com os novos status **não funcionam** com o Operador "**Igual a**", utilize o Operador "**Está contido em**".  
  
**Saiba Mais**

**[FT300D1ST - Inclusão de novos status para o campo AD1\_STATUS](https://tdn.totvs.com/x/UeMGDg)**
