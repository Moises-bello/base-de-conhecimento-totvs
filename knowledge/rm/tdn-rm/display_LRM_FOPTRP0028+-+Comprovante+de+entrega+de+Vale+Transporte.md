---
content_hash: 0ca68b812780f9a67d4a186d89ae07d333cc4018372978cb31666e70ad2b67d7
fetched_at: '2026-06-29T00:05:51.531037+00:00'
page_id: '1050875411'
product: rm
source: tdn-rm
title: FOPTRP0028 - Comprovante de entrega de Vale Transporte
type: documentation
url: https://tdn.totvs.com/display/LRM/FOPTRP0028+-+Comprovante+de+entrega+de+Vale+Transporte
version: 3
---

## **CONTEÚDO**

1. 1. **Versão**
   2. **Visão Geral**
   3. **Exemplo de utilização**
   4. **Tela Visão de Dados/Relatório**
      1. **Principais Campos e Parâmetros**
   5. **Tabelas utilizadas**

   ## **01. VERSÃO**

   O Recurso estará disponível a partir das versões abaixo:

   * 12.1.2606 e superiores

   ## **02. VISÃO GERAL**

   O objeto de negócio e relatório de Comprovante de entrega de Vale Transporte têm como objetivo entregar para o usuário uma previsibilidade de custos em relação a Comprovante de entrega de Vale Transportes.

   Tanto a geração do relatório quanto a visão de dados podem ser feitas utilizando parâmetros pré-definidos, como **CPF, Matrícula e Código da Tarifa**.

   Abaixo os campos disponíveis no objeto de negócio e as regras de como os dados são obtidos.

   | Nome | Descrição | Campo na Tabela do RM |
   | --- | --- | --- |
   | Chapa | String | PFVALETR.CHAPA |
   | Nome do Funcionário | String | PPESSOA.NOME |
   | Descrição da Tarifa | String | PTARIFA.DESCRICAO |
   | Valor da Tarifa | Number | PTARIFA.VALOR |
   | Código da Linha | String | PFVALETR.CODLINHA |
   | Numero de Viagens | Number | PFVALETR.NROVIAGENS |
   | Dias úteis no proximo mes | Number | PFUNC.DIASUTPROXMES |
   | Código da Tarifa | String | PVALETR.CODTARIFA |
   | CPF | String | PPESSOA.CPF |
   | Quantidade | Number | PFVALETR.NROVIAGENS \* PFUNC.DIASUTPROXMES |
   | Valor Total | Number | Valor Somado |
   | Soma Total | Number | Valor Somado |
   | Quantidade Total | Number | Valor Somado |
   | Quantidade de Funcionario | Inteiro | Valor Somado |
   | Logo da Coligada | String | GCOLIGADA.IDIMAGEM |

   **Dica**

   Nem todos os campos do objeto de negócios serão utilizados ou visualizados no relatório disponibilizado pela TOTVS. Alguns campos servirão para parâmetros/filtros. Outros foram disponibilizados para facilitar para o usuário caso o mesmo queira customizar algum relatório com estes dados sem a necessidade de customizar por fórmulas por exemplo.

   ## **03. EXEMPLO DE UTILIZAÇÃO**

   Visão de Dados

   Visão de dados utilizando o Objeto de Negócios disponibilizado que retorna os dados da Relação para Comprovante de entrega de Vale Transporte

   Relatório de Empréstimos

   Gerando o relatório utilizando o SmartView:

## **04. TELA VISÃO DE DADOS/RELATÓRIO**

**Principais Campos e Parâmetros**

| Campo | Descrição |
| --- | --- |
| CPF | Neste campo deverá informar um CPF. Caso o usuário queira gerar para todos os CPF's, deverá informar -1 |
| Matrícula | Neste campo deverá informar uma ou mais matrículas de funcionários, clicando em + e adicionando as chapas que deseja retornar os dados referente a Relação de Comprovante de entrega de Vale Transporte. Caso o usuário queira gerar para todas as chapas, deverá informar -1 |
| Cód. Tarifa | Neste campo deverá informar um ou mais Códigos de Tarifas validos, clicando em + e adicionando os Cod. Tarifa que deseja retornar os dados referente a Relação de Comprovante de entrega de Vale Transporte. Caso o usuário queira gerar para todos os Códigos de Tarifas, deverá informar -1 |

## **05. TABELAS UTILIZADAS**

* GCOLIGADA
* GFILIAL
* PFUNC
* PPESSOA
* PTARIFA
* PFVALETR
