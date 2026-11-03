---
content_hash: 8db7524602abb4b110c036231fa7d8f9a8c8a41946ea8c3f3b3d5280aff37591
fetched_at: '2026-06-29T00:08:34.964541+00:00'
page_id: '274855824'
product: rm
source: tdn-rm
title: CONTROLADORIA01-228 DT Envio Email Cadastro Permissão Tarefa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274855824
version: 104
---

# Parametrizar envio de e-mail para os responsáveis existentes no cadastro de permissão de tarefa

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Cadastro permissão tarefa |
| **Situação/Requisito:** | No cadastro de permissão de tarefa deve ser possível parametrizar quais responsáveis irão receber e-mail após solicitar, executar ou cancelar a tarefa. |
| **Solução/Implementação:** | Para parametrizar o envio de e-mail para os responsáveis, existentes no cadastro de permissão de tarefas, foi necessário criar o campo ENVIAEMAIL na tabela CPERMISSAOTAREFA.  Ele foi adicionado na tela de cadastro de permissões de tarefa e é verificado durante a solicitação, execução ou cancelamento da tarefa. Após a realização de alguma destas atividades o e-mail será enviado apenas para os usuário em que o campo "Enviar Email" foi marcado. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados**: | N/A |
| **Requisito (informe o requisito relacionado):** | N/A |

divs
