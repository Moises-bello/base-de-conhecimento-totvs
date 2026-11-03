---
content_hash: c537495349bb48c7b017d74d638e4e3fb98d6e1faafbe6875c04a96a94719e75
fetched_at: '2026-06-29T00:10:43.143861+00:00'
page_id: '550113125'
product: rm
source: tdn-rm
title: 2.16 Liquidação Duvidosa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=550113125
version: 11
---

Não se aplica a integração com Protheus

O processo de Liquidação Duvidosa tem como objetivo permitir a contabilização, através de regras pré-definidas, das provisões de lançamentos com recebimento duvidoso na forma de crédito de liquidação duvidosa. Este processo somente será executado para lançamentos a receber, vencidos e que ainda não foram recebidos e só estará disponível quando a integração TOTVS Educacional x BackOffice Protheus (Financeiro) não estiver ativa, para todos os registros.

Para **incluir** um lançamento financeiro em liquidação duvidosa, o usuário deve acessar: BackOffice | Gestão Financeira | Contas a Pagar/Receber | Lançamentos.

As seguintes validações serão realizadas para que o processo seja executado:

* Os lançamentos devem estar em aberto ou parcialmente baixados;
* Os lançamentos não podem ter liquidação duvidosa ativa;
* Os lançamentos devem estar vencidos;
* Os lançamentos devem ser a receber;
* Os lançamentos devem ser do tipo contábil ou baixa contábil;
* Para os lançamentos baixados parcialmente, a data da baixa deve ser anterior à data da liquidação duvidosa;
* A data da liquidação duvidosa não pode ser futura, ou seja, deverá ser igual ou anterior à data do sistema.

Selecione os lançamentos que serão incluídos na Liquidação Duvidosa e acesse Processos | Incluir Liquidação Duvidosa

Informe a data da Liquidação e clique em Executar:

**Resultado da execução do processo:**

* Para os lançamentos válidos será alterado o Status de Liquidação não Duvidosa para "Liquidação Duvidosa" caso o lançamento esteja em aberto, e para "Liquidação Duvidosa Parcial" caso esteja parcialmente baixado.
* Será realizada a contabilização desses lançamentos, utilizando o evento contábil informado na tabela default para evento. O Id. da operação e a data da liquidação serão registrados em uma tabela própria para a Liquidação Duvidosa. A contabilização gerada é visível somente no Totvs Gestão Contábil e o número contábil usado será sempre o número do documento.
* A execução do processo será registrada no Histórico de Alteração do lançamento.

"Os lançamentos devem estar vencidos"

Caso o lançamento selecionado não esteja "*vencido*" o erro abaixo será apresentado"

Para **visualizar** a inclusão da Liquidação Duvidosa Acesse Anexos | Liquidação Duvidosa

O Anexo "Liquidação Duvidosa" na visão Geral de Lançamentos irá exibir todas as Liquidações existentes para o lançamento financeiro. 

"Validação de processos para lançamentos com Liquidação Duvidosa"

Se o lançamento estiver com o status de liquidação duvidosa ou liquidação duvidosa parcial, alguns processos não poderão ser executados. Será necessário cancelar a liquidação duvidosa antes de executar os seguintes processos:

* Cancelamento do lançamento
* Alterações no lançamento (valores, data de vencimento, tipo contábil)
* Parcelamento do lançamento
* Cancelamento da baixa processadas antes do processo de liquidação duvidosa. Nesse caso, a verificação será feita pela data da baixa, que deve ser posterior à data da liquidação.

Para **cancelar** uma inclusão em Liquidação Duvidosa, selecione o lançamento, acesse Processos | Cancelar Liquidação Duvidosa

Informe a Data do Cancelamento e clique em Avançar e logo em seguida clique em Executar

Ao executar o processo informando a "Data do Cancelamento", para os lançamentos com status de "*Liquidação Duvidosa*" ou "*Liquidação Duvidosa Parcial*", o status desses lançamentos ficarão com status de "*Liquidação Não Duvidosa*".

**Validações para Cancelamento da Liquidação Duvidosa**

* O Status da liquidação duvidosa do lançamento deverá ser liquidação duvidosa ou liquidação duvidosa parcial;
* O Lançamento deve estar em aberto ou parcialmente baixado (caso a baixa tenha sido executada antes da liquidação duvidosa). Se algum processo tiver sido executado após a liquidação duvidosa, ele deve ser desfeito antes do cancelamento.
* O Lançamento não pode ter "baixa pendente".
* Como podem existir vários registros de liquidação duvidosa em um mesmo lançamento a operação será realizada sobre aquele que estiver ativo (não cancelado). Caso não existe algum nada será realizado.
* A data de cancelamento da liquidação deve ser maior ou igual a data da própria liquidação e não pode ser maior que a data atual.

**Resultado da execução do processo:**

* Para os lançamentos que estiverem com o status de liquidação duvidosa ou liquidação duvidosa parcial, a contabilização será estornada e o status de liquidação duvidosa voltará para não duvidoso.
* O status do registro da liquidação duvidosa passará para "*Cancelada*", para manter o histórico de liquidações duvidosas.

Para **visualizar** a Liquidação Duvidosa Cancelada, acesse Anexos | Liquidação Duvidosa

O Anexo "Liquidação Duvidosa" na visão Geral de Lançamentos irá exibir todas as Liquidações existentes para o lançamento financeiro.
