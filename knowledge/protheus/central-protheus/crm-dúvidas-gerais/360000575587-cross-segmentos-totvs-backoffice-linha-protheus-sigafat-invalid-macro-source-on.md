---
article_id: 360000575587
category: CRM - Dúvidas Gerais
content_hash: 95b4e0c867d50e8cd242d574c047ef53d02c516be9c406d4fb715f978a5f167d
fetched_at: '2026-06-28T22:40:27.523591+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - invalid macro
  source on FT300FUSR (FATA300)
type: support-article
updated_at: '2021-11-17T19:45:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000575587-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-invalid-macro-source-on-FT300FUSR-FATA300
---

***![time.png](https://totvssuporte.zendesk.com/hc/article_attachments/360023739612/time.png) Tempo aproximado para leitura:**00:01:00 min*****

**Ocorrência**Na rotina de Oportunidades, ao realizar a alteração do **Estágio** do **Processo de Venda**, o sistema apresenta uma tela de Atenção com o error.log: invalid macro source on FT300FUSR (FATA300)

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as Versões  
  
**Causa**

O erro ocorre devido ao preenchimento incorreto do campo "**Ação**" (**AC2\_ACAO**) no cadastro de **Processo de Venda** (**FATA010**). O campo serve para inserir uma validação (função) a ser executada quando esta etapa for atingida na oportunidade.

Caso preencha com uma informação que não seja uma função, o sistema tentará executar a informação digitada, gerando erro.

**Solução**

É necessário informar uma função a ser executada ou deixar o campo em branco.
