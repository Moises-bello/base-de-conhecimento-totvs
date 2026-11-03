---
content_hash: 3c4cf110eec01e5f43f96e93be0cdda94cf771ad2dcbd67b4b29de3652a3e37b
fetched_at: '2026-06-29T00:09:17.411286+00:00'
page_id: '421388584'
product: rm
source: tdn-rm
title: Liquidação Duvidosa 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388584
version: 7
---

O processo de Liquidação Duvidosa tem como objetivo permitir a contabilização, através de regras pré-definidas, das provisões de lançamentos com recebimento duvidoso na forma de crédito de liquidação duvidosa. Este processo somente será executado para lançamentos a receber, vencidos e que ainda não foram recebidos e só estará disponível quando a integração Totvs Educacional x Backoffice Protheus (Financeiro) não estiver ativa, para todos os registros. O menu de Boleto está disponível também para integração com TOTVS Educacional x BackOffice Protheus quando ativa.

**Observação:**

Quando a integração do Protheus X Contábil X EAI  estiverem 'Ativas',  o menu de inclusão, exclusão do processo de liquidação duvidosa e cancelamento da liquidação duvidosa no RM, serão disponibilizados para controle do processo de liquidação duvidosa. 

**Parametrização:**

1 - Totvs Gestão Financeira, menu Ambiente | Parâmetros | Gestão Financeira | Integração Contábil | Contabilização | Contab. Financeiro e defina a Tabela Default para Evento (Tipo de Documento ou uma das 5 Tabelas Opcionais).  
2 -  Totvs Gestão Financeira, menu Ambiente | Parâmetros | Gestão Financeira | Integração Contábil | Lote Contábil | Receber, foi criado um parâmetro para lote de inclusão e lote de estorno da contabilização da liquidação duvidosa. Somente lotes do módulo Financeiro e da coligada corrente serão exibidos para seleção.

**Status Liquidação Duvidosa:**

 O campo "Status de Liquidação Duvidosa" será apresentado na visão geral de Lançamento, Contas a Pagar/Receber -> Operações Financeiras -> Lançamentos, com as opções:

* Liquidação não Duvidosa, inserido na inclusão do lançamento.
* Liquidação Duvidosa: O lançamento assume este status quando o processo de Inclusão de Liquidação Duvidosa é executado.
* Liquidação Duvidosa Parcial: Para este status, o processo de Liquidação Duvidosa deve ser executado para um lançamento que esteja Parcialmente Baixado.

**Cadastro Default Contábeis para "Tipo de Documento" ou "Tabelas Opcionais"**

Gestão Financeira -> Cadastros -> Específicos:  
Criados campos para informar os eventos que serão utilizados pelo processo para realizar a contabilização da liquidação duvidosa.

* Evento Contábil para Liquidação Duvidosa.
* Evento Contábil para Baixa em lançamento com liquidação duvidosa
* Evento Contábil para Baixa por acordo em lançamento com liquidação duvidosa.

**Execução do processo de "Liquidação Duvidosa"**

Contas a Pagar/Receber -> Operações Financeiras -> Lançamentos -> Processos -> Incluir Liquidação Duvidosa.  
Para executar o processo basta informar a "Data da liquidação duvidosa para a contabilização". As seguintes validações serão realizadas para que o processo seja executado:

* Os lançamentos devem estar em aberto ou parcialmente baixados;
* Os lançamentos não podem ter liquidação duvidosa ativa;
* Os lançamentos devem estar vencidos;
* Os lançamentos devem ser a receber;
* Os lançamentos devem ser do tipo contábil ou baixa contábil;
* Para os lançamentos baixados parcialmente, a data da baixa deve ser anterior à data da liquidação duvidosa;
* A data da liquidação duvidosa não pode ser futura, ou seja, deverá ser igual ou anterior à data do sistema.

**Resultado da execução do processo:**

* Para os lançamentos válidos será alterado o Status de Liquidação não Duvidosa para "Liquidação Duvidosa" caso o lançamento esteja em aberto, e para "Liquidação Duvidosa Parcial" caso esteja parcialmente baixado.
* Será realizada a contabilização desses lançamentos, utilizando o evento contábil informado na tabela default para evento. O Id. da operação e a data da liquidação serão registrados em uma tabela própria para a Liquidação Duvidosa. A contabilização gerada é visível somente no Totvs Gestão Contábil e o número contábil usado será sempre o número do documento.
* A execução do processo será registrada no Histórico de Alteração do lançamento.

**Validação de processos para lançamentos com Liquidação Duvidosa**

Se o lançamento estiver com o status de liquidação duvidosa ou liquidação duvidosa parcial, alguns processos não poderão ser executados. Será necessário cancelar a liquidação duvidosa antes de executar os seguintes processos:

* Cancelamento do lançamento
* Alterações no lançamento (valores, data de vencimento, tipo contábil)
* Parcelamento do lançamento
* Cancelamento da baixa processadas antes do processo de liquidação duvidosa. Nesse caso, a verificação será feita pela data da baixa, que deve ser posterior à data da liquidação.

**Anexo Liquidação Duvidosa:**

O Anexo "Liquidação Duvidosa" na visão Geral de Lançamentos irá exibir todas as Liquidações existentes para o lançamento financeiro. Não será possível incluir ou excluir registros desse anexo, a alteração somente será permitida para a contabilização, que pode ser regerada, informando outro evento contábil ou alterando a contabilização manualmente. Sempre que alterada um novo "Identificador de Operação" será gerado.  
Não será permitido alterar a liquidação se a mesma possuir "baixa pendente" diferente de "Livre" ou caso a contabilidade estiver integrada ao lote zero.

**Cancelamento da Liquidação Duvidosa**

Contas a Pagar/Receber > Lançamentos > Processos > Cancelar Liquidação Duvidosa.  
Ao executar o processo informando a "Data do Cancelamento", para os lançamentos com status de "Liquidação Duvidosa" ou "Liquidação Duvidosa Parcial", o status desses lançamentos ficarão com status de "Liquidação Não Duvidosa".

**Validações para Cancelamento da Liquidação Duvidosa**

* O Status da liquidação duvidosa do lançamento deverá ser liquidação duvidosa ou liquidação duvidosa parcial;
* O Lançamento deve estar em aberto ou parcialmente baixado (caso a baixa tenha sido executada antes da liquidação duvidosa). Se algum processo tiver sido executado após a liquidação duvidosa, ele deve ser desfeito antes do cancelamento.
* O Lançamento não pode ter "baixa pendente".
* Como podem existir vários registros de liquidação duvidosa em um mesmo lançamento a operação será realizada sobre aquele que estiver ativo (não cancelado). Caso não existe algum nada será realizado.
* A data de cancelamento da liquidação deve ser maior ou igual a data da própria liquidação e não pode ser maior que a data atual.

**Resultado da execução do processo:**

* Para os lançamentos que estiverem com o status de liquidação duvidosa ou liquidação duvidosa parcial, a contabilização será estornada e o status de liquidação duvidosa voltará para não duvidoso.
* O status do registro da liquidação duvidosa passará para "Cancelada", para manter o histórico de liquidações duvidosas.

**Solicitar a exclusão de Operação Contábil**

Contas a Pagar/Receber -> Lançamentos | Anexos -> Liquidação duvidosa-> Processos | Solicitar a Exclusão de Operação Contábil.  
Criado processo de solicitação da exclusão da operação contábil para a contabilização da liquidação duvidosa, que será executado quando a mesma estiver cancelada e a contabilidade relacionada já estiver integrada ao lote zero.

**Liberação de Período**

Utilitários -> Liberação de Período  
Ao executar o processo de Liberação de Período, serão excluídas as informações da tabela de liquidação duvidosa e irá liberar o registro de operação contábil para os lançamentos liberados.  
  
**Tabelas Relacionadas:**

* FLAN – STATUSLIQDUVIDOSA
* FLANHST – STATUSLIQDUVIDOSA
* FTDO – CODEVENTOLIQDUVIDOSA
* FTDO - CODEVENTOBXACORDOLIQDUVIDOSA
* FTB1, FTB2, FTB3, FTB4, FTB5:
* CODEVENTOLIQDUVIDOSA, CODEVENTOBXACORDOLIQDUVIDOSA
* FLANLIQDUVIDOSA
