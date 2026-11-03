---
content_hash: ff07b2643280b97a95e5493ca02228105a4969bd36967dcb07db4da7524b35c5
fetched_at: '2026-06-29T00:08:05.597116+00:00'
page_id: '235599082'
product: rm
source: tdn-rm
title: ER_PCREQ-10902_PEP_2_-_API_do_Formulário_dinâmico_-_Busca_de_informações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235599082
version: 119
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | TOTVS GESTÃO HOSPITALAR |
| **Projeto** | * [R\_SAU\_RM\_V12\_1516](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+R_SAU_RM_V12_1516 "R_SAU_RM_V12_1516") | **IRM** | * [PCREQ-10856](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-10856 "PCREQ-10856") |
| **Requisito** | * [PCREQ-10902](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-10902 "PCREQ-10902") | **Subtarefa** | * [SAU\_DEV-4758](http://jira.totvs.com.br/browse/SAU_DEV-4758) |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

   Esta especificação tem como objetivo detalhar a melhoria à ser implementada na integração entre RM Saúde e a API da aplicação de Formulários Dinâmicos, utilizada pelo PEP 2.

## Definição da Regra de Negócio

 **RN001** **-**Deve ser criado um novo parâmetro, em parâmetros gerais, permitindo ao usuário informar a URL da aplicação de formulários dinâmicos,

**RN002 -**Para a integração entre RM Saúde e Formulários Dinâmicos, deve ser criado um novo cadastro, onde serão necessárias as seguintes informações:

* Tabela do RM e Campo do RM, correspondentes à informação que será buscada do Formulário;
* ID do formulário dinâmico, onde deverá ser informado o ID do formulário cadastrado na aplicação de Formulários Dinâmicos;
* Campo do Formulário Dinâmico, que será o campo buscado na pesquisa à API;
* Utiliza Attention ID, que deverá ser setado como "T", caso o formulário tenha em seu filtro a tag "attentionId".;

***\*\*Importante: Neste cadastro não será permitido incluir ou excluir, apenas editar. Os dados serão alimentados pelo responsável pela implementação, via insert em banco. Cada cliente poderá ter formulários e metadados cadastrados de forma diferente.***

   **RN003 -** Será criada uma Classe Server, bem como sua Interface, que será a responsável por realizar a consulta à API de formulários dinâmicos e retornar a informação desejada. Os seguintes pontos devem ser observados:

* A API espera uma URL como requisição, onde já deverão estar todos os filtros montados, seguindo o padrão descrito no documento que está publicado em: ;
* O Método utilizado para a pesquisa deverá ser genérico, retornando qualquer campo que seja informado na chamada da aplicação;

**RN004 -**Deve ser implementada a consulta à API, no momento da pesquisa por paciente, no registro de Alta do Paciente, seguindo as seguintes regras:

* Quando a pesquisa por paciente for realizada e o parâmetro geral (**RN001**) estiver com a URL configurada, o sistema deverá chamar a integração e retornar o CID de alta do paciente (campo CIDPRINCIPAL da tabela SZATENDIMENTO);
* Quando estiver vazia a URL, sistema mantém a rotina normal de execução.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parâmetros Gerais | Alteração | Opções > Parâmetros > Parâmetros Gerais | **RN001** |
| Correlação com Formulário Dinâmico | Criação | Cadastros > Registro e Controle > Correlação com Form. Dinâmico | **RN002** |
| Pesquisa à Formulários Dinâmicos | Criação | - | **RN003** |
| Registro de Alta | Alteração | Atendimento > Internação > Alta | **RN004** |

**Exemplo de Aplicação:**

* Realize o insert no banco de dados, na tabela "**SZCAMPOSFORMDINAMICO**", com as informações referentes à coluna "**CIDPRINCIPAL**" da tabela "**SZATENDIMENTO**", e de onde será trazida a informação(**IDFORMDINAMICO** e**CAMPOFORMDINAMICO**),  
  a coluna "**UTILIZAATTENTIONID**", deverá ser "**T**", caso o formulário utilize essa tag e "**F**", caso contrário;
* Acesse o menu "**Opções > Parâmetros > Parâmetros Gerais**" e, na aba "**Integração**", informe a URL da aplicação do formulário dinâmico;
* Acesse o menu "**Cadastros > Registro e Controle > Correlação com Form. Dinâmico**" e valide se o registro correspondente à coluna "**CIDPRINCIPAL**" da tabela "**SZATENDIMENTO**", está corretamente correlacionado com o formulário dinâmico;
* Acesse o menu "**Atendimento > Internação > Alta**" e selecione o paciente desejado (que já possua alta preenchida no formulário dinâmico configurado). Sistema deverá preencher o campo CID(Alta) com o valor correspondente.

**Tabelas Utilizadas**

SZCAMPOSFORMDINAMICO

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
