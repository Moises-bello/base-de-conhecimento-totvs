---
article_id: 36452379791383
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 67f33eb9eaa34f972d58de0e1ca9875b0e8cb56ca421ae1502fa60dcc2292098
fetched_at: '2026-06-28T22:37:23.987008+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Os campos CN9_CLIENT
  e CN9_LOJACL podem ser utilizados ou habilitados para uso no Gestão de Contratos
  ?
type: support-article
updated_at: '2026-01-26T20:25:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36452379791383-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Os-campos-CN9-CLIENT-e-CN9-LOJACL-podem-ser-utilizados-ou-habilitados-para-uso-no-Gest%C3%A3o-de-Contratos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36452355925911) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**

Os campos CN9\_CLIENT e CN9\_LOJACL podem ser utilizados ou habilitados para uso no Gestão de Contratos ?

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

Atualmente no padrão do sistema, os campos CN9\_CLIENT e CN9\_LOJACL não possuem mais utilização e/ou gravação de informação pelos fontes padrões no sistema, e estes não devem ser utilizados, e nem serem referenciadas informações referentes a eles, visto que o sistema padrão não mais os utiliza.

No sistema atual as informações de Fornecedor/Cliente vinculados ao contrato são gravados na tabela CNC, onde são informados na Aba Fornecedor/Cliente no cadastro do Contrato da imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36452355926807)

E no caso, após incluir o cliente na aba "Clientes", o vinculo do código do cliente do contrato a cada planilha do contrato fica na tabela CNA, na Aba "Planilhas" da imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36452355928727)

Esta se trata da forma como o sistema padrão trabalha atualmente.

Caso se deseje possuir alguma informação referente Cliente ou Fornecedor no cabeçalho do contrato orienta-se serem criados campos customizados na tabela CN9 para utilização e preenchimento conforme a necessidade.

*Caso necessário apoio no desenvolvimento e adequações de tratativas customizadas do ambiente, é orientado a verificação e apoio junto a um analista especialista desenvolvedor em loco, através de seu ESN.*

***Obs:***

Mesmo que são campos já não utilizados pelo sistema, os campos CN9\_CLIENT e CN9\_LOJACL devem estar com seu cadastro conforme as informações abaixo para não causar problemas no uso do sistema:

Campo ***CN9\_CLIENT:***

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37948224614551)![](https://centraldeatendimento.totvs.com/hc/article_attachments/37948224617111)![](https://centraldeatendimento.totvs.com/hc/article_attachments/37948224619031)![](https://centraldeatendimento.totvs.com/hc/article_attachments/37948224621207)

Campo ***CN9\_LOJACL:***

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37948224622615)![](https://centraldeatendimento.totvs.com/hc/article_attachments/37948233195287)![](https://centraldeatendimento.totvs.com/hc/article_attachments/37948224629015)![](https://centraldeatendimento.totvs.com/hc/article_attachments/37948233197463)

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Documentação Gestão de Contratos do TDN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4441027145623)

[Guia de Referencia - Gestão de Contratos - Protheus 12](https://tdn.totvs.com/pages/viewpage.action?pageId=224127467)

[FAQs - Gestão de Contratos](https://tdn.totvs.com/x/O_tgDQ)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
