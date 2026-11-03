---
article_id: 40384192413463
category: Gestão de Transportes (TMS)
content_hash: eac533a2c931ec2316c2c40787918350982d55993a4175f064ca637d7759cd1d
fetched_at: '2026-06-28T22:45:27.762054+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Falha de conexão - ANTT indisponível
type: support-article
updated_at: '2026-05-11T18:25:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40384192413463-Log%C3%ADstica-Linha-Protheus-TMS-Falha-de-conex%C3%A3o-ANTT-indispon%C3%ADvel
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40384192384279) Tempo aproximado para leitura: **00:01:10 min**  
  
**Dúvida**  
Qual a causa da mensagem **ANTT indisponível** na integração **TMS x Pamcard**?   
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões.  
  
**Solução**  
Na integração **TMS x Pamcard**, em alguns momentos a **Pamcard** precisa de comunicar com a **ANTT** como, por exemplo, na consulta do **RNTRC**.  
Nesses casos, é fundamental que a **ANTT** esteja operacional para que a consulta seja concluída com sucesso.  
Caso a **Pamcard** não obtenha sucesso no retorno da consulta, ela retorna a mensagem **ANTT indisponível**.  
  
Uma vez que se trata de uma comunicação direta entre a **Pamcard** e a **ANTT**, o **TMS** não possui autonomia ou meios de intervenção nesta ocorrência.  
Geralmente, este cenário é reportado apenas em ambiente de homologação da **Pamcard**.  
  
Se desejar, poderá abrir um ticket com a **Pamcard** para validar a situação. Contudo, sendo a instabilidade por parte da própria **ANTT**, a **Pamcard** também não poderá intervir, e será necessário aguardar a normalização da **ANTT**.   
  
**Glossário**  
**ANTT** - Agência Nacional de Transportes Terrestres  
**RNTRC** - Registro Nacional de Transportadores Rodoviários de Cargas
