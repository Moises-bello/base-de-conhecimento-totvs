---
article_id: 7759502298647
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 45a4425ab5a9b15890fb6949e94d7384f9b0b7a84d803baa4adc20e38bd1a048
fetched_at: '2026-06-28T22:42:42.258581+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAPCP - Erro 9995|AUTHENTICATION: USER NOT
  AUTHORIZED| na integração com o MES'
type: support-article
updated_at: '2022-07-27T17:17:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7759502298647-Manufatura-Linha-Protheus-SIGAPCP-Erro-9995-AUTHENTICATION-USER-NOT-AUTHORIZED-na-integra%C3%A7%C3%A3o-com-o-MES
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:47 min****Ocorrência**Erro **9995|AUTHENTICATION: USER NOT AUTHORIZED|** na integração com o **TOTVS MES**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Causa**A partir da *release* **12.1.33**, quando a chave **Security** não é determinada no **appserver.ini** assume automaticamente o valor **1**, conforme documentação do **Saiba mais**  
  
**Solução**Se manter a chave com o valor **1**, deve ser configurado no **TOTVS MES** o usuário e senha para autenticação no **Protheus**, caso contrário é necessário que especifique **Security = 0**.  
  
**Saiba mais**  
Documentação sobre a chave **Security** [Configuração](https://tdn.totvs.com/pages/viewpage.action?pageId=185747842).
