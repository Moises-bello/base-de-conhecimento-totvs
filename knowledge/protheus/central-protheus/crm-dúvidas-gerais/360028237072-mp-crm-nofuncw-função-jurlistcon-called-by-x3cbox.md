---
article_id: 360028237072
category: CRM - Dúvidas Gerais
content_hash: c4f54409024d5a3d157d102142cf6c01000f4a5997bf2b4d5d0325928392a9d7
fetched_at: '2026-06-28T22:40:27.588484+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: 'MP-CRM-NOFUNCW  Função: JURLISTCON Called By X3CBOX'
type: support-article
updated_at: '2021-04-28T14:50:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028237072-MP-CRM-NOFUNCW-Fun%C3%A7%C3%A3o-JURLISTCON-Called-By-X3CBOX
---

**Ocorrência**

Quando clica na Lupa da busca F3, para  pesquisar **natureza** em uma nova proposta o sistema dispara a mensagem de   
**NOFUNCW**  
**Função: JURLISTCON Called By X3CBOX**  
   
 **Ambiente**

Microsiga Protheus -   a partir da versão 12.  
   
 **Causa**

A falta de função (**NOFUNCW**), indica que o fonte onde a função foi criada deve estar desatualizado.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Baixe o pacote mais atual da rotina **JURXFIN.PRW,**de acordo com sua release Protheus:

**12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=748182> ; 12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=748181> ;**

2. Aplique o pacote, via TDS, em seu ambiente de testes para validação e posteriormente, no ambiente de produção.

Obs:  A aplicação do pacote deve ser efetuado por um analista que detenha o conhecimento técnico para o procedimento, caso tenha dúvidas de procedimento, entre em contato com a equipe de FrameWork para auxiliá-lo.
