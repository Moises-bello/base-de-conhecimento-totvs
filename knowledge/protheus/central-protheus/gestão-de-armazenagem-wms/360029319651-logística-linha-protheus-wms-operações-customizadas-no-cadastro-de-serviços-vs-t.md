---
article_id: 360029319651
category: Gestão de Armazenagem (WMS)
content_hash: 1e91efff6b267e1174226118e6547c9af4efdce4afd8fa1067a0acb6730ea57e
fetched_at: '2026-06-28T22:45:48.065384+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Logística - Linha Protheus - WMS - Operações customizadas no cadastro de Serviços
  Vs Tarefas
type: support-article
updated_at: '2025-10-31T20:02:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029319651-Log%C3%ADstica-Linha-Protheus-WMS-Opera%C3%A7%C3%B5es-customizadas-no-cadastro-de-Servi%C3%A7os-Vs-Tarefas
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35447078452375)***Tempo aproximado para leitura:**00:02:06 min****Dúvida**Como funcionam e como configurar as operações customizadas no cadastro de Serviços Vs Tarefas?  
  
**Ambiente**Microsiga Protheus – Gestão de Armazenagem – A partir da versão 12  
  
**Solução**O cadastro **Serviços Vs Tarefas - WMSA070** permite a configuração de serviços que serão informados obrigatoriamente em todos os documentos que geram integração com o **WMS** - **Warehouse Management System**.  
  
Por padrão, estes serviços são a base para a geração dos registros que possibilitam a movimentação de estoque dos produtos e execução de processos complementares dentro do armazém como: conferência, montagem de volumes, distribuição de produtos, entre outros.  
  
Todo serviço possui ao menos uma tarefa que, por sua vez, deve estar vinculada diretamente a uma operação. As operações que estão disponíveis atualmente são:  
  
0 - Customizada  
1 - Endereçamento  
2 - Endereçamento Crossdocking  
3 - Separação  
4 - Separação Crossdocking  
5 - Reabastecimento  
6 - Conferência Entrada  
7 - Conferência Saída  
8 - Transferência  
  
As operações de 1 a 8 são funcionalidades padrões do Sistema, que englobam diversas regras de negócio e boas práticas de mercado para a geração automática dos movimentos de distribuição, no momento da execução de um serviço **WMS**. Estes movimentos podem ou não ser executados posteriormente por meio de coletores de dados de rádio frequência.  
  
Devido à necessidade de executar regras ou rotinas específicas, que não existem ou não são contempladas pelo produto padrão, o **WMS** também disponibiliza a operação 0 - Customizada, que é executada como qualquer outra, ou seja, no mesmo momento e da mesma forma que as demais operações. A diferença é que todas as regras de negócio e geração dos movimentos permanece sob responsabilidade do desenvolvedor da rotina específica, pois o sistema apenas realiza a chamada da função customizada.  
  
**Saiba Mais**  
Mais detalhes podem ser encontrados no documento: [Funcionamento e Configuração de Operações Customizadas no Cadastro de Serviços x Tarefas](http://tdn.totvs.com/pages/viewpage.action?pageId=421381071)  
Também assista ao *Webinar* sobre o cadastro **Serviços** **Vs** **Tarefas** e conheça todas as configurações disponíveis: [Webinar TOTVS | Serviços](https://www.youtube.com/watch?v=f1K8WBRCUUc) [Vs Tarefas #TOTVS\_Logística\_Linha\_Protheus](https://www.youtube.com/watch?v=f1K8WBRCUUc)
