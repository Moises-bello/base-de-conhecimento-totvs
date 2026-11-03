---
article_id: 10004537120023
category: Faturamento - Orçamentos
content_hash: d34c61d2d1ca108672beaaa2a1caa88e4848d4043864824300290f4f2b43aff4
fetched_at: '2026-06-28T22:38:25.013708+00:00'
product: protheus
section_id: 1500001539281
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  M415ICM
type: support-article
updated_at: '2022-11-04T12:01:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10004537120023-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-M415ICM
---

**Dúvida**Exemplo de utilização do Ponto de Entrada **M415ICM - Altera os Valores do ICMS Referentes à Planilha Financeira**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução:**

Permite **alterar os valores do ICMS**, referentes à **planilha financeira**.

O ponto de entrada disponibiliza as seguinte variáveis para alteração:

\_BASEICM         --> Base de ICMS do item

\_ALIQICM         --> Alíquota de ICMS do item

\_QUANTIDADE --> Quantidade do item

\_VALICM           --> Valor do ICMS do item

\_FRETE              --> Valor do frete do item

\_VALICMFRETE --> Valor do ICMS no frete do item

\_DESCONTO     --> Valor do desconto do item  
  
**Exemplo:**

```
#INCLUDE "PROTHEUS.CH"  
  
User Function M415ICM()      
  
    // Local nItem := PARAMIXB[1] //Número do item na planilha  
    _BASEICM := 500  
    _ALIQICM := 25  
    _VALICM  := _BASEICM * (_ALIQICM / 100) //Resultado: 125  
  
    Alert("Passou pelo Ponto de Entrada M415ICM")  
  
Return
```

**Saiba Mais:**

**[M415ICM - Altera os Valores do ICMS Referentes à Planilha Financeira](https://tdn.totvs.com/x/cgESCw)**

**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada M410ICM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7108945879191-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-M410ICM)**  

**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada M460ICM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7109151998103-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-M460ICM)**
