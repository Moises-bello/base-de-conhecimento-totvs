---
article_id: 360020569072
category: ADVPL - Classe e Função
content_hash: c0743ced9438b1e5122bf37e9b0c89ac0e22fab23b57755beb0b3f6eecf82d82
fetched_at: '2026-06-28T22:40:15.815385+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Erro muitos usuários
  on RPCSETENV
type: support-article
updated_at: '2022-01-03T17:38:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020569072-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-muitos-usu%C3%A1rios-on-RPCSETENV
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao executar minha customização ocorre o erro:  
Muitos usuários on RPCSETENV(TBICONN.PRW)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Causa**Em customizações o erro está relacionado por está sendo executado varios processos na mesma thread   
  
**Solução**Em Customização sugerimos utilizar a função **[StartJob](http://tdn.totvs.com/display/tec/StartJob)**
