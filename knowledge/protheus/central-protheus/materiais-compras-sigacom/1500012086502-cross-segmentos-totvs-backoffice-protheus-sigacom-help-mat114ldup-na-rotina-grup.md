---
article_id: 1500012086502
category: Materiais - Compras (SIGACOM)
content_hash: 3758cf6c8cad7e58c18aaf11aabee17a2d0562747918b5a261681b6d71cc3cf0
fetched_at: '2026-06-28T22:41:18.931294+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help MAT114LDUP na
  rotina Grupo de Aprovadores MATA114
type: support-article
updated_at: '2025-06-10T12:17:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012086502-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-MAT114LDUP-na-rotina-Grupo-de-Aprovadores-MATA114
---

**Dúvida**

Como proceder quando acontecer o Help MAT114LDUP na rotina Grupo de Aprovadores MATA114 ?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões]  
  
**Solução**

O Help MAT114LDUP é disparado, devido ao centro de custo ou conjunto de entidades contábeis da linha informada na aba "Entidades Contabeis" digitados já estar vinculado à algum grupo de aprovadores cadastrado.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019509721)

Dessa forma deve ser analisado os grupos de aprovação existentes, e ser informado um novo centro de custo ou combinação de entidades contábeis que não exista neste grupo de aprovação que está incluindo/alterando ou em qualqer outro grupo de aprovação já cadastrado.

**Importante:**

Caso tenha a necessidade de utilizar grupos de aprovação com a mesma entidade contábil para 'Rotinas' do sistema diferentes com perfis de aprovação diferentes, poderá realizar o processo abaixo:

**Exemplo:**

Para que possa criar um grupo para Solicitação de compras com Perfil de aprovação 0,00 a 999999999999,99 e outro Grupo de aprovação com Perfil de aprovação de 0,01 a 1.500 para Pedido de compras é necessário configurar na Aba **Tipo de Documentos**do grupo de aprovação apenas para a Rotina específica  para cada grupo , por exemplo abaixo criei um grupo apenas flegando a opção  solicitação de compras com o centro de custo 000003

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32710146825239)

Se for tentar cadastrar um  Grupo de aprovação que possuir a mesma entidade contábil e que tenha a mesma Rotina flegada nos 2 grupos ao tentar salvar será apresentado o Help "MAT114LDUP".

***Obs1:***

Para verificar quais grupos possuem a mesma chave/combinação de entidades, pode-se verificar na tabela DBL quais são os grupos que tem relação com a chave/combinação de entidade.

***Obs2:***

Caso haja na tabela DBL combinação de entidades de forma repetida que possa ter sido incluídas por manipulação de registros (**procedimento não recomendado**) diretamente na tabela (onde por ter sido feita "manualmente" não passou pelas validações das regras de negócio da rotina), ou já haja esses registros de combinação de entidades repetidas por qualquer outro motivo, o help também poderá ocorrer devido a esses registros repetidos já existentes, mesmo que a entidade/combinação que está sendo incluida no momento não seja repetida no cadastro.

***Obs3:***

Por padrão da rotina, é permitida a inclusão de uma mesma combinação de entidades contabeis em grupos diferentes, apenas quando na Aba "Tipos de Documentos" dos dois grupos de aprovação não haja nenhum tipo de documento em comum selecionado, ou seja, os grupos de aprovação não podem ter o mesmo tipo de documento selecionado ao mesmo tempo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32710146826775)

Mesmo que haja regra de Tipo de Compras diferenciando dois grupos de aprovação, caso esteja um mesmo tipo de documento selecionado na aba "Tipos de Documentos" e houver uma mesma combinação de entidades contabeis na aba "Entidades Contabeis", ocorrerá o help "MAT114LDUP" não permitindo esta inclusão de cadastro, conforme é o conceito da rotina.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM)
