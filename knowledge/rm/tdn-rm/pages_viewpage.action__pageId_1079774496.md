---
content_hash: 33125eabc9e62ca63d83e4a3ad4039bb015f1d6945d9b3bbe2d4fb5465b05b89
fetched_at: '2026-06-29T00:05:54.395259+00:00'
page_id: '1079774496'
product: rm
source: tdn-rm
title: FOPTRP0036 - Funcionários com Férias Vencidas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1079774496
version: 2
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tabelas utilizadas**

## **01. VERSÕES**

**A partir dos patches:**

+ 12.1.2606 e Superiores

## **02. V****ISÃO GERAL**

O objeto de negócio FopProvisaoFeriasBusinessObject tem como finalidade exibir dados das Férias do Funcionario, sendo utilizado para multi relatórios.  
  
Para mais informações pode ser acessado o link com informações do [Objeto de Negócio](https://tdn.totvs.com/pages/viewpage.action?pageId=1054771562)

#### **Regras de Filtro (Importante)**

Para garantir a performance e a segurança dos dados, o objeto possui uma lógica de filtros obrigatórios:

**Importante - Regras de Preenchimento:** O objeto exige que todos os parâmetros declarados recebam um valor para processar a requisição. Para alternar entre os tipos de filtro, utilize a lógica abaixo:

* **Filtrar por Cod. Seção:** Informe o código da Seção do Funcionário ou então -1 para todos
* **Filtrar por Matrícula:** Preencha com a chapa do funcionário ou -1 para todos.
* **Filtrar por Mês(Obrigatório):** Preencha com o Mês Competência
* **Filtrar por Ano(Obrigatório):** Preencha com o Ano Competência

1. ## **03. EXEMPLO DE UTILIZAÇÃO**

   Visão de Dados

   Visão de dados utilizando o Objeto de Negócios disponibilizado que retorna os dados Provisão de Férias

   Relatório

   Gerando o relatório utilizando o SmartView:

## **04. TABELAS UTILIZADAS**

* PFHSTPROV
* PVALFIX
* PPARAMADICIONAIS
* PFUNC
* PSECAO
* PSECAODADOSINSS
* PSECAOFAPALIQUOTA
* GCOLIGADA
* GFILIAL
