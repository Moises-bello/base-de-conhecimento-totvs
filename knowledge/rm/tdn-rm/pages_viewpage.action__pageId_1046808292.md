---
content_hash: c6fa27c240d21e84687249082cb82c4b67b4b99df687231cde9e1ba86b609cb9
fetched_at: '2026-06-29T00:05:51.004492+00:00'
page_id: '1046808292'
product: rm
source: tdn-rm
title: Objeto de Negócio Dependentes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1046808292
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

O objeto de negócio FopDependentesBusinessObject tem como objetivo fornecer uma visão consolidada dos dados cadastrais dos funcionários vinculados aos seus respectivos dependentes. Ele é utilizado principalmente para relatórios de conferência de benefícios, auditoria de encargos (IRRF/Salário Família) e dossiês cadastrais que exijam informações de endereço e identificação visual da coligada.

* Módulo: Folha de Pagamento
* Time Responsável: Rotinas
* Categoria: Cadastral

## **02.  PARÂMETROS DE ENTRADA**

Ao utilizar este objeto no Smart View, os seguintes filtros podem ser aplicados para refinar os dados:

| Parâmetro | Descrição | Comportamento |
| --- | --- | --- |
| Coligada | Código da Empresa | Filtra os dados por uma ou mais coligadas selecionadas. |
| Matrícula | Chapa do Funcionário | Permite a seleção individual ou em lista de funcionários específicos. |
| Seção | Código da Seção | Filtra funcionários alocados em departamentos/seções específicas. |
| Situação | Status do Funcionário | Filtra por Ativos, Rescindidos, Afastados, etc. |
| Data de admissão/demissão. | Período de Início/Fim | Retorna funcionários admitidos dentro do intervalo selecionado. |
| Imprime sem dependente | Opção Sim/Não | Defina se funcionários que não possuem dependentes cadastrados devem aparecer na lista. |

## **03. Estrutura de Dados**

### Dados da Empresa (GCOLIGADA)

* CompanyCode: Código da coligada.
* CompanyName: Nome fantasia da empresa.
* CNPJ: Cadastro Nacional da Pessoa Jurídica.
* CompanyLogo: Logotipo da empresa (formato de imagem/byte).
* Endereço da Empresa: Logradouro, Número, Bairro, Cidade e CEP.

### Dados do Funcionário (PFUNC / PPESSOA)

* EmployeeCode: Chapa do colaborador.
* EmployeeName: Nome completo do funcionário.
* Department: Descrição da seção/departamento.
* EmployeeCpf / EmployeeRg: Documentos de identificação.
* EmployeeCtps / Serie: Dados da Carteira de Trabalho.
* Endereço do Funcionário: Logradouro, Número, Bairro, Cidade e CEP.

### Dados dos Dependentes (PFDEPEND)

* DependentNumber: Número sequencial do dependente.
* DependentName: Nome completo do dependente.
* Relationship: Grau de parentesco (conforme cadastro em PCODPARENT).
* DateOfBirth: Data de nascimento do dependente.
* Cpf: Cadastro de Pessoa Física do dependente.

## **04. Regra de Negócio**

Para garantir a integridade dos dados, este objeto aplica as seguintes regras automáticas:

1. Incidência de IRRF: Por padrão, o objeto filtra dependentes que possuem a flag de incidência de IRRF ativa (INCIRRF = 1), garantindo que apenas dependentes legais para fins fiscais sejam listados em contextos de conferência.
2. Compatibilidade de Banco de Dados: A consulta é otimizada para ambientes SQL Server (utilizando leituras não bloqueantes - *NoLock*) e Oracle (respeitando as regras rigorosas de agrupamento de dados).
3. Tratamento de Endereços: Os campos de Número e Bairro são tratados de forma individualizada, permitindo uma formatação de etiquetas e correspondências mais precisa.
4. Logotipo Dinâmico: O campo CompanyLogo busca automaticamente a imagem vinculada ao cadastro da coligada (GIMAGEM), permitindo a personalização visual imediata do relatório.

## **05. Exemplo de Utilização**

Este objeto é a fonte primária para o relatório de Relação de Dependentes por Funcionário, sendo ideal para:

* Conferência de documentação pendente.
* Geração de listas para concessão de benefícios.
* Auditoria de informações para o eSocial.

## **06. Relatórios que utilizam esse objeto de negócio**

* [FOPTRP0026 - Termo de Responsabilidade para Concessão de Salário Família](https://tdn.totvs.com/pages/viewpage.action?pageId=1048505236)
