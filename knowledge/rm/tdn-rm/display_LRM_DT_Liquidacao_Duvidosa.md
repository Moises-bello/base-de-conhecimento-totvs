---
content_hash: 690fa83d7c86f40c9db76aa09d4b34687caa9817364773edd853f81cd3083b95
fetched_at: '2026-06-29T00:08:25.484671+00:00'
page_id: '270916064'
product: rm
source: tdn-rm
title: DT_Liquidacao_Duvidosa
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Liquidacao_Duvidosa
version: 8
---

# PROCESSO DE LIQUIDAÇÃO DUVIDOSA

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | **RM** | | |
| **Segmento Executor:** | **Educacional** | | |
| **Módulo:** | **TOTVS Gestão Financeira** | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Liquidação Duvidosa* | *Liquidação Duvidosa.* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Baixa*.* | *Baixa de lançamentos financeiros.* | |  |  | | | |
| **Requisito (ISSUE):** | *EDUCTB002-342.* | | |
| **País:** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros:** |  | | |

### Objetivo

A funcionalidade permite a contabilização das provisões para crédito de liquidação duvidosa, de acordo com as regras definidas pelo próprio cliente, para lançamentos vencidos e que ainda não foram recebidos.

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Cadastro de Tipo de Documento | Alteração | Cadastros -> Específicos | - |
| Cadastro de Tabelas Opcionais | Alteração | Cadastros -> Específicos -> Tabelas Opcionais | - |
| Lançamento Financeiro | Alteração | Contas a Pagar/Receber -> Operações Financeiras -> Lançamentos | - |
| Incluir Liquidação Duvidosa | Criação | Contas a Pagar/Receber -> Operações Financeiras -> Lançamentos -> Processos | - |
| Cancelar Liquidação Duvidosa | Criação | Contas a Pagar/Receber -> Operações Financeiras -> Lançamentos -> Processos | - |
| Liquidação Duvidosa | Criação | Contas a Pagar/Receber -> Operações Financeiras -> Lançamentos -> Anexos | - |
| Solicitar a exclusão de Operação Contábil | Criação | Contas a Pagar/Receber -> Operações Financeiras -> Lançamentos -> Anexos -> Liquidação Duvidosa | - |
| Liberação de Período | Alteração | Utilitários -> Liberação de Período | - |
| Parametrizados do Financeiro | Alteração | Ambiente -> Parâmetros -> Totvs Gestão Financeira | - |

- Cadastro de Tipo de Documento e Cadastro de Tabelas Opcionais: criados campos para informar os eventos que serão utilizados pelo processo para realizar a contabilização da liquidação duvidosa.

* Evento Contábil para Liquidação Duvidosa: do tipo de processo "Lançamento".
* Evento Contábil para Baixa em lançamento com liquidação duvidosa: do tipo de processo "Baixa".
* Evento Contábil para Baixa por acordo em lançamento com liquidação duvidosa: do tipo de processo "Baixa com Acordo".

- Lançamento Financeiro: criado o campo Status de Liquidação Duvidosa, com as opções "Liquidação não Duvidosa", "Liquidação Duvidosa" e "Liquidação Duvidosa Parcial", sendo a primeira o valor default. O campo também passa a ser preenchido no histórico de alteração de lançamentos.

Se o lançamento estiver com o status de liquidação duvidosa ou liquidação duvidosa parcial, alguns processos não poderão ser executados. Será necessário cancelar a liquidação duvidosa antes. Os processos são os seguintes:

* Cancelamento do lançamento
* Alterações no lançamento (valores, data de vencimento, tipo contábil)
* Parcelamento do lançamento
* Cancelamento da baixa processadas antes do processo de liquidação duvidosa. Nesse caso, a verificação será feita pela data da baixa, que deve ser posterior à data da liquidação.

- Incluir Liquidação Duvidosa: criado processo de liquidação duvidosa chamado da visão de lançamentos, disponível quando a integração Totvs Educacional x Backoffice Protheus (Financeiro) não está ativa, para todos os registros selecionados pelo usuário. Na interface do processo de Inclusão de liquidação, o usuário deverá preencher a "Data da liquidação duvidosa para a contabilização". No seu processamento receberá os seguintes parâmetros: Lista de lançamentos e Data da contabilização.

As seguintes validações devem ser realizadas para que o processo seja executado:

* Os lançamentos devem estar em aberto ou parcialmente baixados;
* Os lançamentos não podem ter liquidação duvidosa ativa (Status "Não Duvidosa");
* Os lançamentos devem estar vencidos;
* Os lançamentos devem ser a receber;
* Os lançamentos devem ser do tipo contábil ou baixa contábil;
* Para os lançamentos baixados parcialmente, a data da baixa deve ser anterior à data da liquidação duvidosa;
* A data da liquidação duvidosa não pode ser futura, ou seja, deverá ser igual ou anterior à data do sistema.

O processo deve executar as seguintes ações:

* Para os lançamentos válidos alterar o Status de Liquidação não Duvidosa para "Liquidação Duvidosa" caso o lançamento esteja em aberto, e para "Liquidação Duvidosa Parcial" caso esteja parcialmente baixado.
* Deve ser realizada a contabilização desses lançamentos, utilizando o evento contábil informado na tabela default para evento. O Id. da operação e a data da liquidação serão registrados em uma tabela própria para a Liquidação Duvidosa. O número contábil usado será sempre o número do documento.
* Criado histórico de alteração do lançamento.

- Anexo de Liquidação Duvidosa: criado um anexo na visão de lançamentos que irá exibir todas as liquidações existentes. Os dados de um registro específico poderão ser visualizados numa tela, além da contabilização (acessada via botão). Não será possível incluir ou excluir registros, e a alteração permitida somente para a contabilização, que pode ser regerada executando um outro evento contábil ou informada manualmente. Sempre que alterada, um novo Identificador de Operação será gerado. Não será permitido alterar a liquidação se a mesma possuir "baixa pendente" diferente de "Livre" ou caso a contabilidade integrada ao lote zero.

- Cancelar Liquidação Duvidosa: criado um processo para essa tarefa disponível na visão de lançamentos para todos os lançamentos selecionados pelo usuário. Na tela deverá ser preenchido a Data de cancelamento da liquidação duvidosa.

As seguintes validações serão realizadas:

* O Status da liquidação duvidosa do lançamento deverá ser liquidação duvidosa ou liquidação duvidosa parcial;
* Lançamento deve estar em aberto ou parcialmente baixado (caso a baixa tenha sido executada antes da liquidação duvidosa). Se algum processo tiver sido executado após a liquidação duvidosa, ele deve ser desfeito antes do cancelamento.
* Lançamento não pode ter "baixa pendente".

Como podem existir vários registros de liquidação duvidosa num mesmo lançamento a operação será realizada sobre aquele que estiver ativo (não cancelado), já que um único pode estar nesse estado. Caso não existe algum nada será realizado.

Serão necessárias as seguintes validações:

* A data de cancelamento da liquidação deve ser maior ou igual a data da própria liquidação e não pode ser maior que a data atual.

O processo deve ser executado da seguinte forma:

* Para os lançamentos que estiverem com o status de liquidação duvidosa ou liquidação duvidosa parcial, a contabilização será estornada e o status de liquidação duvidosa voltará para não duvidoso.
* O status do registro da liquidação duvidosa passará para "Cancelada", para manter o histórico de liquidações duvidosas.

- Baixa de lançamentos: durante o processo de baixa, se o status do lançamento estiver como liquidação duvidosa ou liquidação duvidosa parcial, deverá ser utilizado o evento contábil de baixa em lançamentos com liquidação duvidosa da tabela default para eventos (tipo de documento ou uma das tabelas opcionais). Se o evento não estiver definido deve ser emitida mensagem de erro e o processo abortado. O mesmo comportamento será visto na baixa de lançamentos por acordo, com a diferença que será usado o evento contábil de baixa por acordo em lançamentos com liquidação duvidosa.

- Solicitar exclusão da operação contábil: desenvolvido o processo de solicitação da exclusão da operação contábil para a contabilização da liquidação duvidosa, que será executado quando a mesma está cancelada e a contabilidade relacionada já  estiver integrada ao lote zero.

- Parametrizador do Financeiro: criado um parâmetro para lote de inclusão e outro para lote de estorno da contabilização da liquidação duvidosa. Somente lotes do módulo Financeiro e da coligada corrente serão exibidos para seleção.

- Liberação de Período: excluir as informações da tabela de liquidação duvidosa e liberar o registro de operação contábil para os lançamentos liberados.

## Procedimento para Configuração

1 - No Totvs Gestão Financeira, menu *Ambiente | Parâmetros | Gestão Financeira* acesse Integração Contábil | Contabilização (02.05.01) | Contab. Financeiro e selecione a Tabela Default para Evento.

*Figura 1- Parametrização de onde buscar o evento contábil*

2 - No menu *Cadastros | Específicos* acesse o cadastro de Tipo de Documento ou Tabelas Opcionais de acordo com a escolha do item anterior. Na aba Eventos Contábeis informe os eventos para as operações de inclusão, baixa e baixa por acordo de lançamentos com liquidação duvidosa.

*Figura 2- Parametrização dos eventos contábeis* 

## Procedimento para Utilização

1 - Acesse o menu *Contas a Pagar/Receber | Operações Financeiras | Lançamentos | Processos | Incluir Liquidação Duvidosa*para executar o processo que irá classificar o lançamento em liquidação duvidosa. Os lançamentos selecionados devem ter as seguintes características: a receber, em aberto ou parcialmente baixados, vencidos, contábil ou baixa contábil e não ter uma liquidação duvidosa ativa. A data da liquidação deve ser informada (menor ou igual à data corrente, e para parcialmente baixados maior ou igual que a data da última baixa). 

*Figura 3- Processo de liquidação duvidosa*

Após a execução do processo o Status de Liquidação Duvidosa do lançamento passar a ser "Liquidação duvidosa", se o mesmo está em aberto, ou "Liquidação Duvidosa Parcial" se parcialmente baixado. A contabilidade será gerada aplicando o Evento Contábil para Liquidação Duvidosa informado no Tipo de Documento/Tabelas Opcionais conforme parametrização indicada no tópico anterior. 

2 - Acesse o menu *Contas a Pagar/Receber | Operações Financeiras | Lançamentos | Anexos | Liquidação Duvidosa*para visualizar as liquidações existentes para o lançamento. É possível alterar a contabilidade manualmente ou aplicando um novo evento (acesso pelo botão *Contabilização*). 

*Figura 4- Registro de liquidação duvidosa* 

3 - Acesse o menu *Contas a Pagar/Receber | Operações Financeiras | Lançamentos | Processos | Cancelar Liquidação Duvidosa*para realizar o cancelamento da liquidação. A data do cancelamento deve ser informada (um valor maior que a data da liquidação). Após a execução, o registro da liquidação altera o status para cancelado, a data do cancelamento armazenada e o Status de Liquidação do lançamento muda para "Liquidação não Duvidosa". Em relação à contabilização, se não integrada ao lote zero é excluída, caso contrário, estornada. Vale ressaltar que, para um mesmo lançamento, só existe uma liquidação ativa (não cancelada). 

*Figura 5- Processo de cancelamento da liquidação duvidosa* 

4 - Acesse o menu *Contas a Pagar/Receber | Operações Financeiras | Lançamentos | Anexos | Liquidação Duvidosa | Solicitar a exclusão de Operação Contábil*para realizar o processo de exclusão de operação contábil quando a contabilidade já está integrada ao lote zero e a liquidação cancelada. O campo Id Operação do registro de liquidação será limpo. 

5 - No processo de baixa de lançamento cujo Status de Liquidação Duvidosa esteja como "Liquidação Duvidosa" ou "Liquidação Duvidosa Parcial" será aplicada o *Evento Contábil para Baixa com Liquidação Duvidosa* parametrizado no Tipo de Documento/Tabelas Opcionais (conforme mostrado no tópico de configuração). 

6 - No processo de baixa de lançamento por acordo cujo Status de Liquidação Duvidosa esteja como "Liquidação Duvidosa" ou "Liquidação Duvidosa Parcial" será aplicada o*Evento Contábil para Baixa por Acordo com Liquidação Duvidosa* parametrizado no Tipo de Documento/Tabelas Opcionais (conforme mostrado no tópico de configuração). 

Importante ressaltar que em ambos os casos de baixa, após a execução desse processo, a liquidação duvidosa não é afetada e nem o Status de Liquidação do lançamento financeiro é alterado.

## Dicionário de Dados

**Arquivo ou Código do Script:** \*$Versao=FS.2016.09\_02\*

|  |  |
| --- | --- |
| **Índice** | **Chave** |
| **01** | PKFLANLIQDUVIDOSA PRIMARY KEY (CODCOLIGADA,IDLIQDUVIDOSA) |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Tabela** | **Campo** | **Tipo** | **Tamanho** | **Valor Inicial** | **Mandatório**  **Sim | Não** | **Descrição** |
| FLAN | STATUSLIQDUVIDOSA | SMALLINT |  | 0 | Não | Status da Liquidação Duvidosa |
| FLANHST | STATUSLIQDUVIDOSA | SMALLINT |  | 0 | Não | Status da Liquidação Duvidosa |
| FTDO | CODEVENTOLIQDUVIDOSA | SMALLINT |  |  | Não | Código do Evento Contábil para Liquidação Duvidosa |
| FTDO | CODEVENTOBXACORDOLIQDUVIDOSA | SMALLINT |  |  | Não | Evento Contábil para Baixa por acordo em lançamento com liquidação duvidosa |
| FTB1 | CODEVENTOLIQDUVIDOSA | SMALLINT |  |  | Não | Código do Evento Contábil para Liquidação Duvidosa |
| FTB1 | CODEVENTOBXACORDOLIQDUVIDOSA | SMALLINT |  |  | Não | Evento Contábil para Baixa por acordo em lançamento com liquidação duvidosa |
| FTB2 | CODEVENTOLIQDUVIDOSA | SMALLINT |  |  | Não | Código do Evento Contábil para Liquidação Duvidosa |
| FTB2 | CODEVENTOBXACORDOLIQDUVIDOSA | SMALLINT |  |  | Não | Evento Contábil para Baixa por acordo em lançamento com liquidação duvidosa |
| FTB3 | CODEVENTOLIQDUVIDOSA | SMALLINT |  |  | Não | Código do Evento Contábil para Liquidação Duvidosa |
| FTB3 | CODEVENTOBXACORDOLIQDUVIDOSA | SMALLINT |  |  | Não | Evento Contábil para Baixa por acordo em lançamento com liquidação duvidosa |
| FTB4 | CODEVENTOLIQDUVIDOSA | SMALLINT |  |  | Não | Código do Evento Contábil para Liquidação Duvidosa |
| FTB4 | CODEVENTOBXACORDOLIQDUVIDOSA | SMALLINT |  |  | Não | Evento Contábil para Baixa por acordo em lançamento com liquidação duvidosa |
| FTB5 | CODEVENTOLIQDUVIDOSA | SMALLINT |  |  | Não | Código do Evento Contábil para Liquidação Duvidosa |
| FTB5 | CODEVENTOBXACORDOLIQDUVIDOSA | SMALLINT |  |  | Não | Evento Contábil para Baixa por acordo em lançamento com liquidação duvidosa |
| FLANLIQDUVIDOSA | CODCOLIGADA | INTEIRO |  |  | Sim | Código da Coligada |
| FLANLIQDUVIDOSA | IDLAN | INTEIRO |  |  | Não | Referência do Lançamento |
| FLANLIQDUVIDOSA | DATA | DATETIME |  |  | Não | Data da Liquidação |
| FLANLIQDUVIDOSA | STATUS | SMALLINT |  |  | Não | Status da Liquidação |
| FLANLIQDUVIDOSA | IDOPERACAO | INTEIRO |  |  | Não | Identificador da operação contábil |
| FLANLIQDUVIDOSA | DATACANCELAMENTO | DATETIME |  |  | Não | Data do Cancelamento da Liquidação |
| FLANLIQDUVIDOSA | RECCREATEDBY | VARCHAR | 50 |  | Não | Usuário criador do registro |
| FLANLIQDUVIDOSA | RECCREATEDON | DATETIME |  |  | Não | Data de criação do registro |
| FLANLIQDUVIDOSA | RECMODIFIEDBY | VARCHAR | 50 |  | Não | Autor da última modificação no registro |
| FLANLIQDUVIDOSA | RECMODIFIEDON | DATETIME |  |  | Não | Data da última modificação no registro |

**Arquivo ou Código do Script:** \*$Versao=FS.2016.12\_05\*

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Tabela** | **Campo** | **Tipo** | **Tamanho** | **Valor Inicial** | **Mandatório**  **Sim | Não** | **Descrição** |
| FLANLIQDUVIDOSA | IDLIQDUVIDOSA | INTEIRO |  | 0 | Sim | Identificador da Liquidação Duvidosa |
| FTDO | CODEVENTOBXLIQDUVIDOSA | SMALLINT |  |  | Não | Evento Contábil para Baixa em lançamento com liquidação duvidosa |
| FTB1 | CODEVENTOBXLIQDUVIDOSA | SMALLINT |  |  | Não | Evento Contábil para Baixa em lançamento com liquidação duvidosa |
| FTB2 | CODEVENTOBXLIQDUVIDOSA | SMALLINT |  |  | Não | Evento Contábil para Baixa em lançamento com liquidação duvidosa |
| FTB3 | CODEVENTOBXLIQDUVIDOSA | SMALLINT |  |  | Não | Evento Contábil para Baixa em lançamento com liquidação duvidosa |
| FTB4 | CODEVENTOBXLIQDUVIDOSA | SMALLINT |  |  | Não | Evento Contábil para Baixa em lançamento com liquidação duvidosa |
| FTB5 | CODEVENTOBXLIQDUVIDOSA | SMALLINT |  |  | Não | Evento Contábil para Baixa em lançamento com liquidação duvidosa |

**Arquivo ou Código do Script:** \*$Versao=FS.2016.12\_07\*

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Tabela** | **Campo** | **Tipo** | **Tamanho** | **Valor Inicial** | **Mandatório**  **Sim | Não** | **Descrição** |
| FLANLIQDUVIDOSA | CODEVENTOLIQUIDACAO | SMALLINT |  | 0 | Sim | Evento Contábil da Liquidação |
