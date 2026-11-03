---
content_hash: 138123b79897af3d13a94de6d87e2f73e392ea14683d8049eabb34391c8641b1
fetched_at: '2026-06-29T00:08:37.892707+00:00'
page_id: '285638806'
product: rm
source: tdn-rm
title: Informações 1/2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285638806
version: 16
---

**Nome do portal de inscrições:** determina qual nome será dado ao Portal de inscrições do Processo Seletivo. O nome dado ao Portal será visualizado na página de login do sistema, também conhecida como área pública do Portal.

**Utilizar senha no portal:** determina se o campo senha será utilizado no Portal. A configuração deste parâmetro impacta no funcionamento de diversos serviços:

**1º -** Cadastro de candidato: se o parâmetro “senha” estiver habilitado, então o sistema exigirá o preenchimento do campo senha e confirmação de senha. No e-mail de confirmação de cadastro será enviada a senha informada pelo candidato. Se o parâmetro estiver desabilitado, então os campos de senha não aparecerão no formulário de cadastro e o e-mail de confirmação irá com uma senha aleatória gerada pelo sistema.

**2º -** Login do sistema: se o parâmetro “senha” estiver habilitado, então será exigido a “Senha” cadastrada. Se o parâmetro estiver desabilitado, então será exigido a “Data de Nascimento” como senha.

**3º -** Esqueci a senha: se o parâmetro “senha” estiver habilitado, então este serviço estará disponível, caso contrário não será disponibilizado no Portal.

**4º -** Alterar senha: se o parâmetro “senha” estiver habilitado, então este serviço estará disponível, caso contrário não será disponibilizado no Portal.

**Formas de identificação:** determina quais dados serão disponibilizados para a identificação do candidato no momento de efetuar login no Portal de Inscrições. Os dados que poderão ser disponibilizados são: CPF, Carteira de identidade, Código de usuário e E-mail. Pelo menos uma forma de identificação deverá ser selecionada.

Importante

Para que os dados CPF, Carteira de identidade e E-mail sejam utilizados no login, é necessários que estes campos estejam visíveis e obrigatórios na aba "Visibilidade/Obrigatoriedade de campos".

Sobre a regra do critério de busca por candidato existentes [clique aqui](https://tdn.totvs.com.br/pages/viewpage.action?pageId=284884269)

**Aproveitar dados do cadastro de pessoa**: através dos critérios de busca o sistema identifica se já existe uma pessoa na base (PPESSOA), caso exista, os dados são copiados para o cadastro de usuários do processo seletivo, caso não exista usuário, somente pessoa, será criado um novo usuário, caso o usuário exista, os dados serão atualizados.

Para saber mais informações [clique aqui](https://tdn.totvs.com.br/display/LRM/Aproveitar+dados+do+cadastro+de+Pessoa).

**Alteração de dados cadastrais do candidato quando é aluno/pessoa:** esta opção permite definir tipo de alteração de dados, ou seja, quando a pessoa existe os dados podem ser bloqueados  ou solicitar alteração aos responsáveis da filial ou nível de ensino.  A escolha de um destes parâmetros reflete diretamente na .

* **Apenas consulta:** esta opção define que caso o usuário/pessoa exista, os campos já preenchidos não poderão ser alterados, somente os campos vazios ficaram habilitados para preenchimento.
* **Solicitar alteração para o Nível de Ensino:** esta opção define que os campos e-mail, endereço e telefone ficaram bloqueados e somente serão alterados após a solicitação, que no caso será enviado um e-mail para o e-mail cadastrado no nível de ensino com os dados alterado. ()
* **Solicitar alteração para Filial:** a mesma situação acima, porém o e-mail será enviado para o e-mail cadastrado na filial.
* **Permite alteração:** esta opção deixará os campos habilitados e ao confirmar a inscrição os dados serão salvos no cadastro do usuário e serão atualizados no cadastro da pessoa vinculada.

**Campus/Polo:**Quando o parâmetro **Utiliza a escolha obrigatória do Campus/Polo, da matrícula, no formulário de Inscrição** estiver habilitado, no momento da inscrição do candidato, a opção de selecionar o Campus/Polo será exibida antes da escolha da Área de Interesse, sendo obrigatório a seleção de um campus/polo.

Regras para atualizar o cadastro de Pessoa

* Serão atualizados no cadastro de pessoa somente as informações (campos) que são disponibilizadas para o preenchimento no processo seletivo
* Se um informação não for preenchida na inscrição e no cadastro de pessoa a mesma informação estiver preenchida, então o cadastro de pessoa não será atualizado, ou seja, será mantida a informação preenchida no cadastro da pessoa.
