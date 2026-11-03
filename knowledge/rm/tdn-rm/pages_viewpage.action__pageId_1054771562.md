---
content_hash: b92f36adf7093b86c078569e711192515bb94557267ae583b39677aa1edb297b
fetched_at: '2026-06-29T00:05:51.748471+00:00'
page_id: '1054771562'
product: rm
source: tdn-rm
title: Objeto de Negócio Declaração de Opção do Vale Transporte
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1054771562
version: 4
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Parâmetros de Entrada (filtros)**
3. **Estrutura de Dados**
4. **Regra de Negócio**
5. **Exemplo de Utilização**
6. **Relatórios que Utilizam esse Objeto de Negócio**

## **01. V****ISÃO GERAL**

O objeto de negócio Declaração de Opção do Vale Transporte tem como finalidade exibir a intenção de utilização de receber o Vale Transporte.

* Módulo: Folha de Pagamento
* Time Responsável: Calculos RM

## **02.  PARÂMETROS DE ENTRADA**

Este objeto possui parâmetros específicos para controlar a profundidade do histórico e a visibilidade de dados sensíveis:

|  |  |  |
| --- | --- | --- |
| CPF | CPF do funcionário | Filtra o funcionário por CPF |
| Matrícula | Matrícula | Filtra os dados por matrículas específicas |
| Deslocamento | Quantidade de passagens Ida e Volta | Exibe a quantidade de passagens utilizadas para Ida e Volta |
| Valores das Passagens | Valores das passagens de Ida e Volta | Exibe os valores das passagens de Ida e Volta |

## **03.  Estrutura de Dados**

Os dados são mapeados através da entidade FopDeclaracaoOpcaoVtBusinessObject:

* EmployeeName: Nome completo do colaborador.
* EmployeeCode: Chapa/Matrícula.
* Employeecpf: CPF
* Cpfwithmask: CPF com mascara usando pontuação para separar
* Employeestreet: Rua ou Avenida
* Employeeneighborhood: Bairro
* Employeecomplement: Complemento
* Employeenumberadress: Numero
* Employeecity: Cidade
* Employeestate: Estado
* Employeectps: CEP
* Employeeworkcardserial: Chapa
* Faredescription: Descrição da Tarifa
* Farevalue: Valor da Tarifa
* Codeline: Codigo da Linha
* Numbertravels: Quantidade de viagens
* Workingdays: Dias trabalhados
* Farecode: Codigo da Tarifa
* Quantidade: Quantidade utilizada
* Totavalue: Valor Total
* Companylogo: Logo da Coligada

## **04. Regra de Negócio**

1. O Objeto de negócio tem como objetivo reunir dados de tarifa e linhas de transporte em um unico lugar para que seja possivel montar diversos relatórios relacionados a Vale-transporte.

## **05. Exemplo de Utilização**

* Este objeto é o componente base para:

  + Gestão de utilização de Vale-Transporte: É possível utilizar o relatório para também entender a quantidade da gastos relacionado a Vale-Transporte
  + Opção de utilização de Vale-Transporte: Utilizado também para verificar a opção ou não de utilização do Vale-Transporte

## **06. Relatórios que utilizam esse objeto de negócio**
