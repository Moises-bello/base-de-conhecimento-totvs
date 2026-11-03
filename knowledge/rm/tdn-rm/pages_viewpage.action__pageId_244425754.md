---
content_hash: 86923eca037057fc91e1521765ba93faf64e39d97d2d02ad7de670e8a3558810
fetched_at: '2026-06-29T00:08:13.538408+00:00'
page_id: '244425754'
product: rm
source: tdn-rm
title: Cadastro de Usuários na MDI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244425754
version: 83
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

    Os usuários são as entidades que acessam o RM e fazem uso de seus recursos. Para cadastrar um novo usuário, entre com o usuário Supervisor do sistema, acesse o cadastro de usuários e inclua um novo registro. Cada usuário no sistema deve ser cadastrado e depois ter suas liberações de acesso aos módulos, menus e funcionalidades do sistema.

## **02. EXEMPLO DE UTILIZAÇÃO**

**Aba Identificação - Confira abaixo as funcionalidades da pasta Identificação do Cadastro de Usuários:**

* **CAMPO USUÁRIO:** Informe um código para o usuário. Este código pode ser preenchido com caracteres alfanuméricos.

**OBSERVAÇÃO:**

Após a inclusão do usuário, o código não pode ser modificado. Além disso, os dados digitados serão gravados e classificados posteriormente na forma "case sensitive", ou seja, letras maiúsculas serão consideradas diferentes de minúsculas, devendo ser digitados estes dados ao acessar o sistema, exatamente como foram cadastrados.

Recomendamos muita atenção no momento de digitar o nome e senha do usuário. Qualquer diferença entre as letras maiúsculas/minúsculas cadastradas e as informadas para acesso ao cadastro serão consideradas e impedirão o acesso.

* **NOME:**Informe o nome completo do usuário, podendo também ser informadas abreviações. É de preenchimento facultativo.
* **E-MAIL:**Informe o e-mail do usuário. Este e-mail poderá ser utilizado para o envio de relatórios, gráficos, consultas SQL, etc., além do seu uso em outras funcionalidades do sistema.

A partir da versão **12.1.2606**, o sistema passa a bloquear a alteração de e-mails de usuários sincronizados com sistemas externos. Além disso, para evitar duplicidade, não será possível utilizar um e-mail que já pertença a outro usuário cadastrado.

* **CÓDIGO DE ACESSO:**É preciso definir um código de acesso ao banco de dados para os usuários, informando o tipo de acesso que os usuários terão. É possível cadastrar mais códigos de acesso no cadastro de código de acesso.
* **ATIVO (CAMPO DE ACESSO EXCLUSIVO AOS USUÁRIOS SUPERVISORES):**Este parâmetro poderá ser alterado somente por um usuário Supervisor. Ele permite o controle de acesso dos usuários. Dessa forma, você deverá habilitá-lo em cada usuário que deseja manter o acesso ao sistema e desabilitar no usuário que desejar bloquear o acesso.
* **SENHA:**Clique no ícone da chave para alterar ou incluir a senha do usuário. A senha poderá ser alterada também

O campo senha aceita um máximo de 20 caracteres

**OBSERVAÇÃO:**

Uma observação importante é quanto ao tamanho da senha que deverá ser de no mínimo de 6 (seis) caracteres.

* **FORÇAR A TROCA DE SENHA A CADA "X" DIAS:**Habilite este parâmetro e informe a quantidade de dias para forçar a troca da senha do usuário a cada "X" dias.

**OBSERVAÇÃO:**

A nova senha informada não poderá ser a mesma da senha atual. A contagem dos dias será a partir do dia que o campo foi ativado.

* **ALTERAR SENHA NO PRÓXIMO LOGIN:**Marque esta opção para forçar a troca da senha de um usuário em seu próximo login no sistema.
* **INICIO DE VALIDADE:**Informe a data de início da validade do acesso dos usuários.
* **EXPIRAÇÃO DE VALIDADE:**Informe a data de fim da validade do acesso dos usuários. Quando chegar esta data, o usuário não terá mais acesso ao sistema, até que uma nova data seja definida. A expiração de validade não pode ser menor que a data de último acesso válido.
* **SEMPRE É VALIDO:**Usuários que têm este parâmetro marcado não expiram.

**Aba Segurança - Configurar a segurança para cada usuário. A pasta Segurança só está habilitada para usuários Supervisores:**

* **PERMISSÃO DE ACESSO A COLIGADAS:**Aqui são listadas as coligadas do sistema e você pode definir se o usuário é supervisor. Além disso, pode definir se o usuário poderá incluir relatórios no sistema. Na coluna da direita, você deverá associar o usuário ao Perfil de permissões que ele melhor adequar.

**USUÁRIOS SUPERVISORES:**

Os usuários que possuírem a condição de Supervisor nos aplicativos terão como diferencial, o acesso autorizado em algumas opções que demais usuários comuns não possuirão. Dessa forma, somente usuários na condição de supervisor terão acesso completo ao cadastro de usuários.

Esta operação deverá ser repetida para cada Coligada que o usuário poderá ter acesso. Todas as coligadas em todos os sistemas devem possuir pelo menos um usuário supervisor cadastrado e este só terá autorização de alterar permissões de usuários das coligadas em que for supervisor.

**ABA REDE: Configurar os parâmetros necessários para que o usuário acesse o RM baseando no usuário de rede do Windows. Se o login de rede for o mesmo do cadastro de usuários, você poderá acessar o sistema bastando acessá-lo e sem precisar digitar a senha:**

* **USUÁRIO DE REDE:**Aqui você deverá preencher o usuário de rede para associá-lo ao usuário do sistema. Com isso, toda vez que o usuário de rede do usuário acessar o sistema não será necessário.
* **DOMÍNIO DE REDE:**Preencha o domínio da rede onde o usuário de rede está incluído.

**OBSERVAÇÃO:**

É preciso que o parâmetro "Ativa Logon Unificado", disponível nos parâmetros globais esteja ativado e as informações neste cadastro para o uso deste recurso. Para saber mais sobre usuários supervisores, acesse o link "Usuários Supervisores" ao fim deste tópico.

Depois que o usuário foi cadastrado, deve ser definido os acessos do usuário no sistema na pasta "Segurança". Nela você pode definir a quais perfis o usuário estará associado.

**OBSERVAÇÃO:**

A restrição aos módulos, menus e funcionalidades do sistema deve ser feita no cadastro de perfis. Veja mais sobre o cadastro de perfis no "Informações Complementares".

# **COMO FAZER**

        Para que você possa cadastrar um usuário através da nova MDI siga as instruções abaixo:

**ENTRANDO NO SISTEMA**

1. Abra o diretório "C:\totvs\CorporeRM\RM.Net".

Acesse o sistema através da nova MDI clicando no executável "RM.exe".  
O sistema irá apresentar a tela ao lado, faça o login.  
**SELECIONANDO MÓDULO**

1. Na tela seguinte você irá clicar no ícone para acessar os módulos do sistema.
2. O sistema irá listar os módulos do sistema. Você deverá escolher a opção "Serviços Globais".

        3. Note que o sistema irá apresentar uma nova caixa de opções no menu superior, você deverá escolher o menu "Segurança":

**TELA DE USUÁRIOS**

1. Clique no botão "Usuários". O sistema irá listar os usuários para o módulo selecionado. No exemplo abaixo, ele está mostrando os usuários do módulo "Gestão Patrimonial".
2. Escolha corretamente para qual aplicativo você irá realizar o cadastro do usuário, selecionando na guia o módulo desejado.
3. Depois que estiver selecionado o módulo correto, basta clicar no ícone "Incluir" para que o formulário de cadastro possa ser visualizado.

**Cadastro do Nome Social:**

A partir da versão 12.1.21, será possível informar o Nome Social de um usuário.

Quando o campo 'Nome Social' estiver preenchido, ao logar na MDI ou no portal, o usuário visualizará seu 'Nome Social' na tela inicial.

Caso o usuário não possua este campo preenchido, ao logar na MDI ou no portal, o usuário visualizará seu 'Nome' na tela inicial.

Em versões anteriores à 12.1.21, é exibido o valor preenchido no campo 'Usuário' na tela inicial da MDI e o 'Nome' do usuário no acesso ao portal.

**PERMISSÕES**

**Observação:**

Esta operação deverá ser repetida para cada Coligada que o usuário poderá ter acesso.

Todas as coligadas em todos os sistemas devem possuir pelo menos um usuário supervisor cadastrado e este só terá autorização de alterar permissões de usuários das coligadas em que for supervisor.

Após preencher todas as informações do usuário, clique em "Segurança", para definir quais as coligadas/perfis o usuário terá permissão.

**PERFIS COMPARTILHADOS ENTRE MÓDULOS**

Os perfis compartilhados podem ser utilizados apenas pelos usuários que tem permissão no módulo origem do perfil compartilhado. Caso contrário o perfil não será listado para ser concedido a permissão no cadastro de usuários.

**Exemplo**: Se eu tenho um perfil de globais que foi compartilhado com outros módulos, e quero dar permissão nesse perfil para um usuário do módulo de “Gestão de pessoas”, só será possível se esse usuário tiver permissão no módulo de globais para aquela coligada.

 Se o usuário possuir um perfil compartilhado vinculado em algum módulo, o usuário automaticamente terá permissão em todos os módulos que o perfil tem permissão. Ao retirar a permissão do usuário em um módulo, o perfil será retirado de todos os módulos que o usuário tem acesso.

Os perfis que compartilham módulos podem ser identificados com o texto “Multiperfil” em frente ao Identificador do perfil. Basta selecionar a coligada a ser editada, conforme imagem abaixo.

Saiba mais sobre o funcionamento dos perfis compartilhados:

# **ATUALIZAÇÃO DE MÚLTIPLOS REGISTROS DE USUÁRIO**

Através desta funcionalidade podemos alterar as configurações de vários usuários simultaneamente. 

Para realização desse processo siga o passo a passo descrito abaixo:

* Acesse "Serviços Globais | Usuários".
* Na visão é necessário selecionar um usuário e em seguida acessar "Processos | Atualização de Múltiplos Registros de Usuários".
* Na tela de Atualização (Parâmetros de Atualização), selecione o campo que será modificado e clique em Executar. (No exemplo, o campo Ativo esta sendo desativado, parâmetro alterado para "0").

* Após a execução ser concluída para o usuário 00001 (utilizado no exemplo) o parâmetro deve ser alterado (campo ativo desmarcado). Neste caso, ao alterar o campo "Ativos" para o valor 0 em múltiplos usuários, é possível cancelar os jobs agendados por eles marcando a opção "Cancelar jobs pendentes".

Para maiores informações:

* [Clique aqui para conhecer mais sobre as funcionalidades da pasta Identificação do Cadastro de Usuários.](http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.Usuario.aspx)
* [Clique aqui para conhecer a nova funcionalidade do Histórico de Senhas do Usuário.](https://tdn.totvs.com/x/IndqJQ)
false

**Versão:** 11.XX, 12.01.18 ou superiores

 ***Veja os principais conteúdos::***
