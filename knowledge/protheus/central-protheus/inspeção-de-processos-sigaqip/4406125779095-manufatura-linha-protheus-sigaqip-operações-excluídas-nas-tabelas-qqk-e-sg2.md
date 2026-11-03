---
article_id: 4406125779095
category: Inspeção de Processos (SIGAQIP)
content_hash: b491ab2a3ef3bf74b29dfc973e749dd3ad94ecbfc296dce66847f493d9b1ba21
fetched_at: '2026-06-28T22:42:25.884146+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Operações excluídas nas tabelas QQK
  e SG2
type: support-article
updated_at: '2021-10-01T13:09:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406125779095-Manufatura-Linha-Protheus-SIGAQIP-Opera%C3%A7%C3%B5es-exclu%C3%ADdas-nas-tabelas-QQK-e-SG2
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:40 min** **Dúvida**Por quê ao excluir uma operação vinculada à um produto na rotina **QIPA010 - Cadastros de Especificações de Produtos** também está sendo excluída a operação no **MATA632 - Roteiro de Operações**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Solução**Na rotina **QIPA010** quando o parâmetro **MV\_QPDELG2 - Determina se as operações excluídas na rotina de especificação do produto Tabela QQK serão excluídas também na tabela SG2 - Operações utilizado no ambiente PCP** possui o conteúdo igual a **T - True**, a exclusão ocorrerá em ambos módulos **SIGAQIP - Inspeção de Processos** e **PCP - Planejamento e Controle da Produção** , ou seja, nas tabelas **QQK - Especificações de Operações** e **SG2 - Operações**.  
Caso o conteúdo do parâmetro **MV\_QPDELG2** esteja igual a **F - False**, a exclusão ocorrerá apenas na rotina **QIPA010**.
