---
article_id: 8029363365399
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 63d6fd31fbf032c76405a0f5be0ed629ec3c6427377dbdb1a63a3217528ca6bc
fetched_at: '2026-06-28T22:38:43.908043+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  M460ORD
type: support-article
updated_at: '2022-08-08T18:46:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8029363365399-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-M460ORD
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **M460ORD - Ordem de processamento**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

ORDEM DE PROCESSAMENTO   
Este ponto de entrada é executado após a montagem da chave de processamento da tabela de itens de pedido liberados (SC9).  
  
**Exemplo**

```
#INCLUDE 'TOTVS.CH'  
  
User Function M460ORD()  
  
    Local cChave  
  
    Alert("PE M460ORD")  
  
    cEscolha := AVISO("Ordem de Processamento","Selecione a Ordem de Processamento",{"Customizado PE","Normal"},1)  
  
    If cEscolha == 1  
        cChave := "C9_FILIAL + C9_PEDIDO + C9_ITEM" //Ordem de processamento Customizada  
    Else  
        cChave := PARAMIXB  
    EndIf  
  
Return cChave
```

**Saiba Mais: [M460ORD - Ordem de processamento](https://tdn.engpro.totvs.com.br/display/public/PROT/M460ORD+-+Ordem+de+processamento)**
