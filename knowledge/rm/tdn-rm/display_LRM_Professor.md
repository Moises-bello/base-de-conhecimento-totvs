---
content_hash: 17e46fca973aabd6e1b3b89407ac599797e75a6defc5b57dba7ae5e899bcf049
fetched_at: '2026-06-29T00:09:32.487542+00:00'
page_id: '425458859'
product: rm
source: tdn-rm
title: Professor
type: documentation
url: https://tdn.totvs.com/display/LRM/Professor
version: 17
---

# Geral

Esta tela permite cadastrar e editar os dados dos professores da instituição.

Existem algumas regras para que momento do cadastro de um professor, caso o usuário não tenha escolhido uma pessoa existente, o sistema irá verificar se já existe aquela pessoa cadastrada de acordo com os seguintes critérios   
Nome, CPF e Data de nascimento; Nome, Carteira de identidade (CI) e UF da CI; Nome, Carteira de trabalho (CT) e Série da CT; Nome e Data de nascimento.

No momento do cadastro preencha apenas os critérios definidos acima, logo após selecione o botão salvar para que o sistema inicie a procura por um cadastro existente. Isso irá agilizar o cadastro.   
Caso o sistema encontre os mesmos dados, será exibida uma mensagem informando se o usuário deseja copiar os dados cadastrados da pessoa existente para o novo cadastro. Em caso negativo, o sistema não irá salvar o registro.Vale ressaltar que o cadastro obedece os critérios parametrizados de unicidade no Gestão de Pessoas (). Além disso, a obrigatoriedade do CPF também pode ser definida, entretanto a parametrização que prevalecerá é a do Totvs Educacional em  e não a do Totvs Gestão de Pessoas em .

## Campo Código

Contém o código da pessoa vinculada a este professor. É possível acessar o cadastro da pessoa por este campo, para isso, basta clicar no valor do campo **Código**.

## Campo Chapa

O campo chapa é de preenchimento automático, porém ele somente é preenchido se o  possui uma função que é vinculado a uma função de professor no  em Menu | Currículo e Oferta | Aluno e Professor | Professores | . Caso este vínculo não tenha sido feito, mesmo o funcionário tendo **chapa** ele não será preenchido automaticamente no cadastro do Professor.

Vale ressaltar que quando ocorre o preenchimento automático deste campo, é feito automaticamente o cadastro  que é um anexo do cadastro do Professor.

O botão **Trocar a chapa** só estará habilitado se o professor for funcionário que exerce função de professor e tiver mais de uma chapa, entretanto a troca de chapa somente será possível o mesmo Professor possuir dois registros de  associados a mesma  com **chapas**diferentes e que as funções esteja associadas as , caso atenda as estas regras, ao clicar no botão será aberta uma janela que o usuário poderá trocar a **chapa**do Professor, conforme abaixo.

## Campo Nacionalidade

Caso o campo de nacionalidade seja diferente de brasileiro, documentos específicos para estrangeiro serão apresentados na pasta de documentos complementares.

## Campos Complementares

Mediante parametrização através do Educacional é possível incluir alterar ou excluir [campos complementares](https://tdn.totvs.com/display/LRM/Campos+Complementares+-+TOTVS+Educacional?draft=true) no cadastro de pessoa.

Além de visualizar ou realizar alterações na máscara de telefone do cadastro de pessoa,  através do Educacional, na tela [parâmetros do RH](https://tdn.totvs.com/pages/viewpage.action?pageId=825322419).

# Documentos

Nesta aba informamos dados necessários como CPF, RG e Título de Eleitor. Em casos de professores estrangeiros, é possível informar o passaporte ou registro geral. Vale ressaltar que o CPF poderá ser obrigatório e esta obrigatoriedade pode ser parametrizada em dois lugares diferentes, sendo um no próprio Totvs Educacional () e outro no Gestão de Pessoas (), entretanto a parametrização do Totvs Educacional que irá prevalecer.

Informações Complementares

---

Como Fazer

---

Veja Também

---

[Titulações](http://tdn.totvs.com.br/pages/viewpage.action?pageId=425458334)
