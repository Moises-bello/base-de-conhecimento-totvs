---
article_id: 8338110088343
category: Inspeção de Processos (SIGAQIP)
content_hash: 8ad6ae3649d5f599b255a635240194d2ba3ac0b890a1f00f4f06c39ac8860ffe
fetched_at: '2026-06-28T22:42:25.819023+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Laudo aprovado automaticamente em Apontamento
  de Produção
type: support-article
updated_at: '2022-08-22T19:24:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8338110088343-Manufatura-Linha-Protheus-SIGAQIP-Laudo-aprovado-automaticamente-em-Apontamento-de-Produ%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:35 min****Dúvida**Na rotina **QIPA215 - Resultados**, como gerar **Laudo Aprovado Automaticamente** em **Apontamento de Produção** quando não há conceito de **Skip-lote** aplicado?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Solução**Para gerar **Laudo Aprovado Automaticamente** em **Apontamento de Produção** quando não há conceito de **Skip-Lote** aplicado, deverá validar conforme:

* **1 -** Quando o parâmetro **MV\_PRAPONT - Configura prioridade no Apontamento de Produção: 1-Tipo de Movimentação / 2-Cadastro de Produto** estiver como **1** e o campo **Envia produção para C.Q.?** como **Não** da rotina **MATA230 - Tipos de Movimentação** da **TM - Tipo de Movimento** os registros ocorrerão como **Certificados** na rotina **QIPA215**, e a inspeção será como **Laudo Aprovado automaticamente**.
* **2 -** Quando o  parâmetro **MV\_PRAPONT - Configura prioridade no Apontamento de Produção: 1-Tipo de Movimentação / 2-Cadastro de Produto** estiver como **2** e o campo **B1\_NUMCQPR = 0** os registros ocorrerão como **Certificados** na rotina **QIPA215**, e a inspeção será como **Laudo Aprovado automaticamente**.
