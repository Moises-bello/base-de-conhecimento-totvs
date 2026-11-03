---
content_hash: 79c926d734b4d1239adbef70d35634a8713a54c4a4917a79995ca8f3beae9341
fetched_at: '2026-06-29T00:12:02.401511+00:00'
page_id: '901942291'
product: rm
source: tdn-rm
title: Objeto de Negócios - Movimentação da Sessão de Caixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=901942291
version: 3
---

Foi disponibilizado um Objeto de Negócio para que possam ser extraídos os dados de movimentação de uma Sessão de Caixa

Serão consideradas as informações referentes a uma determinada sessão de caixa definida pelo usuário, podendo ser utilizado o Smart View como saída.

As seguintes informações estão disponíveis:

**Parâmetros**

Para geração das informações os seguintes parâmetros devem ser informados::

* **Código da Coligada**: Coligada da sessão de caixa (obrigatório);
* **Código da Filial**: Filial da sessão de caixa;
* **Sessão:**Identificador da sessão de caixa (obrigatório);
* **Número do Caixa:** Número da sessão de caixa;
* **Operador:**Código do usuário do operador de sessão de caixa.

**Informações disponíveis**

Os seguintes campos são retornados pelo Objeto de Negócio e podem ser utilizados nos Relatórios, Tabelas Dinâmicas e Visões de Dados:

* **Coligada**: Coligada da sessão de caixa;
* **Nome da Coligada**: Nome da Coligada da sessão de caixa;
* **Código da Filial**: Código Filial da sessão de caixa;
* **Nome da Filial**: Nome Fantasia da Filial da sessão de caixa;
* **Sessão:**Identificador da sessão de caixa;
* **Número do Caixa:** Número da sessão de caixa;
* **Operador:**Código do usuário do operador da sessão de caixa;
* **Nome do Operador:** Nome do operador da sessão de caixa;
* **Data e Hora de Abertura:**Data e hora de abertura da sessão de caixa;
* **Data e Hora de Encerramento:** Data e hora do encerramento da sessão de caixa;
* **Data e Hora da Movimentação:**Data e hora da movimentação;
* **Meio de Pagamento:**Meio de pagamento utilizado;
* **Código da Conta/Caixa:**Código da conta/caixa da sessão de caixa;
* **Nome da Conta/Caixa:**Nome da conta/caixa da sessão de caixa;
* **Operação:**Sequencial da movimentação;
* **Valor:**Valor da movimentação financeira;
* **Número do Documento:**Número do documento do lançamento financeiro;
* **Classificação:**Tipo de movimentação realizada;
* **Código do Cliente/Fornecedor:**Código do cliente/fornecedor do lançamento financeiro;
* **Nome do Cliente/Fornecedor:**Nome fantasia do cliente/fornecedor do lançamento financeiro;
* **Histórico:**Histórico do lançamento financeiro;
* **Data de Vencimento:**Data de vencimento do lançamento financeiro;
* **Data de Baixa:**Data de baixa do lançamento financeiro;
* **Saldo Inicial:**Saldo inicial da sessão de caixa;
* **Ref. Lançamento:**Referência do lançamento do lançamento financeiro;
* **Ref. Baixa:**Referência da baixa;
