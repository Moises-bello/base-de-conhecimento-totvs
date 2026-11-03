---
content_hash: a520dbb4d3c703069d40312fa0b96d286d59e514a18d1fbdb165f490b8568625
fetched_at: '2026-06-29T00:10:07.992835+00:00'
page_id: '452719492'
product: rm
source: tdn-rm
title: Inclusão de Usuário para Acesso ao RM Portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719492
version: 20
---

## **01.****VISÃO GERAL**

Esse processo foi disponibilizado para possibilitar incluir o funcionário como usuário no cadastro de usuários, e assim ser possível acessar os recursos no RM Portal.

Utilizando esse processo, a inclusão de usuário para acesso ao RM Portal pode ser feita de forma automática.

## Considerações:

* Na inclusão de usuário por seleção de funcionários, o e-mail será preenchido no cadastro de usuário com o mesmo endereço eletrônico que estiver cadastrado para o funcionário. Caso não exista e-mail informado no cadastro do funcionário será possível informar um e-mail para a criação do usuário se este for criado individualmente.

* Deverá utilizar o parâmetro **"Utiliza Seleção de Funcionários"** para incluir mais de um funcionário como usuário, devendo ser selecionada na grade de seleção, filtro ou fórmula de seleção. Não marcando este campo o sistema realizará a inclusão de usuário somente para o funcionário que estiver selecionado na visão do cadastro de funcionários.

* Para incluir usuário para funcionários demitidos, deverá marcar o parâmetro **"Gera para funcionários demitidos".**

* A seleção do código de acesso ao banco, já criado nos **"Cadastros de Códigos de Acesso"**, será necessária para que seja utilizado pelo funcionário. Este cadastro tem como finalidade permitir a inclusão e manutenção de códigos especiais de acesso ao banco de dados. Estes códigos devem ser informados para cada usuário do aplicativo, definindo-se e diferenciando-se assim, o usuário administrador do banco de dados a ser utilizado para a conexão.

* Os perfis determinam as permissões de acesso ao aplicativo e ao RM Portal.

* Obrigatoriamente, deverá ser informada a **"Data Inicial"** da validade de utilização do usuário. A Data final é facultativa, mas quando não informada o usuário será criado como **"Sempre Válido"**, ou seja, não terá controle de **"Data Final"** de vigência.

* O código do grupo possibilita selecionar o grupo de acesso que foi criado em "Parâmetros do RM Portal". Após associar o grupo de acesso ao funcionário, o RM Portal reconhecerá qual perfil que o funcionário pertence e apresentar somente as opções disponibilizadas para aquele perfil.

* O parâmetro **"Usuário deve alterar a senha no próximo login"** serve para forçar a troca da senha de um usuário. Assim, na próxima vez que o usuário logar no sistema será solicitado a troca da senha.

**ATENÇÃO:** O processo de inclusão de usuário sempre irá alterar a senha do usuário, conforme os parâmetros definidos no início do processo.

Por exemplo:

* + - Se o parâmetro **"Definir CPF como senha default"** estiver selecionado, a senha gerada será o CPF do usuário.
    - Caso **nenhum parâmetro esteja marcado**, o sistema utilizará o **último nome** do usuário como senha.

Para que o próprio usuário defina uma nova senha pessoal no próximo acesso, selecione o parâmetro **"Usuário deve alterar a senha no próximo login"**.

* Ao selecionar **"Utilizar número da coligada e chapa para código de acesso"** será feita a união dos códigos para criação do usuário.

* O parâmetro **"Utiliza CPF para código de acesso"** foi disponibilizado para que o sistema crie o usuário utilizando o número de CPF cadastrado para o funcionário. Caso não defina CPF como senha default ou não exista CPF cadastrado para o funcionário, quando utilizar CPF como senha default, o sistema incluirá a chapa como código de acesso e a senha será o último nome do funcionário com letras maiúsculas.

* Ao marcar o parâmetro **"Atualizar permissões para usuário existente",** caso o funcionário já possua um usuário vinculado, o sistema irá atualizar os dados abaixo:

  + - Código de acesso ao banco
    - Perfil
    - Validade
    - Código do Grupo
    - Usuário deve alterar senha no próximo login
    - Definir CPF como senha default e
    - Núm. de dias para Forçar a Troca de Senha

**IMPORTANTE:** o parâmetro "Atualizar permissões para usuário existente" só funcionará caso o usuário seja o mesmo criado pelo padrão do sistema (**chapa do** **funcionário**,  **Coligada + Chapa do F****uncionário** (parâmetro "Utiliza número da coligada e chapa para código de acesso" ) ou **CPF** ("Utiliza CPF para código de acesso")).

**ATENÇÃO:** Informe a periodicidade que o usuário deverá alterar sua senha pelo número de dias para forçar troca senha. Caso não seja informada a periodicidade nunca será solicitado ao usuário a troca de senha. 

**OBSERVAÇÃO:**  A validação da senha é realizada de acordo com os parâmetros globais definidos no sistema. Para mais detalhes sobre esses parâmetros, acesse o [link](https://tdn.totvs.com/pages/viewpage.action?pageId=244425754).

Veja mais detalhes na liberação da tratativa:

## **02.** **EXEMPLO DE UTILIZAÇÃO**

**Coligada**: 1   
**Funcionário**: 00012  
**Código de acesso ao banco**: 1-00012

**Exemplo:**

Clique para visualizar imagem

Usuário cadastro no sistema com **Coligada + chapa do funcionario (parâmetro "Utiliza número da coligada e chapa para código de acesso" )**

Para atualização do código do grupo, deverá executar a rotina "Inclusão de usuário para acesso ao RM Portal", selecionando a chapa e marcado os campos conforme abaixo:

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funcionários
