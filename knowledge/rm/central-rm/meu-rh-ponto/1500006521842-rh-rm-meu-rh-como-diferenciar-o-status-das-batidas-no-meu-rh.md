---
article_id: 1500006521842
category: Meu RH - Ponto
content_hash: f20138dcf8c55caddf91a63634433771dd0f4d3b8d25e08668e86628ca17828d
fetched_at: '2026-06-28T22:47:30.393917+00:00'
product: rm
section_id: 1500000861782
source: central-rm
title: RH - RM - Meu RH - Como diferenciar o status das batidas no Meu RH
type: support-article
updated_at: '2025-02-10T12:03:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006521842-RH-RM-Meu-RH-Como-diferenciar-o-status-das-batidas-no-Meu-RH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:03:46 min**

**Dúvida**O que é e qual a diferença do status das batidas realizadas no Meu RH?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir da versão 12.1.23

**Solução**As batidas com o status de coletadas tem origem do arquivo **AFD -** **Arquivo Fonte de Dados** importado utilizando o processo de importação de batidas. As batidas inseridas por geolocalização também são consideradas como Coletadas.  
  
As batidas inseridas de forma manual utilizando o sistema , Portal RH e Meu RH são consideradas digitadas por não terem sido importadas pelo relógio de ponto conforme rege as portaria 671.  
  
Não é permitido alteração do horário do registro da batida e nem exclusão da batida digitada manualmente via Meu RH após a sua aprovação e nem das inseridas por geolocalização. Somente será permitido alterar a sua natureza.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008656321/mceclip0.png)  
  
Esta alteração e exclusão somente é possível via sistema RM no módulo **Automação de Ponto** ou em caso das batidas inseridas por geolocalização podem ser desconsideradas pelo gestor.  
  
Hoje é possível diferenciar através  de símbolos as batidas por geolocalização das digitadas manualmente na apresentação do espelho de ponto no Meu RH. As registradas por geolocalização são apresentadas com este símbolo verde de localização as digitadas manualmente não apresentam este símbolo.  
  
![](https://totvssuporte.zendesk.com/attachments/token/qo4vysIBcj4dLQ6yJwcxkLMX6/?name=inline-294607099.png)  
  
Via sistema RM  não é possível obter a mesma visualização. As batidas registradas por geolocalização ficam armazenadas na tabela APORTARIA373 e seu registro na tabela **ABATFUN** a coluna **IDAPORTARIA373** terá preenchido o valor do ID informado na tabela APORTARIA373. 

Também podem ser consultadas gerando o relatório de espelho da portaria 373p presente na aba relatório do modulo **Automação de Ponto**.

**Observação:** As batidas inseridas por Geolocalização passaram a ser consideradas como Coletadas a partir da **versão** 12.1.29.254 disponibilizada em Maio de 2021, anteriormente elas eram consideradas como Digitadas.   
  
**Saiba mais**  
[9.0 Relógio Batidas Remotas - Portaria 373/2011](https://tdn.totvs.com/pages/viewpage.action?pageId=334338837)
