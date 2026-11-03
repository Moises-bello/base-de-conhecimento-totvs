---
article_id: 1500003510842
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 3a10d4395b217c584e78d61b023bd91f158700eba2e3d9fc497b5d2407b53b0e
fetched_at: '2026-06-28T22:37:21.347763+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Ao incluir  um contrato
  e/ou aprovação de revisão com caução, é apresentado  o Help CNTA100MIN '
type: support-article
updated_at: '2025-04-25T12:03:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003510842-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Ao-incluir-um-contrato-e-ou-aprova%C3%A7%C3%A3o-de-revis%C3%A3o-com-cau%C3%A7%C3%A3o-%C3%A9-apresentado-o-Help-CNTA100MIN
---

**Dúvida**

Ao incluir um contrato e /ou aprovar a revisão com caução, é apresentado o Help CNTA100MIN

**Ambiente**

Microsiga Protheus – Gestão de Contratos – A partir da versão 12  
  
**Solução**

Para corrigir este Help, realize os seguintes passos:

1. Habilite o parâmetro **MV\_CNRVCAU** com conteúdo .T. para que possa habilitar a revisão de caução.

2 . Ao incluir um contrato com caução, informe:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003538342/mceclip0.png)

Ao tornar o contrato vigente, será disparado o Help: CNTA100MIN

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003538402/mceclip3.png)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360104597173/mceclip4.png)

 Acesse a rotina do cadastro de caução, e efetue o cadastro.

O campo Vlr. Efetivo deverá ser preenchido com o valor correspondente do percentual informado no campo % caução do cadastro de contrato, exemplo:

   CNA\_VLTOT      = Valor contrato: 1.000,00

   CN9\_MIMCAU = % caução  : 10%

   CN8\_VLEFET    = Vlr Efetivo  : 100,00

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003586381/mceclip5.png)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102419154/mceclip7.png)

Ao executar uma revisão de contrato, alterando o % de caução de 10% ( origem ), para 20% e executar uma aprovação, o sistema apresentará o  mesmo Help, mas apontando qual valor mínimo que  deverá ser incluído no cadastro de caução.

Ou seja, ao revisar um contrato, obrigatoriamente deverá ser criado novo  cadastro de caução respectivo com o valor mínimo

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003539162/mceclip8.png)

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360104598233/mceclip9.png)

Solução:  Informar o valor correspondente do % do caução.

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003539602/mceclip10.png)

***Saiba Mais:***

[Tipos de Revisões de Contrato - CNTA010 - Gestão de Contratos - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=224447795)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
