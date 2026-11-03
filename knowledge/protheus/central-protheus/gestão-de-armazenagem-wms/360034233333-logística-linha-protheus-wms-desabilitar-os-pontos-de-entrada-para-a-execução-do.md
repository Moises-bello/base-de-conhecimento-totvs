---
article_id: 360034233333
category: Gestão de Armazenagem (WMS)
content_hash: e1888ecd6c23ba5f65b51a6d91b13b4f1c86e4b2ca9be343210e19c02eaaf9dc
fetched_at: '2026-06-28T22:45:48.006935+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Logística - Linha Protheus - WMS - Desabilitar os pontos de entrada para a
  execução do processo
type: support-article
updated_at: '2022-11-08T13:11:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034233333-Log%C3%ADstica-Linha-Protheus-WMS-Desabilitar-os-pontos-de-entrada-para-a-execu%C3%A7%C3%A3o-do-processo
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)***Tempo aproximado para leitura: **00:00:25 min****Dúvida**Como desabilitar os **pontos de entrada** para a execução do processo?  
  
**Ambiente**TOTVS Logística - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (WMS) -  A partir da versão 11.80  
  
**Solução**Basta adicionar a chave **IXBLOG=NORUN** no final das configurações do ambiente ou do *environment*, no arquivo **AppServer.ini**. Não é necessário reiniciar o serviço!  
  
**Importante**  
Este comando **IXBLOG** vai permitir que a rotina seja executada sem as customizações.
