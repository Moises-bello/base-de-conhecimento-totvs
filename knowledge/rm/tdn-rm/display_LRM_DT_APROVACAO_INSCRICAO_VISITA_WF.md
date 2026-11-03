---
content_hash: ae2d931b3937d43e8cbbc8e6922dba823cf7cc0d9484163e9571cb25e98cd01f
fetched_at: '2026-06-29T00:08:32.540204+00:00'
page_id: '273990435'
product: rm
source: tdn-rm
title: DT_APROVACAO_INSCRICAO_VISITA_WF
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_APROVACAO_INSCRICAO_VISITA_WF
version: 3
---

# Visitas técnicas/participação em eventos

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Educacional* |
| **Módulo:** | *Inovação, Pesquisa e Extensão* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Aprovação das Inscrições da Visita/Evento* | *Aprovação das Inscrições da Visita/Evento* | |
| **Cadastros Iniciais:** | *Inscrição em visitas técnicas/eventos* |
| **Requisito (ISSUE):** | **PCREQ-5449** |
| **País(es):** | **Brasil** |
| **Tabelas Utilizadas:** | *SEXTINSCRICAOVISITA* |
| **Versões/Release:** | *12.1.15* |

## Descrição

A aprovação das inscrições da visita/evento permite ao usuário gerenciar as aprovações realizadas através de solicitações do FLUIG.

Pré-requisitos para utilizar a aprovação das inscrições da visita/evento

* Ter o FLUIG devidamente instalado e configurado conforme documentação:
  + Instalação: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409653>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409655>
* Ter o TOTVS Developer Studio (TDS) devidamente instalado e configurado.
  + Instalação: <http://tdn.totvs.com/display/fluig/Como+Instalar+-+TOTVS+%7C+Developer+Studio>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=73078179>
* Criar no FLUIG os papéis necessários para a execução do fluxo de aprovação das inscrições da visita/evento. É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os papéis.
  + Código = **pesquisador**| Descrição = **Pesquisador**
* Associar adequadamente os usuários do FLUIG aos papéis e grupos criados anteriormente.
* Importar o fluxo de aprovação das inscrições da visita/evento para a ferramenta TOTVS Developer Studio (TDS). Caso não tenha alterado a instalação padrão dos produtos TOTVS, os arquivos zipados, contendo o(s) fluxo(s), estarão disponíveis em **c:\totvs\CorporeRM\ObjetosGerenciais\Fluig**  
  + Configuração: [http://tdn.totvs.com/download/attachments/172300565/RM\_BT\_Montagem\_Ambiente\_Workflows\_Fluig.pdf](http://tdn.totvs.com/download/attachments/172300565/RM_BT_Montagem_Ambiente_Workflows_Fluig.pdf?version=1&modificationDate=1432910252000&api=v2)
* Exportar para o servidor do FLUIG os datasets, diagrama, formulário e eventos da aprovação das inscrições da visita/evento.  
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=189313846>

## Procedimento para Utilização

O usuário, vinculado ao papel "Pesquisador", deverá realizar a aprovação dos inscritos através da opção "Educacional | Inovação, Pesquisa e Extensão | Visita Técnica/Evento | Aprovação das Inscrições da Visita/Evento. Ao selecionar esse fluxo será apresentado um formulário com opção de seleção das visitas técnicas/eventos solicitados pelo pesquisador vinculado ao usuário do FLUIG. Assim que a visita for informada serão apresentados todos os alunos que estão inscritos e que não tiveram sua inscrição aprovada. Os aprovados irão receber um e-mail e/ou notificação no FLUIG. O conteúdo desse e-mail deverá ser preenchido na tela "Mensagens de notificação" com o objetivo "Aprovação das inscrições da visita/evento (extensão)", existente na central de notificação do módulo educacional.
