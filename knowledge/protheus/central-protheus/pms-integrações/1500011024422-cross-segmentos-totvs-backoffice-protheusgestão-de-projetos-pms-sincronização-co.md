---
article_id: 1500011024422
category: PMS - Integrações
content_hash: ff9aee9de1541a3d375b91309f343de42355935dc98c88a7d444b05579f8c875
fetched_at: '2026-06-28T22:37:16.743976+00:00'
product: protheus
section_id: 1500001550742
source: central-protheus
title: Cross Segmentos/ Totvs BackOffice Protheus/Gestão de Projetos - PMS - Sincronização
  com o Project
type: support-article
updated_at: '2021-05-17T13:39:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011024422-Cross-Segmentos-Totvs-BackOffice-Protheus-Gest%C3%A3o-de-Projetos-PMS-Sincroniza%C3%A7%C3%A3o-com-o-Project
---

**Ocorrência**Ao Sincronizar o Project  no SigaPMS , caso o parâmetro **MV\_PMSTX30** = .T.  a estrutura no Projeto do PMS fica errada.  As Edts que contém no Microsoft Project, ficam como tarefa na estrutura do Protheus.  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) -Gestão de Projetos - a partir da versão 12.  
  
  
**Solução**

Se utilizar esta integração com o **MV\_PMSTX30 = .T.** é necessário utilizar o processo novo de integração configurado também, com o  parâmetro **MV\_PMSXMSP = 1.**

**Saiba mais: [Novas funcionalidades de integração com o MSProject](https://tdn.totvs.com/pages/releaseview.action?pageId=51249645)**
