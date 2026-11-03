---
content_hash: 4fb290aac34a6579ae4ecca107ff936fad9ee2a6a7b9a41ce459e2a9c661905e
fetched_at: '2026-06-29T00:05:51.044080+00:00'
page_id: '1046819891'
product: rm
source: tdn-rm
title: Objeto de Negócio Ficha de Funcionário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1046819891
version: 6
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Parâmetros de Entrada (filtros)**
3. **Estrutura de Dados**
4. **Regra de Negócio**
5. **Exemplo de Utilização**
6. **Relatórios que utilizam esse objeto de negócio**

## **01. V****ISÃO GERAL**

O objeto de negócio FopFichaFuncBusinessObject tem como finalidade a geração da Ficha de Registro de Empregado. Ele consolida em uma única estrutura todos os dados vitais do contrato de trabalho, incluindo dados pessoais, documentos, fotos, histórico salarial, histórico de funções, afastamentos, férias e anotações gerais.

* Módulo: Folha de Pagamento
* Time Responsável: Rotinas
* Diferencial: Possui lógicas de conversão de valor por extenso e tratamento de fotos/logotipos.

## **02.  PARÂMETROS DE ENTRADA**

Este objeto suporta uma filtragem profunda para garantir que o dossiê seja gerado apenas para o público-alvo necessário:

| Parâmetro | Descrição | Comportamento |
| --- | --- | --- |
| Matrícula | Chapa do Funcionário | Filtro principal por código de matrícula. |
| CPF | Documento Pessoal | Permite filtrar um funcionário específico pelo CPF. |
| Seção | Filtro de Elegibilidade | Filtra funcionários alocados em departamentos específicos. |
| Filial | Código da Seção | Filtra os funcionários por uma ou mais filiais. |
| Situação | Status Cadastral | Filtra por Ativos, Rescindidos, etc. |
| Tipo de Funcionário | Categoria | Filtra por tipo (Ex: Normal, Autônomo, Estagiário). |
| Data de Admissão | Filtro Temporal | Retorna funcionários admitidos a partir da data informada. |

## **03.  Estrutura de Dados**

### Informações Principais

* EmployeeCode / EmployeeName: Dados básicos de identificação.
* Salary / SalaryInFull: Valor do salário atual e sua conversão automática para extenso (Ex: "Dois Mil e Quinhentos Reais").
* CompanyLogo / Photo: Imagens da empresa e a foto do funcionário vinculada ao cadastro (GIMAGEM).
* FatherName / MotherName: Nomes de pai e mãe recuperados via subquery do cadastro de dependentes.

### Históricos (Sub-listas)

Para permitir uma documentação completa, o objeto carrega as seguintes coleções de históricos:

* SalaryHistory: Alterações salariais com data e motivo (PFHSTSAL).
* FunctionHistory: Mudanças de cargo/função (PFHSTFCO).
* DepartmentHistory: Transferências entre seções (PFHSTSEC).
* Vacations: Períodos aquisitivos e de gozo de férias (PFUFERIAS).
* Absences: Histórico de afastamentos e licenças (PFHSTAFT).
* AddressHistory: Mudanças de endereço do colaborador (PFHSTEND).
* TradeUnionTaxes: Registro de contribuições sindicais (PFHSTCSD).
* Notes: Anotações gerais e ocorrências do prontuário (PANOTAC).

## **04. Regra de Negócio**

1. Compatibilidade entre Bancos: O objeto utiliza tratativas distintas para subqueries (Pai/Mãe) entre SQL Server (TOP 1) e Oracle (ROWNUM = 1).

* Gerencia dinamicamente conforme o dialeto do banco de dados.

2. Tratamento de Parentesco: Na listagem de dependentes do dossiê, o sistema exclui automaticamente os registros de Grau de Parentesco 6 (Pai) e 7 (Mãe) da lista geral, pois estes já são mapeados nos campos fixos do cabeçalho.
3. Conversão de Moeda: Utiliza o componente RMSExtenso para transformar o valor numérico do salário em texto descritivo para fins contratuais.
4. Mapeamento de Foto: Diferente de outros objetos, este realiza o JOIN com a GIMAGEM em nível de pessoa (PPESSOA.IDIMAGEM) para carregar a foto do perfil do colaborador.

## **05. Exemplo de Utilização**

Este objeto é a base indispensável para:

* Ficha de Registro Obrigatória: Documento exigido pela fiscalização do trabalho.
* Dossiê de RH: Documento completo para consulta rápida de gestores.
* Integrações de Onboarding: Exportação de dados completos para sistemas parceiros de benefícios ou treinamento.

## **06.****Relatórios que utilizam esse objeto de negócio**

* [FOPTRP0025 - Ficha Salário Família](https://tdn.totvs.com/pages/viewpage.action?pageId=1041761574)
* [FOPTRP0022 - Ficha de Registro do Funcionário](https://tdn.totvs.com/pages/viewpage.action?pageId=1010795528)
* [FOPTRP0032 - Contrato de Teletrabalho](https://tdn.totvs.com/display/LRM/FOPTRP0032+-+Contrato+de+Teletrabalho)
