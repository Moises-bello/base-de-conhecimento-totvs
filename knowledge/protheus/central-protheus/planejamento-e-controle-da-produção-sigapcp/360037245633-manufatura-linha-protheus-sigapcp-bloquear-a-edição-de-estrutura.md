---
article_id: 360037245633
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: dc022aba6c1ecc28cdf6d060329d3299e909bc8de18716ecbe19489241af3662
fetched_at: '2026-06-28T22:42:40.906112+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Bloquear a edição de estrutura
type: support-article
updated_at: '2021-08-13T12:34:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037245633-Manufatura-Linha-Protheus-SIGAPCP-Bloquear-a-edi%C3%A7%C3%A3o-de-estrutura
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:00:45 min**  
**Dúvida**É possível bloquear a alteração de estrutura pelo **MATA200 - Cadastro de Estrutura** quando existe **OP - Ordem de produção** do item pai da estrutura a ser alterado, ainda em aberto?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Não há uma parametrização que bloqueie a alteração da estrutura quando já existe **OP** para o item pai da estrutura.  
Uma vez realizado o empenho, a estrutura, registrada na tabela **SG1 - Estruturas dos Produtos**, através da rotina **MATA200 - Cadastro de Estruturas**, pode ser alterado sem refletir no empenho já gerado para a **OP** e registrado na tabela **SD4 - Requisições Empenhadas**.
