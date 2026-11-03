---
content_hash: c6c7d1229a2c686f4241eab0c95e9af6d9e20dc38ebb0f4363e226c51468ac1d
fetched_at: '2026-06-29T00:05:55.719812+00:00'
page_id: '146179280'
product: rm
source: tdn-rm
title: Agendar Relatório .Net e desabilitar processo agendado com recorrência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=146179280
version: 4
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                     **Versão:**11.XX |
| **Processo** | **:** | Gerenciamento de Jobs |
| **Subprocesso** | **:** | Agendar Relatório .Net e desabilitar processo agendado com recorrência |
| **Data da publicação** | **:** | 12/06/2014 |

**Introdução**   
   
 Quando um relatório é agendado, ele se torna um processo e deve ser gerenciado como um Job.   
   
 **Agendar relatório:**

Para realizar o agendamento de um relatório, faz-se necessário utilizar um ambiente que esteja trabalhando em 3 camadas.   
 Acesse o RM Reports, selecione o relatório desejado, clique em Processos -> Gerar relatório:

Informe os filtros / parâmetros do relatório caso haja, e na janela "Agendamento do Processo", configure-o conforme desejado.

Neste exemplo, o relatório foi agendado para executar no dia 08/06/2014 às 17:30 horas, com recorrência para todas as semanas, no mesmo horário, de segunda à quarta-feira:   
   
    
   
 Finalize o agendamento.

Na tela de Gerenciamento de Jobs, após atualização, será exibido o processo agendado, com status vazio:

No horário configurado, o processo será executado, logo o status do mesmo será alterado para "OK" e será adicionado mais um registro na fila de processos com status em branco. Esse será o próximo registro da recorrência a ser executado conforme configurado anteriormente:

**Desativar Job com recorrência:**

Para desativar um Job agendado, crie um filtro no Gerenciamento de Jobs (Ambiente – Gerenciamento de Jobs), identificando o processo (Crie um novo filtro, por exemplo "Processos criados hoje"), localize o processo que ainda não foi executado (ou seja, status igual a vazio) e selecione a opção "Desabilitar Job" em Ações de Job na barra de Menus de Jobs, conforme imagens abaixo:

  Crie um filtro para identificar o Job que deseja desabilitar:

Localize o processo agendado e que ainda não foi executado, coluna "Finalizado" em branco:

Selecione o processo e clique em "Desabilitar Job", esse ícone será habilitado apenas para Jobs que ainda não foram executados:

Atualize (F5) a tela de Gerenciamento de Jobs, o Status do Job mudará para "Desabilitado pelo usuário":

|  |  |
| --- | --- |
|  | **Para maiores informações:**  Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)    **COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****    **Canais de Atendimento:**  **Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha). |
