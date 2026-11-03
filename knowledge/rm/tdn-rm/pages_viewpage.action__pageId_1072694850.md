---
content_hash: 45efd72acd6391a95b711536cd5f2ecb5d298508ac225f265f3c6469b31f0b0e
fetched_at: '2026-06-29T00:05:53.963615+00:00'
page_id: '1072694850'
product: rm
source: tdn-rm
title: Objeto de Negócio Encargos Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1072694850
version: 5
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Parâmetros de Entrada (filtros)**
3. **Estrutura de Dados**
4. **Regra de Negócio**
5. **Exemplo de Utilização**
6. **Relatórios que Utilizam esse Objeto de Negócio**

## **01. V****ISÃO GERAL**

O objeto de negócio **FopEncargosBusinessObject** tem como finalidade filtrar os encargos por funcionário.

* **Módulo:** Folha de Pagamento
* **Time Responsável:** Cálculos - RM

## **02.  PARÂMETROS DE ENTRADA**

Este relatório não possui parâmetros, mas os campos **Ano Competência** e **Mês Competência** são filtros obrigatórios do Objeto de Negócio. Com isso, qualquer filtro criado nesse Objeto SmartView será necessário o preenchimento desses dois.

## **03.  Estrutura de Dados**

Os dados são mapeados através da entidade **FopEncargosBusinessObjectEntity:**

### Dados da Empresa (GCOLIGADA):

* **CompanyName:** Dados da coligada de origem;
* **CompanyLogo:** Imagem da logo da coligada carregada dinamicamente;
* **CompanyName:** Nome da Coligada;
* **CompanyCode:** Código da Coligada.

### Dados do Funcionário (PFUNC / PPESSOA):

* **EmployeeCode:** Chapa do Funcionário;
* **EmployeeName:** Nome do Funcionário;
* **SectionCode**: Código da Seção;
* **SectionDescription:** Descrição da Seção.

### **Dados do Encargo (PFENCARGO / PENCARGO):**

* **ChargeCode**: Código do encargo;
* **ChargeDescription:** Descrição do Encargo;
* **ChargeValue:** Valor do Encargo;
* **CompetenceYear:** Ano Competência;
* **CompetenceMonth:** Mês Competência.

### **Campos Calculados:**

* **TotalSum:** Total Geral dos Encargos;
* **SubTotal:** SubTotal Encargos por funcionário.

## **04. Regra de Negócio**

* **Obrigatoriedade de Período:** É obrigatório informar o **Ano** e o **Mês** de competência. O sistema não processará a consulta sem esses dados para evitar travamentos por volume excessivo de registros.

## **05. Exemplo de Utilização**

Este objeto de negócio é necessário para o fechamento contábil, sendo ideal para:

* **Auditoria de Encargos:** Validar e conciliar os valores gerados pela Folha de Pagamento por funcionário.

## **06. Relatórios que utilizam esse objeto de negócio**
