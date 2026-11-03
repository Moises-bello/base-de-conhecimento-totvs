---
article_id: 360028666292
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: b0e723fd616373e8d2371006cea5c0a8166591ba161284fa83baf4d2b6eef794
fetched_at: '2026-06-28T22:42:44.606449+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Não requisita material informado no
  apontamento de perda para a OP
type: support-article
updated_at: '2021-08-02T11:57:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028666292-Manufatura-Linha-Protheus-SIGAPCP-N%C3%A3o-requisita-material-informado-no-apontamento-de-perda-para-a-OP
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:30 min****Dúvida**Por que não requisita material informado no**MATA685 - Apontamento de Perda** para a **OP - Ordem de Produção**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
O material não é requisitado para a **OP** quando:

* O parâmetro **Requisita Produto de Origem** da função **F12** do **MATA685** está como **Não**, e nesse caso o material não é movimentado na tabela **SD3 - Movimentações Internas**;
* Está sendo preenchido o produto destino no campo **BC\_CODDEST - Prd. Destino**, desse modo o Sistema realiza um movimento de transferência do produto origem para o destino, mas não apropria o movimento na **OP**.
