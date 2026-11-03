---
article_id: 14549238728855
category: FATURAMENTO - RELATÓRIOS
content_hash: 0c6d9178f341533539bdae6318aaa9df4058a481ff728812db7bba329e686f08
fetched_at: '2026-06-28T22:38:23.053147+00:00'
product: protheus
section_id: 1500001539381
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Mensagem:
  Is not allowed more than one source with same name. Rename your source'
type: support-article
updated_at: '2023-05-12T13:21:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14549238728855-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Mensagem-Is-not-allowed-more-than-one-source-with-same-name-Rename-your-source
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como corrigir a mensagem: **Is not allowed more than one source with same name. Rename your source** ao compilar ou executar RDMAKES?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Causa**

A partir da versão **20.3.1.X** do **AppServer** foi implementada **validação** que **verifica** a existência de **código fonte** com **mesmo nome** em ambos os RPOs, (**RPO Padrão e RPO Custom**). Essa verificação ocorre tanto na **compilação** como também na **execução** da rotina.

Não pode existir um fonte customizado **(RPO Custom)** com o mesmo nome de um fonte padrão **(RPO Padrão)**.  
   
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. **Remover** o fonte que está compilado no **RPO Custom** (caso já esteja compilado);
2. **Alterar** o nome do código fonte;
3. **Compilar** o fonte que foi renomeado.

**Saiba Mais**

**[Is not allowed more than one source with same name](https://tdn.totvs.com/x/L6zaKg)**
