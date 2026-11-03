---
article_id: 360028340252
category: Configurador
content_hash: 5c3928121e90db1b8a66bd70d6b4aa42f718fadf443c6a2175ebce7799ddbd1d
fetched_at: '2026-06-28T22:42:19.267283+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: 'Framework - Linha Protheus  - Schedule: agendando a execução de rotinas'
type: support-article
updated_at: '2024-05-08T11:58:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028340252-Framework-Linha-Protheus-Schedule-agendando-a-execu%C3%A7%C3%A3o-de-rotinas
---

**Dúvida**Como faço para executar rotinas de forma automatizada no Protheus?  
  
 **Ambiente**Protheus - Configurador - A partir da Versão 11  
   
**Solução**O **Schedule Protheus** permite que rotinas do sistema sejam agendadas para que possam ser executadas posteriormente, em um período determinado pelo usuário. É possível definir quando (dias, horários e quantidades de execuções) e em qual Grupo de Empresas e Filiais o processo será executado. O Schedule Protheus não realiza nenhum processamento. Sua função é chamar a rotina agendada no momento definido ou manter esta rotina sendo executada constantemente, quando o agendamento é configurado como **sempre ativo**. Consumo de memória, desempenho e processamento são atributos associados a rotina agenda, e não ao Schedule Protheus em si.  
O **Schedule Protheus** é composto por três componentes principais:  
  
**Manager:** Componente responsável por fazer o gerenciamento das tarefas, como o controle de geração das tarefas (*Task Manager*) e o controle da fila das tarefas que serão executadas (*Queue Manager*);  
**Agent:** Este é o componente que gerencia as execuções e distribui as tarefas para que as Executes configuradas que estão disponíveis no momento. Os Agents podem estar localizados em servidores diferentes, possibilitando o balanceamento da carga de execuções;  
**Execute:** São os componentes responsáveis por realizar a chamada das rotinas agendadas. A única das entidades que consome licença no Schedule Protheus, e isto ocorre na execução da rotina agendada.  
  
Para uma visão mais detalhada do funcionamento do Schedule Protheus, consulte a documentação completa no link abaixo:  
<http://tdn.totvs.com/pages/releaseview.action?pageId=271167961>
