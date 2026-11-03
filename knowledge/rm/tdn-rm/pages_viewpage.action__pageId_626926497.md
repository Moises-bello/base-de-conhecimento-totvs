---
content_hash: e5e1523a94b35ae51d6824bbf7206153f39cd6170f705ea08dff9cd31c722af5
fetched_at: '2026-06-29T00:11:04.457550+00:00'
page_id: '626926497'
product: rm
source: tdn-rm
title: Cópia de DT_CADASTRO_PESQUISADOR_EXTENSIONISTA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=626926497
version: 1
---

# Cadastro de Pesquisador/Extensionista

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Educacional* |
| **Módulo:** | **Pesquisa, Extensão e Inovação** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cadastro de Pesquisador/Extensionista* | *Cadastro de Pesquisador/Extensionista* | |
| **Requisito (ISSUE):** | *PCREQ-5446* |
| **País(es):** | *Brasil* |
| **Tabelas utilizadas:** | *SPROJPESQUISADOR, SPROJPESQUISADORFILIAL* |
| **Versões/Release:** | *12.1.7* |

## Descrição

Essa nova funcionalidade permite que o usuário do FLUIG solicite o seu cadastro como um pesquisador ou extensionista. Isso permitirá que o usuário possa participar de editais publicados pela instituição.

Pré-requisitos para utilizar a funcionalidade de cadastro de pesquisador/extensionista

* Ter o FLUIG devidamente instalado e configurado conforme documentação:
  + Instalação: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409653>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409655>
* Ter o TOTVS Developer Studio (TDS) devidamente instalado e configurado.
  + Instalação: <http://tdn.totvs.com/display/fluig/Como+Instalar+-+TOTVS+%7C+Developer+Studio>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=73078179>
* Criar no FLUIG os papéis necessários para a execução do fluxo de cadastro de pesquisador/extensionista. É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os papéis).
  + Código = **reitoria**| Descrição = **Reitoria**
* Associar adequadamente os usuários do FLUIG aos papéis criados anteriormente.
* Importar o fluxo de cadastro de pesquisador/extensionista para a ferramenta TOTVS Developer Studio (TDS). Caso não tenha alterado a instalação padrão dos produtos TOTVS, os arquivos zipados, contendo o(s) fluxo(s), estarão disponíveis em **c:\totvs\CorporeRM\ObjetosGerenciais\Fluig**  
  + Configuração: [http://tdn.totvs.com/download/attachments/172300565/RM\_BT\_Montagem\_Ambiente\_Workflows\_Fluig.pdf](http://tdn.totvs.com/download/attachments/172300565/RM_BT_Montagem_Ambiente_Workflows_Fluig.pdf?version=1&modificationDate=1432910252000&api=v2)
* Exportar para o servidor do FLUIG os datasets, diagrama, formulário e eventos do cadastro de pesquisador/extensionista.  
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=189313846>

## Procedimento para Utilização

O usuário deve iniciar uma nova solicitação escolhendo a opção "Educacional | Inovação, Pesquisa e Extensão | Pesquisador | Cadastro de Pesquisador/Extensionista". Não é necessário estar vinculado a nenhum papel para realizar essa solicitação.

O formulário de cadastro será aberto com o código da pessoa vinculada ao usuário do FLUIG, sendo esse o usuário que será cadastrado como pesquisador no TOTVS Educacional.

Além dos dados disponíveis na tela, o usuário solicitante deverá incluir, na aba de anexo, o seu currículo lattes. Esse anexo é obrigatório e será usado para importar o currículo do pesquisador para o TOTVS Educacional.

Após preencher os dados necessários ao cadastro, o usuário enviará a solicitação para a etapa de "Definir Características", onde outro usuário do FLUIG, vinculado ao papel de "Reitoria", complementará as informações, e caso tenha alguma incoerência o mesmo poderá retornar o fluxo ao solicitante para realizar ajustes. Esse processo pode acontecer quantas vezes for necessário até as informações do pesquisador estarem corretas. Se tudo estiver correto, o usuário vinculado ao papel de "Reitoria" concluirá o cadastro do solicitante como pesquisador/extensionista.
