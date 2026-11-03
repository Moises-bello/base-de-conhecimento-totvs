---
content_hash: 5363358e138346e5ece3f177ebf26cfbee6182f43e55ca187befaffa8ac0879a
fetched_at: '2026-06-29T00:08:27.202492+00:00'
page_id: '271399790'
product: rm
source: tdn-rm
title: ER_FRW_FRW002-241_ThreadExclusivaControlador
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_FRW_FRW002-241_ThreadExclusivaControlador
version: 105
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | Job Server |
| **Segmento Executor** | Framework | | |
| **Projeto1** | Framework BH - 004 | **IRM/EPIC1** |  |
| **Requisito/Story/Issue1** | FRW\_FRW002-241 | **Subtarefa1** | FRW\_FRW002-243 |
| **Chamado2** |  | | |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 

Revisar o processo de organizar a Fila de Jobs inerente ao Controlador.

O Job Server que responde por ser também o Controlador está tendo uma grande perda de performance para processar os Jobs pois a tarefa de controlar e distribuir os Jobs para criar a Fila de Jobs está sendo executada na mesma Thread que a rotina que processa os Jobs.

Será criada uma Thread própria para que a rotina do Controlador seja executada em paralelo à rotina de processamento de jobs.

## Definição da Regra de Negócio

# Passo a passo da solução

* O método ProcessJobQueue() da classe RMSJobExecutor foi alterado para ser async e retornar como Task. A chamada ao método estático Yield() da classe Task foi adicionada como a primeira instrução a ser executada dentro do método para que as demais instruções sejam executadas em paralelo à Thread que chamou o método ProcessJobQueue() originalmente

await Task.Yield();

* No método ProcessQueue() da classe RMSJobExecutor foi alterado no momento em que é feita a verificação se o Job Server é o Controlador. Se ele for o controlador, a chamada para o método ProcessJobQueue() é feita através de uma action de forma anônima:

// separa a função do controlador em outra Thread para não atrasar na execução dos jobs  
Task.Run(action: async () =>  
{  
  await ProcessJobQueue(dbs);  
});

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
