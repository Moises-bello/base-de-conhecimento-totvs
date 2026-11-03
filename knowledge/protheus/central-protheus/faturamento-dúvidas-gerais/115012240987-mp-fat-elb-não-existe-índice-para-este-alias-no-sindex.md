---
article_id: 115012240987
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 35e9b229e7a3214b35ab4010d9c9be7b45802e498132cb5fa687a09f49bad298
fetched_at: '2026-06-28T22:38:31.051219+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP - FAT - ELB: Não existe índice para este alias no SINDEX'
type: support-article
updated_at: '2025-08-29T17:15:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115012240987-MP-FAT-ELB-N%C3%A3o-existe-%C3%ADndice-para-este-alias-no-SINDEX
---

**Ocorrência**

Ao migrar para a versão 12, é gerado o erro: "ELB: Não existe índice para este alias no SINDEX".  
  
**Causa**

Trata-se de uma deficiência na migração do dicionário de dados, onde não está constatando todos os índices da tabela.  
  
**Ambiente**

Microsiga Protheus - a partir da versão 12, para qualquer release dentro da versão.  
  
**Solução**  
  
Incluir na tabela SIX (índices) que o erro deixará de ocorrer: **![](https://totvssuporte.zendesk.com/attachments/token/GeArzCyJzHdlvZzdq8ZI0edT3/?name=inline-288324270.png)​**  
ELB\_FILIAL+ELB\_TPPROC+ELB\_EXPORT+ELB\_LOJEXP+ELB\_IMPORT+ELB\_LOJIMP+ELB\_NRINVO+ELB\_PROCES+ELB\_SEQPRC

ELB\_FILIAL+ELB\_TPPROC+ELB\_IMPORT+ELB\_LOJIMP+ELB\_NRINVO+ELB\_PROCES+ELB\_SEQPRC                                                                                      
ELB\_FILIAL+ELB\_TPPROC+ELB\_EXPORT+ELB\_LOJEXP+ELB\_NRINVO+ELB\_PROCES+ELB\_SEQPRC
