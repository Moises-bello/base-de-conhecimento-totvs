---
article_id: 14606419008535
category: Faturamento - Orçamentos
content_hash: f3b861b0c4210c69c53053a82373667fe43e161aa6c9dc46bdd3db99b4cbce56
fetched_at: '2026-06-28T22:38:25.049953+00:00'
product: protheus
section_id: 1500001539281
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  MTA416PV
type: support-article
updated_at: '2023-05-15T17:19:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14606419008535-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-MTA416PV
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **MTA416PV - Baixa do Orçamento.**  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

APOS GERACAO DO ACOLS NA BAIXA ORCAMENTO.  
Executado após o preenchimento do aCols na Baixa do Orcamento de Vendas.  
Usar as variaveis \_aCols e \_aHeader  
  
**Exemplo**

```
User Function MTA416PV()  
  
    Local nAux := PARAMIXB  
    _aCols[nAux][5] := 2000     //C6_PRCVEN  
    _aCols[nAux][6] := 2000     //C6_VALOR      
  
    Alert('Passou pelo ponto de entrada MTA416PV')  
  
Return Nil
```

**Saiba Mais**  
**[MTA416PV - Baixa do Orçamento](https://tdn.totvs.com/x/i4Vn)**
