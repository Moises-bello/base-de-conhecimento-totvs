---
content_hash: 6364cdd35844291e3cbc4538f0d06468f09ea5ec473855f1a9e4111668388456
fetched_at: '2026-06-29T00:11:56.600396+00:00'
page_id: '867162472'
product: rm
source: tdn-rm
title: DT - Dashboard -Agendamento do envio de email com mesmo usuário para mais de
  uma coligada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=867162472
version: 6
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Função: | Atualizado o processo de agendamento do envio de e-mail Dashboard para mais de uma coligada com o mesmo usuário |
| País: | Brasil |
| Requisito/Story/Issue: | [DRHJORNRM-6943](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-6943) |

## **02. SITUAÇÃO/REQUISITO**

O sistema não esta enviando e-mail quando faz agendamento para coligadas diferentes com o mesmo usuário.

## **03. SOLUÇÃO**

Atualizado o processo no envio de e-mail quando o mesmo usuário realiza o agendamento para mais de uma coligada.

O envio de e-mail passou a enviar apenas os campos Data Inicial, Data Final, Última atualização e os indicadores.

## **04. VERSÕES**

Disponível a partir dos patches:

* 12.1.2410 e superiores
* 12.1.2406.157

## **05. EXEMPLO**

## Criado 02(dois) agendamentos através do menu Relatórios|Dashboard|envio de email para as coligadas 1 e 6.

O email foi enviado para ambas as coligadas.

Coligada 1

Coligada 6

## **06. ASSUNTOS RELACIONADOS**

* [Dashboard Envio de E-mail](https://tdn.totvs.com/display/LRM/Dashboard++Ponto)
