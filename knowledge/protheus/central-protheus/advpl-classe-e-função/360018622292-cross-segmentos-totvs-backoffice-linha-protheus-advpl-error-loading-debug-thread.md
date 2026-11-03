---
article_id: 360018622292
category: ADVPL - Classe e Função
content_hash: 9ab39505074124fd493ec475b0f4c1bf6818722307878b0f39f0c9429f62b21d
fetched_at: '2026-06-28T22:40:19.260491+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Error loading
  debug thread First (Balance) '
type: support-article
updated_at: '2022-01-10T14:56:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018622292-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Error-loading-debug-thread-First-Balance
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Error loading debug thread. First, run Protheus Remote alone. in file C:\advtec9\_tag\interface\rmtserver.cpp at line 1307

**Importante:**A Causa desta mensagem é o fato do cliente estar usando balanceamento de carga e debugando no Servidor ***Master***.

**Ambiente**  
Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Solução para contornar esta situação é a seguinte:   
No arquivo totvssmartclient.ini, acrescente mais uma seção TCP:

```
TCP DEBUG  
Server= (IP Slave)  
PORT= (Porta Slave)
```

Tanto o IP quando a porta devem apontar para um servidor e uma porta de um servidor Slave, exemplo completo **totvssmartclient.ini**:

```
config  
lastmainprog=sigamdi  
envserver=dbprod  
  
drivers  
active=tcp  
  
tcp  
server=10.1.1.8  
port=1811  
  
tcp_debug  
server=10.1.1.7 -> Seção criada  
port=8026  
  
totvsappserver.ini: (Master)  
  
ServerNetwork  
Servers=operandi2s0,operandi2s1,operandi1s2,operandi1s3  
MasterConnection=0  
  
operandi2s0  
TYPE=TCPIP  
Server=10.1.1.8  
Port=8024  
Connections=30  
  
operandi2s1  
TYPE=TCPIP  
Server=10.1.1.8  
Port=8025  
Connections=40  
  
operandi1s2  
TYPE=TCPIP  
Server=10.1.1.7 -> Referência usada para criar a Seção no totvssmartclient   
Port=8026  
Connections=40  
  
operandi1s3  
TYPE=TCPIP  
Server=10.1.1.7  
Port=8027  
Connections=40
```

**Observação**Lembrando que para essa necessidade é imprescindível que se tenha conhecimento na configuração dos ambiente e do App.ini, pois para que não seja gerado erro no processo verificar se os ambientes estão de acordo e estejam apontado para o slave e não para o master .Caso a inconsistência permaneça, consulte o seu arquivo appserver.ini e verifique se o servidor Master está comentado, caso não esteja, comente-o, pois é necessário que o apontamento para os slaves ocorra tanto no TDS quando no AppServer.
