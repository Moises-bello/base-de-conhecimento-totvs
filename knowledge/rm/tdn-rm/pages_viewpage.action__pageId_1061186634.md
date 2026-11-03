---
content_hash: f7c5ff5053cb659bbfd1b608cda88e87798553323bdc6b73cfd285260cfae03b
fetched_at: '2026-06-29T00:05:52.882846+00:00'
page_id: '1061186634'
product: rm
source: tdn-rm
title: Objeto de Negócio Declaração de Opção de Vale Transporte
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1061186634
version: 2
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Parâmetros de Entrada (filtros)**
3. **Estrutura de Dados**
4. **Regra de Negócio**
5. **Exemplo de Utilização**
6. **Relatórios que Utilizam esse Objeto de Negócio**

## **01. V****ISÃO GERAL**

O objeto de negócio **FopDeclaraOpcaoVtBusinessObject** tem como finalidade registrar a opção do funcionário quanto ao recebimento do benefício de **Vale Transporte**, bem como detalhar o itinerário (residência/trabalho) e os custos envolvidos, em conformidade com a Lei 7.418/1985.

* **Módulo:** Folha de Pagamento
* **Time Responsável:** Cálculos - RM

## **02.  PARÂMETROS DE ENTRADA**

Este objeto possui parâmetros e filtros para melhor visibilidade dos dados:

| Parâmetro | Descrição | Comportamento |
| --- | --- | --- |
| CPF | CPF funcionário | Filtra dados por um CPF especifico |
| Matricula | Chapa funcionário | Filtra uma matricula especifica |
| Deslocamento | Itinerário | Imprime no relatório os sentidos Ida e Volta dos seus respectivos itinerários de deslocamentos |
| Valores das Passagens | Valores Itinerário | Imprime no relatório os valores solicitados pelo funcionário |

## **03.  Estrutura de Dados**

Os dados são mapeados através da entidade **FopResultadoValeTransporteObject:**

### Dados da Empresa (GCOLIGADA):

* **CompanyName / Cnpj:** Dados da coligada de origem;
* **CompanyLogo:** Imagem da logo da coligada carregada dinamicamente;
* **CompanyName:** Nome da Coligada;
* **CompanyCode:** Código da Coligada;
* **NeighborhoodCompany:** Endereço da Coligada (Bairro);
* **NumberCompany:** Endereço da Coligada (Número);
* **Street:** Endereço da Coligada (Rua);
* **City**: Cidade da Coligada;
* **State:** Estado da Coligada.

### Dados do Funcionário (PFUNC / PPESSOA):

* **EmployeeCPF:** CPF do Funcionário;
* **EmployeeCode:** Chapa do Funcionário;
* **EmployeeName:** Nome do Funcionário;
* **EmployeeStreet:** Endereço do Funcionário (Rua);
* **EmployeeNumberAddress:** Endereço do Funcionário (Número);
* **EmployeeNeighborhood:** Endereço do Funcionário (Bairro);
* **EmployeeCity:** Endereço do Funcionário (Cidade);
* **EmployeeState**: Estado do Funcionário.

## **04. Regra de Negócio**

* **Filtro por Chapas Ativas:** Os dados de funcionários apenas são filtrados com a situação 'A'.
* **Filtro de Intervalo de Datas:** Inicio da vigência deve ser maior ou igual à data de referencia do RM.

## **05. Exemplo de Utilização**

Este objeto é a fonte primária para acompanhar o **Controle de Concessão e Custos de Transporte**, sendo ideal para:

* **Auditagem de Custos e Trajetos:** Validar as linhas utilizadas, a quantidade de passagens diárias e a coerência entre o endereço residencial e o local de trabalho.
* **Atualização Cadastral:** Monitorar a validade das declarações de transporte e identificar a necessidade de renovação de itinerários por mudança de domicílio.
* **Centraliza o histórico de decisões do funcionário:** Permite que o RH rastreie alterações de rota que impactam diretamente o custo operacional da empresa e o fluxo de caixa mensal.

## **06. Relatórios que utilizam esse objeto de negócio**

* [FOPTRP0029 - Declaração de Opção do Vale Transporte](https://tdn.totvs.com/pages/viewpage.action?pageId=1054771691)
