---
article_id: 4419105155607
category: CRM - Dúvidas Gerais
content_hash: 2c444706a0534258f7c21be3a15a38bccdea81e9657cbee2a3a8d8c9b101053e
fetched_at: '2026-06-28T22:40:27.705896+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGACRM - Mensagem ao configurar a
  Rotina Contas a Receber no Perfil 360
type: support-article
updated_at: '2024-03-21T14:55:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4419105155607-Cross-Segmentos-Backoffice-Protheus-SIGACRM-Mensagem-ao-configurar-a-Rotina-Contas-a-Receber-no-Perfil-360
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22238894283927) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao cadastrar a rotina Contas a Receber (FINA040) para acesso através do Perfil 360, o sistema apresenta a mensagem: A BO selecionada não pertence ao módulo escolhido.

**Ambiente**Cross Segmentos - Backoffice Protheus - SIGACRM - A partir da versão 12  
  
**Causa**Alguns módulos realizam um controle de acesso às rotinas do sistema, dessa forma as rotinas não ficam disponíveis para acesso quando inseridas em módulos diferentes. Isso pode ocorrer ao configurar o acesso através do Perfil 360 ou do próprio menu da rotina.

A rotina Contas a Receber (FINA040) possui permissão para acesso a partir de alguns módulos onde ela, por padrão, já existe no Menu, quanto aos demais módulos que não possuem ela em seu menu, apresentam a mensagem de bloqueio de acesso.  
  
**Solução**Para os módulos que possuem bloqueio de acesso à rotina Contas a Receber (FINA040), é possível realizar a configuração de acesso à rotina Funções de Contas a Receber (FINA740), que possuem basicamente a mesma visualização dos títulos a receber.

A rotina Funções de Contas a Receber (FINA740) não possui bloqueio de acesso.
