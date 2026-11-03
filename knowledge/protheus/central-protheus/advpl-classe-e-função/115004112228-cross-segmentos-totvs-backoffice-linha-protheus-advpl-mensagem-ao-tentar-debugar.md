---
article_id: 115004112228
category: ADVPL - Classe e Função
content_hash: 10c9e12aaa498e0003671d95daf8581b7bea54496db38698f4b2f6cd0f2bc4bb
fetched_at: '2026-06-28T22:40:20.501463+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Mensagem ao tentar
  debugar customização no TDS ( Error loading debug thread )
type: support-article
updated_at: '2022-01-11T19:32:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004112228-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Mensagem-ao-tentar-debugar-customiza%C3%A7%C3%A3o-no-TDS-Error-loading-debug-thread
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**Ao tentar entrar em modo *debug* para depurar rotinas customizadas (especificas) é exibida a mensagem: "***Error loading debug Thread***"  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Causa**A Causa desta mensagem é o fato do cliente estar usando balanceamento de carga e Debugando no Servidor **Master**.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

```
No arquivo totvssmartclient.ini, acrescente mais uma seção TCP  
Ex:   
  
[TCP DEBUG]  
Server= (IP Slave)  
PORT= (Porta Slave)  
  
Tanto o IP quando a porta devem apontar para um servidor e uma porta de um servidor Slave  
Exemplo completo:  
  
totvssmartclient.ini:  
  
[config]  
lastmainprog=sigamdi  
envserver=dbprod  
  
[drivers]  
active=tcp  
  
[tcp]  
server=10.1.1.8  
port=1811  
  
[tcp_debug]  
server=10.1.1.7 -> Seção criada  
port=8026  
  
totvsappserver.ini: (Master)  
  
[ServerNetwork]  
Servers=operandi2s0,operandi2s1,operandi1s2,operandi1s3  
MasterConnection=0  
  
[operandi2s0]  
TYPE=TCPIP  
Server=10.1.1.8  
Port=8024  
Connections=30  
  
[operandi2s1]  
TYPE=TCPIP  
Server=10.1.1.8  
Port=8025  
Connections=40  
  
[operandi1s2]  
TYPE=TCPIP  
Server=10.1.1.7 -> Referência usada para criar a Seção no totvssmartclient   
Port=8026  
Connections=40  
  
[operandi1s3]  
TYPE=TCPIP  
Server=10.1.1.7  
Port=8027  
Connections=40
```

**Observações:**

* Para apoio e maiores informações referente a configurações sobre o Balanceamento de Cargas consulte o link:
* [Balanceamento de carga entre serviços (Load Balance)](http://tdn.totvs.com.br/display/tec/Balanceamento+de+carga)
* Lembrando que para essa necessidade é imprescindível que se tenha conhecimento na configuração dos ambiente e do **App.ini**, pois para que não seja gerado erro no processo verificar se os ambientes estão de acordo e estejam apontado para o *slave* e não para o *master* .
* Caso a inconsistência permaneça, consulte o seu arquivo **appserver.ini** e verifique se o servidor *Master* está comentado, caso não esteja, comente-o, pois é necessário que o apontamento para os *slaves* ocorra tanto no **TDS** quando no **AppServer**.
