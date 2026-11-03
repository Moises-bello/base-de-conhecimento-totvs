---
article_id: 7109151998103
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 2c902ac28a886ccaecf1ca9a42ea0ca492305f1721a2f97ee2238655d7c4ff92
fetched_at: '2026-06-28T22:38:45.257448+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  M460ICM
type: support-article
updated_at: '2022-07-22T18:40:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7109151998103-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-M460ICM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **M460ICM - Recálculo de ICMS**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução:**

REDEFINE VALOR DE ICMS   
P.E. para recalculo do ICMS. Variáveis disponíveis para uso ou alteração:  
\_ALIQICM, \_QUANTIDADE, \_BASEICM, \_VALICM, \_FRETE, \_VALICMFRETE, \_DESCONTO,  
\_VALRATICM, \_ACRESFIN

Para realizar todo o processo corretamente deve **utilizar em conjunto** com o ponto de entrada **M410ICM** com o mesmo tratamento do ponto **M460ICM**, para que as informações do pedido de vendas (planilha financeira) e da nota fiscal de saída **fiquem iguais**.  
  
**Exemplo:**

```
User Function M460ICM()  
  
    _ALIQICM := 10  
    _BASEICM := 100  
    _VALICM := 10  
    //_QUANTIDADE := 0  
    //_FRETE := 0  
    //_VALICMFRETE := 0  
    //_DESCONTO := 0  
    //_VALRATICM := 0  
    //_ACRESFIN := 0  
  
    Alert("Passou pelo Ponto de Entrada M460ICM")  
  
Return
```

**Observação:**

Conforme verificado junto a equipe de produto, o **objetivo** do ponto de entrada M460ICM é **Recalcular o Valor do ICMS**, este ponto de entrada **não trata PIS/COFINS**, este ponto foi concebido **apenas** para tratamento do **ICMS**.  
  
Caso utilize **PIS/COFINS** **não utilize** o Ponto de Entrada **M460ICM**, utilize o Ponto de Entrada **MACALCICMS**, para deduzir a base de **PIS/COFINS** com valor de **ICMS**.

**Saiba Mais:**

**[M460ICM - Recálculo de ICMS](https://tdn.totvs.com/x/toRn)**

**[PE - MACALCICMS - Atualização Base, Alíquota e Valor de ICMS](https://tdn.totvs.com/x/LbQXJw)**

**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada M410ICM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7108945879191-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-M410ICM?source=search)**
