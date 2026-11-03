---
content_hash: 2738dbeb1b3961422798b38793739415ecf05b2b82a6d235b44be677a0ca3fae
fetched_at: '2026-06-29T00:08:32.438948+00:00'
page_id: '273985965'
product: rm
source: tdn-rm
title: DT_CADASTRO_PESQUISADOR_EXTENSIONISTA_WF
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_CADASTRO_PESQUISADOR_EXTENSIONISTA_WF
version: 4
---

# Cadastro de Pesquisador/Extensionista

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Educacional* |
| **Módulo:** | ************Inovação,********** Pesquisa e Extensão** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cadastro de Pesquisador/Extensionista* | *Cadastro de Pesquisador/Extensionista* | |
| **Requisito (ISSUE):** | *PCREQ-5446* |
| **País(es):** | *Brasil* |
| **Tabelas utilizadas:** | *SPROJPESQUISADOR, SPROJPESQUISADORFILIAL, SPROJPESQUISADORAREACONRESP* |
| **Versões/Release:** | *12.1.15* |

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
  + Código = **aprov\_pesquisador\_extensionista**| Descrição = **Aprovador de pesquisador/extensionista**
* Associar adequadamente os usuários do FLUIG aos papéis criados anteriormente.
* Importar o fluxo de cadastro de pesquisador/extensionista para a ferramenta TOTVS Developer Studio (TDS). Caso não tenha alterado a instalação padrão dos produtos TOTVS, os arquivos zipados, contendo o(s) fluxo(s), estarão disponíveis em **c:\totvs\CorporeRM\ObjetosGerenciais\Fluig**  
  + Configuração: [http://tdn.totvs.com/download/attachments/172300565/RM\_BT\_Montagem\_Ambiente\_Workflows\_Fluig.pdf](http://tdn.totvs.com/download/attachments/172300565/RM_BT_Montagem_Ambiente_Workflows_Fluig.pdf?version=1&modificationDate=1432910252000&api=v2)
* Exportar para o servidor do FLUIG os datasets, diagrama, formulário e eventos do cadastro de pesquisador/extensionista.  
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=189313846>

## Procedimento para Utilização

O usuário deve iniciar uma nova solicitação escolhendo a opção "Educacional | Inovação, Pesquisa e Extensão | Pesquisador | Cadastro de Pesquisador/Extensionista". Não é necessário estar vinculado a nenhum papel para realizar essa solicitação.

O formulário de cadastro será aberto com o código da pessoa vinculada ao usuário do FLUIG, sendo esse o usuário que será cadastrado como pesquisador no TOTVS Educacional.

Além dos dados disponíveis na tela, o usuário solicitante deverá incluir, na aba de anexo, o seu currículo lattes. Esse anexo é obrigatório e será usado para importar o currículo do pesquisador para o TOTVS Educacional.

Após preencher os dados necessários ao cadastro, o usuário enviará a solicitação para a etapa de "Definir Características", onde outro usuário do FLUIG, vinculado ao papel de "aprov\_pesquisador\_extensionista", complementará as informações, e caso tenha alguma incoerência o mesmo poderá retornar o fluxo ao solicitante para realizar ajustes. Esse processo pode acontecer quantas vezes for necessário até as informações do pesquisador estarem corretas. Se tudo estiver correto, o usuário vinculado ao papel de "aprov\_pesquisador\_extensionista" concluirá o cadastro do solicitante como pesquisador/extensionista.
