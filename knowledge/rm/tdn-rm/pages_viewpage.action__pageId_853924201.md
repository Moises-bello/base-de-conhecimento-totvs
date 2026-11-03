---
content_hash: 0a7b52adcabddf634edbad77da2557260650a8230e74da723f667d26028792f3
fetched_at: '2026-06-29T00:11:54.558319+00:00'
page_id: '853924201'
product: rm
source: tdn-rm
title: DT - Relatório AEJ da Portaria 671 -Adequação registro tipo 07-Ausências e
  Banco de horas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=853924201
version: 17
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Função: | Geração do AEJ para o tipo de registro 07-Ausência considerando descanso conforme a escala horário |
| País: | Brasil |
| Requisito/Story/Issue: | [DRHJORNRM-6535](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-6535) |

## **02. SITUAÇÃO/REQUISITO**

Gerar o relatório AEJ para o registro 07 quando o tipo de ausência for 1-Descanso Semanal Remunerado (DSR) conforme escala do horário do colaborador.

## **03. SOLUÇÃO**

O Relatório AEJ passou a considerar o descanso conforme a Escala do horário.

## **04. VERSÕES**

12.1.2310.231  e superiores.

## **05. CONFIGURAÇÃO**

Realize a  [Configuração para geração do Relatório AEJ](https://tdn.totvs.com/pages/viewpage.action?pageId=705446680#1-2)

## **06. EXEMPLO DE UTILIZAÇÃO**

11Geração do Relatório AEJ para horário com descanso

Funcionário  João esta vinculado ao horário código 0004 com  a seguinte escala de descanso datas  05/05/2024,12/05/2024,19/05/2024 e 26/05/2024.

Gerando o Relatório AEJ

2Geração do Relatório AEJ- Para horário com descanso e batidas 

Quando o  funcionário possui batidas em dia de descanso, será demonstrado o Tipo ausência igual a 1 (DSR) e 3 (Movimento no banco de horas).

Funcionário João esta vinculado ao horário código 0004 com a seguinte escala de descanso datas   05/05/2024,12/05/2024,19/05/2024 e 26/05/2024 e no dia 05/05/2024 teve batidas.

Espelho do funcionário

Gerando o Relatório AEJ Data início 01/05/2024  e Data Fim 05/05/2024

Tipo de registro 07 irá considerar os descansos de acordo o horário e no data da batida será demonstrado o movimento.

## **07. ASSUNTOS RELACIONADOS**

[Relatório AEJ- Portaria 671/2021](https://tdn.totvs.com/pages/viewpage.action?pageId=712490784)
