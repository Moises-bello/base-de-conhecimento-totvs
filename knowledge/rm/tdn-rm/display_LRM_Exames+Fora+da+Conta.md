---
content_hash: 8e0c55b7d0ae4498433522d7380edf139a4852563751d15e9316ac6b213e50a7
fetched_at: '2026-06-29T00:10:47.442595+00:00'
page_id: '557332410'
product: rm
source: tdn-rm
title: Exames Fora da Conta
type: documentation
url: https://tdn.totvs.com/display/LRM/Exames+Fora+da+Conta
version: 1
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela Cadastro de Condições Contratuais**
4. **Tela Cadastro de Retorno de Consultas**
5. **Tela de Regras de Lançamentos Dentro ou Fora da Conta**

## **01. VISÃO GERAL**

Esse documento tem como finalidade demostrar a funcionalidade de definir automaticamente quais os exames estão Fora da Conta. Exames Fora da Conta são exames que são realizados dentro do período de retorno configurado no Saúde e é utilizado para evitar as glosas realizadas pelo convênio para cobrir exames dentro do período de retorno.

## **02. EXEMPLO DE UTILIZAÇÃO**

Para **Unidades de Atendimento** que tenham o campo **Validar Retorno de Consulta**e que tenham  nas **Condições Contratuais do Convênio** (anexo: **Retorno Consultas**) a quantidade de dias definidos para retorno da consulta, ao realizar a inclusão de um pedido de exame,  o RM Saúde irá percorrer os registros de pedidos de exames buscando o último exame com mesmo código de procedimento. O processo então irá realizar o cálculo da diferença em dias da data da solicitação atual menos a data da última solicitação do procedimento realizada. Se essa diferença de dias for **menor** do que o **Valor Configurado no anexo Retorno consultas** do convênio essa solicitação de exame será definida como **Exame Fora da Conta**.

Caso o Administrador do RM Saúde veja a necessidade de incluir uma regra mais especifica para um Prestador a rotina irá verificar no cadastro de Regras Dentro Fora se o prestador atual do atendimento está incluso dentro dessa regra sobrepondo dessa maneira o resultado encontrado acima, isso acontece por que as **Regras Dentro Fora** tem maior **peso** na definição de Exames Fora da Conta.

O Administrador do RM Saúde pode realizar incluir filtros adicionais na busca dos últimas solicitações abaixo estão listados os parâmetros que afetam a busca.

* **Valida Retorno de Consulta de Atendimento de Emergência**: Ao desmarcar essa parâmetro nos Parâmetros Gerais o RM Saúde irá incluir os atendimentos de emergência no filtro de busca da última data do procedimento.
* **Considerar contagem de retorno a partir de atendimentos não classificados como retorno:** Ao marcar esse parâmetros no cadastro **Condições Contratuais do Convênio** o RM Saúde irá incluir no filtro de busca de atendimento, somente atendimentos que não são **Retorno**.
* **Considerar como retorno apenas o primeiro atendimento dentro do prazo**: Ao marcar esse parâmetros no cadastro **Condições Contratuais do Convênio** a rotina irá considerar como retorno apenas o primeiro atendimento dentro do prazo.

## **03. TELA CADASTRO DE CONDIÇÕES CONTRATUAIS**

**Outros Cadastros/Condições Contratuais do Convênio**

## **04. TELA****CADASTRO DE RETORNO DE CONSULTA**

**Outros Cadastros/Condições Contratuais do Convênio/Anexos/Retorno Consulta**

## **05. TELA****REGRAS DE LANÇAMENTOS DENTRO OU FORA DA CONTA**

**Outros Cadastros/Regras de Lançamentos Dentro ou Fora da Conta**

]]>
