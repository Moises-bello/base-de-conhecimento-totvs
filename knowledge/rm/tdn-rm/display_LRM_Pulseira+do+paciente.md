---
content_hash: 458a5cdeee14e7728fd12a35ffb99b1112ffa08b7f8da004708e93bdd3d2fc8d
fetched_at: '2026-06-29T00:12:01.580515+00:00'
page_id: '896372917'
product: rm
source: tdn-rm
title: Pulseira do paciente
type: documentation
url: https://tdn.totvs.com/display/LRM/Pulseira+do+paciente
version: 6
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Parametrização relacionada**
4. **Impressão**
   1. **Ajustes**
   2. **Sugestões**
   3. **Associação**

Pulseira do paciente1. Visão geral

## **01. VISÃO GERAL**

Possibilita ao usuário bipar a pulseira do paciente para abrir automaticamente o prontuário.

2. Exemplo de utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

|  |
| --- |
| Painel - Internação - [https://tdn.totvs.com/display/LRM/Painel+de+Pacientes+Internados](https://tdn.totvs.com/display/LRM/Painel+de+Pacientes+Internados "Seguir link") |
| Painel - Urgência e Emergência - [https://tdn.totvs.com/pages/viewpage.action?pageId=646226744](https://tdn.totvs.com/pages/viewpage.action?pageId=646226744 "Seguir link") |
| Painel - Eletivos - [https://tdn.totvs.com/display/LRM/Painel+de+Eletivos+PEP](https://tdn.totvs.com/display/LRM/Painel+de+Eletivos+PEP "Seguir link") |
| Painel - Plano Terapêutico - [https://tdn.totvs.com/pages/viewpage.action?pageId=721739455](https://tdn.totvs.com/pages/viewpage.action?pageId=721739455 "Seguir link") |
| Painel - Interconsulta - [https://tdn.totvs.com/display/LRM/Painel+de+Interconsulta](https://tdn.totvs.com/display/LRM/Painel+de+Interconsulta "Seguir link") |
| Agenda do dia - [https://tdn.totvs.com/display/LRM/Agenda+PEP+RM](https://tdn.totvs.com/display/LRM/Agenda+PEP+RM "Seguir link") |
| Pacientes - [https://tdn.totvs.com/display/LRM/Listagem+de+Pacientes+PEP+RM](https://tdn.totvs.com/display/LRM/Listagem+de+Pacientes+PEP+RM "Seguir link") |
| Central de Laudos - [https://tdn.totvs.com/display/LRM/Central+de+Laudos](https://tdn.totvs.com/display/LRM/Central+de+Laudos "Seguir link") |

3. Parametrização relacionada

## **03. PARAMETRIZAÇÃO RELACIONADA**

É necessário realizar a configuração do tipo de código de barras utilizado em: RM > Ambiente > Parâmetros > Gestão hospitalar > Registro e Controle > Registro e Controle 7.

**Parâmetros utilizados:**

* Dados do código de barra:  
  Opções:   
  Simples: Código do paciente; Prontuário.  
  Compostas: Código do paciente + Atendimento; Prontuário + Atendimento.
* Tipo do código de barra  
  Opções: EAN13; CODE128; DATAMATRIX.  
  Observação: Ao utilizar a opção EAN13 não será possível utilizar o tipo de código de barra composto.

* Caractere separador   
  Observação: Obrigatório caso utilize tipo de código de barra composto.  
  Sugestão: Uso do traço "-".
4. Impressão

## **04. IMPRESSÃO**

Para realizar a impressão da pulseira do paciente é necessário realizar a importação e configuração do relatório de acordo com os parâmetros selecionados.

Para isso, utilize o relatório SAUREL0026 - Etiqueta de atendimento - Código de Barras.TotvsReport

Após realizar a importação configure o report:

## **a.** **Ajustes:**

* + Selecione o respectivo tipo de código de barras:
  + Ajuste o retorno da query para o tipo de dado selecionado, simples ou composto;

## **b.** **Sugestões:**

* + EAN13 + CodPaciente:  
    SqlServer: RIGHT('000000000000' + CONVERT(VARCHAR, A.CODPACIENTE), 12)  
    Oracle: LPAD(A.CODPACIENTE, 12, '0')
  + EAN13 + Prontuário:  
    SqlServer: RIGHT('000000000000' + CONVERT(VARCHAR, A.PRONTUARIO), 12)  
    Oracle: LPAD(A.PRONTUARIO, 12, '0')
  + Code128 ou DataMatrix e CodPaciente  
    A.CODPACIENTE
  + Code128 ou DataMatrix e Prontuário  
    A.PRONTUARIO
  + Code128 ou DataMatrix e CodPaciente + Atendimento  
    CONCAT(CONCAT(A.CODPACIENTE, '-'), E.CODATENDIMENTO)
  + Code128 ou DataMatrix + Prontuário + Atendimento  
    CONCAT(CONCAT(A.PRONTUARIO, '-'), E.CODATENDIMENTO)

## **c.** **Associação**

Após realização das configurações pode-se realizar a associação do relatório junto ao registro de atendimento do paciente:

RM > Atendimento > Registro de Atendimento > Anexos > Relatórios > Inserir Relatório.

Feito isso será possível realizar a impressão do mesmo e utilizar para bipar dentro do PEP RM.
