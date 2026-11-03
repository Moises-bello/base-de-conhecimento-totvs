---
article_id: 360028020271
category: ADVPL - Classe e Função
content_hash: 6afd1496a76756cc29382b417685dd854e8d2793fb9875b67a70055031bad233
fetched_at: '2026-06-28T22:40:14.322936+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - A função FDescAfast()
  está disponível para uso em customizações
type: support-article
updated_at: '2022-03-21T11:45:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028020271-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-A-fun%C3%A7%C3%A3o-FDescAfast-est%C3%A1-dispon%C3%ADvel-para-uso-em-customiza%C3%A7%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**A função FDescAfast() está disponível para uso em customizações?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Dado ao fato de ser uma função interna que consequentemente sofre com alterações, não recomendamos o uso da função FDescAfast().  
Atualmente (versão 12, release 1.17) ela não busca informação das SXs, mas sim da SR8 (Ausências) e SRN (Tipos de Ausências).  
Desta forma, deve ser utilizada passando o número de identificação do afastamento R8\_NUMID no quinto parâmetro.  
Contudo, caso a intenção seja apenas saber a descrição do afastamento, deve ser utilizado a função FDesc():

```
FDesc("RCM", SR8->R8_TIPOAFA, "RCM_DESCRI")
```

**Saiba mais**  
[FDESC() - Funções Genéricas](http://tdn.totvs.com/pages/releaseview.action?pageId=6078970)
