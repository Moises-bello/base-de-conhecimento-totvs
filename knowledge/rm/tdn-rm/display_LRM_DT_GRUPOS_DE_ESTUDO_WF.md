---
content_hash: e87fcdbe1d15f89587acb10c258b9412b1267ec391cbec609288bee6f6941b80
fetched_at: '2026-06-29T00:08:32.373861+00:00'
page_id: '273983724'
product: rm
source: tdn-rm
title: DT_GRUPOS_DE_ESTUDO_WF
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_GRUPOS_DE_ESTUDO_WF
version: 4
---

# CADASTRO E ACOMPANHAMENTO DE GRUPOS DE ESTUDO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Educacional* |
| **Módulo:** | ************Inovação,********** Pesquisa e Extensão** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cadastro de Grupos de Estudo* | *Cadastro de Grupos de Estudo* | | *Acompanhamento de Grupos de Estudo* | *Acompanhamento de Grupos de Estudo* | |
| **Cadastros Iniciais:** | *Tipos de Ação*   *Áreas de Conhecimento*  *Pesquisador* |
| **Requisito (ISSUE):** | *PCREQ-5449* |
| **País(es):** | *Brasil* |
| **Tabelas Utilizadas:** | *SEXTGRUPOESTUDO, SEXTAREASGRUPOESTUDO,*  *SEXTPARTICIPANTESGRUPO, SEXTLEMBRETEGRUPO,*  *SEXTATIVIDADEGRUPO* |
| **Versões/Release:** | *12.1.15* |

## Descrição

Possibilita ao usuário gerenciar seus processos referentes a criação/acompanhamento de grupos de estudo, permitindo realizar o cadastro, submeter a análise e avaliação utilizando-se do processo de aprovação através de FLUIG.

Pré-requisitos para utilizar a funcionalidade de cadastro de grupos de estudo

* Ter o FLUIG devidamente instalado e configurado conforme documentação:
  + Instalação: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409653>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409655>
* Ter o TOTVS Developer Studio (TDS) devidamente instalado e configurado.
  + Instalação: <http://tdn.totvs.com/display/fluig/Como+Instalar+-+TOTVS+%7C+Developer+Studio>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=73078179>
* Criar no FLUIG os papéis necessários para a execução do fluxo de cadastro/acompanhamento de grupos de estudo. É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os papéis).
  + Código = **pesquisador**| Descrição = **Pesquisador**
  + Código = **reitoria\_extensao**| Descrição = **Reitoria de Extensão**
* Associar adequadamente os usuários do FLUIG aos papéis criados anteriormente.
* Importar os fluxos de "cadastro de grupos de estudo" e "acompanhamento de grupos de estudo" para a ferramenta TOTVS Developer Studio (TDS). Caso não tenha alterado a instalação padrão dos produtos TOTVS, os arquivos zipados, contendo o(s) fluxo(s), estarão disponíveis em **c:\totvs\CorporeRM\ObjetosGerenciais\Fluig**  
  + Configuração: [http://tdn.totvs.com/download/attachments/172300565/RM\_BT\_Montagem\_Ambiente\_Workflows\_Fluig.pdf](http://tdn.totvs.com/download/attachments/172300565/RM_BT_Montagem_Ambiente_Workflows_Fluig.pdf?version=1&modificationDate=1432910252000&api=v2)
* Exportar para o servidor do FLUIG os datasets, diagrama, formulário e eventos do "cadastro de grupos de estudo" e "acompanhamento de grupos de estudo".  
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=189313846>

## Procedimento para Utilização

## Cadastro de Grupos de Estudo

O usuário deve iniciar uma nova solicitação escolhendo a opção "Educacional | Inovação, Pesquisa e Extensão | Grupos de Estudo | Grupos de Estudo". É necessário estar vinculado ao papel de "Pesquisador" para realizar essa solicitação.

O formulário de cadastro será aberto com o código do pesquisador vinculado ao usuário do FLUIG, sendo esse o usuário que será cadastrado como solicitante do grupo no TOTVS Educacional.

Após preencher as informações do cadastro o usuário enviará a solicitação para "**Solicitar Aprovação**", onde um usuário, vinculado ao papel de "Reitoria de Extensão", vai verificar as informações preenchidas.

Nessa etapa, o usuário vinculado ao papel de "Reitoria de Extensão" terá duas opções:

* Avançar etapa para "**Solicitação Reprovada**"  
  O grupo de estudo será cadastrado mas não será aprovado e um parecer deverá ser informado pelo usuário responsável pela solicitação.
* Avançar etapa para "**Solicitação Aprovada**"  
  O grupo de estudo será cadastrado como aprovado no TOTVS Educacional.

## Acompanhamento de Grupos de Estudo

O usuário deve iniciar uma nova solicitação escolhendo a opção "Educacional | Inovação, Pesquisa e Extensão | Acompanhamento Grupos Estudo | Acompanhamento Grupos Estudo". É necessário estar vinculado ao papel de "Pesquisador" para realizar essa solicitação.

Para o correto funcionamento desse fluxo, o grupo de estudo já deve estar cadastrado e aprovado, conforme descrito no primeiro fluxo acima.

O formulário de acompanhamento será aberto e mostrará apenas os grupos de estudo que estiverem relacionados ao usuário logado no FLUIG.

Após preencher as informações do acompanhamento o usuário enviará a solicitação para "Atividade Cadastrada", onde as informações serão atualizadas no TOTVS Educacional e o fluxo será concluído.
