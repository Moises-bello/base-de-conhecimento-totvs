---
content_hash: cb6e93f35f1f9fc5c56b4ec59bad821c02523c7e250f242446f8b71e5915878e
fetched_at: '2026-06-29T00:10:56.724308+00:00'
page_id: '592759685'
product: rm
source: tdn-rm
title: Horas Falta Jornada - Configurar jornada planejada
type: documentation
url: https://tdn.totvs.com/display/LRM/Horas+Falta+Jornada+-+Configurar+jornada+planejada
version: 3
---

## Parâmetro: "Horas Falta Jornada".

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | RH |
| Módulo: | Automação de Ponto |
| Função: | Parâmetro do cadastro de horário |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | PONTO01-10893 - Criação de controle de horas faltas por jornada |

## **02. SITUAÇÃO/REQUISITO**

Este parâmetro foi criado, para informar o número de horas das faltas calculadas por jornada, e será considerado no sistema folha de pagamento (RM Labore) no campo

FRACAODIAFALTA da tabela PFHSTFALTA dividido pelo campo HORASFALTA considerado no cadastro da jornada da falta.

        Ele será utilizado para o cálculo de avos da folha de pagamento.

Exemplo: na jornada do dia 1 possui informação de horas faltas jornada 8,66 (8:40) e horas faltas 7,33 (07:20) o valor a ser preenchido no campo seria 8,66 / 7,33 = 1,18.

Maiores informações veja:  [Visualização da jornada planejada](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719128)
