---
content_hash: 7f203051c87d36cab115300aa32005f24ec9c529e5ad79fcfb5cf6b75c066ae2
fetched_at: '2026-06-29T00:11:12.265035+00:00'
page_id: '65208891'
product: rm
source: tdn-rm
title: NF-e - xPed (numero do pedido de compra) e nItemPed (item do pedido de compra)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=65208891
version: 4
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | NF-e                        **Versão:***a partir 11.40* |
| **Processo** | **:** | xPed (numero do pedido de compra) e nItemPed (item do pedido de compra) |
| **Subprocesso** | **:** | xPed (numero do pedido de compra) e nItemPed (item do pedido de compra) |
| **Data da publicação** | **:** | 05/07/2013 |

**Introdução:**

No layout da NF-e 2.00 foram criados dois campos para as empresas que desejam informar na Nota o número e item do pedido de compra. Este campo é opcional e para levado no XML basta seguir este procedimento.

**1º Passo:**Criar dois campos complementares no produto **ou no item de movimento**:

É necessário criar dois campos complementares do tipo texto no produto com os nomes XPED e NITEMPED

*****Acesse o RM Nucleus no seguinte menu: Cadastros / Campos Complementares / Produtos*******ou  ***Cadastros / Campos Complementares / Itens de Movimentos.*****

Procedimento para criação dos dois Campos Complementares:

Clique na opção “Novo” (Incluir), em “Nome da Coluna” preencha “XPED” em “Descrição” preencha “XPED”. Clique em “Salvar”.

Para incluir o segundo, clique novamente em “Novo” (Incluir), em “Nome da Coluna” preencha “NITEMPED” em “Descrição” preencha “NITEMPED” e clique em “Salvar”.

**Parametrização no produto**: no cadastro de Produtos aba “Campos complementares” existem estes dois campos e sempre que estiverem preenchidos serão levados no XML da Nota.

**Parametrização do item de movimento**: acesse os parâmetros do tipo de movimento opções | parametros | RM Nucleus | selecione onde esta o tipo de movimento (compra, venda ou outras movimentações) edite o tipo de movimento - etapa "item - campos complementares", e inclua os campos criados.

OBS: O Preenchimento destes campos (tamanho mínimo e máximo) deve seguir as regras do manual de integração 5.00 que define a NF-e 2.00

**Para maiores informações:**

**[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)** 

**COMUNIDADE **R**[@](https://totvs.byyou.com/?space=rnfe)Nfe**

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções: 2 – (Software), 2 – (Suporte Técnico), 3 - (RM), 3 - (Fiscal), 3 - (Nota Fiscal Eletrônica)
