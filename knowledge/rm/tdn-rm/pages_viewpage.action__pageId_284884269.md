---
content_hash: a6bba89a9bb120bc590108fd9ad987d0a168f17e8c7223b345e5a47d4d419897
fetched_at: '2026-06-29T00:08:37.813642+00:00'
page_id: '284884269'
product: rm
source: tdn-rm
title: Busca de Candidato (Critério de unicidade)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284884269
version: 55
---

É possível parametrizar o processo seletivo para recuperar dados de usuários (candidatos ou responsável) que já realizaram a inscrição anteriormente.

Foram criados critérios de reconhecimento de unicidade que, ao serem preenchidos, permitem ao sistema realizar a verificação e, em caso de coincidência, reutilizar os dados já existentes na base de dados.

Os critérios são:

* Nome, data de nascimento, estado natal e naturalidade
* CPF, passaporte ou registro geral
* E-mail

A instituição pode marcar nenhum, um ou mais critérios para que a busca na base fique ainda mais refinada e não encontre duplicidade. Caso a instituição não marque nenhum critério, aquele processo seletivo não realizará buscas, ou seja, sempre irá criar **novos usuários** na base.

Campos obrigatórios / visíveis

Os campos que fazem parte da opção do critério selecionado serão habilitados automaticamente para serem exibidos no formulário de inscrição (vaja a aba: visibilidade/obrigatoriedade de campos), ou seja, a sua visibilidade e obrigatoriedade será marcada automaticamente conforme o critério utilizado "**E**" ou "**OU**".

Se o processo seletivo estiver com a opção "**Utilizar responsável por candidato na inscrição**" marcada, as regras a seguir serão aplicadas a visibilidade e obrigatoriedade do responsável.

* **Para o critério "E":** os campos correspondentes as opções selecionadas serão marcadas como obrigatório e visível.

Ao marcar a opção será apresentada a mensagem conforme o exemplo abaixo orientando o usuário.

Para a opção "**CPF, passaporte ou registro geral**" os campos não serão marcados automaticamente como obrigatório, pois é um ou outro, neste cenário é o usuário que vai definir qual será obrigatório, no entanto ao salvar o sistema irá validar se pelo menos um destes campos está marcado como obrigatório.

* **Para o critério "Ou":** os campos correspondentes as opções selecionadas serão marcadas como visível.

Ao marcar a opção será apresentada a mensagem conforme o exemplo abaixo orientando o usuário.

Caso seja marcado mais de um critério, para que a busca seja executada com sucesso, todos os campos marcados devem ser informados exatamente iguais ao dados já existentes no cadastro de usuários (SPSUSUARIO), para que o sistema entenda que se trata do mesmo usuário.

Caso a instituição marque algum critério de busca, esses campos serão exibidos no mini formulário (para Candidato ou para Responsável pela Inscrição) para que o usuário digite seus dados e ao clicar em 'Continuar' seja realizada a busca na base. Caso seja encontrado algum resultado com os dados informados, será exibido mensagem para o usuário informando que seus dados foram encontrados na base de dados. Ele deve realizar o login, logo em seguida os dados do candidatos e seus responsáveis (caso possua) serão preenchidos automaticamente no formulário e não será criado um novo usuário.

Importante saber

Para evitar **duplicidade** de registros, principalmente no cadastro de filiação, o critério de unicidade é aplicado duas vezes no processo: no início da inscrição, avaliando candidato e responsável pela inscrição, e posteriormente ao finaliza-la. Mesmo que seja um novo candidato esse será o comportamento do sistema.

Exemplo: Ao cadastrar um novo candidato, por ser um novo registo, não será apresentada a mensagem de unicidade. No decorrer da inscrição, ao incluir uma Filiação 1, o sistema identificou através dos critérios de unicidade que essa Filiação 1 já existe como usuário cadastrado no TOTVS Processo Seletivo (SPSUSUARIO). Para evitar duplicidade, a unicidade é aplicada ao finalizar a inscrição, de forma a não incluir novamente a mesma pessoa como usuário, mas sim aproveitar o registo já existente.

Regra do Critério de Busca

A partira das versões **12.1.32.178, 12.1.33.109, 12.1.34** e com todos os scripts executados, foi criado uma nova opção no parâmetro "Critério de Busca" do Processo Seletivo denominado **"Critério"** que permite parametrizar se os critérios de busca de candidatos inscritos contemplará a regra do "E" ou do "OU", esta melhoria impactará nos casos em que forem selecionados 2 ou mais critérios de busca.

* **Critério E**

Caso seja parametrizado para utilizar o critério "E", **o sistema continuará tendo o comportamento descrito acima** em que realiza a busca verificando se existe um candidato existente na base cujo os valores de todos os critérios de busca estejam iguais aos informados na inscrição e caso um desses valores do critério de busca seja divergente o sistema identifica como um novo candidato e realiza uma nova inscrição.

**Regra do critério de busca:** (Nome, data de nascimento, estado natal e naturalidade) **E** (CPF, passaporte ou registro geral)

Por exemplo:

Caso seja selecionado os critérios "Nome, data de nascimento, estado natal e naturalidade" e "CPF, Passaporte ou Registro Geral" o sistema irá validar se todos estes campos estão iguais e caso algum tenha alguma alteração será criado um novo registro, ou seja, mesmo que exista um outro candidato com o mesmo CPF informado, se o nome estiver diferente será criado um novo registro.

* **Critério OU**

Caso seja parametrizado para utilizar o critério "OU", o sistema realizará a busca verificando se existe um candidato existente na base **cujo os valores de um único critério de busca** esteja igual aos informados na inscrição e apenas caso todos os critérios de busca tenham seus valores divergentes o sistema identifica como um novo candidato e realiza uma nova inscrição.

**Regra do critério de busca:** (Nome, data de nascimento, estado natal e naturalidade) **OU** (CPF, passaporte ou registro geral)

Por exemplo:

Caso seja selecionado os critérios "Nome, data de nascimento, estado natal e naturalidade" e "CPF, Passaporte ou Registro Geral" o sistema irá validar se os campos de um único critério de busca estão iguais como por exemplo o CPF informado já exista para outro candidato que esteja inscrito, o sistema irá retornar a mensagem de reconhecimento de dados e redirecionar o candidato para a página de login/recuperação de dados, mesmo se o nome e outros dados estiverem diferentes.

É possível realizar também o aproveitamento de dados do cadastro de pessoas, para maiores informações [clique aqui](https://tdn.totvs.com.br/display/LRM/Aproveitar+dados+do+cadastro+de+Pessoa)

A partir da versão **12.1.2410**  se estiver utilizando a opção "**Aproveitar dados do cadastro de Pessoa**” será obrigatório marcar no critério de unicidade a opção "**CPF, passaporte ou registro geral**". Esta obrigatoriedade tem como objetivo trazer uma maior segurança  e robustez no processo de aproveitamento dos dados.

  
Comportamento da Inscrições no Portal

Ao informar os dados para inscrição e continuar, o sistema aplicara as regras de busca conforme o critério parametrizado, e caso o candidato já possua cadastro no TOTVS Processo Seletivo será apresentada a mensagem abaixo.

Após clicar em "Ok" o usuário será redirecionado para a pagina de login, sendo necessário realizar o login para prosseguir com as inscrição.

Caso o processo seletivo esteja parametrizado para utilizar senha, e o usuário não lembrar ou não possuir uma senha será necessário acionar a opção "Esqueci minha senha" para que seja enviada uma nova senha para o e-mail cadastrado. 

Tela de Login da Central do Candidado

Após realizar o login os dados já cadastrados serão carregados e o usuário poderá prosseguir com a inscrição.
