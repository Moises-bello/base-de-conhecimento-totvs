---
article_id: 360044375134
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 79ccfacbf3f2a720821f0ccf20dffe37e3b4b61e6ae4f827b88003f595b36743
fetched_at: '2026-06-28T22:42:40.830902+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Apontamentos parciais na Ordem de Produção
type: support-article
updated_at: '2021-08-13T12:47:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044375134-Manufatura-Linha-Protheus-SIGAPCP-Apontamentos-parciais-na-Ordem-de-Produ%C3%A7%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:10 min**  
**Dúvida**É possível realizar vários apontamentos parciais nas rotinas **MATA250 - Produção Simples**, **MATA681** - **Produção PCP Mod 2** e **MATA680 - Produção PCP Mod 1**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
É possível realizar inúmeros apontamentos, porém observe o preenchimento do campo **Parc/Total** da rotina de apontamento usada. A cada apontamento parcial realizado, o Sistema verificará se a soma dos apontamentos anterior juntamente com o apontamento atual é igual ou superior a quantidade da **OP** **- Ordem de Produção.**

* Se for igual ou superior, o Sistema preenche no campo **Parc/Total** o conteúdo **T - Total**, e assim a **OP** é encerrada;
* Se for inferior, preenche neste campo o conteúdo **P - Parcial** e mantem a **OP** em aberta.

Portanto, se mesmo atingindo a quantidade prevista na **OP**, desejar manter ela em aberto, altere o conteúdo do campo **Parc/Total** para **P**, até o momento de encerrá-la. Ela será encerrada quando utilizada a opção **Encerrar** da rotina usada para o apontamento ou alterando o campo **Parc/Total** para **T** ao realizar o último apontamento.
