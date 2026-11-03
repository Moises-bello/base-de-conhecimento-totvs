---
content_hash: be055ee7cb1d005d5a02f51ab6c91cecd3abb58e176e8749f02646b6910eba0f
fetched_at: '2026-06-29T00:08:04.520447+00:00'
page_id: '235573268'
product: rm
source: tdn-rm
title: ER_PCREQ-10643_Funcionalidade_para_Empresa_Consultar_Grades_Curriculares
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-10643_Funcionalidade_para_Empresa_Consultar_Grades_Curriculares
version: 117
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Educacional | **Módulo** | Educacional |
| **Segmento Executor** | Educacional | | |
| **Projeto1** | [WBS\_R\_EDU016\_1219](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+WBS_R_EDU016_1219 "WBS_R_EDU016_1219") | **IRM1** | PCREQ-10641 |
| **Requisito1** | [PCREQ-10643](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-10643 "PCREQ-10643") | **Subtarefa1** | [PDR\_EDU\_EDU021-15](http://jira.totvs.com.br/browse/PDR_EDU_EDU021-15) |
| **Chamado2** |  | | |
| **País** | (  ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 Disponibilizar para as empresas as informações a respeito das matrizes curriculares da instituição de ensino. 

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Consultar grades curriculares | Criação | Portal - Empresa - Cursos da Instituição | - |
|  |  |  |  |

Disponibilizar para as empresas as informações a respeito das matrizes curriculares da instituição de ensino. Para tanto serão respeitadas as seguintes regras:

1. Matrizes curriculares inativas não serão exibidas.
2. Apenas as matrizes curriculares vinculadas as coligadas, filiais e níveis de ensino que o usuário logada tiver acesso serão exibidas. A permissão deve ser cadastrada com direitos para acessar o Portal.  
   Essas permissões de acesso podem ser definidas através do processo de criação de usuários para o funcionário ou no cadastro de "Usuário" anexo "Usuário/Filial".
3. Algumas disciplinas da matriz curricular podem não ser exibidas dependendo do parâmetro "Exibir as disciplinas para o aluno de acordo com o campo ‘Imprime no Boletim' do cadastro de disciplinas da matriz curricular".
4. A interface de consulta as matrizes curriculares não solicitará nenhum tipo de filtro
5. As matrizes curriculares serão agrupadas na grid pelo contexto ao qual pertencem (Contexto: coligada -  nível de ensino)
6. O cabeçalho da página deverá exibir o nome do funcionário e o nome da empresa.
7. Será criado um novo menu no Portal na parte de administração denominado "Cursos da instituição"
8. A exibição das informações a respeito das matrizes curriculares da instituição de ensino seguirá o seguinte formato:  
   1. Lista das matrizes curriculares
      1. Informações do Curso
      2. Lista das disciplinas obrigatórias
         * Informações das disciplinas
         * Lista de complementos da disciplina
      3. Lista das disciplinas optativas e eletivas
         * Informações das disciplinas
         * Lista de complementos da disciplina
9. A lista com os complementos da disciplina seguirá a seguinte regra:
   1. Parâmetro "Manter histórico de complemento de disciplina por período letivo" estiver desmarcado todos os complementos serão listados.
   2. Parâmetro  "Manter histórico de complemento de disciplina por período letivo" marcado é listado os complementos do período letivo corrente que é definido no parâmetro do educacional. Caso este não esteja parametrizado nenhum complemento de disciplina será exibido.

## Protótipo de Tela

Menu:

 

Interface:

 

*<Caso necessário inclua protótipos de telas com o objetivo de facilitar o entendimento do requisito, apresentar conceitos e funcionalidades do software>.*

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
