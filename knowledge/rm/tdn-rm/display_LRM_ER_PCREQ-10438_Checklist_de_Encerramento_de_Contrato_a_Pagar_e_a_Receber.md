---
content_hash: 0ff5bc4a1993b84f0a3f23b23b83c242c7cd2cbf3106af27fa72c63b3f25584d
fetched_at: '2026-06-29T00:06:30.122670+00:00'
page_id: '235312989'
product: rm
source: tdn-rm
title: ER_PCREQ-10438_Checklist_de_Encerramento_de_Contrato_a_Pagar_e_a_Receber
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-10438_Checklist_de_Encerramento_de_Contrato_a_Pagar_e_a_Receber
version: 131
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Contrato |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_C&P\_TOP011 | **IRM1** | PCREQ-1605 |
| **Requisito1** | PCREQ-10438 | **Subtarefa1** | PDR\_CP\_TOP011-20 |
| **Chamado2** | Não se aplica. | | |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | |  |  | | --- | --- | | **Pré-requisitos para melhor entendimento da especificação** | | | **Entidade** | **Link para o Wikihelp** | | Projetos | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Projetos.aspx> | | Contratos | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Contrato.aspx> | | Histórico do Contrato | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.HistoricosContrato.aspx> | | Encerramento de Contrato | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.EncerramentodeContrato.aspx> | | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Essa melhoria tem por objetivo flexibilizar o encerramento dos contratos (à Pagar e à Receber)  no TOP, deixando a cargo do usuário decidir quais comportamentos serão executados e validados no momento que o contrato está sendo encerrado, ou seja, está sendo concluído ou cancelado.

## Definição da Regra de Negócio

### Introdução

O encerramento de um contrato (Concluído ou Cancelamento) fornece ao usuário a opção de definir o encerramento das “atividades” do mesmo, sendo de fundamental importância ao módulo de contrato.

Atualmente neste encerramento é realizada a validação de “retenções contratuais não liberadas”, permitindo ao usuário apenas decidir se ele bloqueia o encerramento ou alerta o operador da existência da condição das retenções, dando ao operador a opção de executar ou não o procedimento.

O checklist de encerramento de contrato visa flexibilizar essa rotina, fornecendo ao usuário a opção de definir como ele gostaria que fosse o comportamento do sistema ao encerrar um contrato, sendo: Não realizar nenhuma validação (Não confere), decidir no momento do encerramento (Avisa) ou não deixar encerrar o contrato (Barra). Serão validados ao encerrar o contrato as seguintes situações:

* Contrato com Retenção;
* Saldo do Contrato;
* Período Medido e Não liberado;
* Contrato de fornecimento de material com movimentos em aberto;
* Adiantamento;

### Parâmetros de Projeto

O procedimento de encerramento de contrato anteriormente possuía apenas um parâmetro, permitindo ao usuário gerar os comportamentos de avisar (Avisa) ou barrar (Barra) o encerramento do contrato em função da validação das “retenções contratuais não liberadas”.

Para permitir o comportamento esperado do checklist de encerramento, esse parâmetro será alterado, e a ele será incorporada mais uma opção de comportamento a ser selecionado pelo usuário, o de não realizar nenhuma validação (Não confere).

Além da alteração do parâmetro existente serão incluídos mais 4 parâmetros para contratos à Pagar e 4 parâmetros para contratos à Receber para as validações de: Saldo do Contrato, Período Medido e Não liberado, Contrato de fornecimento de material com movimentos em aberto e Adiantamento.

Os parâmetros serão verificados imediatamente antes de salvar o novo status do contrato, seja concluído ou cancelado, e o comportamento do encerramento irá variar conforme a configuração dos parâmetros do checklist de encerramento.

### Regras de Validação

#### Contrato com Retenção

No momento de encerramento de um contrato, seja por conclusão ou cancelamento, caso exista alguma retenção contratual ainda não liberada, será consistido o parâmetro e o comportamento da execução levará em consideração a opção selecionada no parâmetro.

* **"Não confere":** Nada será validado independentemente da existência ou não de retenções o procedimento será executado normalmente;
* **"Avisa":** O sistema irá exibir uma mensagem de alerta comunicando ao usuário a existência de retenções não liberadas para aquele contrato, e solicitará ao mesmo uma ação a ser tomada, parar o procedimento ou continuar sua execução.
* **"Barra":** O procedimento será barrado caso o sistema encontre alguma retenção sem liberação, e o usuário não conseguirá executar o encerramento enquanto não resolver essa pendência.

O comportamento padrão para o parâmetro "Contrato com Retenção" será definido como "Barra".

#### Saldo do Contrato

Ao encerrar um contrato e o mesmo ainda possuir saldo de utilização,o usuário poderá customizar o comportamento do sistema conforme abaixo:

* **"Não confere":** Nada será validado e independentemente da existência ou não de saldo no contrato o procedimento de encerramento será executado normalmente;
* **"Avisa":** O sistema irá exibir uma mensagem de alerta comunicando ao usuário a existência de saldo naquele contrato, e solicitará ao mesmo uma ação a ser tomada, encerrar o procedimento ou continuar sua execução.
* **"Barra":** O procedimento será barrado caso o sistema encontre saldo no contrato, e o usuário não conseguirá executar o encerramento enquanto não resolver essa pendência.

O comportamento padrão para o parâmetro "Saldo do Contrato" será definido como "Não Confere".

#### Período Medido e não Liberado

Quando o contrato for encerrado e existir algum período que esteja medido, mas que não esteja liberado, o usuário poderá customizar o comportamento, conforme os parâmetros abaixo:

* **"Não confere":** Nada será validado e independentemente da existência ou não períodos medidos e não liberados o procedimento será executado normalmente;
* **"Avisa":** O sistema irá exibir uma mensagem de alerta comunicando ao usuário a existência de períodos medidos e não liberados para aquele contrato, e solicitará ao mesmo uma ação a ser tomada, parar o procedimento ou continuar sua execução.
* **"Barra":** O procedimento será barrado caso o sistema encontra alguns períodos medidos e não liberados, e o usuário não conseguirá executar o encerramento enquanto não resolver essa pendência.

O comportamento padrão para o parâmetro "Período Medido e não Liberado" será definido como "Barra".

#### Contrato de Fornecimento de Material com Movimentos em aberto

Quando o usuário tentar encerrar o contrato e houver algum contrato de fornecimento de material com movimento em aberto, o sistema irá consistir o parâmetro, tomando como ação a opção selecionada pelo usuário, conforme listado abaixo:

* **"Não confere":** Nada será validado e independentemente da existência ou não de contrato de fornecimento de material com movimentos em aberto o procedimento será executado normalmente;
* **"Avisa":** O sistema irá exibir uma mensagem de alerta comunicando ao usuário a existência de contrato de fornecimento de material com movimentos em aberto para aquele contrato, e solicitará ao mesmo uma ação a ser tomada, abortar o procedimento ou continuar sua execução.
* **"Barra":** O procedimento será barrado caso o sistema encontra alguns contrato de fornecimento de material com movimentos em aberto, e o usuário não conseguirá executar o encerramento enquanto não resolver essa pendência.

O comportamento padrão para o parâmetro "Contrato de Fornecimento de Material com Movimento em aberto" será definido como "Não Confere".

#### Adiantamento

Se o usuário executar o encerramento de contrato (concluído/cancelado) o sistema irá consistir se existe algum adiantamento não pago (relacionando todos os adiantamentos liberados com os períodos medidos liberados e suas deduções), e caso ele encontre algum irá consistir o parâmetro, e executando a ação selecionada pelo usuário dentre as listadas abaixo:

* **"Não confere":** Nada será validado e independentemente da existência ou não de adiantamento não pago o procedimento será executado normalmente;
* **"Avisa":** O sistema irá exibir uma mensagem de alerta comunicando ao usuário a existência de adiantamento não pago para aquele contrato, e solicitará ao mesmo uma ação a ser tomada, abortar o procedimento ou continuar sua execução.
* **"Barra":** O procedimento será barrado caso o sistema encontra algum adiantamento não pago , e o usuário não conseguirá executar o encerramento enquanto não resolver essa pendência.

O comportamento padrão para o parâmetro "Adiantamento" será definido como "Não Confere".

### Regras de Integridade

#### Introdução

Para possibilitar a existência desse novo comportamento será necessário criar novos parâmetros para definir as ações do sistema diante de alguma condição inválida para as consistências propostas. Esses parâmetros serão responsáveis por liberar ou bloquear a execução do procedimento dependendo do que for definido no parâmetro. Esse parâmetro será do tipo combo de seleção com as opções "Não confere", "Avisa" ou "Barra", permitindo ao usuário customizar as ações de validação do sistema no ato de encerrar (concluir/cancelar) o contrato.

Como existe mais de uma validação poderão haver diferentes tipos de mensagens. Para as mensagens geradas pelo parâmetro marcado como "Barra" o sistema irá empilhar estas mensagens para exibir ao usuário, para as consistências do tipo "Avisa" ele mostraria a tela de confirmação para cada uma das mensagens. Existirá uma hierarquia para essas mensagens, sendo que mensagens geradas por validações cujo o parâmetro esteja definido como "Avisa" terão menor importância e serão exibidas caso não exista nenhuma mensagem de hierarquia maior. Mensagens geradas por validações cujo parâmetro esteja definido como "Barra" terão maior importância, sendo agrupadas e exibidas ignorando mensagens de hierarquia menor (Avisa).

**Exemplo**: As condições de validação estão da seguinte forma antes de encerrar o contrato:

* Contrato com Retenção: Avisa e inválida;
* Saldo do Contrato: Barra e inválida;
* Período Medido e Não liberado: Não confere e valido;
* Contrato de fornecimento de material com movimentos em aberto: Avisa e inválida;
* Adiantamento não pago: Barra e inválida;

Diante das condições acima, o sistema irá exibir as mensagens de validação das consistências "Saldo do Contrato" e "Adiantamento", pois estão definidas como "Barra" e estão inválidas. Caso não estivessem definidas como "Barra" ou não estivessem inválidas seriam mostradas as mensagens de "Contrato com Retenção" e "Contrato de fornecimento de material com movimentos em aberto", dando ao usuário a opção de prosseguir ou não diante cada uma das inconsistências do tipo "Avisa".

#### Não Confere

Se o usuário definir para algum dos parâmetros de validação o comportamento "Não Confere", o sistema deve impreterivelmente não realizar nenhuma validação para aquela consistência. Sendo assim, nenhuma mensagem poderá ser exibida ao usuário alertando de uma condição inválida daquela consistência, mesmo que em alguma condição a consistência pudesse retornar uma condição inválida. Neste ponto qualquer condição para aquela consistência é considerada como "válida".

#### Avisa

Caso o usuário defina para algum dos parâmetros de validação o comportamento "Avisa", o sistema deverá primeiro validar a consistência atrelada a aquele parâmetro. Caso ela esteja válida, o procedimento segue seu fluxo normalmente, caso contrário o sistema deverá alertar ao usuário sobre a condição de invalidade daquela consistência.

Ao ser alertado da condição inválida da consistência, o mesmo deve selecionar se deseja parar o procedimento, ou continuar assim mesmo, ignorando a inconsistência alertada.   
Se alguma condição descrita como "Avisa" estiver inconsistente e o usuário definir que não deseja continuar o procedimento, o mesmo deve ser finalizado independente das demais condições.

#### Barra

Caso o usuário defina para algum dos parâmetros de validação o comportamento "Barra", o sistema deverá impreterivelmente bloquear a continuação do procedimento de encerramento ao encontrar uma condição inválida para a consistência. Sendo assim, o procedimento será interrompido independente das condições das demais validações, exibindo uma mensagem de alerta ao usuário informando da condição adversa encontrada.

### Avaliação da existência de Workflow

Será necessário ao procedimento validar se os workflows presentes no TOP "WF – Contrato" e "WF – Pedido de material" irão influenciar o comportamento do encerramento do contrato. Para casos positivos deverão ser adotadas como "Barra" as consistências influenciadas por eles.

Neste caso os dois workflows presentes irão alterar o comportamento dos parâmetros "Período medido e não liberado" e "Contrato de fornecimento de material com movimento em aberto", que por padrão serão marcados como "Barra", e a menos que os parâmetros referentes aos workflows sejam desmarcados esses parâmetros permacerão como "Barra".

Essa validação foi necessária para que o comportamento dos workflows não fosse alterado, de tal modo que as decisões tomadas a partir deles não tivesse nenhum peso, sendo assim em caso de existência dos mesmos o comportamento será padrão.

## Protótipo de Tela

**Protótipo 01 - Tela de Parâmetros de Projeto**

****Protótipo 02 - Histórico do Contrato (Encerramento)****

********Protótipo 03 - Modelo de mensagem com o parâmetro marcado como "Avisa"********

****************Protótipo 04 - Modelo de mensagem com o parâmetro marcado como "Barra"****************

## Fluxo do Processo

**Diagrama de Casos de Uso**

**Diagrama de Atividades**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
