---
content_hash: bb2900028e4736d14e72c395c1d2d7b260e56086f14d20d94a6c2e6563edf0df
fetched_at: '2026-06-29T00:10:51.260041+00:00'
page_id: '563947988'
product: rm
source: tdn-rm
title: Portal de Imóveis - Backend - Usuários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=563947988
version: 63
---

Nesta tela temos o controle de usuários do Portal de Imóveis, que é dividida em três abas, sendo elas Usuários, Grupos e Imobiliárias.ÍndiceX| Usuários

Na aba de Usuário, encontram-se os seguintes campos informativos:

* **Grupo:** Esta seção exibe o grupo ao qual o usuário pertence. Caso seja necessário criar um novo grupo, utilize o botão "Adicionar Grupo" na aba correspondente. Ao cadastrar um novo grupo, você pode definir uma série de parâmetros que estarão associados aos usuários que pertencem a esse grupo.
* **Imobiliária:** Esta informação indica em qual imobiliária o usuário está registrado. Na mesma visão, é possível adicionar uma nova imobiliária clicando no botão "Adicionar Imobiliária" na aba específica.
* **Reservas:** O número apresentado nesta seção indica a quantidade de reservas simultâneas de unidades que o usuário pode realizar.
* **Comissão:** Refere-se ao percentual de comissão definido no cadastro do usuário.
* **Superior:** Esta entidade está hierarquicamente acima do usuário em questão. O superior terá acesso a todas as informações do usuário e será o contato imediato para qualquer comunicação ou pedido. Por exemplo, se um corretor realiza uma venda com um desconto de 5% e a proposta não é aprovada, o corretor pode solicitar a aprovação ao supervisor associado.

Ao acessar o portal e se a mensagem for exibida, será necessário efetuar uma ajuste na parametrização.

***"O sistema está desativado no momento. Se necessário, entre em contato com a equipe de TI ou administrador do sistema."***

Acesse *Backend > Parâmetros > Sistema* e localize sistema ativo (Alterando para SIM), esta parametrização possibilitará usuários que não possuem acesso ao backend acessem o sistema.

| Grupo Usuários Administradores

### Edição de Propostas por Administradores no Portal de Imóveis

No Portal de Imóveis, administradores têm acesso completo para gerenciar propostas criadas por qualquer corretor. Isso garante flexibilidade e agilidade no gerenciamento de negociações imobiliárias.

#### Como editar uma proposta

Acesse o Portal de Imóveis e faça login com seu usuário e senha de administrador.

Localize a proposta que deseja editar.

Use os filtros de pesquisa para encontrar a proposta, como:

* Nome do cliente.
* Identificação do corretor responsável.
* Status da proposta (em andamento, concluída, etc.).

Importante

* Como administrador, você tem acesso a todas as propostas, sem restrições, mesmo que não tenha sido o corretor original que as cadastrou.
* Certifique-se de revisar as alterações antes de salvá-las para evitar inconsistências nos dados da proposta.

#### Exemplo de cadastros no PI.

* Mestre ( Adm do Sistema )
* Corretor ( Somente proposta do Corretor )
* SCORRETOR ( Superior do Corretor que poderá ver tanto a proposta dele como do Corretor )
* Diretor ( Somente proposta do Diretor )

Localizar o Grupo do usuário desejado.  
**Neste primeiro caso , vamos no Grupo do Administrador do PI.**

PI Base Apartada - Administrador

Ao deixar todos os papéis exercidos desmarcados, o usuário passará a possuir perfil de **Administrador**. Nesse cenário, a validação referente ao bloqueio de propostas para prospects vinculados a outros corretores não será aplicada.

**Exemplo:**  
O usuário possui a permissão **"Trocar corretor da proposta"** habilitada e a permissão **"Pode salvar proposta c/ prospect de outro corretor"** desabilitada. Ainda assim, caso todos os papéis exercidos estejam desmarcados, o sistema permitirá o cadastro de propostas para o mesmo prospect utilizando corretores diferentes.

Esse comportamento ocorre apenas para a validação em que o proponente está vinculado a outro corretor e o sistema está configurado para não permitir propostas para prospects de outros corretores.

Caso seja necessário restringir esse comportamento, recomenda-se marcar ao menos um papel exercido para o usuário. Dessa forma, o sistema passará a respeitar as permissões configuradas para o grupo e para o usuário.

---

PI Base Unificada - Administrador

No grupo de usuários do ADM.

* Permissões: Proposta
* Marcar a opção: "Escolher usuário da Proposta"
* Pode salvar proposta c/ prospect de outro corretor: "Sim"

Papel Exercido

Não deixar marcada nenhuma das opções :

* Corretor
* Correspondente Bancário
* SDR

Administrador: Habilitando esse parâmetro, o grupo terá o papel de Administrador no Portal.

---

Por ser ADM conseguirá visualizar todos usuários.

**Neste segundo caso , vamos no Grupo do Corretor e Diretor  do PI.**

No grupo de usuários do Corretor e Diretor.

* Permissões: Proposta
* Desmarcar a opção: "Escolher usuário da Proposta"
* Pode salvar proposta c/ prospect de outro corretor = Não

Papel Exercido

Marcar o Papel deste usuário, neste exemplo (Corretor).

* Corretor
* Correspondente Bancário
* SDR

Administrador: Desabilitar

**Neste terceiro caso , vamos no Grupo do Superior do Corretor.**

**Este Superior vai ter permissão para visualizar suas propostas e do corretor por ser seu superior.**

No grupo de usuários do Corretor e Diretor.

* Permissões: Proposta.
* Desmarcar a opção: "Escolher usuário da Proposta".
* Pode salvar proposta c/ prospect de outro corretor = Não

Papel Exercido

Marcar o Papel deste usuário, neste exemplo ( Corretor ).

* Corretor
* Correspondente Bancário
* SDR

Administrador: Desabilitar

No cadastro do Usuário – Corretor informar o usuário **Superior do Corretor**. 

**Observação Importante:** O Superior e o corretor não devem fazer parte do mesmo Grupo, evitando conflitos de permissões.

Superior do Corretor ao logar no sistema, vai visualizar apenas ele e seus subordinados.

| Grupos

Visão dos grupos cadastrados responsáveis pelas permissões do usuário acerca as funcionalidades do Portal de Imóveis.

##### **Recebe e-mail após enviar venda para o BackOffice**

---

A opção **Recebe e-mail após enviar venda para o BackOffice** nos "**Parâmetros**" do Grupo, enviará um e-mail para todos os usuários dos grupos onde o parâmetro está marcado, independente do usuário estar vinculado na proposta ou não.

**Grupo de usuários para correspondente bancário**

---

É possível determinar um grupo de usuários como correspondente bancário para que o mesmo tenha acesso ao Portal de Imóveis e consiga preencher as informações referentes à análise financeira realizada por ele.

Para que o parâmetro seja ativado, é necessário acessar o menu **Backend > Usuários** e realizar a edição de um grupo:

Após entrar na visão de edição, na seção **"Papel Exercido"** o parâmetro **Correspondente bancário** estará disponível:

##### **Permissão: Correspondente Bancário**

---

Este conjunto de parâmetros visa lidar com as permissões relacionadas ao papel do correspondente bancário no sistema.

* **Notificar por email ao aprovar / reprovar a avaliação do prospect:** Quando este parâmetro está ativo, o Portal de Imóveis irá enviar um email de notificação ao corretor associado ao prospect quando o correspondente aprovar ou reprovar as informações financeiras do prospect.

Importante: Somente o usuário com o papel de correspondente bancário, poderá editar as informações financeiras de um prospect, seja no cadastro de pessoa ou na edição da proposta.

Além das informações financeiras, estará disponível também a aba de documentos, bem como a aba de propostas. Todos os outros cadastros permanecerão bloqueados.

**Quando o papel exercido é o de corretor, as informações financeiras ficarão bloqueadas.**

##### **Permissão de edição do correspondente bancário**

---

É possível determinar dentro de um grupo de usuários a permissão para edição ou não nas propostas de um correspondente bancário.

Para que o parâmetro seja ativado, é necessário acessar o menu **Backend > Usuários** e realizar a edição de um grupo:

Após entrar na visão de edição, na seção **"Permissões: Proposta"** o parâmetro **Pode alterar correspondente bancário da proposta** estará disponível:

Na "**Proposta**" será permitido o preenchimento do **"Correspondente Bancário"** somente se o parâmetro acima estiver marcado, caso contrário, o campo estará bloqueado para edição:

##### **Grupo de usuários para SDR's**

---

A partir da versão 12.1.2205, estamos disponibilizando no cadastro de grupo de usuários o papel de SDR.

SDR é a sigla de Sales Development Representative, ou  Representante de Desenvolvimento de Vendas. Visando agrupar estes analista de pré-vendas, temos também dois parâmetros que irão influenciar no comportamento destes atores.

Ainda dentro do cadastro de grupo, em Permissões: Prospect, foram criados dois parâmetros. São eles:

* Permite editar SDR: O usuário pode editar os SDR's dos prospects. Entretanto, quando o usuário já está definido como SDR, ele não conseguirá editar um usuário que não seja o próprio. Esta opção é mais voltada a administradores, quando é necessário ajustar o SDR do prospect, ou mesmo removê-lo.
* Vincular prospect ao SDR ao salvar: Define o comportamento de que, quando um usuário que está definido como papel de SDR está editando um Prospect, ao clicar em salvar, o campo SDR será preenchido com o seu nome de usuário.

Observações

* Um usuário definido como SDR não poderá associar um prospect a um outro SDR, independente dos parâmetros.
* O SDR só conseguirá ver os prospects de sua autoria ou somente prospects associados ao seu usuário.
| Imobiliária

Visão das imobiliárias cadastradas no sistema. Há a possibilidade de incluir uma nova imobiliária através do botão "Adicionar Imobiliária".

Este botão irá abrir a tela de cadastro de imobiliária, onde poderemos informar os dados da imobiliária, por exemplo, em relatórios. Uma parte importante deste cadastro é o campo de Comissão.

Exemplo de utilização:   
O Gestor, quando acessar o Portal poderá criar um usuário de gestão de imobiliárias para acesso externo.

* Selecione Backend > Usuários e em seguida a Guia imobiliárias

* Adicione um novo registro de Imobiliária e em seguida selecione o Empreendimento ao qual a imobiliária terá acesso:

* Acesse o menu usuários e selecione o usuário que será associado a esta imobiliária:

* Ao acessar este cadastro informe a Imobiliária e selecione qual o (os) empreendimento (s) este usuário terá a permissão.

* Após Salvar observe que na Visão de usuários será apresentada os dados respectivos a Imobiliária que está associada a este usuário.

* Ao realizar acesso ao Portal de Imóveis com este usuário, observe que o mesmo terá acesso apenas para aquele empreendimento que encontra-se associado a imobiliária marcada em seu cadastro.

**A partir da versão 12.1.2506:**

Ao cadastrar ou editar um usuário no sistema, é possível definir quais empreendimentos ele poderá visualizar e trabalhar.  
Essa configuração depende do campo Imobiliária dentro do cadastro do usuário.

A seguir, veja como o sistema se comporta:

##### 1. Quando uma Imobiliária é selecionada

Se o usuário tiver uma imobiliária definida no cadastro (ou seja, o campo **Imobiliária** estiver preenchido):

* O sistema procura essa imobiliária na lista geral de imobiliárias cadastradas.

* Quando encontra, o sistema **carrega automaticamente todos os empreendimentos que pertencem àquela imobiliária**.

* Esses empreendimentos são exibidos para você na tela, para que você possa definir quais deles o usuário terá acesso.

**Exemplo:**Se você escolher a Imobiliária *"Alfa Imóveis"*, o sistema mostra somente os empreendimentos da *Alfa Imóveis*.

##### 2. Quando nenhuma Imobiliária é selecionada

Se o campo **Imobiliária** estiver vazio (*null* ou não preenchido):

* O sistema junta todos os empreendimentos de todas as imobiliárias cadastradas.

* Remove entradas repetidas.

* Mostra ao usuário **a lista completa de empreendimentos disponíveis no sistema**.

**Exemplo:**Se você não escolher nenhuma imobiliária, o usuário terá acesso para selecionar empreendimentos de **todas** as imobiliárias.  
Mesmo que o campo **Imobiliária** esteja vazio (*null*) e nenhum empreendimento tenha sido selecionado, caso o usuário possua permissão vinculada a um empreendimento inativo, o sistema exibirá a mensagem **'Não existem empreendimentos ativos'** em vez de listar todos os empreendimentos

##### O que isso significa no dia a dia?

* A lista de empreendimentos **sempre muda automaticamente** conforme você escolher (ou não) uma imobiliária.

* Isso deixa o cadastro mais rápido e evita erros.

* Você não precisa saber quais empreendimentos pertencem a qual imobiliária — o sistema já faz essa filtragem para você.

#### Resumo:

|  |  |
| --- | --- |
| **Imobiliária selecionada** | Mostra apenas os empreendimentos daquela imobiliária |
| **Imobiliária não selecionada** | Mostra todos os empreendimentos do sistema |
| **Imobiliária não encontrada** | Não mostra empreendimentos (lista vazia) |

##### Impacto de não informar Imobiliária para quem utiliza PI → RM (TCGI) com cálculo de comissão:

##### Para bases integradas PI → RM TCGI, onde existem funcionalidades de equipe, orientador e cálculos de comissão, deixar um usuário sem imobiliária definida causa impactos importantes:

##### Consequências de deixar “Imobiliária” vazia:

* ##### O usuário não será vinculado a uma equipe, pois a imobiliária é usada como referência para montar a estrutura das equipes.
* ##### Ele não poderá ter orientador de equipe.

* ##### Os cálculos de comissão podem ficar incompletos ou incorretos, pois: metas e gatilhos são organizados por imobiliária/equipe, a ausência de imobiliária impede o vínculo correto do usuário à lógica de cálculo.

**Impacto na Roleta de Vendas**  
A lista de empreendimentos configurada no cadastro do usuário também impacta a distribuição da Roleta de Vendas.  
Se o corretor não possuir acesso ao empreendimento do lead, o sistema não realizará a distribuição para esse usuário naquele giro, mesmo que ele esteja ativo na equipe e corretamente posicionado na ordenação da roleta.

##### Se o usuário participa de equipes, metas, comissões ou orientações, a Imobiliária deve sempre ser selecionada.

| Permissão Usuário Propostacr| Criação de Usuários
