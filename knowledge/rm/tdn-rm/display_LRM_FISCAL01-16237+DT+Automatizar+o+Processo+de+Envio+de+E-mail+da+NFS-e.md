---
content_hash: b6dd8e8a5d1c3c80472239a147ab8d04c93e75abfe168183945da42295c68e49
fetched_at: '2026-06-29T00:11:05.543004+00:00'
page_id: '632301582'
product: rm
source: tdn-rm
title: FISCAL01-16237 DT Automatizar o Processo de Envio de E-mail da NFS-e
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-16237+DT+Automatizar+o+Processo+de+Envio+de+E-mail+da+NFS-e
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Envio da NFS-e por e-mail |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16237 |

## **02. SITUAÇÃO/REQUISITO**

Automatizar o Processo de Envio de E-mail da NFS-e.

Alterar o processo de Consulta de autorização da NFS-e para que ao ser autorizada o e-mail seja enviado conforme as definições dos parâmetros de envio de e-mail (Tipo de Movimento) da NF-e/NFS-e

## **03. SOLUÇÃO**

Foi realizado uma alteração no serviço de consulta de Nota Fiscal de serviço para enviar e-mail, conforme parametrização do tipo de movimento.

A parametrização pode ser realizada em BackOffice | Gestão de Estoque, compras e faturamento | Ambiente | Parâmetros | Gestão de Estoque, compras e faturamento | "Selecionar o tipo do movimento" | Fis - NF-e

É possível parametrizar a **Mensagem** encaminhada, o **Formato do Relatório** e **Tipo de Envio**, este último podendo ser entre os tipos abaixo:

A **Mensagem** pode ser passada conforme o tipo da **Classificação da Mensagem** como **E-mail** no caminho BackOffice | Gestão de Estoque, compras e faturamento | Cadastros | Mais... (Estoque, Compras e Faturamento) |  Tabelas Auxiliares | Mensagens do Sistema

**Disponível na versão 12.1.33**
