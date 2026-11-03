---
content_hash: 23589d5447bf3b9352c3b3c56b8764b947e12cd0ebe00e95dc1ac7b694249a0c
fetched_at: '2026-06-29T00:11:20.572793+00:00'
page_id: '687154015'
product: rm
source: tdn-rm
title: Lançar CAT e ou afastamento pela previdência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=687154015
version: 4
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. ****Tela Cálculo de Produção Agrária****
   1. **Principais Campos e Parâmetro**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Nesse parâmetro será calculada a produção em dias que houve afastamento do funcionário.

A regra de cálculo da Tarefa agrária pode estar configurada como segue abaixo:

* A finalidade deverá ter o campo “Tarefa de Produção” desmarcado;
* O campo ***“Tipo de cálculo”*** deverá ter sido marcado a opção “Depende de outras Tarefas”;
* A prioridade de cálculo deverá ser maior que as Tarefas produção;
* O campo “Validar quantidade de Diária” e “Incide no Cálculo do Homem-Dia” pode estar marcado ou não.
* O campo “Complemento de Diária Mínima” deve estar marcado.

No caso acima será verificado nos dias em que não há produção para o tipo de cálculo “Depende de outras tarefas”, ou seja, do 2º ao 15º dia devidos pela empresa para que seja pago o mínimo de diária.

**Observações:**

01 - A prioridade da tarefa de complemento de afastamento deve ser menor que a prioridade da tarefa de complemento de diária porque o afastamento deve ser calculado primeiro. Caso contrário corre-se o risco de pagar complemento de diária no lugar do complemento de afastamento.

02 - Não deve marcar complemento de diária no complemento de afastamento.

03 – Caso não exista tarefa de produção para lançamento do complemento no dia do afastamento serão utilizados os valores default parametrizados para Unidade Agrária, Fração Agrária e Programação em Parametrizador / Folha Agrária / Parâmetros da filial / Valores Default

## **02. EXEMPLO DE UTILIZAÇÃO**

Funcionário afastado por mais de 15 dias a partir do dia 20/05/2021 e não teve tarefa de produção no dia do afastamento. O cálculo considera a regra da tarefa que tem o retorno zerado e depois calcula o mínimo da diária.

    Dia quinta-feira, 20 de maio de 2021:

        Tarefa: 90028 - AUX ACIDENTE DO TRABALHO **Regra: 6 - DEPENDE DE OUTRAS TAREFAS - Prioridade: 999**

        Programa: 1 Unidade: 01 Fração: 1 Finalidade: 03 Tipo: Empreita Evento: 0215

        Preço Unitário: 0,0000 Somátorio das produções de prioridades menor a 999 ou prioridades não informada

**Valor Ganho de 0 não foi alterado. Preço unitário zerado**

        Tarefa: 00004 - TAREFA MINIMO DIÁRIA **Regra: 4 - MINIMO DIÁRIA** - Prioridade: 5

        Programa: 1 Unidade: 01 Fração: 1 Finalidade: 04 Tipo: Empreita Evento:

        (Salario / jornada Mensal ) = Preço Unitário Mínimo Diária.

        (1.900,76 / 220,00 ) = 8,6398

        (Quantidade \* Preço Unitário) = Valor Ganho

        (1,0000 \* 8,6398) = 8,6400

        Calculo do complemento de Produção. Diária Mínima - Valor obtido  = Valor a Complementar

        (8,6400 - 0,0000) = 8,6400

        Tarefa atualizada na produção.

## **03.** **TELA Cálculo de Produção Agrária**

**Principais Campos e Parâmetro**

| Campo | Descrição |
| --- | --- |
| Quebra de Seção | Selecione a quebra de seção |
| Seleção de Funcionários | Filtrar funcionários |
| Período | Período para o cálculo |
| Parâmetro | Lançar CAT e ou afastamento pela previdência |

## **04. TABELAS UTILIZADAS**

* + PPRODUCAOAGRARIA
