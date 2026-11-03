---
article_id: 13516042486679
category: Encargos
content_hash: b24eb6566b98f752188d298ade9003865748cb9c22570a38023cca8b5e47466f
fetched_at: '2026-06-28T22:46:52.109070+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Lançamento contábil não integra no Gestão Contábil
type: support-article
updated_at: '2024-10-09T19:49:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13516042486679-RH-RM-FOP-Lan%C3%A7amento-cont%C3%A1bil-n%C3%A3o-integra-no-Gest%C3%A3o-Cont%C3%A1bil
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16780105413143) Tempo aproximado para leitura: **00:01:35 min****Ocorrência**Ao gerar o lançamento contábil na folha de pagamento, o lote não é integrado automaticamente no módulo gestão contábil.   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Este problema ocorre, pois o sistema RM esta parametrizado para gerar o lote contábil primeiro na folha de pagamento antes de integrar com o **Saldus.**    
  
**Solução**Para que o lote contábil seja integrado de forma automática para o módulo Gestão Contábil acesse: **Módulo Folha de Pagamento | Configurações | Parametrizador | Folha Normal | Contabilização** e **desmarque** a flag: **Gera contabilização na folha de pagamento antes de enviar para Gestão Contábil.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13515780966551)  
  
Após desmarcar esta flag, encerre o acesso ao sistema, reinicie o host e gere o lote novamente que o mesmo será integrado de forma automática para o gestão contábil.   
  
**Importante**  
Se a empresa desejar permanecer com a parametrização deverá integrar o lote de forma manual acessando: **Encargos | Lançamentos | Lançamentos ( Folha de Pagamento).**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13515904888343)  
  
Localize o lote, selecione o mesmo e clique em : **Processos | Integrar lote contábil com Gestão contábil** , após este processo o lote será integrado. 

![](https://p23.zdusercontent.com/attachment/888110/e8PPaJzujy6k4Bl3gwOKzWRp6?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..HtfH1TiJ_BKJTy612fxv2g.d5CzwdhtP-7a_cXAlSZN4F0-JhklE2fY31QBjwzQH7W7B04FQzJLRff84j7zRA1cxyzqVg_iXeF1Sbv-Cc-GqRVdoAw03SLVoI5R8e6v5EMOJKalXaoHd8mPnCz6r_7GobCO5t8IzZEXJlj6o3CTwni5Y9UQ-LKKv7cCZQNMvQtTtCSKX6k_eQ3_6ERD2Weky4WVZv-f4zk7pzb_5B46K9i1khigi6nmg6ytGislEBWFAwP3anvaEAGISxt7V593UjWsm6suHGI_emUQPpUHsPD3XccqTWdbsjoCsr77DO8.JQQ08o_nnc-EIdGt4OHB9Q)
