---
article_id: 360000514367
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 7c2a919ef04c40f4737afced4dc086a0b0f1d84de639cd089d9871ee6ee2ae78
fetched_at: '2026-06-28T22:38:31.122696+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP- FAT-  InterFunctionCall cannot find function FT600CBXST in AppMap on X3CBOX
type: support-article
updated_at: '2021-04-28T15:56:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000514367-MP-FAT-InterFunctionCall-cannot-find-function-FT600CBXST-in-AppMap-on-X3CBOX
---

**Ocorrência**

Erro ao clicar em proposta comercial (**Fata600**) na alteração de uma oportunidade de vendas (**Fata300**):

**InterFunctionCall: cannot find function FT600CBXST in AppMap on X3CBOX(AP5TRANSLATE.PRW)** 23/10/2018 18:06:50 line : 403

**Ambiente**

Microsiga Protheus - a partir da 12.1.17

**Causa**

O erro ocorre, devido a função **FT600CBXSTATUS**não estar Disponível no RPO ou a rotina pai, a qual a função pertence estar desatualizada.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Efetue o download do **FATA600**, rotina pai da função **FT600CBXSTATUS**, mais atual: <https://suporte.totvs.com/portal/p/10098/download?e=729532> ;  
2. Aplique o pacote via TDS ou o antigo IDE, aceitando os fontes mais atualizados;  
3. Posteriormente, inicialize o Smartclient e refaça o processo.

**OBS: O processo informado acima para ser realizado requer um analista com conhecimentos em estrutura de Protheus. Qualquer dúvida no processo, acione a equipe de Framework.**
