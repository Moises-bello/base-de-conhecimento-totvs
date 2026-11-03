---
content_hash: 28072c71c5da38d160a8bfb99233dec69075adeb05c38bdaa6629beaa5e1c848
fetched_at: '2026-06-29T00:06:17.586946+00:00'
page_id: '213980154'
product: rm
source: tdn-rm
title: DT_ACOMPANHAMENTO_BOLSISTA_DESISTENCIA
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_ACOMPANHAMENTO_BOLSISTA_DESISTENCIA
version: 76
---

# ACOMPANHAMENTO DE BOLSISTA (DESISTÊNCIA)

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | ***TOTVS Educacional*** |
| **Módulo:** | *****Pesquisa, Extensão e Inovação***** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Acompanhamento de Bolsista (Desistência)** | ***Acompanhamento de Bolsista (Desistência)*** | |
| **Cadastros Iniciais:** | *Cadastro de Projetos* |
| **Requisito (ISSUE):** | *PCREQ-5448* |
| **País(es):** | *Brasil* |
| **Tabelas Utilizadas:** | *SPROJDESISTENCIABOLSISTA* |
| **Versões/Release:** | *1.12.9* |

## Descrição

Possibilita ao usuário gerenciar seus processos referentes ao acompanhamento de desistência do bolsista, permitindo realizar o cadastro, submeter a análise e avaliação utilizando-se do processo de aprovação através de FLUIG.

Pré-requisitos para utilizar a funcionalidade de acompanhamento de bolsista (desistência)

* Ter o FLUIG devidamente instalado e configurado conforme documentação:
  + Instalação: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409653>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409655>
* Ter o TOTVS Developer Studio (TDS) devidamente instalado e configurado.
  + Instalação: <http://tdn.totvs.com/display/fluig/Como+Instalar+-+TOTVS+%7C+Developer+Studio>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=73078179>
* Criar no FLUIG os papéis necessários para a execução do fluxo de acompanhamento de bolsista (desistência). É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os papéis).
  + Código = **pesquisador**| Descrição = **Pesquisador**
* Associar adequadamente os usuários do FLUIG aos papéis criados anteriormente.
* Importar o fluxo de "acompanhamento bolsista (desistência)" para a ferramenta TOTVS Developer Studio (TDS). Caso não tenha alterado a instalação padrão dos produtos TOTVS, os arquivos zipados, contendo o(s) fluxo(s), estarão disponíveis em **c:\totvs\CorporeRM\ObjetosGerenciais\Fluig**  
  + Configuração: [http://tdn.totvs.com/download/attachments/172300565/RM\_BT\_Montagem\_Ambiente\_Workflows\_Fluig.pdf](http://tdn.totvs.com/download/attachments/172300565/RM_BT_Montagem_Ambiente_Workflows_Fluig.pdf?version=1&modificationDate=1432910252000&api=v2)
* Exportar para o servidor do FLUIG os datasets, diagrama, formulário e eventos do fluxo "acompanhamento bolsista (desistência)".  
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=189313846>

## Procedimento para Utilização

O usuário deve iniciar uma nova solicitação escolhendo a opção "Educacional | Inovação, Pesquisa e Extensão | Acompanhamento Bolsista (Desistência) | Acompanhamento Bolsista (Desistência)". É necessário estar vinculado ao papel de "Pesquisador" para realizar essa solicitação.

Após preencher as informações necessárias ao acompanhamento do bolsista o usuário enviará a solicitação para "Confirmar Desistência/Desligamento", onde o coordenador do projeto vai verificar as informações preenchidas. O coordenador do projeto será identificado automaticamente e o fluxo será encaminhado para ele ao avançar a etapa.

 Após validar as informações preenchidas pelo bolsista, o coordenador do projeto terá duas opções:

* Avançar etapa para "Desistência/Desligamento Confirmado".  
  Os dados serão gravados na base RM (SPROJDESISTENCIABOLSISTA) aprovando a desistência do bolsista (DESISTENCIAAPROV = S). O fluxo será concluído como "Desistência/Desligamento Confirmado".
* Avançar etapa para "Desistência/Desligamento Não Aceito".  
  Os dados serão gravados na base RM (SPROJDESISTENCIABOLSISTA) negando a desistência do bolsista (DESISTENCIAAPROV = N). Será obrigatório informar um parecer e o fluxo será concluído como "Desistência/Desligamento Não Aceito".

Caso o bolsista tenha algum valor a receber, o mesmo deverá executar o fluxo de "Acompanhamento de bolsista (Frequência)" antes de solicitar sua desistência.

divs
