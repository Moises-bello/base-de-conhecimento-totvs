---
content_hash: e22c0a79dbc152f8ec9a6fe2a542afbdf1e159477352a394b331136294401f2f
fetched_at: '2026-06-29T00:11:17.458076+00:00'
page_id: '680955990'
product: rm
source: tdn-rm
title: FISCAL01-17717 - DT - Melhoria de mensagem de erro ao enviar NFS-e sem informar
  código de Classificação de Município da Filial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=680955990
version: 3
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Enviar NFS-e |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17717 |

## **02. SITUAÇÃO/REQUISITO**

Ao realizar o envio de uma NFS-e sem informar o campo Classificação Município nos parâmetros da filial, o processo apresentava uma mensagem de erro técnica que não ajudava o usuário a entender o motivo do erro:

NFS - Incorrect syntax near ')'.

Essa mensagem era exibida pois não havia nenhuma validação do parâmetro de Classificação de Município da filial. Ao executar o processo sem ter esse campo preenchido uma exceção geral era disparada com essa mensagem de erro.

## **03. SOLUÇÃO**

Adicionada uma verificação do parâmetro de Classificação de Município da Filial com a seguinte mensagem de erro sendo exibida quando o mesmo não está preenchido:

> Classificação do Município não informada nos parâmetros da filial.
>
> Acesse BackOffice > Gestão De Estoque > Ambiente >
>
> Parâmetros > Gestão De Estoque > Integrações >
>
> Fiscais > Dados Fiscais > Parâmetros por Filial >
>
> Etapa Ambiente NF-e e informe o campo "Classificação Município"
>
> de acordo com o município em questão.
