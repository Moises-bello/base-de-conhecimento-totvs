---
content_hash: d59e5f8fe15a42cd959a9c645e02ca872f218765bab3e1a6d34b91cd1ba6ab74
fetched_at: '2026-06-29T00:11:43.355431+00:00'
page_id: '804054467'
product: rm
source: tdn-rm
title: FOPTRP0008 - Relatório da Ficha Financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=804054467
version: 7
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Relatório Ficha Financeira**
5. **Tabelas utilizadas**

## **01. VERSÕES**

false

**A partir dos patches:**

* 12.1.2402 e Superiores

## **02. V****ISÃO GERAL**

Relatório para emitir os dados da Ficha Financeira

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
* **Código do Evento:** Retorna o código dos eventos da Ficha Financeira
* **Descrição do Evento:** Retorna a descrição dos eventos da Ficha Financeira
* **Referencia :** Retorna a quantidade relacionada a este evento
* **Hora:** Caso este evento seja do tipo Hora será exibido neste campo
* **Valor:** Retorna o valor do evento
* **Tipo do Evento:** Retorna o tipo de evento (Provento, Desconto ou Base)
* **Data do Pagamento:** Retorna a data em que o evento foi pago

A visualização do relatório será de acordo com o filtro inserido via visão do Smart View, sendo esse filtro incluído pelo usuário. 

## **03. EXEMPLO DE UTILIZAÇÃO OBJETO DE NEGOCIO (VISAO DE DADOS)**

No Smart View, após acessarmos a visão de dados e incluirmos uma nova visão. Iremos escolher o Objeto de negócio da Ficha Financeira / Ficha Financeira Complementar **( TOTVS Folha de Pagamento - RM | Ficha Financeira / Ficha Financeira Complementar ).** Para a utilização do relatório será utilizado o mesmo objeto de negocio da Ficha Financeira Complementar

Mudanças na segurança do Relatório

A partir dos patches 12.1.2606, será necessário aplicar a Tag de segurança para a utilização do relatório, para aplicar basta seguir o caminho abaixo:  
  
Serviços Globais | Perfil | (Selecione o perfil utilizado para o usuário) | Acesso a Menus | Folha de Pagamento | [01] Administração de Pessoal | [01.04.01] Relatórios | [01.04.01.03] Relatórios SmartView | [01.04.01.03.02] Relatório Envelope de Pagamento 

Após a confirmação, será necessário agora preencher os parâmetros obrigatórios, que são:

* **Código da Coligada** (Poderá ser utilizado N Coligadas, basta clicar no icone de adição )
* **Chapa do Funcionário** (Poderá ser utilizado N Chapa de Funcionarios, basta clicar no icone de adição )
* **Ano Inicial**
* **Ano Final**
* **Mês Inicial**
* **Mês Final**
* **Período** (Poderá ser utilizado N periodos, basta clicar no icone de adição )
* **Cod. Seção** (Pode ser utilizado como "Similaridade" Exemplo: Cód. Seção 02 Deverá ser retornado funcionarios da Seção 01.02 / 02 / 02.01 / 03.02 / 04.02 )

DICA

* Caso queira retornar todos os valores, basta incluir -1 nos Parâmetros

Para melhor visualização e ramificação dos dados, é possível também incluir Filtros na nossa busca, tornando a mais dinâmica possível.  Para isso basta incluir os filtros clicando em **Alterar filtro** através da **Edição de Filtro.**

Após acessarmos a funcionalidade de filtros, podemos customizar da melhor maneira para atender nosso objetivo. Sendo permitido a inclusão de um ou mais filtros, podendo escolher os filtros disponíveis bem como na imagem abaixo.

## **04. RELATÓRIO FICHA FINANCEIRA**

Para a execução do relatório deveremos preencher necessariamente os parâmetros obrigatórios, vale lembrar que o relatório leva em consideração os filtros pré-definidos no passo do Objeto de Negócio.  
  
Então, após o preenchimento o relatório será exibido conforme abaixo:

## **05. TABELAS UTILIZADAS**

* GFILIAL
* PSECAO
* PFUNC
* PFFINANC
* PEVENTO
* PFPERFF
