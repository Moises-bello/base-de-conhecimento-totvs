---
article_id: 4429843527447
category: Materiais - Compras (SIGACOM)
content_hash: 9d16e0641bd22cc058027f0efb677bab4555103117230d2f28ba585f0eb11ff6
fetched_at: '2026-06-28T22:41:08.728306+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Configuração para XML
  do Fornecedor com segunda unidade de medida no Importador XML
type: support-article
updated_at: '2025-11-19T17:42:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4429843527447-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Configura%C3%A7%C3%A3o-para-XML-do-Fornecedor-com-segunda-unidade-de-medida-no-Importador-XML
---

**Dúvida**

Como configurar para que o sistema reconheça a segunda unidade de medida ao realizar a integração da nota com o Importador XML/ TOTVS Colaboração?

**Ambiente**Protheus – Compras – A partir da versão 12

**Solução**

**Para o calculo da Segunda Unidade de Medida, seguir o passo a passo abaixo;**

**1. Cadastro de Produto x Fornecedor**

    O campo A5\_UMNFE/A7\_UMNFE será verificado qual unidade de medida vem o XML.

**OBS:** O campo A5\_UNID é preenchido com a unidade de medida utilizada pelo seu fornecedor.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23634660727959)

**1. Cadastro de****Produto x Cliente**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23634660742935)

**2)** No cadastro de produto, deverá ser informado a segunda unidade de medida e seu fator de conversão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23634685738007)

**3)** Na importação da NFE e/ou CTE, sera verificado a existência dos campos DT\_UM / DT\_SEGUM / DT\_QTSEGUM

**3.1)** Não existe o campos: Nenhuma conversão sera realizada. Portanto será necessário criá-los:

| Campo: | DT\_UM |
| --- | --- |
| Tamanho: | 2 |
| Descrição: | Unidade de Medida |
| Grupo de Campo: | 122 (Unidade de Medida) |

| Campo: | DT\_SEGUM |
| --- | --- |
| Tamanho: | 2 |
| Descrição: | Segunda Unidade de Medida |
| Grupo de Campo: | 122 (Unidade de Medida) |

| Campo: | DT\_QTSEGUM |
| --- | --- |
| Tamanho: | 14 |
| Decimal | 2 |
| Descrição: | Qtde Segunda Unidade de Medida |

**OBS: Ao precisar criar os campos, orientamos que seja feito a exclusão dos documentos no monitor que foram integrados e precisam que a segunda unidade de medida, seja indicada para que os campos referentes a unidade de medida sejam preenchidos corretamente, assim evitando problemas na geração do documento.**

**3.2)** Existe os campos: Existindo no cadastro de produto a informação da segunda unidade de medida, sera feita a conversão e sua quantidade convertida.

**4)** Os campos referente a segunda unidade de medida, são enviados para os campos respectivos na SD1 (Itens da NFE/CTE), conforme padrão do Documento de Entrada e Conhecimento de Frete.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4429838374679)

***Importante:***

Para o correto funcionamento, deve-se no cadastro de produto, deve-se possuir corretamente informado  a segunda unidade de medida e seu fator de conversão,

Para o apoio nesta configuração do cadastro de produtos, pode-se verificar junto ao Suporte ao módulo de Estoque/Custos.

Nesta configuração, o sistema entenderá que a quantidade vinda no XML é na segunda unidade do cadastro do Produto no Protheus, e na inclusão na NF será gatilhada automaticamente a quantidade da primeira unidade de medida baseado nas configurações do fator de conversão do cadastro de Produto.

***Obs1*:** Os fontes MATA140I, MATA116I e COMXCOL com data superior a 19/09/2019

***Obs2*:**Para que a conversão para a segunda unidade de medida funcione corretamente, é obrigatório informar o código do Produto do Fornecedor no campo  **"Cod.Prod.For"** do cadastro da amarração Produto x Fornecedor. Para maiores informações sobre o cadastro a Amarração Produto x Fornecedor, verifique documentação abaixo.

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML - Amarração de Produto x Fornecedor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22924903652887-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML-Amarra%C3%A7%C3%A3o-de-Produto-x-Fornecedor)

***Saiba Mais :***

[TC07008 - Totvs Colaboração - Segunda unidade de medida](https://tdn.totvs.com/x/_pi8Hg)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
