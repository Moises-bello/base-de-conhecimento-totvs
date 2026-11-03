---
content_hash: 7b92346efb2f8c8c54b2462d3b0d11030b400fc7d19f4f3e3cef06dae645db54
fetched_at: '2026-06-29T00:05:53.044244+00:00'
page_id: '1064385907'
product: rm
source: tdn-rm
title: Objeto de Simulador de Rescisão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1064385907
version: 1
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Parâmetros de Entrada (filtros)**
3. **Estrutura de Dados**
4. **Regra de Negócio**
5. **Exemplo de Utilização**
6. **Relatórios que Utilizam esse Objeto de Negócio**

## **01. V****ISÃO GERAL**

O objeto de negócio **Simulador de Rescisão** tem como realizar uma simulação detalhada dos valores de uma rescisão.

* **Módulo:** Folha de Pagamento
* **Time Responsável:** Cálculos - RM

## **02.  PARÂMETROS DE ENTRADA**

Este objeto possui parâmetros e filtros para melhor visibilidade dos dados:

| Parâmetro | Descrição | Comportamento |
| --- | --- | --- |
| Data de Desligamento | Data de Desligamento do Funcionário | Filtra os dados por data de desligamento do funcionário |
| Matricula | Chapa funcionário | Filtra uma matricula especifica |
| Data do Aviso | Data do Aviso | Filtra os dados por data do aviso prévio |
| Usa Aviso | Utilização do Aviso prévio | Filtra os dados por utilização do aviso ou não |

## **03.  Estrutura de Dados**

* companycode = Código da Coligada
* companylogo = Logo da Coligada
* companyname = Nome da Coligada
* cnpj = Cnpj da coligada
* sectioncode = Código da Seção
* sectionname = Código da seção
* functioncode = Código da função
* functionname = Nome da função
* costcentercode = Código do centro de custo
* costcentername = Nome do Código do Centro de Custo
* employeecode = Código da Matricula / Chapa
* employeename = Nome do Funcionário
* admissiondate  = Data de Admissão
* salarybase  = Salário Base
* vacationduedate  = Data de vencimento de férias
* fgtsatbank = Saldo de FGTS
* salary13fractions  = Divisão de 13º
* vactionfractions = Divisão de Férias
* remuneration = Remuneração
* notice = Aviso prévio
* inss = Inss
* salary13 = 13º Salário
* inss13salary = Inss de 13º Salário
* fgts = FGTS
* total = Totalizador
* vacation = Férias
* irrf = IRRF
* irrf13 = IRRF de 13º Salário
* vacationirrf = IRRF de férias
* noticedays = Dias de Aviso de férias
* inssemployer = INSS do Empregador
* inssthirdparty = INSS 13º

## **05. Exemplo de Utilização**

Este objeto é a fonte primária para realizar a Simulação de Rescisão de um funcionário, com principal utilização no relatório de Simulação de Rescisão.
