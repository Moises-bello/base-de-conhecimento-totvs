---
article_id: 360021545931
category: CRM - Dúvidas Gerais
content_hash: b2a096f3f28b395785469846499b46e08ac9079525befe114ab75674f7fb4167
fetched_at: '2026-06-28T22:40:27.747415+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: MP - CRM - Vincular o acessório TMKA030 na Proposta Comercial
type: support-article
updated_at: '2021-04-28T14:50:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021545931-MP-CRM-Vincular-o-acess%C3%B3rio-TMKA030-na-Proposta-Comercial
---

**Dúvida**

Processo para vincular os acessórios do produto na proposta comercial  
   
 **Ambiente**  
Protheus – CRM – A partir da versão 12.1.17  
  
   
**Solução**

Para os acessórios sejam automaticamente carregados na proposta comercial, efetue o seguinte processo:

• Ative os seguintes parâmetros: **MV\_HABACES** = **.T.**  e **MV\_KIT** = **S.**

• Inclua o acessório por meio da rotina **TMKA030,** informando o produto principal na tabela **SUG,** os acessórios na tabela **SU1** e deixe o campo **U1\_KIT**= **sim.**

• Inclua uma tabela de preço (OMSA010) para todos os produtos acessórios e informe também o produto principal.

• Na rotina **FATA300,** ao incluir a proposta comercial, coloque a tabela de preço com todos os produtos (ADY\_TABELA) e informe o produto principal no campo **ADZ\_PRODUTO.** Todos os componentes deste Kit serão carregados automaticamente na aba **Acessórios.**

**Obs:**Na versão 12, a rotina TMKA030 (Acessórios) está no módulo SIGACRM, localizada no menu Atualizações/ Administração/ Portfólio/ Acessórios.

Saiba mais: <http://tdn.totvs.com/pages/viewpage.action?pageId=243630998>
