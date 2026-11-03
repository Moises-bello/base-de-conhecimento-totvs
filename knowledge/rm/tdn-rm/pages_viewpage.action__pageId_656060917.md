---
content_hash: abf29ae2283e6a470040e264fab7a5c6b2a2d70e469e3fb9149bef4367779700
fetched_at: '2026-06-29T00:11:12.678701+00:00'
page_id: '656060917'
product: rm
source: tdn-rm
title: Cadastro de usuários, grupos e imobiliárias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=656060917
version: 22
---

Para que os usuários tenham acesso ao portal é importante cadastrá-los no Portal de Imóveis, para isto acesse Backend> Usuários e adicione as informações solicitadas. 

#FF9000Usuários

Na tela de entrada dos dados de cadastro do usuário, na parte inferior, é apresentado uma tela denominada, mapa de permissão de grupos visualizados, esta opção serve para indicar quais grupos de usuários este novo usuário poderá selecionar se ele puder incluir novos usuários. 

Isto se faz necessário para evitar que ele possa criar um usuário no grupo administrador e ter acessos indesejados ao sistema. Portanto se no MAPA DE PERMISSOES DE GRUPOS estiver marcado somente o grupo CORRETORES para o usuário criado e se ele puder incluir novos usuários ele poderá selecionar somente o grupo CORRETORES para os usuários criados por ele.

O Portal de Imóveis permite que usuários possam ter uma hierarquia infinita de superiores definida através do campo SUPERIOR, onde é selecionado o usuário que é superior ao que está sendo cadastrado. Por padrão um usuários que está acima de você pode ver todas as suas ações no Portal de Imóveis, portanto seu supervisor vê todas as pessoas que você está tratando e todas as propostas e reservas feitas por você.

Durante o cadastro do usuário, se for associado um CPF ou CNPJ, o Portal de Imóveis irá validar a existência deste dado no RM no cadastro de vendedores, caso não exista, ao salvar o registro o Portal de Imóveis demonstrará a mensagem abaixo mas o cadastro será feito normalmente

#FF9000Grupos

No cadastro de grupos definidos as permissões de acesso dos usuários. O Portal de Imóveis já traz por padrão grupos de usuários definidos, como Administrator, Corretor, Gerente e Diretor. O grupo Administrador tem permissão em todas as opções e visões do sistema.

#FF9000Imobiliárias

Um usuário pode estar relacionado a uma imobiliária durante seu cadastro, portanto é necessário definirmos quais são as imobiliárias que atuam no Portal de Imóveis. Para cada imobiliária cadastrada podemos limitar quais empreendimentos ela pode ver e atuar.  Para parametrizar esta situação, primeiro salve os dados da imobiliária em cadastro e depois edite este registro e selecione quais empreendimentos ela terá acesso. Se nenhum empreendimento for selecionado a imobiliária terá acesso a todos.

**A partir da versão 12.1.2506:**

Ao cadastrar ou editar um usuário no sistema, é possível definir quais empreendimentos ele poderá visualizar e trabalhar.  
Essa configuração depende do campo Imobiliária dentro do cadastro do usuário.

A seguir, veja como o sistema se comporta:

##### 1. Quando uma Imobiliária é selecionada

Se o usuário tiver uma imobiliária definida no cadastro (ou seja, o campo **Imobiliária** estiver preenchido):

* O sistema procura essa imobiliária na lista geral de imobiliárias cadastradas.

* Quando encontra, o sistema **carrega automaticamente todos os empreendimentos que pertencem àquela imobiliária**.

* Esses empreendimentos são exibidos para você na tela, para que você possa definir quais deles o usuário terá acesso.

**Exemplo:** Se você escolher a Imobiliária *"Alfa Imóveis"*, o sistema mostra somente os empreendimentos da *Alfa Imóveis*.

##### 2. Quando nenhuma Imobiliária é selecionada

Se o campo **Imobiliária** estiver vazio (*null* ou não preenchido):

* O sistema junta todos os empreendimentos de todas as imobiliárias cadastradas.

* Remove entradas repetidas.

* Mostra ao usuário **a lista completa de empreendimentos disponíveis no sistema**.

**Exemplo:** Se você não escolher nenhuma imobiliária, o usuário terá acesso para selecionar empreendimentos de **todas** as imobiliárias.

Mesmo que o campo **Imobiliária** esteja vazio (*null*) e nenhum empreendimento tenha sido selecionado, caso o usuário possua permissão vinculada a um empreendimento inativo, o sistema exibirá a mensagem **'Não existem empreendimentos ativos'** em vez de listar todos os empreendimentos

##### O que isso significa no dia a dia?

* A lista de empreendimentos **sempre muda automaticamente** conforme você escolher (ou não) uma imobiliária.

* Isso deixa o cadastro mais rápido e evita erros.

* Você não precisa saber quais empreendimentos pertencem a qual imobiliária — o sistema já faz essa filtragem para você.

#### Resumo:

| Situação | O que o sistema faz? |
| --- | --- |
| **Imobiliária selecionada** | Mostra apenas os empreendimentos daquela imobiliária |
| **Imobiliária não selecionada** | Mostra todos os empreendimentos do sistema |
| **Imobiliária não encontrada** | Não mostra empreendimentos (lista vazia) |

##### Impacto de não informar Imobiliária para quem utiliza PI → RM (TCGI) com cálculo de comissão:

##### Para bases integradas PI → RM TCGI, onde existem funcionalidades de equipe, orientador e cálculos de comissão, deixar um usuário sem imobiliária definida causa impactos importantes:

##### Consequências de deixar “Imobiliária” vazia:

* ##### O usuário não será vinculado a uma equipe, pois a imobiliária é usada como referência para montar a estrutura das equipes.
* ##### Ele não poderá ter orientador de equipe.

* ##### Os cálculos de comissão podem ficar incompletos ou incorretos, pois: metas e gatilhos são organizados por imobiliária/equipe, a ausência de imobiliária impede o vínculo correto do usuário à lógica de cálculo.

**Impacto na Roleta de Vendas**  
A lista de empreendimentos configurada no cadastro do usuário também impacta a distribuição da Roleta de Vendas.  
Se o corretor não possuir acesso ao empreendimento do lead, o sistema não realizará a distribuição para esse usuário naquele giro, mesmo que ele esteja ativo na equipe e corretamente posicionado na ordenação da roleta.

##### Se o usuário participa de equipes, metas, comissões ou orientações, a Imobiliária deve sempre ser selecionada.

---

Mais informações

* [Portal de Imóveis - Backend - Usuário](https://tdn.totvs.com/pages/viewpage.action?pageId=563947988)
