---
content_hash: 48d72f4e00b37c2e3b194f991012e3bb21ecdac4e5ec93dd366f598c1dc23fa8
fetched_at: '2026-06-29T00:10:58.182814+00:00'
page_id: '604509624'
product: rm
source: tdn-rm
title: FISCAL01-13721 DT NFS-e Motivo do Cancelamento - Processo
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-13721+DT+NFS-e+Motivo+do+Cancelamento+-+Processo
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Cancelamento de NFS-e |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-13721 |

## **02. SITUAÇÃO/REQUISITO**

Ao executar o cancelamento de uma NFS-e, seja integrada ao TOTVS Colaboração ou não, a tela referente ao motivo de cancelamento será exibida sempre que o município em questão tiver motivos de cancelamento cadastrado em seu formulário em anexo.

Este comportamento sobrepõe o antigo (somente exibia o formulário para determinados municípios e TOTVS Colaboração).

## **03. SOLUÇÃO**

Foi criado um lookup no wizard de cancelamento da Nota Fiscal de Serviço eletrônica. O processo irá verificar os códigos de motivo de cancelamento, cadastrados no anexo do município do emitente para exibir o formulário e preencher os dados do lookup. Caso o mesmo não possua motivo de cancelamento cadastrado, o formulário não será exibido.
