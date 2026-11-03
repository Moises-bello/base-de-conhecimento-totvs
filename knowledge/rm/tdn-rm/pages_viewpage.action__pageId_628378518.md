---
content_hash: 4565066b3a9045174f6be85fd1177642281cbfc96f685f7ccca507269a434b92
fetched_at: '2026-06-29T00:11:05.269871+00:00'
page_id: '628378518'
product: rm
source: tdn-rm
title: Cópia de DT_INSCRICAO_VISITA_EVENTO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=628378518
version: 1
---

# Visita técnica/Participação em evento

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Educacional* |
| **Módulo:** | *Pesquisa, Extensão e Inovação* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Inscrição em Visitas Técnicas/Eventos* | **Inscrição em* Visitas Técnicas/Eventos* | |
| **Cadastros Iniciais:** | *Solicitação de visita técnica/participação em evento* |
| **Requisito (ISSUE):** | **PCREQ-5449** |
| **País(es):** | **Brasil** |
| **Tabelas Utilizadas:** | *SEXTINSCRICAOVISITA* |
| **Versões/Release:** | *12.1.9* |

## Descrição

A inscrição em visitas técnicas/ventos permite ao usuário gerenciar as inscrições realizadas através de solicitações do FLUIG.

Pré-requisitos para utilizar a inscrição em visitas técnicas/eventos

* Ter o FLUIG devidamente instalado e configurado conforme documentação:
  + Instalação: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409653>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409655>
* Ter o TOTVS Developer Studio (TDS) devidamente instalado e configurado.
  + Instalação: <http://tdn.totvs.com/display/fluig/Como+Instalar+-+TOTVS+%7C+Developer+Studio>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=73078179>
* Criar no FLUIG os papéis necessários para a execução do fluxo de inscrição em visitas técnicas/eventos. É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os papéis.
  + Código = **aluno**| Descrição = **Aluno**
  + Código = **pesquisador**| Descrição = **Pesquisador**
* Criar no FLUIG os grupos necessários para a execução do fluxo de inscrição em visitas técnicas/eventos. É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os grupos.
  + Código = **setor\_visitas**| Descrição = **Setor de visitas**
* Associar adequadamente os usuários do FLUIG aos papéis e grupos criados anteriormente.
* Importar o fluxo de inscrição em visitas técnicas/eventos para a ferramenta TOTVS Developer Studio (TDS). Caso não tenha alterado a instalação padrão dos produtos TOTVS, os arquivos zipados, contendo o(s) fluxo(s), estarão disponíveis em **c:\totvs\CorporeRM\ObjetosGerenciais\Fluig**  
  + Configuração: [http://tdn.totvs.com/download/attachments/172300565/RM\_BT\_Montagem\_Ambiente\_Workflows\_Fluig.pdf](http://tdn.totvs.com/download/attachments/172300565/RM_BT_Montagem_Ambiente_Workflows_Fluig.pdf?version=1&modificationDate=1432910252000&api=v2)
* Exportar para o servidor do FLUIG os datasets, diagrama, formulário e eventos da inscrição em visitas técnicas/eventos.  
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=189313846>

## Procedimento para Utilização

O usuário, vinculado ao papel "Aluno" ou "Secretaria", deverá realizar a inscrição escolhendo a opção "Educacional | Inovação, Pesquisa e Extensão | Visita Técnica/Evento | Inscrição em Visitas Técnicas/Eventos. Ao selecionar esse fluxo será apresentado um formulário com o código do aluno vinculado ao usuário do FLUIG. Nele deverão ser informados o termo de responsabilidade e a visita técnica/evento em que o aluno deseja se inscrever, porém serão listadas somente as visitas cujo público-alvo contemple o curso e habilitação desse aluno. Vale ressaltar que alunos menores de idade não podem realizar inscrição, somente seus responsáveis legais. Ela deverá ser realizada de forma presencial por um usuário com o papel "Secretaria". Após preencher as informações necessárias o fluxo será finalizado.
