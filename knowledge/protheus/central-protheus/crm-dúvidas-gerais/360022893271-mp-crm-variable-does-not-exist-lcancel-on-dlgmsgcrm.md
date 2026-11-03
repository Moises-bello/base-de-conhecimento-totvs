---
article_id: 360022893271
category: CRM - Dúvidas Gerais
content_hash: 2d8caf6313af1a8f8541aed3dc48dcbaa60f15ddc5c862e5521a6a865b147569
fetched_at: '2026-06-28T22:40:27.594374+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: MP-CRM-variable does not exist LCANCEL on DLGMSGCRM
type: support-article
updated_at: '2021-04-28T14:50:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022893271-MP-CRM-variable-does-not-exist-LCANCEL-on-DLGMSGCRM
---

**Ocorrência**

Na gravação da proposta comercial (**Fata600**), gera o erro: **variable does not exist LCANCEL on DLGMSGCRM(CRMXFUNGEN.PRW).**

**Ambiente**

Microsiga Protheus - a partir da versão 12.  
   
 **Causa**

O problema ocorre por conta da variável **LCancel** ter sido declarada com a instrução "**Default**" (Default lCancel), algumas versões de binários não conseguem efetuar a leitura da mesma, gerando o erro.  
   
 **Solução**

Para solucionar essa ocorrência, realize os seguintes passos:  
 1. Faça o download do pacote mais atual do fonte CRMXFUNGEN : <https://suporte.totvs.com/portal/p/10098/download?e=732088> ;  
 2. Via TDS ou o antigo IDE, efetue a aplicação do pacote;  
 3. Faça o download do Binário (Server+Smartclient) mais recente no portal do cliente: <https://suporte.totvs.com/portal/p/10098/download?e=732088#000006/368/> ([Home](https://suporte.totvs.com/portal/p/10098/download?e=732088#)

[Protheus](https://suporte.totvs.com/portal/p/10098/download?e=732088#000006/)  [TOTVSTEC-FRAMEWORK](https://suporte.totvs.com/portal/p/10098/download?e=732088#000006/368/)) e atualize seu ambiente.

**OBS: Para realizar os procedimentos acima requer que o analista detenha conhecimento em estrutura de dados Protheus.**

**Em caso de dúvida dos processo citados,acionem a equipe de Framework para auxiliar.**
