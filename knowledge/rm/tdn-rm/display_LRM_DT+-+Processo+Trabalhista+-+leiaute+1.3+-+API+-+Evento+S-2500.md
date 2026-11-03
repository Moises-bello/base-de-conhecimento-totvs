---
content_hash: a1485afb3385f33f844faeb26467e491970644f2fa72a3a959fc04f8663d108c
fetched_at: '2026-06-29T00:11:56.538693+00:00'
page_id: '867143205'
product: rm
source: tdn-rm
title: DT - Processo Trabalhista - leiaute 1.3 - API - Evento S-2500
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Processo+Trabalhista+-+leiaute+1.3+-+API+-+Evento+S-2500
version: 4
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Gestão de Pessoas |
| Função: | Cadastro do S-2500 |
| País: | Brasil |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHHCM-13431](https://jiraproducao.totvs.com.br/browse/DRHHCM-13431) | [DRHHCM-13683](https://jiraproducao.totvs.com.br/browse/DRHHCM-13683) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2410

## **03.****SITUAÇÃO/REQUISITO**

Atender as implementações referentes ao novo leiaute do eSocial S-1.3, que tem previsão de implantação em ambiente de produção em**02/12/2024.**

## **04. SOLUÇÃO**

Adaptação da API:

| Propriedade | Descrição | Tipo | JSON |
| --- | --- | --- | --- |
| dtAdmRespDir | Data de admissão do trabalhador no empregador de origem | Campo | infoProcesso.ideResp.dtAdmRespDir |
| matRespDir | Matrícula no empregador de origem | Campo | infoProcesso.ideResp.matRespDir |
| infoInterm | Informações relativas ao trabalho intermitente | Grupo | ideTrab.infoContr.ideEstab.infoVlr.idePeriodo.infoInterm |
| dia | Dia do mês efetivamente trabalhado pelo empregado com contrato de trabalho intermitente | Campo | ideTrab.infoContr.ideEstab.infoVlr.idePeriodo.infoInterm.dia |
| hrsTrab | Horas trabalhadas no dia pelo empregado com contrato de trabalho intermitente, no formato HHMM | Campo | ideTrab.infoContr.ideEstab.infoVlr.idePeriodo.infoInterm.hrsTrab |

## **05. DOCUMENTAÇÃO**

**[eSocial versão S-1.3 - Leiautes](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.3/index.html)**
