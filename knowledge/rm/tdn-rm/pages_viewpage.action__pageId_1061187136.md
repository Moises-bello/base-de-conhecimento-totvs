---
content_hash: 2c8863145cd0e43966bbe48edc4d616b62e869678f872c2db1b16a7f7d647c83
fetched_at: '2026-06-29T00:05:52.892283+00:00'
page_id: '1061187136'
product: rm
source: tdn-rm
title: Objeto de Negócio Relação para Compra de Vale Transporte
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1061187136
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

O objeto de negócio **FopRelacaoCompraVtObjectEntity** tem como finalidade consolidar as necessidades de compra de **Vale Transporte** da coligada. Ele agrupa as solicitações por tipo de tarifa, calculando volumes totais e valores financeiros necessários para o pedido junto às operadoras de transporte.

* **Módulo:** Folha de Pagamento
* **Time Responsável:** Cálculos - RM

## **02.  PARÂMETROS DE ENTRADA**

Este objeto possui filtros para melhor visibilidade dos dados:

| Parâmetro | Descrição | Comportamento |
| --- | --- | --- |
| CPF | CPF funcionário | Filtra dados por um CPF especifico |
| Matrícula | Chapa funcionário | Filtra uma matricula especifica |
| Tarifa | Tarifa do funcionário | Permite filtrar apenas uma tarifa específica |

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
* **WorkingDays:** Dias úteis para o próximo mês;
* **WorkingDaysMonth**: Dias úteis do mês;

**Dados da Tarifa (PTARIFA/PVALETR/PFVALETR):**

* **Farecode:** Código da Tarifa;
* **Faredescription:** Descrição (nome) da Tarifa;
* **FareValue:** Valor da Tarifa;
* **Fares:** Tarifas;
* **CodeLine:** Código da Linha;
* **NumberTravels:** Número de Viagens.

**Dados para campos Calculados:**

* **QuantitySum:** Quantidade geral de tarifas por funcionário;
* **TotalSum:** Valores Totais das tarifas por quantidade.

## **04. Regra de Negócio**

* **Filtro por Chapas Ativas:** Os dados de funcionários apenas são filtrados com a situação 'A'.
* **Filtra as requisições de Vale Transporte dentro do período de referência:** Mês e Ano atual e a vigência das tarifas especificas de cada funcionário.

## **05. Exemplo de Utilização**

Este objeto é a fonte primária para acompanhar o **Valores gerais para compra de Vale Transporte por funcionário**, sendo ideal para:

* **Auditoria de Custos e Trajetos:** Validar as linhas utilizadas, a quantidade de passagens diárias e a coerência entre o endereço residencial e o local de trabalho.
* **Provisão Financeira:** Envio do montante total (Total Geral) para o setor financeiro autorizar a compra de benefícios.

## **06. Relatórios que utilizam esse objeto de negócio**
