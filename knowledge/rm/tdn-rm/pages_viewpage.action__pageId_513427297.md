---
content_hash: 05042859b0d54b4a9ca69569c14819725233ad35ab65226a5ff41481f4ddebef
fetched_at: '2026-06-29T00:10:26.174561+00:00'
page_id: '513427297'
product: rm
source: tdn-rm
title: DT Cancelamento de transação com cartão de crédito e débito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=513427297
version: 10
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Totvs Gestão Financeira |
| Função: | Solicitar cancelamento de transação |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | <https://jiraproducao.totvs.com.br/browse/DEDUCONNECT-69> |

## **02. SITUAÇÃO/REQUISITO**

Solicitar o cancelamento da transação de pagamento com cartão de crédito junto ao gateway de pagamento ou adquirente.

## **03. SOLUÇÃO**

Na visão de transações com cartão de crédito/débito, foi criado o processo ***Solicitar o cancelamento de transação***. Esse processo realiza o cancelamento das transações para os modelos de pagamento:

* IFrame GetNet.
* CyberSource
* e-Rede

Este processo somente solicitará o cancelamento da transação com cartão onde o status da transação for "Pagamento Confirmado" ou  "Pagamento Concluído". Ao solicitar o cancelamento da transação o status da transação no TOTVS Gestão Financeira será alterada da seguinte forma:

* CyberSource - para "Pagamento Pendente"
* IFrame Getnet - para "Cancelamento Pendente", onde posteriormente deverá ser executado o processo para "Ajustar transação" para ser atualizado para "Pagamento Cancelado".

**Obs:** Para transações dos modelos CheckOut e BuyPage, caso algum cancelamento for solicitado, o sistema irá apresentar um aviso informando que para esses modelos o cancelamento não é realizado nesse formato pelas adquirente.

* e-Rede - para "Pagamento Cancelado" caso a solicitação do cancelamento seja feito no mesmo dia do pagamento, caso contrário será alterado para "Cancelamento Pendente". Pode ser cadastrado no portal userede a Url que receberá o callback com o status do cancelamento após processado pela Rede, onde será automaticamente alterado o status da transação para "Pagamento Cancelado".URL CALLBACK *{alias}/Corpore.Net/Source/Fin-Financeiro/RM.Fin.Lan/Rede/FinLanCartaoCallback.aspx*

**Configuração:**

O processo de "Cancelar transação com cartão" deve ser habilitado no perfil do usuário.

**ATENÇÃO:**

O modelo de pagamento e cancelamento da  "CyberSource" só será disponibilizado a partir da versão **12.1.28**.
