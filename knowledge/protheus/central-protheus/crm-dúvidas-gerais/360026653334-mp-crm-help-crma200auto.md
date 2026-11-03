---
article_id: 360026653334
category: CRM - Dúvidas Gerais
content_hash: 757cbbbbc2bdf314a0bb5ba2cba4c736710b09e61ec43995d537a17a4dd8d525
fetched_at: '2026-06-28T22:40:27.563222+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: MP-CRM-HELP CRMA200AUTO
type: support-article
updated_at: '2021-04-28T14:50:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026653334-MP-CRM-HELP-CRMA200AUTO
---

**Ocorrência**Ao excluir um cadastro de **prospect (TMKA260)**, o sistema mostra a mensagem "**CRMA200AUTO**" - Não foi possível executar a rotina automática Controle de privilégios :

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042554853/mceclip0.png)  
 **Ambiente**

Microsiga Protheus - a partir da versão 12.  
   
 **Causa**O Help ocorre devido a falta de atualização da da rotina CRMA200.  
   
 **Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

1. Baixe o pacote mais atual da rotina **crma200: <https://suporte.totvs.com/portal/p/10098/download?e=724313>**

2. Aplique o pacote, via TDS, em seu ambiente de testes para validação e posteriormente, no ambiente de prodição.

Obs:  A aplicação do pacote deve ser efetuado por um analista que detenha o conhecimento técnico para o procedimento, caso tenha dúvidas de procedimento, entre em contato com a equipe de FrameWork para auxiliá-lo.
