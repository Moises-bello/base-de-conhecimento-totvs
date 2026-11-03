---
content_hash: b026acf6bcdf25c2e80150cba513e1a785d5814b5c3a33f8f321c40d79da9883
fetched_at: '2026-06-29T00:08:28.091200+00:00'
page_id: '271658360'
product: rm
source: tdn-rm
title: MCP-1740 ER Valida a Alteração da Quantidade e/ou dos Recursos da Tarefa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271658360
version: 125
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Orçamento |
| **Segmento Executor** | Construção & Projetos | | |
| **País** | (X) Brasil  (X) Argentina  (X) México  (X) Chile  (X) Paraguai  (X) Equador (X) Colômbia | | |

## 

## Objetivo

Garantir a integridade da Planilha de Atividades, não permitindo que alterações na quantidade da tarefa ou em seus recursos sejam efetuadas, caso resultem em uma quantidade inferior à dos insumos que já foram pedidos para a tarefa.

## Definição da Regra de Negócio

Para se garantir a integridade da Planilha de Atividades, no momento da alteração da quantidade de uma tarefa para uma quantidade inferior, ou da alteração dos recursos (composições / insumos) da tarefa, o sistema irá:

* Verificar as composições e insumos associados à tarefa;
* Calcular a quantidade já pedida dos insumos associados às composições da tarefa ou à própria tarefa;
* Validar se todos os insumos pedidos para a tarefa fazem parte dos recursos (composições / insumos) da tarefa;
* Validar se a quantidade informada para a tarefa é maior ou igual à quantidade solicitada dos seus insumos através da rotina de Pedido de Material;
* Permitir ou não a alteração da quantidade da tarefa ou dos recursos da tarefa, conforme resultado da validação acima.

Para o cálculo das quantidades pedidas serão consideradas apenas Requisições de Compra que já foram enviadas para Suprimentos/Faturamento, ou seja, apenas aquelas que já geraram movimento no backoffice (TOTVS Gestão de Estoque, Compras e Faturamento ou Microsiga Protheus) e cujo Status de Geração consequentemente é "Em processo em Suprimentos/Faturamento".

Assim, caso a quantidade informada pelo usuário para a tarefa seja superior à quantidade já pedida dos insumos dessa tarefa, o sistema permitirá a alteração, da mesma forma a alteração dos recursos (composições / insumos) da tarefa também será checada e permitida somente caso atendam à  quantidade já pedida dos insumos desta tarefa.

Por outro lado, caso a quantidade informada pelo usuário para a tarefa seja inferior à quantidade já pedida dos insumos dessa tarefa, ou caso a alteração dos recursos da tarefa não atenda à quantidade já pedida dos insumos para a tarefa, o  sistema não permitirá a alteração, exibindo mensagem de erro com o seguinte conteúdo:

"A tarefa 'XXXXXXXX' possui inconformidades: Insumo XXX já possui YYY de quantidade pedida."

As validações aqui citadas também serão efetuadas no processo de ***"Atualização Múltipla de Registros"*** que se encontra em ***"Orçamento | Planilha | Planilha de Atividades | Processos | Atualização Múltipla"***.

Não serão validados nessa rotina:

* Requisições de Cotação: Já que são geradas apenas para Cotação de Preços não atualizando a quantidade pedida;

* Requisições de Compra que ainda não foram enviadas para Suprimentos/Faturamento (Status de Geração: "Aguardando envio para Suprimentos/Faturamento"): No momento do seu envio para Suprimentos/Faturamento essas requisições irão checar a quantidade das tarefas e o pedido somente será enviado caso suas quantidades não sejam superiores à quantidade disponível conforme a Planilha de Atividades;

* Pedidos de Material Extra: Não há que se falar em consistência neste caso, visto que esses pedidos já são gerados justamente por extrapolarem a quantidade disponível conforme a Planilha de Atividades.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Planilha de Atividades | Alteração | Orçamento | Planilha | Planilha de Atividades | Conforme descrito neste documento |
| Atualização Múltipla | Alteração | Orçamento | Planilha | Planilha de Atividades | Processos | Atualização Múltipla | Conforme descrito neste documento |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
