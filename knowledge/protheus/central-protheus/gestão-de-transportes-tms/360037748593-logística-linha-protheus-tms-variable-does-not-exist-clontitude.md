---
article_id: 360037748593
category: Gestão de Transportes (TMS)
content_hash: d2cd948061e48931f3622013f8a8343574c2a1d8e14b635677735646f38abedf
fetched_at: '2026-06-28T22:45:33.475189+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: 'Logística - Linha Protheus - TMS - variable does not exist CLONTITUDE '
type: support-article
updated_at: '2021-07-09T18:20:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037748593-Log%C3%ADstica-Linha-Protheus-TMS-variable-does-not-exist-CLONTITUDE
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:36 min**  
**Ocorrência**Na rotina **MATA030 - Cadastro de Cliente,** ao confirmar inclusão de cliente, ocorre o erro: **variable does not exist CLONTITUDE on { || TMSROT015(CFILENT,CENTIDA,CCODENT,CLATITUDE,CLONTITUDE) }** na rotina **TMSAO48 - Integração com a MapLink**  
  
**Ambiente**

TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - A partir da versão 12.1.25  
  
**Causa**O erro ocorre pois o fonte **TMSAO48 - Integração com a MapLink**foi liberado no repositório da versão 12.1.25 com esta inconsistência.  
  
**Solução**Para solucionar a situação, basta atualizar o repositório com o seguinte *patch*:

* [12.1.25 - TMSAO48 - 05/09/2019](https://suporte.totvs.com/portal/p/10098/download?e=817813)

Efetue *backup* do repositório antes de aplicar a atualização.
