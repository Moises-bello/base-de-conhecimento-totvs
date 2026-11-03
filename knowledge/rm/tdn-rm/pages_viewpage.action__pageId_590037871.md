---
content_hash: 01628ee81ec41498a02d00445556a9afe22ffbe5098225e80be61fbe6928b61e
fetched_at: '2026-06-29T00:10:53.937090+00:00'
page_id: '590037871'
product: rm
source: tdn-rm
title: 95209 FISCAL01-175 DT DIRF x COSIRF - MÊS DE GERAÇÃO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=590037871
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | DIRF |
| Ticket: | 95209 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-175 |

## **02. SITUAÇÃO/REQUISITO**

O Cliente solicita que Rotina da DIRF seja gerada conforme a Apuração do Tributo.

O Tributo COSIRF deve ser gerado na Rotina da **DIRF**conforme **"Data de Previsão de Baixa"** informada na pasta "Dados Financeiros" do lançamento fiscal, que foi utilizada na Apuração.

## **03. SOLUÇÃO**

Realizado ajuste no mês de geração dos valores do COSIRF na rotina DIRF, se tratando do tributo COSIRF o mesmo será gerado no mês da **"Data previsão de baixa"** se essa data estiver preenchida, caso essa data não esteja preenchida será considerada a DATALF conforme comportamento anterior.
