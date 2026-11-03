---
article_id: 1500010840462
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 2775623df40754d01a394437fc7dbbd0733139d399659440dc49b62c7095800b
fetched_at: '2026-06-28T22:42:43.307232+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Funcionalidade do parâmetro MV_OPAPOPR
type: support-article
updated_at: '2021-05-17T10:42:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010840462-Manufatura-Linha-Protheus-SIGAPCP-Funcionalidade-do-par%C3%A2metro-MV-OPAPOPR
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:01:35 min  
  
Dúvida**Qual a funcionalidade do parâmetro **MV\_OPAPOPR - Gerar ordem de produção no apontamento por produto**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
Através do parâmetro **MV\_OPAPOPR** é possível selecionar o tipo da geração da **OP - ordem de produção** no **apontamento por produto**.  
  
Opções do parâmetro **MV\_OPAPOPR**:  
  
**1 -** Nunca irá criar **OP**. Utilizando a opção **1,** o Sistema nunca irá criar uma **OP** automaticamente, ou seja, irá selecionar automaticamente as **ordens** disponíveis para atender a quantidade informada e efetuará o **apontamento**, priorizando as que devem ser entregues primeiro, ou seja, ordenando pela data de entrega. Neste caso, o saldo das **ordens** disponíveis precisa atender a quantidade **apontada**. Caso não houver saldo ou houver saldo parcial, o **apontamento** não será realizado.  
  
**2 -** Sempre irá criar **OP**. Utilizando a opção **2**, o Sistema sempre irá criar uma **OP** automaticamente, independentemente se possuir ou não **ordens** disponíveis para realizar o **apontamento**. Neste caso, sempre será criada uma **OP** com a quantidade **apontada** e esta **ordem** será **apontada** e encerrada pelo **apontamento**.  
  
**3 -** Usa **OPs** abertas e cria nova para saldo faltante. Utilizando a opção **3**, o Sistema irá selecionar as **ordens** disponíveis, priorizando as que devem ser entregues primeiro, ou seja, ordenando pela data de entrega. Caso o saldo disponível não atenda a quantidade **apontada,** será criada uma nova **OP** automaticamente com a quantidade faltante.
