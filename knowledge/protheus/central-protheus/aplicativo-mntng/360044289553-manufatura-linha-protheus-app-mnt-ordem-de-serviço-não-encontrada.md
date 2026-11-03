---
article_id: 360044289553
category: 'Aplicativo MNTNG '
content_hash: 8a96fe339751b5ccbae7405a6405e818932bfd6756c27eeb24da933d066a4808
fetched_at: '2026-06-28T22:42:37.752254+00:00'
product: protheus
section_id: 360010992174
source: central-protheus
title: Manufatura - Linha Protheus - APP MNT - Ordem de Serviço Não Encontrada
type: support-article
updated_at: '2021-08-10T19:44:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044289553-Manufatura-Linha-Protheus-APP-MNT-Ordem-de-Servi%C3%A7o-N%C3%A3o-Encontrada
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:45 min**  
**Ocorrência**No aplicativo **MNTNG** quando tenta **atualizar**, **cancelar** ou **finalizar** uma **O.S - Ordem de Serviço** ocorre a mensagem **O.S não encontrada**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Aplicativo MNTNG - Versão 12  
  
**Causa**A mensagem **O.S não encontrada** ocorre quando a **O.S** é finalizada por um usuário e outro usuário que está consultando no aplicativo não efetua a sincronização.   
Por exemplo: Márcio e Lucas possuem listados nos seus aplicativos a **O.S** 012555. Márcio finaliza a **O.S**. Lucas não realiza a sincronização e tenta atualizar na **O.S** 012555. O aplicativo então irá mostrar a mensagem **O.S não encontrada** pois ela já foi finalizada por Márcio.  
 **Solução**Realize a [sincronização](https://tdn.totvs.com/pages/viewpage.action?pageId=266961176) dos dados e tente novamente.
