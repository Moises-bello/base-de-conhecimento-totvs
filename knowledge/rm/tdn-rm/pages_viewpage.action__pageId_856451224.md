---
content_hash: 508f3ed3dfc8a6ecd6ad5c0c2fc515698a5b255a30f7eab40847226112859b05
fetched_at: '2026-06-29T00:11:54.637189+00:00'
page_id: '856451224'
product: rm
source: tdn-rm
title: DT - Ausência de Refeição no horário Semi-flexível
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=856451224
version: 11
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: |  |
| Segmento: | RH |
| Módulo: | Espelho |
| Função: | Verificando o cálculo das ocorrências AREF |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHJORNRM-6541](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-6541) |

## **02. SITUAÇÃO/REQUISITO**

Validação do cálculo AREF para horário semi-flexivel.

## **03. SOLUÇÃO**

Validação e cálculo da Ausência de refeição

**04. EXEMPLO DE UTILIZAÇÃO**

Este documento tem por objetivo demonstrar o cálculo da ausência de refeição .

11Exemplo 1

Horário: 08:00-12:00-14:00-18:00 

Limite de refeição: 11:00-15:00

Intervalo de Ausência:  12:00-14:00

Funcionário realizou batida dia 06/05/2024 das 14:00-18:00

A batida realizada pelo colaborador não faz interseção com a ausência do limite, desta forma, o sistema irá considerar no cálculo para AREF a ausência de refeição 12:00-14:00

2Exemplo 2

08:00-12:00-14:00-18:00

Horário: 08:00-12:00-14:00-18:00 

Limite de refeição: 11:00-15:00

Intervalo de Ausência:  12:00-14:00

Funcionário realizou batida dia 06/05/2024 das 13:00-18:00

A batida realizada pelo colaborador  faz interseção com a ausência do limite, desta forma, o sistema irá considerar no cálculo para AREF a ausência de refeição 11:00-13:00

3Exemplo 3

Horário: 08:00-12:00-14:00-18:00 

Limite de refeição: 11:00-15:00

Intervalo de Ausência:  12:00-14:00

Funcionário realizou batida dia 06/05/2024 das 08:00-11:30

A batida realizada pelo colaborador não faz interseção com a ausência de refeição.

Para esses casos, o sistema verifica o total de ausência e soma como tempo o qual o funcionário deveria ficar ausente, que nesse exemplo seria 2h, ficando então 13:30+2Horas= 13:30.

4Exemplo 4

Horário: 08:00 -12:00 -13:00 -17:00 

Limite de refeição: 11:00 -15:00

Intervalo de Ausência:  12:00 -13:00

Nesta data, o funcionário registrou duas ausências que coincidem com o limite de horário estipulado para a refeição.

Conforme o log de Cálculo, o limite para a refeição é das 11:00 às 15:00, a ausência planejada do horário é de 01:00 (das 12:00 às 13:00).

Será considerado a ocorrência de ausência de refeição o intervalo que mais se aproxima do tempo planejado de refeição.

Serão considerados os intervalos que estão dentro do limite de início e fim da refeição.

**1º intervalo:** das 11:52 às 13:24, totalizando 1 hora e 32 minutos.

**2º intervalo:** das 13:50 às 15:00, totalizando 1 hora e 10 minutos.

O intervalo das 15:00 às 15:29 será desconsiderado por ultrapassar o limite de refeição.

O 2º intervalo (1:10:00) é o que apresenta o número de horas mais próximo do tempo planejado de 01:00 para a refeição. Portanto, a ausência de refeição será aplicada a este intervalo, e o tempo que exceder será considerado como Atraso ou Saída Antecipada.
