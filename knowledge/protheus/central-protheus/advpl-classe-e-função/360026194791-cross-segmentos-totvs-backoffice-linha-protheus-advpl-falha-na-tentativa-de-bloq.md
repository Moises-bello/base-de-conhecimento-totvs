---
article_id: 360026194791
category: ADVPL - Classe e Função
content_hash: 1ea9b2bf92915a2f31150cc1031ff10bcd8107459ca423f2618ee90a07a920a5
fetched_at: '2026-06-28T22:40:19.302287+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Falha na tentativa
  de bloquear alias SB2
type: support-article
updated_at: '2024-03-06T15:10:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026194791-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Falha-na-tentativa-de-bloquear-alias-SB2
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: 00:02:00 min  
  
Ocorrência**Temos um serviço via *web service* que executa a rotina automática que utiliza a SB2 e quando outro usuário acessa outra rotina que irá alocar a SB2, gerar o erro or log abaixo e trava o serviço.

```
THREAD ERROR ([XXXX], XXXXXX, THIS) XX/XX/XXXX  
Falha na tentativa de bloquear alias SB2, recno213.O registro está sendo usado por outro usuário: XXXX MATA103 - TCPIP - ThreadID(9632) (localhost:4323) on LOCKERRORLOG(APLIB060.PRW)   
  
Called from LOCKERRORLOG(APLIB060.PRW)   
Called from HELPLOCK(APLIB060.PRW)
```

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Causa**Foi verificado que o HELPLOCK ocorre quando há concorrência de trava entre usuário A e B a um mesmo registro, onde o tempo em que o registro fica travado pelo usuário A é maior que timeout(tempo de espera) na requisição do usuário B.

**Solução**Para evitar a mensagem, será necessário avaliar o tempo médio que o registro fica travado em seus processos, e alterar o timeout no client que requisita o serviço com um tempo condizente.
