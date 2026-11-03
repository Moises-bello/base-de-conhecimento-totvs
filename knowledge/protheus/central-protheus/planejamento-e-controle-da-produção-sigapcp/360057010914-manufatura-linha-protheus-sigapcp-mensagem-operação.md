---
article_id: 360057010914
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 7bc765fdb66eafccca938ae1b983c72caa00a2580ba7af1ae2a05cfe63cd6b62
fetched_at: '2026-06-28T22:42:44.530227+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem OPERAÇÃO
type: support-article
updated_at: '2024-04-23T19:54:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057010914-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-OPERA%C3%87%C3%83O
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:01 min  
  
Ocorrência**Ao informar a operação na rotina **MATA681 - Produção PCP Mod2** é apresentada a mensagem **OPERAÇÃO**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096780054/mceclip0.png)

**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
 **Causa**  
Essa mensagem pode ocorrer quando:

* É informada uma data de validade final para a **operação** através do campo **G2\_DTFIM - Data de validade final** na rotina **MATA632 - Cadastro de operações** e a mesma é anterior a data do apontamento de produção.  
  ou
* É exibida quando o Sistema não encontra um **roteiro** válido para a **OP - Ordem de Produção**.

**Solução**  
Para conseguir apontar a produção através da rotina **MATA681**, realize a alteração da data de validade final da **operação** para uma data válida e/ou informe um **roteiro** do produto no campo **C2\_ROTEIRO - Roteiro**.
