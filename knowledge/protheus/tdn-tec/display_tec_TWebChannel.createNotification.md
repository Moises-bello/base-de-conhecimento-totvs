---
content_hash: b220f6a301dc3f09ec3d97c0754d3d9d31a314799b0129ddea0264c4e0cd7027
fetched_at: '2026-07-02T19:24:22.578997+00:00'
page_id: '270914828'
product: protheus
source: tdn-tec
title: TWebChannel.createNotification
type: documentation
url: https://tdn.totvs.com/display/tec/TWebChannel.createNotification
version: 2
---

TWebChannel.createNotification

Exibe uma notificação no dispositivo móvel que permite o envio de um Identificador que será enviado ao ADVPL para tratamento pelo bloco de código \*bNotificationTapped\* definido para o componente TMobile. Mais detalhes no exemplo.

## Sintaxe

false )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| options | objeto | Objeto JSON contendo as propriedades necessárias para criação da notificação. Consulte a tabela na área de observações para conhecer as propriedades requeridas. | X |  |

## Observações

Propriedades requeridas pelo objeto JSON do parâmetro "options":

| Identificador | Tipo | Descrição |
| --- | --- | --- |
| ID | Numérico | Código identificador da notificação. |
| Title | Caractere | Texto da mensagem a ser exibida no titulo da notificação. |
| Message | Caractere | Texto da mensagem a ser exibida no corpo da notificação. |

* Função disponível em builds superiores a 7.00.131227A.

## Exemplos

cppEclipsetruefalse

### Preview
