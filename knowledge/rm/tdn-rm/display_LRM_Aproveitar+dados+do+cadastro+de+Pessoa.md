---
content_hash: 10e7ffac78b0f5c53a41918ee0634d2693a2f153b19c55f6c49bb3df7df2ef38
fetched_at: '2026-06-29T00:11:22.379716+00:00'
page_id: '701686520'
product: rm
source: tdn-rm
title: Aproveitar dados do cadastro de Pessoa
type: documentation
url: https://tdn.totvs.com/display/LRM/Aproveitar+dados+do+cadastro+de+Pessoa
version: 17
---

A partir das versões **12.1.2205.102 e superiores** foi disponibilizada a opção "**Aproveitar dados do cadastro de Pessoa**" (para habilitar o recurso será necessário executar o RM Atualizador).

Na inscrição do candidato, se a opção "**Aproveitar dados do cadastro de Pessoa**" estiver marcada o sistema aplicará internamente a busca de candidatos nos cadastros de usuário do TOTVS Processo Seletivo e também no cadastro de **Pessoa.**

A pesquisa utilizará o mesmo critério de unicidade parametrizado no processo seletivo (para saber mais sobre critério de unicidade [clique aqui](https://tdn.totvs.com.br/pages/viewpage.action?pageId=284884269)).

Esta funcionalidade tem como objetivo agilizar o processo de inscrição, uma vez que os dados do candidato já fazem parte da base de dados do RM, e também manter os dados atualizados conforme o cadastro de **Pessoas**.

Para utilizar a opção "**Aproveitar dados do cadastro de Pessoa**” será obrigatório marcar no critério de unicidade a opção "**CPF, passaporte ou registro geral**" e não será permitido utilizar o critério **"Ou"**.

Esta obrigatoriedade tem como objetivo trazer uma maior segurança  e robustez no processo de aproveitamento dos dados.

**Por exemplo**

Um funcionário ou aluno da instituição que já está cadastrado como **Pessoas** e não possui registro no cadastro de usuário no TOTVS Processo Seletivo realiza a inscrição em um determinado processo seletivo. Neste exemplo, se a opção "**Aproveitar dados do cadastro de Pessoa**" estiver marcada, o sistema identificará seu registro no cadastro de **Pessoas** e apresentará no portal a tela abaixo:

A mensagem acima sempre será apresentada se um candidato já possuir cadastro no TOTVS Processo Seletivo (se estiver parametrizado para utilizar critério de unicidade), mesmo que o usuário não seja encontrado no cadastro de pessoa.

No momento em que esta mensagem é apresentada, o **TOTVS Processo Seletivo** realiza a importação do cadastro de **Pessoas** para o cadastro de usuários.

**Regras da opção "Aproveitar dados do cadastro de Pessoa":**

* Se não for localizado nenhum registro no cadastro de usuário do TOTVS Processo Seletivo será aplicada a mesma busca no cadastro de **Pessoas**, caso seja localizado um registro, o cadastro da **Pessoa** será importado para o cadastro de usuário do TOTVS Processo Seletivo.
* Quando recuperados os dados do cadastro de **Pessoas**, caso existam **Filiações** **associadas a esta pessoa**, os dados das **Filiações** existentes também serão recuperados e aproveitados no cadastro de usuários do TOTVS Processo Seletivo mantendo os relacionamentos existentes. (Por exemplo: Se no cadastro de Pessoas uma determinada pessoa possui uma Filiação do Tipo Pai, esta filiação será importada para o cadastro de usuários do Processo Seletivo como uma Filiação/Responsável do candidato do Tipo Pai).
* Se o candidato já possuir um cadastro no TOTVS Processo Seletivo, ainda assim o sistema realizará a busca das informações no cadastro de **Pessoas**.Caso seja localizado um registro no cadastro de **Pessoas** iremos copiar os dados do cadastro de Pessoa **sobrescrevendo** os dados no Cadastro do Usuário.

Validação adicional

Em alguns casos observamos que os clientes estavam via rotinas customizadas atualizando o campo **CODPESSOA** com um código de uma pessoa com os dados totalmente divergentes  dos dados do candidato, e com isso os dados estavam sendo aproveitados de forma incorreta.

Com objetivo de evitar esse cenário, foi implementada a partir da versão **12.1.2410** uma nova camada de validação, que baseado no critério de unicidade verifica se os dados do cadastro da pessoa vinculada (**CODPESSOA)** corresponde aos dados cadastrados para o candidato, caso os dados estejam divergentes o sistema limpa o campo CODPESSOA para que a matricula ou inscrição seja concluída considerando os dados do candidato de forma correta.

A regra acima será aplicada somente se o processo seletivo estiver com a opção "**CPF, passaporte ou registro geral**" marcada no critério de unicidade.

Atenção

Caso uma informação esteja preenchida no Cadastro de Usuário e essa informação não esteja preenchida no Cadastro de Pessoa ela não será sobrescrita, mantendo a informação cadastrada no Usuário.

**Exemplo:**

Cadastro de Pessoa → Campo E-mail = Vazio  
Cadastro de Usuário → Campo E-mail = [processoseletivo@totvs.com.br](mailto:processoseletivo@totvs.com.br)

Considerando o exemplo acima, o campo e-mail do Cadastro de Usuário será mantido com o valor "[processoseletivo@totvs.com.br](mailto:processoseletivo@totvs.com.br)"

**Atenção**

Ao recuperar os dados da pessoa, podem ocorrer não conformidades relacionadas à inconsistências no cadastro, por exemplo, podem existir cadastros antigos com informações incompletas, dados inválidos, e quando isto ocorrer será apresentada a mensagem de alerta conforme a imagem abaixo, sendo permitido ao candidato prosseguir com a inscrição.

*É possível visualizar a mensagem original  reportada pelo TOTVS Processo Seletivo ao solicitar o recurso de inspeção de código do navegador.*

Filiação

Esta mesma regra será aplicada ao copiar os dados do cadastro de **Filiações da Pessoa**, caso as Filiações já estejam cadastradas como usuários no TOTVS Processo Seletivo.

**Observação:** O sistema não irá recuperar as informações de Responsável Acadêmico e Responsável Financeiro vinculado ao Aluno, tendo em vista que somente as informação do Cadastro de Pessoas e as suas Filiações que serão recuperadas.

É possível manter atualizado o cadastro de Pessoa do RM conforme a informações preenchidas na inscrição do processo seletivo, para isso é necessário habilitar uma parametrização no processo seletivo.

Para saber mais informações [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=285638806).

Integração TOTVS RH (candidato ou responsável é um funcionário)

A partir da criação do parâmetro "**Aproveitar dados do cadastro de Pessoa**” os usuários que forem aproveitados do cadastro de Pessoa (TOTVS RH) passarão a possuir vínculo com o cadastro de usuário do TOTVS Processo Seletivo.

Além desta evolução, mesmo que o processo seletivo não esteja com o parâmetro "**Aproveitar dados do cadastro de Pessoa**” habilitado, realizamos uma melhoria na funcionalidade de matricula do TOTVS Processo Seletivo para que ao matricular o aluno o TOTVS Educacional também realize o vínculo lógico do cadastro da Pessoa com o cadastro do usuário do processo seletivo (criamos o campo CODPESSOA na tabela SPSUSUARIO).

Portanto, não será possível realizar alterações nos **dados pessoais ou de filiações** de um candidato que seja um **funcionário da instituição** (que esteja cadastrado no TOTVS RH, estando ativo ou não), pois o cadastro de usuário do TOTVS Processo Seletivo é totalmente integrado com o cadastro de Pessoa do TOTVS RH e qualquer alteração poderá afetar o eSocial.

Quando este cenário ocorrer, ao realizar a inscrição será apresentado a informação abaixo:

Atenção

Se um dos responsáveis do candidato for um funcionário da instituição, a mensagem a acima será apresentada para o responsável em questão e seus dados não poderão ser alterados.

Por exemplo,

**Candidato:** João

**Filiação 1 (Pai):** José (é um funcionário)

**Filiação 2(Mãe):** Maria

Será permitido alterar os dado do candidato, filiação 2 (Mãe) e não será permitido alterar os dados da filiação 1(Pai), pois é um funcionário.

Quando na inscrição alguma informação não estiver preenchida e estiver bloqueada para alteração em função de ser um funcionário, e esta informação for **obrigatória**, será permitido dar prosseguimento na inscrição, ou seja, não será apresentado nenhum alerta informando que o campo não foi preenchido.
