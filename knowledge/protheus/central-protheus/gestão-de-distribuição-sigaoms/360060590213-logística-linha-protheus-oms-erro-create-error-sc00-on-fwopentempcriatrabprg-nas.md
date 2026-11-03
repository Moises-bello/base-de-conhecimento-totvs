---
article_id: 360060590213
category: Gestão de Distribuição (SIGAOMS)
content_hash: a64e8303f2cb66c600c462b2c8e79e0149f99288c5a872570f4ab0559be260c7
fetched_at: '2026-06-28T22:45:49.813865+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: 'Logística - Linha Protheus - OMS - Erro Create error: _SC00 on FWOPENTEMP(CRIATRAB.PRG)
  nas rotinas do TOTVS OMS x TOL/TRE'
type: support-article
updated_at: '2022-10-18T18:17:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060590213-Log%C3%ADstica-Linha-Protheus-OMS-Erro-Create-error-SC00-on-FWOPENTEMP-CRIATRAB-PRG-nas-rotinas-do-TOTVS-OMS-x-TOL-TRE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:48 min** **Ocorrência**Nas rotinas do **TOTVS OMS x TOL/TRE**, ocorre **erro Create error: \_SC00 on FWOPENTEMP(CRIATRAB.PRG)**.  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões.  
  
**Causa**As rotinas **OMSXCPL6 - Envio de Pedidos** e **OMSXCPL7 - Monitor de Carga** utilizadas no **TOL/TRE**, podem apresentar o error.log **erro Create error: \_SC00 on FWOPENTEMP(CRIATRAB.PRG),** caso não tenha a configuração de **Grant** **para o usuário SQL** no **DBAccess**.  
  
**Solução**Para solucionar essa ocorrência, será necessário que o usuário **SQL - Standard Query Language** configurado no **DBAccess** tenha configuração de **Grant.** **Saiba mais**Mais informações poderão ser acessadas no *link*: [MSSQL - Grants mínimos para o funcionamento do DBAccess.](https://tdn.totvs.com/pages/viewpage.action?pageId=327323773)  
  
**Glossário**  
**TOL** - TOTVS Otimização Logística   
**TRE** - TOTVS Roteirização e Entrega  
**TOTVS OMS** - Order Management System
