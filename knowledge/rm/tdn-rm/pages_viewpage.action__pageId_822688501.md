---
content_hash: d98682674c664caecbe3505caddad8b6d6cb5cf76e8f355dd7ff3f0d1627de69
fetched_at: '2026-06-29T00:11:46.512175+00:00'
page_id: '822688501'
product: rm
source: tdn-rm
title: valores/vServPrest
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822688501
version: 11
---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Pai | Obrigatório | Origem | Descrição |
| **vServPrest** | **DPS/infDPS/valores** | **Sim** | **Grupo** | **Grupo de informações relativas ao endereço do tomador da nota.** |
| vReced | DPS/infDPS/valores/vServPrest | Não | Valor monetário recebido pelo intermediário do serviço (R$). | **Não será gerado.** |
| vServ | DPS/infDPS/valores/vServPrest | Sim | Valor monetário do serviço (R$) | Se o tipo de movimento estiver habilitado o campo edita preço total e preço total for maior que zero o campo será preenchido com o valor total dos itens senão ele irá preencher o campo com a fórmula (quantidade \* valor unitário do item) |

vServ - Valor monetário do serviço

É permitido parametrizar um movimento com um ou mais serviços. Porém, de acordo com o layout da nota de serviço nacional, apenas é permitido um serviço por nota e apenas uma tag de serviço por nota (diferente do layout único, que permite inclusão de N tags de serviço).   
Caso sejam cadastrados dois ou mais serviços em um movimento, a tag vServ irá **somar** o valor de todos os serviços, independentemente de seu código ou parametrização, o que pode gerar valores incorretos a serem demonstrados na nota.
