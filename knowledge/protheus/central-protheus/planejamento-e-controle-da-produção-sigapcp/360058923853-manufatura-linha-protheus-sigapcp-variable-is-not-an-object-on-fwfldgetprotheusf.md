---
article_id: 360058923853
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: ebdcd23e8274b95ae14f14e3b063f0a93cd64becc9cca255756fd2b71e056e8b
fetched_at: '2026-06-28T22:42:47.133254+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - variable is not an object  on FWFLDGET(PROTHEUSFUNCTIONMVC.PRX)
  no MATA255
type: support-article
updated_at: '2021-06-21T17:40:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058923853-Manufatura-Linha-Protheus-SIGAPCP-variable-is-not-an-object-on-FWFLDGET-PROTHEUSFUNCTIONMVC-PRX-no-MATA255
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:45 min**  
**Ocorrência**Ao tentar realizar o cadastro de opcionais na rotina **MATA255 - Opcionais** é apresentado o erro **variable is not an object on FWFLDGET(PROTHEUSFUNCTIONMVC.PRX)**  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**  
Esse erro é apresentado pois a rotina **MATA255** para a **Versão 12** foi descontinuada.  
  
**Solução**Para realizar o cadastro de opcionais na **Versão** **12** deve-se utilizar a rotina **MATA256 - Opcionais**.  
Neste caso é necessário alterar a chamada no menu para a nova rotina.  
  
**Saiba mais**  
Documentação que explica como realizar a alteração de menu [Logística - Linha Protheus - GFE - Adicionar um novo programa no Menu padrão do SIGAGFE ou outro módulo do Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/236147867-MP-GFE-Adicionar-um-novo-programa-no-Menu-padr%C3%A3o-do-SIGAGFE-ou-outro-m%C3%B3dulo-do-Protheus)
