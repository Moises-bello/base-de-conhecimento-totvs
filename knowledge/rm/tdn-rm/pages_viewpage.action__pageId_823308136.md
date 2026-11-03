---
content_hash: 81a2aeb6319179b15c9f8376c5f09475fa9c94f612fe609f046cab9c6a204481
fetched_at: '2026-06-29T00:11:46.616455+00:00'
page_id: '823308136'
product: rm
source: tdn-rm
title: FOPTRP0013 - Relatório do Recibo de Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=823308136
version: 15
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Relatório Recibo de Pagamento**
5. **Tabelas utilizadas**

## **01. VERSÕES**

false

**A partir dos patches:**

* 12.1.2402 e Superiores

**Observação:** A mensagem referente a MP 1.292 - Programa Crédito do Trabalhador, disponível somente na 12.1.2406 e superiores.

**(Portal)**Para utilização do relatório de recibo de pagamento no Portal, utilizar o relatório  
  
**FOPTRP0013 - Recibo de Pagamento (Portal)**

## **02. V****ISÃO GERAL**

Relatório para emitir os dados do recibo de pagamento.

Nesse relatório temos os seguintes campos nos objetos de negócio disponíveis:

* **Chapa**: Retorna a chapa do funcionário
* **Nome do Funcionário:** Retorna o nome do Funcionário
* **Função:**Retorna a função atrelada ao funcionário
* **Salário:** Retorna o salário do funcionário
* **Situação:** Retorna a situação do funcionário
* **Data de Admissão:** Retorna a data de admissão do funcionário
* **Data de Demissão:** Retorna a data de demissão do funcionário
* **Ano Competência:** Retorna o ano competência da Ficha Financeira Complementar
* **Mês Competência:** Retorna o mês competência da Ficha Financeira Complementar
* **Período:** Retorna o período da Ficha Financeira Complementar
* **Base INSS:** Retorna a Base do INSS que está na Ficha Financeira
* **Base FGTS:** Retorna a Base do FGTS que está na Ficha Financeira
* **Base FGTS 13:** Retorna a Base do FGTS do décimo terceiro salário que está na Ficha Financeira
* **Codigo do Evento:** Retorna o código dos eventos da Ficha Financeira
* **Descrição do Evento:** Retorna a descrição dos eventos da Ficha Financeira
* **Referencia :** Retorna a quantidade relacionada a este evento
* **Hora:** Caso este evento seja do tipo Hora será exibido neste campo
* **Valor:** Retorna o valor do evento
* **Tipo do Evento:** Retorna o tipo de evento (Provento, Desconto ou Base)
* **Data do Pagamento:** Retorna a data em que o evento foi pago
* **Nome da Empresa:** Retorna o nome da Coligada
* **CNPJ da Empresa:** Retorna o CNPJ da Empresa
* **Nome Social do Funcionário:** Retorna o Nome Social do Funcionário (Caso o mesmo não possua)
* **CPF:** Retorna o CPF do Funcionário
* **Banco:** Retorna o Código do banco de pagamento do Funcionário
* **Nome do Banco:** Retorna o Nome do banco de pagamento do Funcionário
* **Agencia:** Retorna a Agencia de pagamento do Funcionário
* **Conta:** Retorna a Conta de pagamento do Funcionário
* **IR PLR (Anual):** Retorna a quantia do IR PLR do ano todo
* **Mensagem:** É exibido uma mensagem custodiável

A visualização do relatório será de acordo com o filtro inserido via visão do Smart View, sendo esse filtro incluído pelo usuário. 

## **03. EXEMPLO DE UTILIZAÇÃO OBJETO DE NEGOCIO (VISAO DE DADOS)**

No Smart View, após acessarmos a visão de dados e incluirmos uma nova visão. Iremos escolher o Objeto de negócio da Ficha Financeira complementar **( TOTVS Folha de Pagamento - RM | Ficha Financeira / Ficha Financeira Complementar )**

Mudanças na segurança do Relatório

A partir dos patches 12.1.2606, será necessário aplicar a Tag de segurança para a utilização do relatório, para aplicar basta seguir o caminho abaixo:  
  
Serviços Globais | Perfil | (Selecione o perfil utilizado para o usuário) | Acesso a Menus | Folha de Pagamento | [01] Administração de Pessoal | [01.04.01] Relatórios | [01.04.01.03] Relatórios SmartView | [01.04.01.03.02] Relatório Envelope de Pagamento 

Após a confirmação, será necessário preencher os parâmetros obrigatórios, que são:

* **Chapa do Funcionário** (Poderá ser utilizado N Chapa de Funcionários, basta clicar no ícone de adição )
* **Ano Inicial**
* **Ano Final**
* **Mês Inicial**
* **Mês Final**
* **Período** (Poderá ser utilizado N períodos, basta clicar no ícone de adição )
* **Cod. Seção** (Pode ser utilizado como "Similaridade" Exemplo: Cód. Seção 02 Deverá ser retornado funcionários da Seção 01.02 / 02 / 02.01 / 03.02 / 04.02 )

DICA

* Caso queira retornar todos os valores, basta incluir -1 nos Parâmetros

Para melhor visualização e ramificação dos dados, é possível também incluir Filtros na nossa busca, tornando a mais dinâmica possível.  Para isso basta incluir os filtros clicando em **Alterar filtro** através da **Edição de Filtro.**

Após acessarmos a funcionalidade de filtros, podemos customizar da melhor maneira para atender nosso objetivo. Sendo permitido a inclusão de um ou mais filtros, podendo escolher os filtros disponíveis bem como na imagem abaixo.

## **04. RELATÓRIO RECIBO DE PAGAMENTO**

Para a execução do relatório deveremos preencher necessariamente os parâmetros obrigatórios, vale lembrar que o relatório leva em consideração os filtros pré-definidos no passo do Objeto de Negócio.  
  
Então, após o preenchimento o relatório será exibido conforme abaixo:

A partir da MP 1.292 - Programa Crédito do Trabalhador, quando houver insuficiência de saldo para desconto das parcelas de empréstimo tomadas pelo funcionário, será gerada no final do recibo a seguinte mensagem: "ATENÇÃO TRABALHADOR! Não foi possível realizar o desconto total ou parcial do seu empréstimo consignado, por exceder o percentual (35%) da remuneração disponível prevista na lei nº10.820/2003 e Portaria MTE nº 435/2025. Procure sua instituição financeira para regularizar o pagamento desse empréstimo."

## **05. TABELAS UTILIZADAS**

* GFILIAL
* PSECAO
* PFUNC
* PFFINANC
* PEVENTO
* PFPERFF
