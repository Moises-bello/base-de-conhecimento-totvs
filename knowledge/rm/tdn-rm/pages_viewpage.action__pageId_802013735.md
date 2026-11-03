---
content_hash: 9106dc0a3219429b1a37dedc2f0d18bd3b3e0f977865728d07a112e9ee3a9bbe
fetched_at: '2026-06-29T00:11:43.113205+00:00'
page_id: '802013735'
product: rm
source: tdn-rm
title: FOPTRP0007 - Relatório de Recibo de Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=802013735
version: 10
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Relatório Recibo de Férias**
5. **Tabelas utilizadas**

## **01. VERSÕES**

false

**A partir dos patches:**

* 12.1.2402 e Superiores

## **02. V****ISÃO GERAL**

Relatório para emitir os dados do Recibo de Férias

Nesse relatório, temos os seguintes campos nos objetos de negócio disponíveis:

* **Nome do Funcionário**
* **Data de Início do Período aquisitivo**
* **Data final do Período aquisitivo**
* **Data inicio de gozo de férias**
* **Data final de gozo de férias**
* **Dias de Licença Remunerada**
* **Dias de Gozo de Férias**
* **Dias de abono pecuniário**
* **Salário**
* **Cidade da Filial**
* **Cod. Filial**
* **Cód. Agência**
* **Nome da Agência**
* **Cod. banco**
* **Nome do Banco**
* **Numero Conta**
* **Cód. do Evento**
* **Referência**
* **Descrição do Evento**
* **Valor**
* **Tipo de Evento**
* **Total Proventos**
* **Total Descontos**
* **Líquido de Férias**
* **Liquido de Férias (Texto)**
* **Seção**
* **Centro de Custo**
* **Categoria Salarial**
* **Descrição da Função**
* **Código da Função**
* **Data de Pagamento**
* **Código da Seção**
* **Chapa do Funcionário**
* **Cód. Filial**
* **Cód. Coligada**
* **Cód. Centro de Custo**
* ******Situação de Férias******

  Mudanças na segurança do Relatório

  Mudanças na segurança do Relatório

  A partir dos patches 12.1.2606, será necessário aplicar a Tag de segurança para a utilização do relatório, para aplicar basta seguir o caminho abaixo:  
    
  Serviços Globais | Perfil | (Selecione o perfil utilizado para o usuário) | Acesso a Menus | Folha de Pagamento | [01] Administração de Pessoal | [01.04.01] Relatórios | [01.04.01.03] Relatórios SmartView | [01.04.01.03.03] Relatório Recibo de Férias

## **03. EXEMPLO DE UTILIZAÇÃO OBJETO DE NEGOCIO (VISAO DE DADOS)**

No Smart View, após acessarmos a visão de dados e incluirmos uma nova visão. Iremos escolher o Objeto de negócio do Recibo de Férias **( TOTVS Folha de Pagamento - RM | Recibo de Férias )**

Após a confirmação, será necessário preencher os parâmetros obrigatórios, que são:

* **Cód. Coligada (É possível incluir 1 ou mais situações neste parâmetro)**
* **Chapa do Funcionário (É possível incluir 1 ou mais situações neste parâmetro)**
* **Situação de Férias (É possível incluir 1 ou mais situações neste parâmetro)**
* **Data de Início das Férias >=**
* **Data de Início das Férias <=**
* **Data de Pagamento das Férias >=**
* **Data de Pagamento das Férias <=**
* **Cód. Departamento (Cod. Seção)**

DICA

* Caso queira retornar todos os valores, basta incluir -1 nos parâmetros

Para melhor visualização e ramificação dos dados, é possível também incluir filtros na nossa busca, tornando a mais dinâmica possível.  Para isso, basta incluir os filtros clicando em **Alterar filtro** através da **Edição de Filtro.**

## **04. RELATÓRIO RECIBO DE FÉRIAS**

Para a execução do relatório, deveremos preencher necessariamente os parâmetros obrigatórios. Vale lembrar que o relatório leva em consideração os filtros pré-definidos no passo do Objeto de Negócio.  
  
Então, após o preenchimento, o relatório será exibido conforme abaixo:

## **05. TABELAS UTILIZADAS**

* **PFUFERIASPER**
* **PFUNC**
* **PFUFERIAS**
* **GFILIAL**
* **GAGENCIA**
* **GBANCO**
* **PFUFERIASVERBAS**
* **PEVENTO**
* **PFUFERIASRECIBO**
* **PSECAO**
* **PCODRECEB**
* **PCCUSTO**
