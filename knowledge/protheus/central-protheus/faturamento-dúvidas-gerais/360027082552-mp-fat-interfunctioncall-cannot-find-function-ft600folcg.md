---
article_id: 360027082552
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: d875a389ae2c7a580050582a2d586f4577d2fe5585d7aed290785b06b5fe3ba3
fetched_at: '2026-06-28T22:38:31.257581+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP-FAT-InterFunctionCall: cannot find function FT600FOLCG'
type: support-article
updated_at: '2021-04-28T15:54:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027082552-MP-FAT-InterFunctionCall-cannot-find-function-FT600FOLCG
---

**Ocorrência**Ao clicar no folder acessório da proposta comercial (**FATA600**), ocorre o erro:

**InterFunctionCall: cannot find function FT600FOLCG in AppMap on {|| Ft600Folcg()}(FATA600.PRW) 07/01/2019 16:35:43 line : 6033**  
   
 **Ambiente**

Microsiga Protheus- a partir da release 12.1.17.

**Causa**

O erro ocorre, devido a função **FT600FOLCG**não estar disponível no RPO ou a rotina pai, a qual a função pertence estar desatualizada.

**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:  
1. Efetue o download do **FATN600A**, rotina pai da função **FT600FOLCG**, mais atual: [**https://suporte.totvs.com/portal/p/10098/download?e=734962**](https://suporte.totvs.com/portal/p/10098/download?e=734962) ;  
2. Aplique o pacote via TDS ou o antigo IDE, aceitando os fontes mais atualizados;  
3. Posteriormente, inicialize o Smartclient e refaça o processo.

**OBS: O processo informado acima para ser realizado requer um analista com conhecimentos em estrutura de Protheus. Qualquer dúvida no processo, acione a equipe de Framework.**
