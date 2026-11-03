---
article_id: 1500002240902
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: bd63de81c0cd83161011cbab1f4869ab7e07e443480e17a355f07ee666f9c4ad
fetched_at: '2026-06-28T22:42:44.543102+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem REGNOIS Não existe registro
  relacionado a chave informada no alias SB2
type: support-article
updated_at: '2021-07-14T10:50:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002240902-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-REGNOIS-N%C3%A3o-existe-registro-relacionado-a-chave-informada-no-alias-SB2
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:35 min  
  
Ocorrência**Ao cadastrar um novo registro de empenho no **MATA380 - Ajuste de Empenho Simples** ou no **MATA381 - Ajuste de Empenho Múltiplo**, após informar o armazém, apresenta a mensagem **REGNOIS**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103082853/mceclip0.png)

**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**  
Essa mensagem é apresentada, caso o **produto** em questão não possua relacionamento com o **armazém** informado no **empenho**.  
  
**Solução**  
Deve-se criar o relacionamento entre **produto** X **armazém** através da rotina **MATA220 - Saldos em estoque**, informando **produto** e **armazém**.
