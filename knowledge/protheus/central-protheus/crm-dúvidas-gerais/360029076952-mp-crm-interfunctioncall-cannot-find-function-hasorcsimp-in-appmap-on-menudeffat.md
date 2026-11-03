---
article_id: 360029076952
category: CRM - Dúvidas Gerais
content_hash: 8d283ee5fe6bc5bf5265325c948b1af85b9569ea2847f9109a4f5003c2a2b10b
fetched_at: '2026-06-28T22:40:27.580778+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: 'MP-CRM-InterFunctionCall: cannot find function HASORCSIMP in AppMap on MENUDEF(FATA300.PRX)'
type: support-article
updated_at: '2021-04-28T14:50:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029076952-MP-CRM-InterFunctionCall-cannot-find-function-HASORCSIMP-in-AppMap-on-MENUDEF-FATA300-PRX
---

**Ocorrência**

Ao entrar em uma oportunidade, pelo CRM ou pelo Faturamento ou pelo gestão de Serviços, ocorre o erro: **InterFunctionCall: cannot find function HASORCSIMP in AppMap on MENUDEF(FATA300.PRX)**  
   
 **Ambiente**

Microsiga Protheus -  a partir da release 12.1.17.  
   
 **Causa**

A falta de função (**NOFUNCW**), indica que o fonte onde a função foi criada deve estar desatualizado.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. Baixe o pacote mais atual da rotina **tecxfunb : <https://patch.engpro.totvs.com.br/download.php?id=90283>**

2. Aplique o pacote, via TDS, em seu ambiente de testes para validação e posteriormente, no ambiente de produção.

Obs:  A aplicação do pacote deve ser efetuado por um analista que detenha o conhecimento técnico para o procedimento, caso tenha dúvidas de procedimento, entre em contato com a equipe de FrameWork para auxiliá-lo.
