---
content_hash: 75d86c204222cc0173474e5a55722820ef61b9bfa059b4fb5311ba90c9017425
fetched_at: '2026-06-29T00:10:42.835514+00:00'
page_id: '547861431'
product: rm
source: tdn-rm
title: 2.7 Baixa Manual de Lançamentos Financeiros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=547861431
version: 8
---

O processo Baixa ou Quitação consiste em atualizar o Lançamento Financeiro registrando os dados que comprovem a sua quitação. Este processo está relacionado a atualização dos saldos das contas caixa e à contabilização. A baixa poderá ser realizada manualmente pelo usuário ou por importação de arquivos de retorno de cada Banco. A principal tabela que grava as informações das baixas realizadas é a *FLANBAIXA*.

No processo de baixa ou quitação do titulo:

* Poderão ser utilizados um ou vários meios de pagamento.
* Através do Anexo/Baixas do Lançamento poderá ser visualizado todos os meios de pagamento utilizados na baixa.
* Será gravado no extrato de caixa tantos registros quantos forem os meios de pagamento utilizados.
* Todas as informações referentes à baixa ficarão armazenadas no lançamento de origem.
* Poderá haver o cancelamento de um item de baixa e o lançamento ficará com o status de parcialmente quitado.

Para realizar esse processo o usuário deve acessar o Módulo Gestão Financeira e seguir os passos sinalizados abaixo:

Para isso acessar: Menu TOTVS - Linha RM | BackOffice | Módulo Gestão Financeira

O usuário pode utilizar o filtro do Sistema para selecionar lançamentos financeiros desejados.

Após selecionar o filtro desejado, o sistema listará os lançamentos financeiros. Para realizar a baixa do lançamento o usuário deve selecionar o boleto e realizar os passos a seguir.

O usuário deve selecionar o lançamento desejado e acessar “*Processos | Baixa | Baixar Lançamento*”.

O usuário poderá acessar este processo também através do ícone ().

Neste exemplo, iremos demonstrar a baixa "*completa*"

O usuário deve informar os campos:

* **Tipo de Baixa:** Informar a opção “COMPLETA”;
* **Data Baixa:** Informar a data em que o lançamento será baixado;
* **Moeda:** Moeda já será carregada do lançamento financeiro (R$ - Real);
* **Gerar:** Marcar uma das opções apresentadas “Um extrato para cada lançamento” "Um extrato para todos os lançamentos";
* **Histórico:** Será carregado automaticamente de acordo com a parametrização realizada.

Será apresentada a tela para edição do meio de pagamento, o usuário deve escolher o meio de pagamento (Ex.: Dinheiro, Cheque, Cartão, etc) e preencher as informações:

* **Valor:** Informar o valor que está sendo baixado neste meio de pagamento;
* **Conta Caixa:** Informar a conta caixa que está recebendo os valores. Sempre será carregada a conta caixa do lançamento financeiro;
* **Compensar no Extrato:** Marcando esta opção, o Sistema compensará o extrato bancário;
* **Data Compensação Extrato:** Informar a data de compensação do extrato bancário.

Após clicar em “Ok”, o Sistema retorna para a tela de baixa do lançamento com o meio de pagamento informado.

Na tela a seguir é possível visualizar a contabilização de baixa.

Após clicar em “Executar” o Sistema retornará com a tela informando o sucesso da baixa realizada.

Veja Também
