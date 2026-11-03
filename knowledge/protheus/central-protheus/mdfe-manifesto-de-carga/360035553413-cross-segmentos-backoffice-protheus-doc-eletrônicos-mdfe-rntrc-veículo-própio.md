---
article_id: 360035553413
category: MDFe - Manifesto de Carga
content_hash: 3d2c7780fd751d5fa190910bed415012c48e168265e2db684c15808aed0117a4
fetched_at: '2026-06-28T22:40:08.331994+00:00'
product: protheus
section_id: 1500001549242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDFE - RNTRC Veículo
  Própio
type: support-article
updated_at: '2025-06-17T18:03:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035553413-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDFE-RNTRC-Ve%C3%ADculo-Pr%C3%B3pio
---

**Dúvida**É possível informar o RNTRC de veículo próprio para MDFE?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões

**Solução**Quando o veículo é próprio não gera o **RNTRC** no MDFE.  
  
Isso está no Manual de Orientação do Contribuinte da SEFAZ, versão 3.00a, página 21.  
  
O **RNTRC** é uma tag no XML dentro do Grupo <prop>, e o grupo <prop> só é preenchido quando o veículo não pertencer a empresa emitente do MDFE.  
  
![](https://totvssuporte.zendesk.com/attachments/token/IjtinPwoIiRsBpxw0koWyQRdU/?name=inline126066327.png)

No MOC 3.00a do MDFE outra vez menciona sobre o RNTRC do proprietário

![](https://totvssuporte.zendesk.com/attachments/token/WN5KyRKnP2aroMHctv8mbYAnP/?name=inline-1415519885.png)

Existe o RNTRC da empresa, que fica no cabeçalho do DAMDFE, deve preencher o RNTRC no cadastro da empresa no configurador. Preencher o campo M0\_RNTRC no sigamat.
