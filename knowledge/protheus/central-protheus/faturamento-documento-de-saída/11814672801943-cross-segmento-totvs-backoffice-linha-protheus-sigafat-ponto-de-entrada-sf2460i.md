---
article_id: 11814672801943
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 585cedb1325c5a0591a9331f23c5283ea22bec2fb8c25313ec7ca91318b92588
fetched_at: '2026-06-28T22:38:45.281237+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  SF2460I
type: support-article
updated_at: '2023-01-20T21:20:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11814672801943-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-SF2460I
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **SF2460I - Atualização das tabelas referentes à nota fiscal**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

Ponto de entrada localizado **após a atualização das tabelas** referentes à nota fiscal (**SF2/SD2**). O Ponto de entrada **é executado após** a exibição da tela de **contabilização On-Line**, mas antes da contabilização oficial.   
**ATENÇÃO:** Este ponto de entrada está **dentro da transação** na gravação das tabelas do documento.

**Exemplo**

```
#INCLUDE "PROTHEUS.CH"  
  
User Function SF2460I()  
  
    RecLock("SF2",.F.)  
  
    F2_TXMOEDA := 10 //Altera o conteúdo do campo F2_TXMOEDA  
  
    MsUnLock()  
  
    Alert("Passou pelo PE SF2460I")  
  
Return()
```

**Saiba Mais**

**[SF2460I - Atualização das tabelas referentes à nota fiscal](https://tdn.totvs.com/x/v4Vn)**
