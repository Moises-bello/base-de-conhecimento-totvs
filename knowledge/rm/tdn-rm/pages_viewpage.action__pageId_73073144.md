---
content_hash: 7d8b2e1151ab65958883c39c0cb05f702d5014cd7489c12c8cb0030ade606397
fetched_at: '2026-06-29T00:11:28.239177+00:00'
page_id: '73073144'
product: rm
source: tdn-rm
title: RMPAT00001_Cancelamento de Contabilizações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=73073144
version: 5
---

|  |  |  |
| --- | --- | --- |
| **Produto** | : | Totvs Gestão Patrimonial – **Versão:** 11.5x |
| **Processo** | : | Cancelamento de Contabilizações |
| **Subprocesso** | : | Contabilizações |
| **Data da publicação** | : | 24/07/2013 |

**Introdução**

Este processo permite que as contabilizações, integradas ou não ou sistema contábil, sejam excluídas de forma que o processo de [Contabilização de Depreciação/Correção Monetária](http://wikihelp.totvs.com.br/WikiHelp/PAT/PAT.ContabilizaDepreciacoCorrecao.aspx) seja executado novamente.   
 Deve-se selecionar qual o tipo de contabilização será excluída: Correção, Depreciação ou as duas ao mesmo tempo.

Os lançamentos contábeis já enviados para o sistema contábil, que ainda estão na Manutenção de Lotes definido no processo de integração contábil serão excluídos automaticamente.Caso os lançamentos já tenham sido integrados ao lote oficial da contabilidade serão gerados lançamentos de estorno que, posteriormente, devem ser integrados ao lote oficial.

**Procedimento (Procedimentos para cancelamento)**

**Disponível em:** Utilitários > Lançamentos contábeis > Exclusão da Contabilização.  
 Informe o Cenário e marque as exclusões.

Se a Contabilização estiver na Manutenção de Lançamentos do TOTVS Gestão Contábil, marque para "Excluir Via Tarefa".

   
 Informe o motivo da Solicitação da Exclusão.

   
 Após o termino clique no botão "Bloco de Notas" para verificar a mensagem completa apresentada na execução do processo.   
   
   
   
    
 **Execução da tarefa**   
 Conforme informa acima ao marcar o processo de **(exclusão via tarefa)** e necessária executar a tarefa no RM SALDUS ( **Gestão contábil** ) para concluir a exclusão da contabilidade.   
 **Disponível em:** Menu > utilitários > tarefas > gerenciador

Seleciona a tarefa em questão > Processo > executar tarefa

Em seguida verifique o log apresentado:
