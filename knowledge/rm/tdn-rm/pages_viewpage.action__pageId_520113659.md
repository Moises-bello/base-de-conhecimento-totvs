---
content_hash: c614088098a3fd119fb59bb10b3fba7ac739ec66700a65e039b248ec9e64ee7b
fetched_at: '2026-06-29T00:10:30.908279+00:00'
page_id: '520113659'
product: rm
source: tdn-rm
title: Identificação do documento de estoque (Integração Datasul)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520113659
version: 1
---

## 

1. **Visão Geral**
2. **Importante**
3. **Exemplo de utilização**
4. **Mensagem de integração com o Backoffice Datasul com a implementação**

## **01. VISÃO GERAL**

     Este processo possibilita que o sistema registre o identificador da requisição e o identificador do mapa como número do documento da movimentação de estoque no Backoffice EMS / Datasul.

## **02. IMPORTANTE**

Quando utilizado o mapa de dispensação é enviado ao Backoffice o número do documento no formato XXXXX-YYYYY, onde XXXXX representa o identificador da requisição de estoque e o YYYYY representa o identificador do mapa gerado.

Quando utilizada a movimentação de estoque é enviado ao Backoffice o número do documento no formato XXXXX, onde XXXXX representa o identificador da requisição de estoque, assim como é o funcionamento atual do sistema.

Essa implementação é aplicada apenas à clientes que utilizam Backoffice da linha Datasul.

## **03. EXEMPLO DE UTILIZAÇÃO**

**Outras Ações / Ações relacionadas**

| Ação | Descrição |
| --- | --- |
| 1 – Prescrição Médica no Prontuário Eletrônico | Realizar uma prescrição médica na qual ao concluir/liberar a prescrição a mesma tenha horários de aprazamento gerados para o medicamento; |
| 2 – Mapa de Dispensação | Ao selecionar os horários referente ao turno de trabalho, gerar o mapa, confirmar e processar os itens o sistema irá gerar a mensagem de XML conforme descrição da implementação na TAG <DocumentNumber>. |

## **04. MENSAGEM DE INTEGRAÇÃO COM O BACKOFFICE DATASUL COM A IMPLEMENTAÇÃO.**
