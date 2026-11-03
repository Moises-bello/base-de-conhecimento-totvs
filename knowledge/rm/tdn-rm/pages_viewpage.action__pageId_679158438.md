---
content_hash: 0ad67115bf8f7b1e6400b279819dd07c65dccb2be42f3fe863d462613171a479
fetched_at: '2026-06-29T00:11:17.307654+00:00'
page_id: '679158438'
product: rm
source: tdn-rm
title: 2- Avaliações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=679158438
version: 52
---

Nesta tela, o professor poderá visualizar um resumo completo das avaliações da turma/disciplina. A partir deste menu, será possível cadastrar, editar, excluir e consultar as notas das avaliações registradas.

Permissão de acesso

Para acessar a funcionalidade, o perfil do professor deverá ter a permissão em: **Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional (Portal) | Professor | Diário de classe | Cadastro de Avaliações**

Listar avaliação

O portal exibirá as avaliações disponíveis para a turma/disciplina, conforme a seguinte regra:

A opção "**Exibe no portal e na central do aluno**" esteja **marcada**no cadastro da etapa da avaliação

Incluir avaliaçãoPerfil de professor

Para incluir uma avaliação o professor deverá ter permissãoem:  **Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional (Portal) | Professor | Diário de classe | Cadastro de Avaliações | Incluir Provas (Professor)**

Perfil de coordenador

Essa funcionalidade está disponível a partir do patch: 12.1.2510.100

Se o usuário logado for um **coordenador** e estiver editando as avaliações de **outro professor** (que não ele mesmo), o portal permitirá a alteração com base na ativação do seguinte parâmetro:  **Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional (Portal) | Professor | Diário de classe | Cadastro de Avaliações | Permite ao coordenador do curso incluir provas**

Caso o **coordenador também atue como professor** (ele mesmo), as devidas permissões correspondentes à função de professor devem ser concedidas a ele, estando configuradas e vinculadas também dentro do seu perfil de coordenador após ativar o seguinte parâmetro: **Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional (Portal) | Professor | Diário de classe | Cadastro de Avaliações | Incluir Provas (Professor)**

Campos complementares

Para que a opção **Dados Complementares** fique ativa no cadastro de avaliações, o usuário deverá cadastrar previamente os campos complementares em **Configurações > Campos Complementares > Avaliações**, dentro do período letivo.

Os campos complementares devem ser marcados no nível de ensino desejado em **Configurações > Níveis de Ensino > (selecionar o nível de ensino) > aba Campos Complementares Disponíveis**.

Dessa forma, ao configurar essa opção, ao acessar o portal do professor a opção **Dados Complementares** ficará ativa para o usuário.

Editar avaliaçãoPerfil de professor

Para editar uma avaliação o professor deverá ter permissãoem:  **Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional (Portal) | Professor | Diário de classe | Cadastro de Avaliações | Editar Provas (Professor)**

Perfil de coordenador

Essa funcionalidade está disponível a partir do patch: 12.1.2510.100

Se o usuário logado for um **coordenador** e estiver editando as avaliações de **outro professor** (que não ele mesmo), o portal permitirá a alteração com base na ativação do seguinte parâmetro:**Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional (Portal) | Professor | Diário de classe | Cadastro de Avaliações | Permite ao coordenador do curso editar provas**

Caso o **coordenador também atue como professor** (ele mesmo), as devidas permissões correspondentes à função de professor devem ser concedidas a ele, estando configuradas e vinculadas também dentro do seu perfil de coordenador após ativar o seguinte parâmetro: **Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional (Portal) | Professor | Diário de classe | Cadastro de Avaliações | Editar Provas (Professor)**

Excluir avaliaçãoPerfil de professor

Para excluir uma avaliação o professor deverá ter permissãoem:  **Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional (Portal) | Professor | Diário de classe | Cadastro de Avaliações | Excluir Provas (Professor)**

Perfil de coordenador

Essa funcionalidade está disponível a partir do patch: 12.1.2510.100

Se o usuário logado for um **coordenador** e estiver editando as avaliações de **outro professor** (que não ele mesmo), o portal permitirá a alteração com base na ativação do seguinte parâmetro:  **Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional (Portal) | Professor | Diário de classe | Cadastro de Avaliações | Permite ao coordenador do curso excluir provas**

Caso o **coordenador também atue como professor** (ele mesmo), as devidas permissões correspondentes à função de professor devem ser concedidas a ele, estando configuradas e vinculadas também dentro do seu perfil de coordenador após ativar o seguinte parâmetro: **Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional (Portal) | Professor | Diário de classe | Cadastro de Avaliações | Excluir Provas (Professor)**

Para excluir avaliações, o professor poderá optar por excluir uma ou mais avaliações, ou realizar a exclusão individual de uma avaliação.

* Para excluir mais de uma avaliação, basta selecionar as avaliações na página principal e clicar no botão **Excluir**.
* Para excluir uma avaliação específica, basta clicar nos três pontos (**…**) e selecionar a opção **Excluir**.

Replicar avaliação para outra(s) turma(s)/disciplina(s)Criar uma nova avaliação

O processo de replicação de avaliação para outra(s) turma(s)/disciplina(s) de destino consiste na criação de uma nova avaliação nas turma(s)/disciplina(s) de destino, a partir da seleção de uma avaliação existente, permitindo a alteração de seus campos, se desejado.

Para replicar a avaliação para outra(s) turma(s)/disciplinas o professor deverá ter a permissãoem:  **Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional (Portal) | Professor | Diário de classe | Cadastro de Avaliações | Incluir Provas (Professor)**

1º passo: Visualizar/Editar avaliação

O portal exibirá o formulário contendo todos os campos já preenchidos com as informações da avaliação selecionada. No entanto, o professor poderá alterar todos os campos, inclusive as informações complementares, se necessário. Após as alterações, poderá seguir para o próximo passo clicando no botão **Continuar**.

2º passo: Selecionar as turmas/disciplinas destino

O professor irá selecionar as turmas/disciplinas de destino nas quais a avaliação será criada.

Regras para listagem das turmas/disciplinas

O portal listará as turmas/disciplinas de destino, considerando a seguinte regra:

* O professor deve **estar vinculado** a turma/disciplina.

* O período letivo da turma/disciplina deve estar com a opção de "Exibir no portal do professor" **marcada**.

* A turma/disciplina deve estar com a opção de "Ativa" **marcada**.

Os períodos letivos considerados são:

* O período letivo da turma/disciplina **de origem**

* Operíodo letivo presente no campo "Período letivo anterior" preenchido com o **período letivo da turma/disciplina de origem**.

3º passo: Visualizar o resultado

O portal exibirá o resultado da(s) réplica(s) executada(s).

Em caso de sucesso

Caso a(s) réplica(s) da avaliação seja(m) realizada(s) **com sucesso para todas** as turmas/disciplinas de destino, o portal exibirá a mensagem **“Avaliação replicada com sucesso”**.

Em caso de aviso/inconsistência

Caso a(s) réplica(s) da avaliação seja(m) realizada(s) com **inconsistência ou erro** em alguma(s) turma(s)/disciplina(s) de destino, o portal exibirá a mensagem de alerta **“Não foi possível replicar a avaliação para alguma(s) turma(s)/disciplina(s)”**.

Iniciar o processo novamente

Nesse caso, o professor poderá, se desejar, voltar aos passos anteriores e iniciar o processo novamente.

Replica de avaliação para turma(s)/disciplina(s) com sucesso

O portal **não exibirá** a(s) turma(s)/disciplina(s) para as quais as réplicas foram **realizadas com sucesso**.

Vincular a subturma a avaliação

O portal permite vincular a(s) subturma(s) à avaliação desejada. Para que a opção **Subturmas** esteja disponível, devem ser atendidas as seguintes regras:

* A turma/disciplina deve possuir subturma;
* O professor deve estar vinculado a um horário, e esse horário deve estar vinculado a uma subturma.

Não disponível para todas as subturmas

O vínculo das subturmas é válido apenas quando a opção **Disponível para Todas as Subturmas**, no cadastro da avaliação, estiver **desmarcada**.

Visualizar notas

Esta funcionalidade oferece uma forma rápida de visualizar as notas diretamente na tela de avaliações. Ao selecionar essa opção, o usuário será redirecionado para a tela de notas, com a etapa e a avaliação já previamente filtradas.

Para acessar a funcionalidade, o perfil do professor deverá ter a permissão em: **Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional (Portal) | Professor | Diário de classe | Notas de avaliação**
