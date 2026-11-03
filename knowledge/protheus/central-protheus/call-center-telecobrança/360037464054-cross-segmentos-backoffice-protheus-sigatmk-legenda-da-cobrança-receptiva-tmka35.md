---
article_id: 360037464054
category: Call Center - Telecobrança
content_hash: c2c0c34361c57140df8eac68ccfd76cebc10d32452ed09cb7be27426380dfd26
fetched_at: '2026-06-28T22:41:28.594667+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - Legenda da Cobrança Receptiva
  (TMKA350)
type: support-article
updated_at: '2024-04-25T14:11:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037464054-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Legenda-da-Cobran%C3%A7a-Receptiva-TMKA350
---

**Dúvida**

Como o sistema trata as legendas da rotina do Cobrança Receptiva(**TMKA350)**?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGATMK - A partir da release 12

**Solução**

A legenda do **TMKA350** é formatada na rotina inicial do Call Center, **TMKA271**, as cores significam:  
  
![](https://totvssuporte.zendesk.com/attachments/token/s2GvN4Pz8a1Mw5b4Zbf9rglTJ/?name=inline1531547248.png)​

1 - Atendimento, quando se modifica o o campo Status (**ACF\_STATUS**) de cobrança para  atendimento,assumindo a cor azu;

![](https://totvssuporte.zendesk.com/attachments/token/hRBeRUtfJAsiFV89qO6EwHvK8/?name=inline203570604.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/q8VU3UGoUJI0yISGKPjmTcnfD/?name=inline1158800494.png)​  
2 - Atendimento  de cobrança em aberto ou que acabou de incluir, atribuindo a cor verde ao atendimento;  
  
3 - Atendimento encerrado, após dar a baixa de cobrança via rotina tmka290 ou se alterar o status do atendimento para encerrado, atribuindo a cor vermelha;  
  
4 - Atendimento de cobrança cancelado, é quando se entra no atendimento, outras ações e clica em Cancelar Atendimento, atribuindo a cor cinza ao atendimento em questão:

![](https://totvssuporte.zendesk.com/attachments/token/Cq2BfcIoZOWfybF17IXyzNJC9/?name=inline-1152745786.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/bEhQMTPZsdch2Gc61mpAvWwsr/?name=inline-1155570186.png)​

Ao cancelar o atendimento, o campo **ACF\_CCANC** ficará marcado com um código de cancelamento, que poderá ser verificado na tabela **SYP**:  
![](https://totvssuporte.zendesk.com/attachments/token/O9HwoRliyKuxy4dWVrEyHAKg8/?name=inline-1789725572.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/ZU9T4hCkbyFwkqbM5jSSYg9ND/?name=inline429315920.png)
