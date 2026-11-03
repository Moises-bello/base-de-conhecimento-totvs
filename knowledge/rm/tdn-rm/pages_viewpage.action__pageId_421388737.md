---
content_hash: d8856591708cad16ddb02ca8c5fe911badbe480619fcb3c6a6c3fcbccfbcf43d
fetched_at: '2026-06-29T00:09:18.657577+00:00'
page_id: '421388737'
product: rm
source: tdn-rm
title: Reajuste Parcelas do Totvs Incorporação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388737
version: 5
---

Nesta versão o processo apenas estará disponível caso o cliente não tenha tido baixas no Modelo Antigo de Baixa e somente lançamento do Totvs Imobiliário terá os Valores de Integração reajustado.

Implementação dos Parâmetros:

Menu:  Ambiente  | Parâmetros  | Totvs Gestão Financeira  | Contas a Receber  | Integração Imobiliária.

Reajusta os valores de integração dos lançamentos até a data de reajuste

Define se será chamada a função do Totvs Incorporação que calcula o reajuste até a data de reajuste para os lançamentos oriundos deste produto com a natureza "A Receber". Se o parâmetro estiver desmarcado, não será realizado o reajuste. Caso contrário, o reajuste será realizado.  Necessário habilitar o parâmetro uma única vez, feito isso não será possível desmarcar o mesmo.

Default da data de reajuste

Define o valor default para data de reajuste na Baixa Manual. Com as opções "Data da Baixa" e "Vencimento da Parcela".

Permite o usuário alterar a data de reajuste.

Define se o usuário terá permissão na Baixa Manual de alterar a data de reajuste. Se o parâmetro estiver desmarcado o usuário não poderá alterar a data para reajuste. Caso contrário, o usuário poderá alterar.

Permite reajustar lançamentos registrados ou remetidos ao banco na Baixa Manual e Recebimento Via Cheque

Define se o reajuste será ou não executado na baixa manual e no recebimento via cheque para os lançamentos que já estiverem remetidos ou registrados (Status CNAB).   
 Se o parâmetro estiver desmarcado, não será realizado o reajuste se o Status CNAB do lançamento for "Remetido" ou "Registrado" e será apresentada a mensagem: "O valor deste lançamento não está sendo reajustado devido ao fato de estar remetido a banco". Caso contrário, o reajuste será realizado sempre.

Estará habilitando quando o parâmetro "Permite baixar lançamentos com Borderô ou enviandos ao Banco" estiver habilitado.

Menu:  Ambiente  | Parâmetros  | Totvs Gestão Financeira  | Contas  a Receber  |  Baixas   | Baixa 1/4

Permite alterar lançamento a receber remetidos ao banco

Define que será possível alterar lançamentos a receber remetidos ao banco.

Menu:  Ambiente  | Parâmetros  | Totvs Gestão Financeira  | Contas  a Receber  |  Manutenção de Lançamentos  | Inclusão a Receber.

Através dos campos de valores de integração será realizado o reajuste das parcelas do Totvs Incorporação no Totvs Gestão Financeira utilizando as rotinas como Baixa, Emissão de Cheque e Integração Bancária (Cobrança Não Registrada).
