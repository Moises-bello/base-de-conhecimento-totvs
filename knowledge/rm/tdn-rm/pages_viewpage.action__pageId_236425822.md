---
content_hash: cc4312a5ccd616931674f0dd7e44c4fa234ed7e48d8aede3f2d09cd3f81c9fbc
fetched_at: '2026-06-29T00:08:05.996325+00:00'
page_id: '236425822'
product: rm
source: tdn-rm
title: DT_Alteracao_Dados_Cadastrais_Empresa_Funcionário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=236425822
version: 123
---

# Alteração de dados cadastrais da empresa/funcionários pelo portal

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Dados da empresa parceira. | Alteração dos dados da empresa parceira pelo portal | | Dados do funcionário da empresa parceira | Alteração dos dados dos funcionários da empresa parceria pelo portal | | Central de notificações | Central de notificações | | Geração de usuários (funcionários) | Geração de usuários (funcionários) | | Cadastro de funcionários da empresa | Cadastro de funcionários da empresa |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | |  |  | |  |  | |
| **Requisito (ISSUE):** | [PCREQ-10622](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-10622 "PCREQ-10622") |
| **País(es):** | Todos |

## Descrição

Possibilitar que a empresa possa pelo portal alterar os seus dados cadastrais e de seus funcionários.

**Definição de permissão para os perfis de empresa**

Basta acessar **Serviços Globais | Segurança | Perfis**, selecionar o sistema "**Educacional**" e em seguida alterar o perfil desejado incluindo ou excluindo as permissões de acesso. Abaixo as permissões disponíveis (**Educacional - Outras permissões - RM Portal - Portal - Empresa**):

* Dados da Empresa Parceira
  + Editar dados da empresa parceira
* Dados do Funcionário da Empresa Parceira
  + Inserir funcionário da empresa parceira
  + Excluir funcionário da empresa parceira
  + Editar dados do funcionário da empresa parceira
  + Editar dados apenas do funcionário da empresa parceira logado

A partir dessas permissões o acesso as novas funcionalidades no portal da empresa poderão ser negadas ou liberadas.

**Alteração dos dados da empresa parceira**

A forma como esta tela será apresentada dependerá das permissões definidas no perfil do usuário logado, podendo ter os seguintes comportamentos:

* Disponibilizar apenas a consulta dos dados cadastrais ou também sua edição.
* Disponibilizar a visualização dos funcionários da empresa, possibilitando apenas a consulta ou também a inclusão, alteração e exclusão de funcionários.

Apenas os campos "Identificador da empresa", "categoria" e "parceria de estágio" não serão exibidos no portal da empresa, estes são dados de uso interno da instituição de ensino. 

**Alteração dos dados do funcionário da empresa parceira**

* Se o perfil associado ao usuário logado no portal tiver a permissão "Editar dados do funcionário da empresa parceira" ou "Editar dados apenas do funcionário da empresa parceira logado" o usuário poderá alterar todos os dados cadastrais exceto o código do usuário de acesso ao portal.
* Se o perfil associado ao usuário logado no portal tiver apenas a permissão "Dados do Funcionário da Empresa Parceira" este poderá apenas visualizar os dados de seu cadastro, no entanto, não poderá fazer nenhuma alteração

**Central de notificações**

Criada uma nova notificação que pode ser disparada sempre que o endereço da empresa for alterado, para tanto serão respeitadas as seguintes regras:

* A mensagem "Informar inscritos sobre alteração de endereço da empresa" deve estar configurada em **Atividades Acadêmicas | Central de notificações | Mensagens de notificação**
* A mensagem será disparada se pelo menos um dos seguintes campos for alterado: CEP, logradouro, número, complemento, bairro, país, estado, município
* Para definição da mensagem a ser encaminhada o usuário poderá utilizar as seguintes tag's:
  + - IDVAGA (Identificador da vaga de estágio)
    - NOMEEMPRESA (Nome fantasia da empresa)
    - NUMEROCONVENIO (Número do convênio da empresa com a instituição de ensino)
    - CARGO (Cargo referenciado na vaga de estágio)
    - DEPARTAMENTO (Departamento referenciado na vaga de estágio)
    - LOCALTRABALHO (Local de trabalho)
    - RUA (Logradouro da empresa)
    - NUMERO (Número da empresa)
    - BAIRRO (Bairro da empresa)
    - ESTADO (Unidade da federação onde está localizada a empresa)
    - MUNICIPIO (Município da empresa)
    - PAIS (País da empresa)
    - CEP (CEP da empresa)
    - COMPLEMENTO (Complemento do endereço da empresa)

**Processo de geração de usuário para funcionários**

Os funcionários inativos não mais são listados no processo de geração de usuários para os funcionários.

**Cadastro de funcionários para a empresa parceira**

A alteração do status do funcionário da empresa parceira (SEMPRESA) poderá refletir na alteração do status do seu usuário de acesso ao portal, desde que este usuário não esteja vinculado a nenhuma outra entidade (aluno, professor, pesquisador, responsáveis do aluno e coordenadores).

Exemplo: O funcionário da empresa é também um aluno da instituição, neste cenário se o funcionário tiver seu status modificado para inativo o sistema não pode atualizar o status do usuário.

As funcionalidades do portal da empresa ficam visíveis ao funcionário da empresa parceira que estiver inativo e vinculado a um usuário ativo do portal que possua perfil de acesso a estas funcionalidades. No entanto, neste cenário quando o usuário tentar acessá-las receberá como retorno uma mensagem informando que tal acesso não será permitido 

 Observação: O termo funcionário utilizado neste documento faz referência ao cadastro de funcionário da empresa parceira (SEMPRESAFUNCIONARIO - **Atividades acadêmicas | Empresas | Funcionários da empresa**) e não a cadastro de funcionários do Labore (PFUNC).

divs
