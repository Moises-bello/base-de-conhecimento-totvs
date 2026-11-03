---
article_id: 7108945879191
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 6d6cd18ca95489b6d143b42ea8771d3c9f220ca8bc632afc8aee5fbd87ad36aa
fetched_at: '2026-06-28T22:38:42.385439+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  M410ICM
type: support-article
updated_at: '2022-07-25T12:27:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7108945879191-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-M410ICM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **M410ICM - Retorno do valor de ICMS**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução:**

Este ponto de entrada **retorna o valor do ICMS** para ser demonstrado na **planilha financeira** do pedido de vendas.  
  
Para realizar todo o processo corretamente deve **utilizar em conjunto** com o ponto de entrada **M460ICM** com o mesmo tratamento do ponto **M410ICM**, para que as informações do pedido de vendas (planilha financeira) e da nota fiscal de saída **fiquem iguais**.  
  
**Variáveis disponíveis** para uso ou alteração:  
  
\_BASEICM, \_ALIQICM, \_QUANTIDADE, \_VALICM, \_FRETE, \_VALICMFRETE e \_DESCONTO  
  
**Exemplo:**

```
User Function M410ICM()  
  
    _ALIQICM := 10  
    _BASEICM := 100  
    _VALICM := 10  
    //_QUANTIDADE := 1  
    //_FRETE := 0  
    //_VALICMFRETE := 0  
    //_DESCONTO := 0  
  
    Alert("Passou pelo Ponto de Entrada M410ICM")  
  
Return
```

**Saiba Mais:**

**[M410ICM - Retorno do valor de ICMS](https://tdn.totvs.com/x/koRn)**

**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada M460ICM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7109151998103-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-M460ICM)**
