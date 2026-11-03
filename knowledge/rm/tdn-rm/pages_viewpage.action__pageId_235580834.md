---
content_hash: 6d90e129ed22227617c23f944cd47dca095b328e593b38a7a62057dc6ca51740
fetched_at: '2026-06-29T00:08:04.750879+00:00'
page_id: '235580834'
product: rm
source: tdn-rm
title: ER_PCREQ-10622_Alteracao_Dados_Cadastrais_Empresa_Funcionário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235580834
version: 126
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Educacional | **Módulo** | EDU |
| **Segmento Executor** | Educacional | | |
| **Projeto1** | WBS\_R\_EDU016\_1219 | **IRM1** | [PCREQ-10621](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-10621 "PCREQ-10621") |
| **Requisito1** | [PCREQ-10622](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-10622 "PCREQ-10622") | **Subtarefa1** | PDR\_EDU\_EDU021-30 |
| **Chamado2** |  | | |
| **País** | (  ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Possibilitar que a empresa possa pelo portal alterar os seus dados cadastrais da empresa e de seus funcionários.

## Definição da Regra de Negócio

**Requisito 1:** Criar controle de acesso para as funcionalidades do portal da empresa

* Consulta aos dados cadastrais da empresa/funcionários
* Alterar dados da empresa (possibilitar que o usuário logado possa alterar os dados cadastrais da empresa)
* Alterar dados do funcionário da empresa (possibilita que o usuário logado possa alterar apenas os seus dados cadastrais)
* Alterar dados de qualquer funcionário da empresa (possibilita que o usuário logado possa alterar os dados cadastrais de todos os funcionários)

**Requisito 2:** Criar página para exibir os "Dados da empresa/funcionários" pelo portal da empresa.

* Todos os campos disponíveis no executável estarão vísiveis na página da web, exceto, os campos "Empresa",  "Categoria" e "Parceria de estágio" não poderão ser alterados.
* No topo da página será exibido o nome do usuário e empresa logados

**Requisito 3:** A alteração do status do funcionário da empresa parceira (SEMPRESA) deve refletir no status do usuário vinculado a ele, desde que este usuário não esteja vinculado a nenhuma outra entidade (aluno, professor, pesquisador, responsáveis do aluno e coordenadores).

Exemplo:

* O funcionário da empresa é também um aluno da instituição, neste cenário se o funcionário tiver seu status modificado para inativo o sistema não pode atualizar o status do usuário.

**Requisito 4:** A geração de usuário para funcionário da empresa parceira não deve ser permitida para funcionários inativos(SEMPRESAFUNCIONARIO)

**Requisito 5:**  As funcionalidades do portal da empresa ficam visíveis ao funcionário da empresa parceira que estiver inativo e vinculado a um usuário ativo do portal com perfil de acesso a estas funcionalidades (este cenário pode acontecer como já detalhado no requisito 3). No entanto, neste cenário quando o usuário tentar acessar as funcionalidades receberá como retorno uma mensagem informando que tal acesso não será permitido.

**Requisito 6:** Criar uma nova mensagem de notificação para determinar o envio ou não de um aviso aos alunos matriculados quando houver alteração no endereço da empresa.

* A notificação será encaminhada para todos os inscritos em vagas cujo status é igual a  "Em aberto"
* Alterações nos seguintes campos da empresa disparam o envio da notificação
  + CEP
  + Logradouro
  + Número
  + Complemento
  + Bairro
  + Estado
  + Cód. Município
  + País
* Esta nova mensagem deverá possuir as seguintes tag's
  + IDVAGA
  + NOMEEMPRESA
  + NUMEROCONVENIO
  + CARGO
  + DEPARTAMENTO
  + LOCALTRABALHO
  + RUA
  + NUMERO
  + BAIRRO
  + ESTADO
  + MUNICIPIO
  + PAIS
  + CEP
  + COMPLEMENTO

Observação:

* O termo funcionário utilizado nesta especificação faz referencia ao cadastro de funcionário da empresa parceira (SEMPRESAFUNCIONARIO) e não a cadastro de funcionários do Labore (PFUNC).

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Dados cadastrais da empresa/funcionários | Criação | Portal - Empresa - Dados cadastrais da empresa/funcionários | - |
| Funcionários da empresa | Alteração | Atividades Acadêmicas - Empresas - Funcionários da empresa | - |
| Geração de usuários (Funcionários) | Alteração | Atividades Acadêmicas - Empresas - Geração de usuários (Funcionários) | - |
| Empresas | Alteração | Atividades Acadêmicas - Empresas | - |
| Mensagens de notificação | Alteração | Atividades Acadêmicas - Central de notificações - Mensagens de notificação | - |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
