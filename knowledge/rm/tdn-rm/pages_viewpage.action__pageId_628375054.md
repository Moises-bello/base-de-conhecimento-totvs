---
content_hash: bb108d5a3bda11445026c4aaeb71fcd9fd0582d2ca4cb43a84b263a65ebf45b6
fetched_at: '2026-06-29T00:11:05.209019+00:00'
page_id: '628375054'
product: rm
source: tdn-rm
title: Cópia de DT_VISITA_EVENTO_WF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=628375054
version: 1
---

# Visitas técnicas/participação em eventos

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Educacional* |
| **Módulo:** | ***********Inovação,********** Pesquisa e Extensão* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Visitas Técnicas/Participação em Eventos* | *Visitas Técnicas/Participação em Eventos* | |
| **Cadastros Iniciais:** | *Pesquisador,* *Filial do pesquisador,* *Empresa,* *Tipo de ação,* *Subtipo de ação,* *Tipo de curso*  *Curso e* *Habilitação* |
| **Requisito (ISSUE):** | *PCREQ-5449* |
| **País(es):** | *Brasil* |
| **Tabelas Utilizadas:** | *SEXTVISITAEVENTO, SEXTVISITAAVALIACAO, SEXTPUBLICOVISITA,*  *SEXTINSCRICAOVISITA* |
| **Versões/Release:** | *12.1.15* |

## Descrição

A solicitação de visitas técnicas/participação em eventos permite ao usuário gerenciar todos os tramites necessários para solicitar, aprovar, executar, gerar lançamentos e emitir certificados da visita através de uma solicitação do FLUIG.

Pré-requisitos para utilizar a solicitação de visitas técnicas/participação em eventos

* Ter o FLUIG devidamente instalado e configurado conforme documentação:
  + Instalação: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409653>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=144409655>
* Ter o TOTVS Developer Studio (TDS) devidamente instalado e configurado.
  + Instalação: <http://tdn.totvs.com/display/fluig/Como+Instalar+-+TOTVS+%7C+Developer+Studio>
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=73078179>
* Criar no FLUIG os papéis necessários para a execução do fluxo de solicitação de visitas técnicas/participação em eventos. É importante criar da mesma forma descrita abaixo pois o fluxo utiliza essa definição para referenciar os papéis.
  + Código = **pesquisador**| Descrição = **Pesquisador**
  + Código = **coordenacao**| Descrição = **Coordenação**
  + Código = **setor\_visitas**| Descrição = **Setor de visitas**
  + Código = **financeiro**| Descrição = **Financeiro**
  + Código = **secretaria**| Descrição = **Secretaria**
* Associar adequadamente os usuários do FLUIG aos papéis criados anteriormente.
* Importar o fluxo de solicitação de visitas/eventos para a ferramenta TOTVS Developer Studio (TDS). Caso não tenha alterado a instalação padrão dos produtos TOTVS, os arquivos zipados, contendo o(s) fluxo(s), estarão disponíveis em **c:\totvs\CorporeRM\ObjetosGerenciais\Fluig**  
  + Configuração: [http://tdn.totvs.com/download/attachments/172300565/RM\_BT\_Montagem\_Ambiente\_Workflows\_Fluig.pdf](http://tdn.totvs.com/download/attachments/172300565/RM_BT_Montagem_Ambiente_Workflows_Fluig.pdf?version=1&modificationDate=1432910252000&api=v2)
* Exportar para o servidor do FLUIG os datasets, diagrama, formulário e eventos da solicitação de visitas/eventos.  
  + Configuração: <http://tdn.totvs.com/pages/viewpage.action?pageId=189313846>

## Procedimento para Utilização

O usuário, vinculado ao papel "Pesquisador", deverá iniciar uma nova solicitação escolhendo a opção "Educacional | Inovação, Pesquisa e Extensão | Visita Técnica/Evento | Solicitação de Visitas Técnicas/Eventos. Ao selecionar esse fluxo será apresentado um formulário com o código do pesquisador (coordenador) vinculado ao usuário do FLUIG. Nele deverão ser informados os dados da solicitação e o público alvo da visita. Após o preenchimento do formulário o fluxo avançará para a atividade "Aprovar Solicitação", onde um usuário vinculado ao papel "Coordenação" deverá preencher os dados referentes a aprovação da visita técnica/evento. Após entrar com as informações necessárias ele terá 3 opções:

* Retornar para a atividade "Solicitar Visita Técnica/Participação em Evento"
* Reprovar a solicitação de visita técnica/evento.
* Avançar para a atividade "Reservar Transporte e Confirmar Visita Técnica/Evento".

Na atividade "Reservar Transporte e Confirmar Vista Técnica/Evento" o usuário, vinculado ao papel "Setor de visitas", deverá preencher os dados referentes a aprovação do setor de visitas. Após entrar com as informações necessárias ele terá 3 opções: 

* Retornar para a atividade "Solicitar Visita Técnica/Participação em Evento"
* Reprovar a solicitação de visita técnica/evento.
* Avançar para a atividade "Executar Visita Técnica/Evento e Elaborar Relatório Final".

Na atividade  "Executar Visita Técnica/Evento  e Elaborar Relatório Final" o fluxo deverá ser interrompido por um intervalo de tempo, para que os alunos possam se inscrever no evento (através do fluxo de inscrição) e para que o pesquisador possa aprovar as inscrições (através do fluxo de aprovação). Ao término desse período a visita técnica/evento deverá ser executada e o relatório final elaborado pelo pesquisador que solicitou a visita. Nesse relatório deverão estar presentes todos os participantes da visita e, se necessário, o valor que cada um deles deverá pagar ou receber. Se houver necessidade de reembolsar algum participante o responsável pela confecção do relatório final deverá anexar todos os comprovantes de pagamento enviados por eles (através do fluxo de auxílio para visitas técnicas/eventos). Ao término da confecção do relatório final o usuário deverá enviar o fluxo para a atividade "Aprovar Relatório Final". Nessa etapa o usuário, vinculado ao papel "Setor de visitas", deverá avaliar o relatório final e toda a documentação anexada. Ao fim dessa verificação os certificados serão gerados e o usuário terá as seguintes opções:

* Retornar para a atividade "Executar Visita Técnica/Evento  e Elaborar Relatório Final"
* Finalizar o fluxo de visita técnica/evento.
* Avançar para a atividade "Emitir Certificados".
* Avançar para a atividade "Gerar Lançamentos".

Na atividade "Gerar Lançamentos" serão gerados lançamentos a pagar ou a receber. Se o participante precisar pagar pela visita técnica/evento será gerado um lançamento a receber (a instituição recebe), porém se o participante for reembolsado será gerado um lançamento a pagar (a instituição paga). Durante a geração dos lançamentos poderão surgir mensagens de aviso, que deverão ser avaliadas por um usuário com o papel "Financeiro". Ao avançar para a atividade "Emitir Certificados" um usuário, com o papel de "Secretaria" deverá emitir os certificados gerados e, em seguida, avançar para a atividade "Validar Certificados". Nessa etapa o usuário, vinculado ao papel "Coordenação", deverá avaliar os certificados gerados. Ao final dessa verificação ele terá duas opções:

* Retornar para a atividade "Emitir Certificados".
* Finalizar o fluxo.

Durante a execução do fluxo são gerados registros de aprovação. Esse histórico é gravado na tabela SEXTVISITAAVALIACAO e contém informações sobre o usuário aprovador, etapa movimentada, data da movimentação, justificativa, dentre outras.

Cancelamento do processo no Fluig

Caso o processo no Fluig seja cancelado, a visita técnica receberá o status de "**Cancelada**", mas não será excluída da base de dados do TOTVS Educacional. Vale ressaltar que a solicitação não poderá ser cancelada nas etapas Gerar Lançamentos, Emitir Certificados e Validar Certificados, pois haverão lançamentos financeiros e/ou certificados gerados.
