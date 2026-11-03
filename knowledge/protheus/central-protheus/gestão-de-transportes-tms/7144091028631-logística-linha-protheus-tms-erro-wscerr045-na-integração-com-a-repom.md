---
article_id: 7144091028631
category: Gestão de Transportes (TMS)
content_hash: 08c2304b53d663054d04fed6380e22928d8e650ce3db24c19562fa83454bcf42
fetched_at: '2026-06-28T22:45:27.714957+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Erro WSCERR045 na integração com a Repom
type: support-article
updated_at: '2022-07-12T18:09:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7144091028631-Log%C3%ADstica-Linha-Protheus-TMS-Erro-WSCERR045-na-integra%C3%A7%C3%A3o-com-a-Repom
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Erro **WSCERR045** na integração com a **Repom**.  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões  
  
**Causa**Após uma alteração de segurança no ambiente da **Repom**.  
  
**Solução**Na integração com a **Repom**, está sendo apresentado a mensagem **Não foi possível estabelecer comunicação com a Operadora de Frotas, entre em contato com o Administrador de Sistema e informe o código a seguir WSCERR045 / Retorno VAZIO**, conforme imagens abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7143973287959/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7144004513943/mceclip1.png)

Este erro ocorre pois houve uma alteração na segurança do ambiente de homologação da **Repom**, onde os *links* de integração passaram a ser iniciados por **https://**. Antes os *links* eram **http://**.  
  
Desta forma, será necessário acessar o seu cadastro **Operadora de Frotas - TMSAE60**, localizado em **Atualizações/Operadora de frotas**, e no campo **URL** informar o *link* com **https://** na frete.
