---
article_id: 360021621132
category: ADVPL - Classe e Função
content_hash: f6445846a4761029accfea4e8a98b97c9355b25ad96fd9a7765f8bddb899bb07
fetched_at: '2026-06-28T22:40:19.454549+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Função SALDOTIT()
type: support-article
updated_at: '2022-04-27T16:42:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021621132-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-SALDOTIT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**

A função padrão **SaldoTit**() olha para o campo de decréscimo e retorna o valor do titulo com o desconto (decréscimo)?

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**![KCS_SALDOTIT.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360018517791/KCS_SALDOTIT.gif)

Acima está evidenciado um teste de utilização da função **SALDOTIT**(), onde o titulo tem o valor de R$100,00 , e passamos o valor de R$ 20,00 para o campo **E2\_DECRESC**, onde validamos que o retorno da função foi R$ 80,00, concluindo que a função considera o campo de decréscimo dos títulos.  
  
**Exemplo:**

```
User function SaldoTit()  
  
Local nSaldo  
  
dbSelectArea('SE2')  
dbsetorder(1)  
dbSeek(xFilial('SE2')+"ABC"+"00000027",.f.)//PREFIXO+NUM  
   nSaldo := SaldoTit(SE2->E2_PREFIXO,SE2->E2_NUM,SE2->E2_PARCELA,SE2->E2_TIPO,SE2->E2_NATUREZ,"P",SE2->E2_FORNECE,1,,,SE2->E2_LOJA,,0/*nTxMoeda*/)  
Alert(nSaldo)  
  
return
```

**Saiba mais****[SaldoTit() - Retorna o saldo do título](https://tdn.totvs.com/pages/releaseview.action?pageId=682450690)**
