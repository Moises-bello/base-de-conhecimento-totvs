---
content_hash: 562aa491894489c567d823bdfcc232dfe5ca9af5652804eb79c50e216da7b632
fetched_at: '2026-06-29T00:06:18.537304+00:00'
page_id: '219121393'
product: rm
source: tdn-rm
title: DT_AUXILIO_VISITA_EVENTO
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_AUXILIO_VISITA_EVENTO
version: 8
---

# Visitas técnicas/participação em eventos

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Educacional* |
| **Módulo:** | *Pesquisa, Extensão e Inovação* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Auxílio para Visitas Técnicas/Eventos.* | *Auxílio para Visitas Técnicas/Eventos.* | |
| **Cadastros Iniciais:** | *Solicitação de visitas técnicas/participação em eventos*  *Inscrição em visitas técnicas/eventos*  *Aprovação das inscrições da visita/evento* |
| **Requisito (ISSUE):** | **PCREQ-5449** |
| **País(es):** | **Brasil** |
| **Tabelas Utilizadas:** | *SEXTAUXILIOVISITA, SEXTTIPOAUXILIO* |
| **Versões/Release:** | *12.1.9* |

## Descrição

O auxílio para visitas técnicas/eventos permite ao usuário gerenciar as solicitações de reembolso realizadas através de solicitações do FLUIG.

Pré-requisitos para utilizar o auxílio para visitas técnicas/eventos

* Ter o FLUIG devidamente instalado e configurado conforme documentação:
  + Instalação: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409653>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409655>
* Ter o TOTVS Developer Studio (TDS) devidamente instalado e configurado.
  + Instalação: <http://tdn.totvs.com/display/fluig/Como+Instalar+-+TOTVS+%7C+Developer+Studio>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=73078179>
* Criar no FLUIG os papéis necessários para a execução do fluxo de auxílio para visitas técnicas/eventos. É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os papéis.
  + Código = **aluno**| Descrição = **Aluno**
  + Código = **reitoria**| Descrição = **Reitoria**
  + Código = **pesquisador**| Descrição = **Pesquisador**
* Associar adequadamente os usuários do FLUIG aos papéis.
* Importar o fluxo de auxílio para visitas técnicas/eventos para a ferramenta TOTVS Developer Studio (TDS). Caso não tenha alterado a instalação padrão dos produtos TOTVS, os arquivos zipados, contendo o(s) fluxo(s), estarão disponíveis em **c:\totvs\CorporeRM\ObjetosGerenciais\Fluig**  
  + Configuração: [http://tdn.totvs.com/download/attachments/172300565/RM\_BT\_Montagem\_Ambiente\_Workflows\_Fluig.pdf](http://tdn.totvs.com/download/attachments/172300565/RM_BT_Montagem_Ambiente_Workflows_Fluig.pdf?version=1&modificationDate=1432910252000&api=v2)
* Exportar para o servidor do FLUIG os datasets, diagrama, formulário e eventos do auxílio para visitas técnicas/eventos.  
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=189313846>

## Procedimento para Utilização

O usuário, vinculado ao papel "Aluno", deverá iniciar uma nova solicitação escolhendo a opção "Educacional | Inovação, Pesquisa e Extensão | Visita Técnica/Evento | Auxílio para Visitas Técnicas/Eventos. Ao selecionar esse fluxo será apresentado um formulário com o código do aluno vinculado ao usuário do FLUIG. Nele deverão ser informados a visita técnica/evento, os dados do reembolso e os tipos de auxílio. Após o preenchimento do formulário o fluxo avançará para a atividade "Aprovar Solicitação de Auxílio", onde um usuário vinculado ao papel "Reitoria" deverá avaliar os dados preenchidos e toda a documentação anexada. Após finalizar a avaliação ele terá 3 opções:

* Retornar para a atividade "Solicitar Auxílio".
* Reprovar a solicitação de auxílio.
* Avançar para a atividade "Analisar Documentação".

Na atividade "Analisar Documentação" o pesquisador, que solicitou a visita técnica/evento, deverá analisar os dados preenchidos e toda a documentação anexada. Após finalizar a avaliação ele terá duas opções:

* Retornar para a atividade "Solicitar Auxílio".
* Finalizar o fluxo de solicitação de auxílio.

Assim que o fluxo for finalizado o pesquisador deverá retornar para o processo "Solicitação de Visitas Técnicas/Eventos" e, na etapa "Executar Visita Técnica/Evento e Elaborar Relatório Final", anexar a documentação enviada pelo aluno.
