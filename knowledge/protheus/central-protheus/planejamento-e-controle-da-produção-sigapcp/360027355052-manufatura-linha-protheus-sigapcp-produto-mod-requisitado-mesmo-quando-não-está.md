---
article_id: 360027355052
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: d5cbeecf00faa88024ffb916429c009964b9ef098c56d31437c2ebc24dd5ca06
fetched_at: '2026-06-28T22:42:45.763988+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Produto MOD requisitado mesmo quando
  não está na estrutura
type: support-article
updated_at: '2021-11-10T10:36:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027355052-Manufatura-Linha-Protheus-SIGAPCP-Produto-MOD-requisitado-mesmo-quando-n%C3%A3o-est%C3%A1-na-estrutura
---

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:01:00 min****Dúvida**Por que o programa está requisitando **MOD - Mão de obra** mesmo quando não está na estrutura?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Quando o apontamento de produção é realizado pelo **MATA680 -****Produção** **PCP MOD 1** ou **MATA681 - Produção PCP MOD 2**, tendo ou não **MOD** na estrutura o programa lê o **centro de custo** cadastrado para o **recurso** e faz a requisição da **MOD** através dele.  
Isso ocorre mesmo que o campo **Transf. MOD - F5\_TRANMOD**na rotina **MATA230 - Movimentações Internas**, esteja com valor igual a **N** **- Não** para o **Tipo de Movimentação** em uso.  
Ele apenas não será requisitado se no apontamento não for informado tempo.  
Caso o **MOD** esteja também na **estrutura**, o mesmo será requisitados duas vezes, uma pelo **centro de custo** e outra pela **estrutura**.
