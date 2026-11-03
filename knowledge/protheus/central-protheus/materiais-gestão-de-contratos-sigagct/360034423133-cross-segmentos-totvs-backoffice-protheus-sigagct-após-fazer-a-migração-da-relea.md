---
article_id: 360034423133
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 706445ac8b604d7de50c64f10f6fdd20f6362a5bb47a4dab15fe3d67d38198ac
fetched_at: '2026-06-28T22:37:21.387116+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Após fazer a migração
  da release os gatilhos de usuários não existem mais no Gestão de Contratos
type: support-article
updated_at: '2022-05-19T21:07:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034423133-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Ap%C3%B3s-fazer-a-migra%C3%A7%C3%A3o-da-release-os-gatilhos-de-usu%C3%A1rios-n%C3%A3o-existem-mais-no-Gest%C3%A3o-de-Contratos
---

**Ocorrência**

Após fazer a migração da release os gatilhos de usuários não existem mais no Gestão de Contratos  
  
**Ambiente**Protheus– GCT – A partir da versão 12.1.23  
  
**Causa**No módulo **Gestão de contratos**, foi observado que ao fazer a **migração** da **release 12** para **12.1.23** os **gatilhos de usuários** não existem mais, dessa forma ao ser feito os processos no sistema as funcionalidades vinculadas aos gatilhos criados não estão de acordo com a regra de negócio implantada pelos clientes.

Os gatilhos de usuário, ***desde que cadastrados via configurador***, tem suas sequências alteradas para que fiquem após os gatilhos do produto, e não sejam alterados por gatilhos novos, isso acontece, pois a prioridade será sempre manter o padrão do sistema na respectiva release, considerando os novos gatilhos gerados pelo **UPDDISTR**.

**Solução**

Para solucionar essa ocorrência, é necessário identificar se ja existe uma linha utilizando a chave **X7\_CAMPO + X7\_SEQUENC** ( **campo + sequência** ) e assim fazer o ajuste necessário nas sequencias criadas

OBS:. Esse comportamento visa preservar eventuais modificações efetuadas nas tabelas pelos clientes usuários do sistema Protheus

Para mais detalhes saiba mais em: [Regras para atualização do dicionário SX7 - UPDDISTR e migrador de versão](http://tdn.totvs.com/pages/viewpage.action?pageId=255756976)

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
