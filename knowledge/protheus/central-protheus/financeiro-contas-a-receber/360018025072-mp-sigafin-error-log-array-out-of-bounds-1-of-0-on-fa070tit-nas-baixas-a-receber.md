---
article_id: 360018025072
category: Financeiro - Contas a Receber
content_hash: d9791212dcf9858852a7566d77dbb8c257566c80841007740a8db8bf8c4e9771
fetched_at: '2026-06-28T22:38:14.269917+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: MP - SIGAFIN - Error "log array out of bounds ( 1 of 0 ) on FA070TIT nas  baixas
  a receber
type: support-article
updated_at: '2021-04-28T15:17:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018025072-MP-SIGAFIN-Error-log-array-out-of-bounds-1-of-0-on-FA070TIT-nas-baixas-a-receber
---

**Ocorrência**Ao realizar algum movimento de baixa no contas a pagar ou a receber, é apresentado a mensagem ***array out of bounds ( 1 of 0 ) on FA070TIT(FINA070.PRX) 27/03/2018 15:08:02 line : 1181*** **.****Ambiente**Microsiga Protheus – Financeiro – A partir da versão 12

**Causa**Arquivo corrompido por cenários diversos.  
   
 **Solução**Para solução deste *error log*, é necessário renomear o arquivo: **SIGAADV.MOT** do ambiente na pasta ***System,*** para criar um novo arquivo **SIGAADV.MOT**.  
  
**Exemplo:** Renomeie o arquivo para "**SIGAADV.MOT-CORROMPIDO".**O sistema irá recriar o arquivo em sua forma padrão.   
  
***Importante:***Avalie a necessidade de re-inclusão de seus motivos de baixas customizados.
