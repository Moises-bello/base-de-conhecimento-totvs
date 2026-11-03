---
article_id: 360018655832
category: CRM - Dúvidas Gerais
content_hash: 550f358d2ffb5240e722fc85647deca5cc0beda36b67be006fe16675e3f7dd94
fetched_at: '2026-06-28T22:40:27.560639+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: MP-CRM-Erro na inclusão do suspect
type: support-article
updated_at: '2021-04-28T14:50:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018655832-MP-CRM-Erro-na-inclus%C3%A3o-do-suspect
---

**Ocorrência**

Ao incluir um suspect é gerado o erro: argumento #6, parâmetrolShowBarerro, previstoL->A on FWFORMVIEW:ADDUSERBUTTON(FWFORMVIEW.PRW)  
   
 **Ambiente**

Microsiga Protheus - a partir da versão 12.  
   
 **Causa**O erro ocorre na montagem dos botões da opção outras ações.  
   
 **Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:  
 1. Efetue o download do pacote de atualização da rotina **TMKA341: <https://suporte.totvs.com/portal/p/10098/download?e=712003>**;  
 2. Aplique o pacote no RPO através do TDS ou Ide;  
 3. Reinicie o smartclient e refaça o processo.

OBS: Para aplicação de pacote, requer que o analista tenha conhecimento em estrutura de ambiente Protheus.

Sempre efetuar a aplicação do pacote em ambiente de homologação para validar e posteriormente, aplicar no ambiente de produção, efetuando o devido backup do ambiente.
