---
article_id: 11912039796887
category: Faturamento - Integrações
content_hash: a33781eba86a0d8a69be461289d49893e798a1f7ec1716ee5453c97ec3b4d78d
fetched_at: '2026-06-28T22:38:26.626689+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  MTI030NOM
type: support-article
updated_at: '2023-01-25T14:05:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11912039796887-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-MTI030NOM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **MTI030NOM - Permite a inclusão de campos customizados no array.**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução:**

O Ponto de Entrada **MTI030NOM** é **executado após** as tratativas de **recebimento da mensagem** **CUSTOMERVENDOR**. É possível **incluir campos** customizados no array que é direcionado para a execauto do MATA030.  
  
**Exemplo**

```
#Include 'Protheus.ch'  
  
User Function MTI030NOM()  
  
    Local aArea := GetArea()  
    Local aArray := PARAMIXB[1]  
  
    aAdd(aArray,{"A1_NATUREZ",'000001',Nil}) //Preenche o campo Natureza (A1_NATUREZ)  
  
    RestArea(aArea)  
  
Return aArray 
```

**Saiba Mais**

**[MTI030NOM - Permite a inclusão de campos customizados no array](https://tdn.totvs.com/x/SAvMCg)**
