---
article_id: 360041294494
category: NFe - Nota Fiscal Eletrônica
content_hash: b310cd818e24313d4eac83cea2fe3d3b55ae4bb3ae18a6c2c73511cfe414d2f1
fetched_at: '2026-06-28T22:40:01.755398+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar Dados
  da DI em informações complementares do Xml e no Danfe'
type: support-article
updated_at: '2021-10-11T18:56:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041294494--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-Dados-da-DI-em-informa%C3%A7%C3%B5es-complementares-do-Xml-e-no-Danfe
---

**Dúvida**Como gerar Dados da DI em informações complementares do Xml e no Danfe ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Neste caso deve alterar o seguinte parâmetro:

**MV\_DIDANFE = T** // Parâmetro para informar os dados da DI nas informações complementares do Xml/Danfe

Impressão dos dados da DI nas informações complementares do Danfe são os campos:

"Numero DI"  
"Local do Desembaraco'  
"UF do Desembaraco"  
"Data do Desembaraco"

* **Saiba mais:**

Podem ser utilizados os campos das documentações abaixo, para a gerar a mensagem:

[MP - NFE - Como gerar mensagem em informações complementares (TAG infcpl e infadfisco) do Danfe utilizando fórmula ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026944871)

[MP - NFE - Como gerar informações na TAG infCpl ou infAdFisco no XML e no DANFE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024950773)
