---
content_hash: ba39db98e07834148c1705093c8db2d480973466b3acab03f836ab8ffd3a3f9e
fetched_at: '2026-06-29T00:10:51.359419+00:00'
page_id: '566489478'
product: rm
source: tdn-rm
title: FISCAL01-13622 DT Parâmetros de Guias ICMS-ST Antecipado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=566489478
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Parâmetros do Gestão Fiscal - ICMS ST |
| Ticket: | FISCAL01-13622 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-13622 |

## **02. SITUAÇÃO/REQUISITO**

 Precisamos de um parâmetro para indicar se as guias de ICMSST Antecipado devem ser geradas individualmente por nota fiscal ou agrupadas. Esse parâmetro precisa ser por Filial uma vez que a regra é definida por cada UF.

## **03. SOLUÇÃO**

Implementação do parâmetro ICMS ST antecipado para geração de guias Nota a Nota ou Agrupado.

O novo parâmetro foi implementado em Visão do Modulo Gestão Fiscal -> Ambiente -> Configuração -> TOTVS Gestão Fiscal -> 03.02 Apuração de Tributos -> 03.02.01 - ICMS -> Apur. ICMS por Filial -> Guias de Recolhimento 2/2 -> campo "Gerar Guias de ICMS-ST Antecipado".
