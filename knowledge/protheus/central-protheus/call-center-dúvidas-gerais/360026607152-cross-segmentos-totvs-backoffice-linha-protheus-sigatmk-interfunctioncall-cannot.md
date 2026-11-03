---
article_id: 360026607152
category: Call Center - Dúvidas Gerais
content_hash: a36f74d7c76ddab904c8c0be9d4d916422d1c4bf5864724db429096807a4317f
fetched_at: '2026-06-28T22:41:26.874178+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice -(Linha Protheus-)SIGATMK-InterFunctionCall
  -cannot find function TK090ESTAC in AppMap
type: support-article
updated_at: '2022-06-17T18:16:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026607152-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-InterFunctionCall-cannot-find-function-TK090ESTAC-in-AppMap
---

**Ocorrência**

Ao incluir um operador, ocorre o erro: **InterFunctionCall: cannot find function TK090ESTAC in AppMap on {|x| Self:lActive .and. Tk090Estac() }(MSMGETPR.PRW) 23/10/2018 18:06:47**

**Ambiente**

Cross Segmentos-TOTVS Backoffice -(Linha Protheus-)SIGATMK- a partir da release 12.1.17.

**Causa**

O erro ocorre, devido a função **TK090ESTAC**não estar Disponível no RPO ou a rotina pai, a qual a função pertence estar desatualizada.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Efetue o download do **TMKA090**, rotina pai da função TK090ESTAC, mais atual: <https://suporte.totvs.com/portal/p/10098/download?e=730100> ;  
2. Aplique o pacote via TDS ou o antigo IDE, aceitando os fontes mais atualizados;  
3. Posteriormente, inicialize o Smartclient e refaça o processo.

**OBS: O processo informado acima para ser realizado requer um analista com conhecimentos em estrutura de Protheus. Qualquer dúvida no processo, acione a equipe de Framework.**
