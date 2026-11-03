---
content_hash: 9ddaf61e61034b0fb5a0404dd9789bf3fba6e98efa684da20b6d2c0240b7a512
fetched_at: '2026-06-29T00:09:17.427693+00:00'
page_id: '421388589'
product: rm
source: tdn-rm
title: Métodos de Inclusão de Fatura
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388589
version: 2
---

Para realizar o processo de inclusão de fatura é necessário escolher qual o método que será utilizado, os métodos disponíveis são:

Uma Fatura para todos os lançamentos selecionados

Utilizando este método é possível incluir uma Fatura gerando um ou vários Vencimentos de Faturas para um ou vários lançamentos.  
 Só é possível gerar Vencimentos de Fatura para "um Cliente/Fornecedor".

Exemplos

* Lançamento 1: Cliente/Fornecedor 1, Valor: R$600,00
* Lançamento 2: Cliente/Fornecedor 1, Valor: R$600,00
* Lançamento 3: Cliente/Fornecedor 2, Valor: R$1.600,00

Um Lançamento, um Vencimento de Fatura e Cliente/Fornecedor diferente

É possível informar um cliente/fornecedor que não seja o informado no lançamento e gerar um Vencimento de Fatura:

* Selecionado um lançamento:
* Lançamento 1, Cliente/Fornecedor 1, Valor: R$600,00
* Incluída uma Fatura:
* Cliente/Fornecedor 4, Valor: R$600,00
* Gerado um Vencimento de Fatura:
* Cliente/Fornecedor 4, Valor: R$600,00

Vários Lançamentos, um Vencimento de Fatura e Cliente/Fornecedor diferente

É possível informar um cliente/fornecedor que não seja o informado nos lançamentos e gerar um Vencimento de Fatura:

* Selecionados todos os lançamentos
* Incluída uma Fatura:
* Cliente/Fornecedor 4, Valor: R$2.800,00
* Gerado um Vencimento de Fatura:
* Cliente/Fornecedor 4, Valor: R$2.800,00

Vários Lançamentos, um Vencimento de Fatura e Cliente/Fornecedor de um dos lançamentos

É possível informar um dos clientes/fornecedores informado nos lançamentos e gerar um Vencimento de Fatura:

* Selecionados todos os lançamentos
* Incluída uma Fatura:
* Cliente/Fornecedor 1, Valor: R$2.800,00
* Gerado um Vencimento de Fatura:
* Cliente/Fornecedor 1, Valor: R$2.800,00

Vários Lançamentos, vários Vencimentos de Fatura e Cliente/Fornecedor de um dos lançamentos

É possível informar um dos clientes/fornecedores informado em um dos lançamentos e gerar vários Vencimentos de Fatura:

* Selecionados todos os lançamentos
* Incluída uma Fatura:
* Cliente/Fornecedor 2, Valor: R$2.800,00
* Gerados quatro Vencimentos de Fatura:
* Cliente/Fornecedor 2, Valor: R$700,00 - Cliente/Fornecedor 2, Valor: R$700,00 - Cliente/Fornecedor 2, Valor: R$700,00 - Cliente/Fornecedor 2, Valor: R$700,00

Uma fatura para cada Cliente/Fornecedor

Utilizando este método é possível incluir uma Fatura para cada cliente/fornecedor dos lançamentos selecionados, gerando um ou vários Vencimentos de Faturas para um ou vários lançamentos. O Cliente/Fornecedor dos Vencimentos de Fatura sempre será o mesmo do lançamento selecionado.

**Observação**

Quando houver inconsistência na Inclusão de Fatura para algum Cliente/Fornecedor, a Inclusão para os outros será realizada normalmente.

Existem os seguintes lançamentos:

* Lançamento 1: Cliente/Fornecedor 1, Valor: R$600,00
* Lançamento 2: Cliente/Fornecedor 1, Valor: R$600,00
* Lançamento 3: Cliente/Fornecedor 2, Valor: R$1.600,00

Vários Lançamentos, um Vencimento de Fatura para cada Cliente/Fornecedor

Selecionando vários lançamentos de clientes/fornecedores diferentes é possível Incluir uma Fatura para cada cli/for gerando um Vencimento de Fatura para cada cli/for: - Selecionados todos os lançamentos

* Incluídas duas Faturas:
* Cliente/Fornecedor 1, Valor: R$1.200,00
* Cliente/Fornecedor 2, Valor: R$1.600,00
* Gerados dois Vencimentos de Fatura:
* Cliente/Fornecedor 1, Valor: R$1.200,00
* Cliente/Fornecedor 2, Valor: R$1.600,00

Vários Lançamentos, vários Vencimentos de Fatura para um Cliente/Fornecedor e um Vencimento de Fatura para outro Cliente/Fornecedor

Selecionando vários lançamentos de clientes/fornecedores diferentes é possível Incluir uma Fatura para cada cli/for gerando um Vencimento de Fatura para um cli/for e vários Vencimentos de Fatura para o outro cli/for:

* Selecionados todos os lançamentos
* Incluídas duas Faturas:  
   Cliente/Fornecedor 1, Valor: R$1.200,00

            Cliente/Fornecedor 2, Valor: R$1.600,00

* Gerados cinco Vencimentos de Fatura:  
   Cliente/Fornecedor 1, Valor: R$300,00

            Cliente/Fornecedor 1, Valor: R$300,00

            Cliente/Fornecedor 1, Valor: R$300,00

            Cliente/Fornecedor 1, Valor: R$300,00

            Cliente/Fornecedor 2, Valor: R$1.600,00

Uma fatura para cada Movimento

Utilizando este método é possível incluir uma Fatura para cada movimento dos lançamentos selecionados, gerando um ou vários Vencimentos de Faturas para um ou vários lançamentos. Este método é utilizado para lançamentos gerados pelo aplicativo RM Nucleus. O Cliente/Fornecedor dos Vencimentos de Fatura sempre será o mesmo do lançamento selecionado. Exemplos Existem os seguintes lançamentos:

* Lançamento 1: Cliente/Fornecedor 1, Movimento: 100, Valor: R$600,00
* Lançamento 2: Cliente/Fornecedor 1, Movimento: 200, Valor: R$600,00
* Lançamento 3: Cliente/Fornecedor 2, Movimento: 300, Valor: R$800,00 - Lançamento 4: Cliente/Fornecedor 2, Movimento: 300, Valor: R$800,00

Vários Lançamentos, um Vencimento de Fatura para cada Movimento

Selecionando vários lançamentos de movimentos diferentes é possível Incluir uma Fatura para cada movimento gerando um Vencimento de Fatura para cada movimento:

* Selecionados todos os lançamentos
* Incluídas três Faturas:  
   Cliente/Fornecedor 1, Movimento: 100, Valor: R$600,00  
   Cliente/Fornecedor 1, Movimento: 200, Valor: R$600,00  
   Cliente/Fornecedor 2, Movimento: 300, Valor: R$1.600,00

* Gerados três Vencimentos de Fatura:  
   Cliente/Fornecedor 1, Movimento: 100, Valor: R$600,00  
   Cliente/Fornecedor 1, Movimento: 200, Valor: R$600,00  
   Cliente/Fornecedor 2, Movimento: 300, Valor: R$1.600,00

Vários Lançamentos, um Vencimento de Fatura para um Movimento e vários Vencimentos de Fatura para os outros Movimentos

Selecionando vários lançamentos de movimentos diferentes é possível Incluir uma Fatura para cada movimento gerando um Vencimento de Fatura para um movimento e vários Vencimentos de Fatura para outros movimentos:

* Selecionados todos os lançamentos
* Incluídas três Faturas:  
   Cliente/Fornecedor 1, Movimento: 100, Valor: R$600,00  
   Cliente/Fornecedor 1, Movimento: 200, Valor: R$600,00  
   Cliente/Fornecedor 2, Movimento: 300, Valor: R$1.600,00

* Gerados seis Vencimentos de Fatura:  
   Cliente/Fornecedor 1, Movimento: 100, Valor: R$600,00 Cliente/Fornecedor 1, Movimento: 200, Valor: R$150,00 Cliente/Fornecedor 1, Movimento: 200, Valor: R$150,00 Cliente/Fornecedor 1, Movimento: 200, Valor: R$150,00 Cliente/Fornecedor 1, Movimento: 200, Valor: R$150,00 Cliente/Fornecedor 2, Movimento: 300, Valor: R$1.600,00

Uma fatura para cada Meio de Pagamento

Utilizando este método é possível incluir uma Fatura para cada meio de pagamento dos lançamentos selecionados, gerando um ou vários Vencimentos de Faturas para um ou vários lançamentos. Este método é utilizado para lançamentos gerados pelo aplicativo RM Nucleus e que tenham a informação de "Meio de Pagamento". O Cliente/Fornecedor dos Vencimentos de Fatura sempre será o mesmo do lançamento selecionado.

Existem os seguintes lançamentos:

* Lançamento 1: Cliente/Fornecedor 1, Movimento: 100, Meio de Pagamento: 4, Valor: R$700,00
* Lançamento 2: Cliente/Fornecedor 2, Movimento: 200, Meio de Pagamento: 1, Valor: R$600,00
* Lançamento 3: Cliente/Fornecedor 2, Movimento: 300, Meio de Pagamento: 7, Valor: R$800,00
* Lançamento 4: Cliente/Fornecedor 2, Movimento: 400, Meio de Pagamento: 1, Valor: R$1.000,00

Vários Lançamentos, um Vencimento de Fatura para cada Meio de Pagamento

Selecionando vários lançamentos de Meios de Pagamento diferentes é possível Incluir uma Fatura para cada Meio de Pagamento gerando um Vencimento de Fatura para cada Meio de Pagamento:

* Selecionados todos os lançamentos
* Incluídas três Faturas:  
   Cliente/Fornecedor 1, Meio de Pagamento: 4, Valor: R$700,00  
   Cliente/Fornecedor 2, Meio de Pagamento: 1, Valor: R$1.600,00  
   Cliente/Fornecedor 2, Meio de Pagamento: 7, Valor: R$800,00

* Gerados três Vencimentos de Fatura:  
   Cliente/Fornecedor 1, Meio de Pagamento: 4, Valor: R$700,00  
   Cliente/Fornecedor 2, Meio de Pagamento: 1, Valor: R$1.600,00  
   Cliente/Fornecedor 2, Meio de Pagamento: 7, Valor: R$800,00

Vários Lançamentos, um Vencimento de Fatura para uma Meio de Pagamento e vários Vencimentos de Fatura para as outros Meios de Pagamento

Selecionando vários lançamentos de Meios de Pagamento diferentes é possível Incluir uma Fatura para cada Meio de Pagamento gerando um Vencimento de Fatura para um Meio de Pagamento e vários Vencimentos de Fatura para outros Meios de Pagamento:

* Selecionados todos os lançamentos

* Incluídas três Faturas:

Cliente/Fornecedor 1, Meio de Pagamento: 4, Valor: R$700,00  
 Cliente/Fornecedor 2, Meio de Pagamento: 1, Valor: R$1.600,00  
 Cliente/Fornecedor 2, Meio de Pagamento: 7, Valor: R$800,00

* Gerados sete Vencimentos de Fatura:

Cliente/Fornecedor 1, Meio de Pagamento: 4, Valor: R$700,00  
 Cliente/Fornecedor 2, Meio de Pagamento: 1, Valor: R$400,00

Cliente/Fornecedor 2, Meio de Pagamento: 1, Valor: R$400,00

Cliente/Fornecedor 2, Meio de Pagamento: 1, Valor: R$400,00

Cliente/Fornecedor 2, Meio de Pagamento: 1, Valor: R$400,00  
 Cliente/Fornecedor 2, Meio de Pagamento: 7, Valor: R$400,00

Cliente/Fornecedor 2, Meio de Pagamento: 7, Valor: R$400,00

Uma fatura para cada Filial

Para gerar vencimentos de fatura agrupados por filial, você deverá selecionar a opção "Uma fatura para cada Filial" e em seguida clicar sobre a Filial e informar o número da fatura. Repetir o processo para todas as filiais envolvidas.
