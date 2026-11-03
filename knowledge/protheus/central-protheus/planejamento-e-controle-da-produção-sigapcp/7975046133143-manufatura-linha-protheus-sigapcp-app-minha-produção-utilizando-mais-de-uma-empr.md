---
article_id: 7975046133143
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 9eb8121fc322d9342090a78f709803a0342890f5959ebb47e1535036ffbf1640
fetched_at: '2026-06-28T22:42:40.839276+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - APP Minha Produção utilizando mais
  de uma empresa e/ou filial
type: support-article
updated_at: '2024-04-23T16:08:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7975046133143-Manufatura-Linha-Protheus-SIGAPCP-APP-Minha-Produ%C3%A7%C3%A3o-utilizando-mais-de-uma-empresa-e-ou-filial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:14 min** **Dúvida**Como realizar a configuração do **appserver.ini** pra utilizar o **APP Minha Produção** em mais de uma **empresa** e/ou **filial**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Primeiro é necessário configurar no **appserver.ini** as **URIs**com as instâncias do **REST** para cada empresa/filial.   
Depois de configurar as **URIs**, abrir um *ticket* para o **[MINGLE](https://mingle.totvs.com.br/landpage)**configurar o **Server Address**e a**empresa/filial**Segue **exemplo**de como deve configurar o **appserver**, considerando uma **empresa 01** duas **filiais 01** e **02**:  
  
**[HTTPREST]**  
Port=8400  
IPsBind=  
**URIs=HTTPURI,HTTPURI02**  
Security=1  
  
**[HTTPURI]**  
**URL=/rest**  
**PrepareIn=01,01**  
OnStart=REST\_START  
OnConnect=REST\_CONNECT  
OnExit=REST\_EXIT  
Instances=1,1  
CORSEnable=1  
AllowOrigin=\*  
   
**[HTTPURI02]**  
**URL=/rest02**  
**PrepareIn=01,02**  
OnStart=REST\_START  
OnConnect=REST\_CONNECT  
OnExit=REST\_EXIT  
Instances=1,1  
CORSEnable=1  
AllowOrigin=\*  
  
**Saiba mais**  
Documentação sobre a configuração do **APP**: [Manufatura - Linha Protheus - SIGAPCP - Configurações para utilização do APP Minha Produção](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049910714-Manufatura-Linha-Protheus-SIGAPCP-Configura%C3%A7%C3%B5es-para-utiliza%C3%A7%C3%A3o-do-APP-Minha-Produ%C3%A7%C3%A3o)
