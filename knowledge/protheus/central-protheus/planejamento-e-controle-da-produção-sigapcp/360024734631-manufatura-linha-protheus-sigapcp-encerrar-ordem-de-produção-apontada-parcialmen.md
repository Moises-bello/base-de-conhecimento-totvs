---
article_id: 360024734631
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: cc52bdd2b1245ed29fb7bee4188d768888672fa8f9dc8767bbd61e493500a684
fetched_at: '2026-06-28T22:42:42.249531+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Encerrar ordem de produção apontada
  parcialmente
type: support-article
updated_at: '2025-11-24T01:40:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024734631-Manufatura-Linha-Protheus-SIGAPCP-Encerrar-ordem-de-produ%C3%A7%C3%A3o-apontada-parcialmente
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24593982618647)**Tempo aproximado para leitura: **00:00:00 min****Dúvida**Como encerrar uma **OP - Ordem de Produção** apontada parcialmente?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Para encerrar a **OP**, primeiramente verifique por qual rotina foi realizado o apontamento e pela mesma rotina execute o processo:

* Se o apontamento ocorreu pelo **MATA250** **- Produção simples**, selecione o último movimento de apontamento da **OP** a ser encerrada, **Tipo RE/DE** igual a **PR0**, vá em **Outras ações - Encerrar**.
* Se o apontamento ocorreu através do **MATA680** - **Produção PCP Mod1** ou **MATA681** - **Produção PCP Mod2**, selecione o último apontamento da última **operação**, vá em **Outras ações -  Encerrar.**

**Importante**

* Não será permitido o encerramento de **OPs** que possuem requisições, mas não possuem apontamentos de produção.
* Não será permitido o encerramento de **OPs** que possuem requisições realizadas com data superior a última produção. Será apresentado o *help* **A250NOENC - A ordem de produção não pode ser encerrada pois possui saldo de requisição em processo**.
