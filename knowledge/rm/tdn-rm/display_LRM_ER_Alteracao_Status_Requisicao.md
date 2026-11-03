---
content_hash: d2728a755751d4e8e9c96c7d3b60f60a285f7c29624e3da21f50ebf2226344c1
fetched_at: '2026-06-29T00:06:04.130229+00:00'
page_id: '200905780'
product: rm
source: tdn-rm
title: ER_Alteracao_Status_Requisicao
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Alteracao_Status_Requisicao
version: 7
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Pessoas | **Módulo** | RHU |
| **Segmento Executor** |  | | |
| **Projeto1** | RHU – DESENVOLVIMENTO RHU007 | **IRM1** | PCREQ-6304 |
| **Requisito1** | PCREQ-6308 | **Subtarefa1** | PDR\_RHU\_RHU007-16 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** |  | **Réplica** |  |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Permitir que as requisições tenham seu status alterado para "Em Andamento" quando o Status da requisição for "Aprovada", "Reprovada" ou "Cancelada".

## Definição da Regra de Negócio

Será criado um processo com nome de "Alterar Status para 'Em Andamento'" que irá alterar o status de uma requisição para "Em andamento". Este processo só irá mudar o status de requisições Aprovadas, Reprovadas ou Canceladas. Este processo deverá reabrir o atendimento no Agilis e o atendente deve ser o ultimo atendente antes da execução do processo. O processo também irá incluir um parecer com informações sobre a mudança de status da requisição, informando que a mesma teve seu status alterado para em andamento. O novo processo também deve exibir uma mensagem de confirmação para usuário alertando sob a execução da operação, após o usuário confirmar, o processo será executado diretamente. 

Deverá ser realizada a validação se não existe nenhuma outra requisição em andamento, pendente ou suspensa para um mesmo beneficiário, caso exista o sistema tem que retornar uma mensagem para o usuário informando que já existe uma requisição e o seu status. Esta validação aplica-se as requisições de Desligamento, Transferência, Transferência com Promoção e Transferência em Lote.

Obs.: Esse processo deve estar disponível para todos os tipos de requisições.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Processo Alterar Status para 'Em Andamento' | [Criação] | Requisições > Processos > Alterar Status para 'Em Andamento' | - |
|  |  |  | - |
|  |  |  | - |

## Protótipo de Tela

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Pessoas | **Módulo** | RHU |
| **Segmento Executor** |  | | |
| **Projeto1** | RHU – DESENVOLVIMENTO RHU007 | **IRM1** | PCREQ-6304 |
| **Requisito1** | PCREQ-6308 | **Subtarefa1** | PDR\_RHU\_RHU007-16 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** |  | **Réplica** |  |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Permitir que as requisições tenham seu status alterado para "Em Andamento" quando o Status da requisição for "Aprovada", "Reprovada" ou "Cancelada".

## Definição da Regra de Negócio

Será criado um processo com nome de "Alterar Status para 'Em Andamento'" que irá alterar o status de uma requisição para "Em andamento". Este processo só irá mudar o status de requisições Aprovadas, Reprovadas ou Canceladas. Este processo deverá reabrir o atendimento no Agilis e o atendente deve ser o ultimo atendente antes da execução do processo. O processo também irá incluir um parecer com informações sobre a mudança de status da requisição, informando que a mesma teve seu status alterado para em andamento. O novo processo também deve exibir uma mensagem de confirmação para usuário alertando sob a execução da operação, após o usuário confirmar, o processo será executado diretamente. 

Deverá ser realizada a validação se não existe nenhuma outra requisição em andamento, pendente ou suspensa para um mesmo beneficiário, caso exista o sistema tem que retornar informando que já existe uma requisição e o seu status.  
Esta validação aplica-se as requisições de: Desligamento, Promoção, Transferência, Transferência com Promoção e Transferência em Lote.

 

Obs.: Esse processo deve estar disponível para todos os tipos de requisições.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Processo Alterar Status para 'Em Andamento' | [Criação] | Requisições > Processos > Alterar Status para 'Em Andamento' | - |
|  |  |  | - |
|  |  |  | - |

## Protótipo de Tela

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
