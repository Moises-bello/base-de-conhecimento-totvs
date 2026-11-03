---
article_id: 12609013648023
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 866d6a83cc51282e1a8bc5511234ba4655137a4200fb5622ae25e036cc5825aa
fetched_at: '2026-06-28T22:38:45.264835+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  M460NUM
type: support-article
updated_at: '2023-02-22T18:28:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12609013648023-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-M460NUM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **M460NUM - Seleção da série**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

O ponto de entrada é **executado após a seleção da série** na rotina de documento de saída.

Seu objetivo é **permitir a troca da série e do número do documento** através de customização local.

O número do documento de saída pode ser alterado através da variável Private **cNumero** e a série pela variável **cSerie**.

***Observações:***

**1)** O ponto de entrada é executado fora da transação do programa de preparação do documento de saída.

**2)** O ponto de entrada tem um comportamento diferente quando o parâmetro **MV\_TPNRNFS** estiver configurado como 3. Nesta situação o valor informado na variável **cNumero** não condiz com o próximo número que será gerado e caso o desenvolvedor queira que o sistema obtenha o próximo número, deve-se atribuir a variável **cNumero** uma string vazia.

**Exemplo**

```
#Include 'Protheus.ch'  
#INCLUDE "TOPCONN.CH"  
  
User Function M460NUM()  
  
    Local aParam := ParamIxb  
    Local cNumero := "000460" //Número da NF  
    Local cSerie := "1" //Série da NF  
  
    Alert ("Ponto de Entrada M460NUM - NF: " + cNumero + " - Serie: " + cSerie)  
  
Return
```

**Saiba Mais**

**[M460NUM - Seleção da série](https://tdn.totvs.com/x/wYRn)**
