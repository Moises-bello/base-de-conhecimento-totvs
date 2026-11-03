---
article_id: 4402441230359
category: TAF - REINF
content_hash: 2654b0101f3f88236d3d1144174bde0c841abc2089993a1483c518fc0f71197a
fetched_at: '2026-06-28T22:41:34.683259+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Failed to locate the
  main Schema Resource
type: support-article
updated_at: '2023-08-10T20:15:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402441230359-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Failed-to-locate-the-main-Schema-Resource
---

**Ocorrência**Ao transmitir algum evento da Reinf, está ocorrendo Failed to locate the main Schema Resource

**Ambiente**TAF - SIGATAF - A partir de 12.1.33  
  
**Causa**

Esse erro ocorre quando o TSS não está atualizado para a reinf 1.5.

**Solução**

![XSD.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12250070705175)

1) O parâmetro **MV\_TAFVLRE**precisa estar com o conteúdo**1\_05\_01**

* [TAF - CONFIGURADOR - Como acessar os parâmetros do sistema?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036109233-TAF-CONFIGURADOR-Como-acessar-os-par%C3%A2metros-do-sistema-?source=search)

2) É **obrigatório** a atualização do TSS, caso contrário ocorrerá erro de Schema nos eventos. Os schemas do layout 1.5 possuem o nome do **evento + nome do schema,** não devem ser renomeados. É um novo padrão da Receita Federal,

Para corrigir:

Atualização dos Schemas:

[TSS - Atualização dos SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552-TSS-Atualiza%C3%A7%C3%A3o-dos-SCHEMAS?source=search)

Atualização RPO

[MP - TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS?source=search)

Após a atualização, a **apuração** do evento inconsistente deverá ser **excluída**, após, **apurar** e **transmitir** novamente.
