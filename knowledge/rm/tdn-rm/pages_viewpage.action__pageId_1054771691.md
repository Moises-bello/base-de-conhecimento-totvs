---
content_hash: 0041056529a4dcd71c4b35da108f3556ce6ff247bd45099e244dfd9ee61865b8
fetched_at: '2026-06-29T00:05:51.753070+00:00'
page_id: '1054771691'
product: rm
source: tdn-rm
title: FOPTRP0029 - Declaração de Opção do Vale Transporte
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1054771691
version: 2
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

   O objeto de negócio Declaração de Opção do Vale Transporte tem como finalidade exibir a intenção de utilização de receber o Vale Transporte.   
     
   Para mais informações pode ser acessado o link com informações do [Objeto de Negócio](https://tdn.totvs.com/pages/viewpage.action?pageId=1054771562)

   ## **03. EXEMPLO DE UTILIZAÇÃO**

   Visão de Dados

   Visão de dados utilizando o Objeto de Negócios disponibilizado que retorna os dados Declaração de Opção do Vale Transporte

   Relatório de Empréstimos

   Gerando o relatório utilizando o SmartView:

## **04. TELA VISÃO DE DADOS/RELATÓRIO**

**Principais Campos e Parâmetros**

| Campo | Descrição |
| --- | --- |
| CPF | Neste campo deverá informar um CPF. Caso o usuário queira gerar para todos os CPF's, deverá informar -1 |
| Matrícula | Neste campo deverá informar uma ou mais matrículas de funcionários, clicando em + e adicionando as chapas que deseja retornar os dados referente a Relação de Comprovante de entrega de Vale Transporte. Caso o usuário queira gerar para todas as chapas, deverá informar -1 |
| Deslocamento | Quantidade de passagens de Ida e Volta |
| Valores das Passagens | Valores das passagens utilizadas na Ida e Volta |

## **05. TABELAS UTILIZADAS**

* GCOLIGADA
* GFILIAL
* PFUNC
* PPESSOA
* PTARIFA
* PFVALETR
