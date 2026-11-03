---
article_id: 360050981013
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 07d513392949181a0f3f2921909e8fdc14935a4e478628957738ff06fde98b83
fetched_at: '2026-06-28T22:38:44.000736+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Atualizar a database do Smartclient
  na geração de Documento de Saída
type: support-article
updated_at: '2025-06-25T14:39:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050981013-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Atualizar-a-database-do-Smartclient-na-gera%C3%A7%C3%A3o-de-Documento-de-Sa%C3%ADda
---

**Dúvida**

Atualizar a database do Smartclient na geração de Documento de Saída.  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12  
  
**Solução**

O que define a **alteração da Data Base** na virada do dia para **emissão do Documento Fiscal de Saída** é o parâmetro **"MV\_NFS36"**.

* **MV\_NFS36 = 1**- A alteração da Data Base ocorrerá apenas para os usuários que **NÃO** possuírem o Acesso 36 (Alterar Data Base do Sistema) no Configurador (SIGACFG).
* **MV\_NFS36 = 2** - A alteração da Data Base ocorrerá para **TODOS** os usuários, **independente** **da** **configuração** do Acesso 36 (Alterar Data Base do Sistema) no Configurador (SIGACFG).
* **MV\_NFS36 = 3** - Não será alterada a Data Base.
