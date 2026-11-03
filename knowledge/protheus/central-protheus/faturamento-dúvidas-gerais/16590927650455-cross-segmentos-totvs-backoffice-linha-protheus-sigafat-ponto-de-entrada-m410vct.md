---
article_id: 16590927650455
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: dcd0930a0e7a22d9043411fc1a790b5dd3c4ead587f37590c31e2b65308d3b0a
fetched_at: '2026-06-28T22:38:33.094612+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  M410VCT
type: support-article
updated_at: '2025-01-10T19:49:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16590927650455-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-M410VCT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16590913355543) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **M410VCT - Alteração das duplicatas na Planilha Financeira**.  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

A finalidade do ponto de entrada **M410VCT** é permitir que seja **alterado o vencimento** **e valor** das parcelas **na aba de duplicatas da Planilha Financeira**.

**PARAMIXB[1]** - Tipo: Array --> Duplicatas com os vencimentos e valores, sendo:  
aDupl[1] - Tipo: Data --> Data de Vencimento  
aDupl[2] - Tipo: Caracter --> Valor da Duplicata

**PARAMIXB[2]** - Tipo: Numérico --> Valor total da fatura

**Exemplo**

```
#Include 'Protheus.ch'  
  
User Function M410VCT()  
  
    Local aDupl   := PARAMIXB[1]  //Array com as duplicatas  
    Local nTotFat := PARAMIXB[2]  //Valor total da fatura  
  
    //Parcela 1  
    aDupl[1][1] := CtoD("02/09/2023")   //Data de vencimento  
    aDupl[1][2] := TransForm(50.55,PesqPict("SE1","E1_VALOR"))  //Valor da duplicata  
  
    //Parcela 2  
    //aDupl[2][1] := CtoD("03/09/2023")   //Data de vencimento  
    //aDupl[2][2] := TransForm(80.00,PesqPict("SE1","E1_VALOR"))  //Valor da duplicata  
  
    Alert("Passou pelo Ponto de Entrada M410VCT")  
  
Return aDupl
```

**Saiba Mais**

**[M410VCT - Alteração das duplicatas na Planilha Financeira](https://tdn.totvs.com/x/k2ImDg)**
