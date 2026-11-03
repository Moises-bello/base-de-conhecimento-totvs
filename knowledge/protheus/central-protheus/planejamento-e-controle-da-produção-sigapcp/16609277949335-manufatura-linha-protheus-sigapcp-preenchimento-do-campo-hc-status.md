---
article_id: 16609277949335
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 756c635ac0ed21f3dcbe89b18cc92ab8796d305a1353df3a4679c465581bda80
fetched_at: '2026-06-28T22:42:45.726967+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Preenchimento do campo HC_STATUS
type: support-article
updated_at: '2023-08-09T21:37:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16609277949335-Manufatura-Linha-Protheus-SIGAPCP-Preenchimento-do-campo-HC-STATUS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16609337257623) Tempo aproximado para leitura: **00:00:46 min** **Dúvida**Quando o campo **HC\_STATUS - Status do Plano Mestre de Produção** é preenchido com a letra **E**, o que faz a legenda no **MATA750 - Manutenção do Plano Mestre de Produção** ser alterada para **executado**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**O campo **HC\_STATUS** tem seu conteúdo alterado para **E**, quando esse plano mestre de produção é importado para uma demanda no **PCPA136 - Demandas do MRP** e a partir dele através do **PCPA712-  MRP Memória** ou da rotina **ResultadoMRP - Resultados MRP** é gerada ordem de produção.
