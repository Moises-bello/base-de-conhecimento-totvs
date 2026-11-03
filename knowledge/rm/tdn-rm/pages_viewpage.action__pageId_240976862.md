---
content_hash: 01198feb7fc3993dd5d1d731d48ad4491479fb82d3ac49288d9ffbcb5cc22559
fetched_at: '2026-06-29T00:08:10.683758+00:00'
page_id: '240976862'
product: rm
source: tdn-rm
title: DT_Funcionalidades_para_empresa_responder_avaliações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=240976862
version: 120
---

# Funcionalidades para a empresa (responder avaliações)

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Cadastrar Avaliação Institucional | Processo de Geração de Avaliação Institucional | | Funcionários da Empresa | Cadastro de Funcionários da Empresa Parceira | | Avaliação Institucional Portal | Responder Avaliação Institucional Pelo Portal | |
| **Requisito (ISSUE):** | [EDUEDU001-4](http://jiraproducao.totvs.com.br/browse/EDUEDU001-4 "EDU - Funcionalidades para a empresa (Responder avaliações)") |
| **País(es):** | Todos |

## Descrição

Essa implementação tem como objetivo possibilitar que os funcionários das empresas parceiras da instituição para estágio, possam através do portal, responder à avaliações institucionais, da mesma forma como já é possível para alunos, professores, funcionários e egressos.

**Definição de permissão para os perfis de empresa**

Basta acessar**Serviços Globais | Segurança | Perfis**, selecionar o sistema "**Educacional**" e em seguida alterar o perfil desejado incluindo ou excluindo as permissões de acesso, que nesse caso se resumem ao item **Educacional - Outras Permissões - RM Portal - Portal - Avaliação Institucional.**

****Cadastro de funcionário da empresa parceira****

A partir dessa release (12.1.12), foi feita uma mudança no cadastro de funcionários da empresa no sistema, no portal, na página pública de solicitação de cadastro de funcionários de empresas parceiras e no Fluig dentro do fluxo de solicitação de cadastro de funcionários de empresas parceiras de estágio.

Essa alteração foi necessário pois, para responder aos questionários de avaliação institucional, há um requisito de sistema que precisava ser atendido, e está detalhado a seguir:

O questionário de avaliação institucional é criado com a utilização do TOTVS Avaliação e Pesquisa e exige que todos os candidatos que responderão às questões criadas sejam pessoas cadastradas no sistema. Dessa forma, foi necessário incluir no cadastro de funcionários de empresas parceiras, todos os campos que possibilitassem a validação de unicidade de pessoas no sistema para o caso de ser necessário a criação de um registro de pessoa para os funcionários selecionados para responderem à avaliação institucional.

Sendo assim, as seguintes alterações foram realizadas:

* Inclusão dos campos Estado Natal e Naturalidade do funcionário;
* Aumento do tamanho do campo Nome do Funcionário para 120 caracteres;
* Inclusão do campo Código da Pessoa no Cadastro de Funcionários da Empresa Parceira;
* O campo Código da Pessoa só será preenchido caso haja a geração de avaliação institucional a ser respondida pelo funcionário;
* Para acesso ao portal o código de usuário a ser considerado continuará sendo o definido no cadastro de funcionários da empresa;
* Quando o campo Código da Pessoa estiver preenchido para um funcionário, os campos a seguir precisam estar sincronizados entre funcionários e pessoas:
  + Nome do funcionário;
  + CPF do funcionário.
  + Telefone de contato do funcionário;
  + Data de nascimento do funcionário;
  + Código da cidade natal do funcionário;
  + Estado natal do funcionário;
  + Número do passaporte do funcionário;
  + País de origem do passaporte do funcionário;
  + Data de emissão do passaporte do funcionário;
  + Data de validade do passaporte do funcionário;
  + Carteira de identidade do funcionário;
  + Unidade da federação da carteira de identidade do funcionário;
  + Órgão emissor da carteira de identidade do funcionário;
  + Data de emissão da carteira de identidade do funcionário;
* Uma alteração nos campos de sincronização automática (citados anteriormente) no cadastro de funcionário deve disparar a atualização das informações no cadastro de pessoa e em todos os funcionários vinculados a esta mesma pessoa. De forma inversa toda alteração em uma pessoa deve disparar a atualização em todos os funcionários vinculados a esta pessoa.

Foram incluídos 3 anexos ao cadastro de funcionários da empresa parceira, que são:

* Provas realizadas: possibilita a visualização da lista de provas respondidas pelo funcionário;
* Pesquisas realizadas: possibilita a visualização da lista de pesquisas respondidas pelo funcionários;
* Provas e pesquisas pendentes: possibilita a visualização da lista de provas e pesquisas pendentes de resposta pelo funcionário.

Não será possível associar uma pessoa à um funcionário manualmente, direto da tela de cadastro de funcionários da empresa parceira ou da tela de cadastro de pessoas. Esse procedimento será realizado automaticamente pelo sistema no momento da geração da avaliação institucional, caso seja necessário, a intervenção do usuário será solicitada como um dos passos do processo para definição nos casos em que mais de um perfil de pessoa puder ser associado a um funcionário e essa associação só será realizada após o processo de geração de avaliação institucional ser concluído com sucesso.

**Processo de cadastro de avaliação institucional**

O processo de geração de avaliação institucional foi alterado para possibilitar, além das opções existentes, a geração de avaliação institucional para funcionários das empresas parceiras de estágio.

A seleção de candidatos será feita a partir do cadastro de funcionários de empresas parceiras, sendo que, apenas funcionários ativos poderão ser selecionados.

A partir desse filtro, que deverá ser definido pelo usuário, houveram as seguintes mudanças

* De acordo com os critérios de unicidade de pessoas definido no sistema (Recursos Humanos | Configurações | Parametrizador | Gerais | Validações), os campos obrigatórios são validados e caso não estejam preenchidos o usuário recebe uma mensagem solicitando o preenchimento antes de habilitar o avanço para a próxima etapa do processo;
* Na etapa seguinte, seguindo o critério de unicidade de pessoas, o sistema identifica com base nos campos de unicidade, as possibilidades de funcionários que correspondem à pessoas já cadastradas na base de dados e caso seja necessário, solicita ao usuário que faça a associação de um funcionário à pessoa que foi encontrada.

Da mesma forma como já era feito para alunos, professores e egressos, ao selecionar um candidato, podemos visualizar as avaliações já cadastradas para o mesmo.

A seleção da avaliação, período e grupo segue da mesma forma, porém, caso a tipo de objeto avaliado seja o curso, a empresa parceira deve ter convênio e público alvo cadastrados para que seja possível gerar avaliação para seus funcionários. para o caso do tipo de objeto avaliado ser pessoa ou um novo tipo, não é obrigatório que a empresa possua convênio e público alvo cadastrados no sistema.

Após a execução do processo, os funcionários selecionados, caso tenham usuário e senha de acesso ao portal, poderão acessá-lo para executar a avaliação institucional.

divs
