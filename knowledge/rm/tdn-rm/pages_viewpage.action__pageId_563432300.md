---
content_hash: 941092186ef6f1ac865900bf29247ba3d9e3432f69dba2cf958193e1b6ffe839
fetched_at: '2026-06-29T00:10:50.816533+00:00'
page_id: '563432300'
product: rm
source: tdn-rm
title: Validação de autorizações pendentes para Honorários e Diárias.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=563432300
version: 8
---

**CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela de Elaboração de Contas | Encerramento de Parciais** 
   1. Exemplo de encerramento de uma parcial com o número de lançamentos na conta do paciente maior que o número de autorizações (honorários)
   2. Exemplo de encerramento de uma parcial com o número de lançamentos na conta do paciente igual ao número de autorizações (honorários)
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

No encerramento da parcial é verificado se existem Honorários / Diárias lançados na conta do paciente com autorizações pendentes. Essa validação não impede o encerramento da parcial, são informações de alertas.

## **02. EXEMPLO DE UTILIZAÇÃO**

Para que sejam apresentado as mensagens de alertas no encerramento da conta, o parâmetro "Mostrar Relatório com Mensagem Não Impeditivas" localizado em "Parâmetros Gerais | Faturamento II" deverá está marcado, caso contrario, não será apresentado as mensagens de alertas.

## **03. TELA  ELABORAÇÃO DE CONTAS | Encerramento de Parciais**

**Outras Ações / Ações relacionadas**

**3.1 Exemplo de encerramento de uma parcial com o número de lançamentos na conta do paciente maior que o número de autorizações (honorários):**

Os códigos da mensagem são, respectivamente: código da especialidade, código do grupo de itens e código do item.

Mensagem não impeditiva para encerramento da parcial: "Quantidade de PROCEDIMENTOS COBRADOS maior do que a quantidade de AUTORIZADOS. Código: 10.10.1136".

Como neste exemplo acima o número de Honorários lançados na conta do paciente foi superior as autorizações, sendo assim, as mensagens não impeditivas serão apresentadas.

**3.1 Exemplo de encerramento de uma parcial com o número de lançamentos na conta do paciente igual ao número de autorizações (honorários):**

Neste exemplo acima o número de Honorários lançados na conta do paciente é igual ao numero de autorizações, a parcial será encerrada sem apresentar as mensagens não impeditivas.

**04. TABELAS UTILIZADAS**

* SZATENDAUTORIZ
* SZCENTRALAUTORIZACAO
* SZATENDDIARIAS
* SZATENDHONORARIO
