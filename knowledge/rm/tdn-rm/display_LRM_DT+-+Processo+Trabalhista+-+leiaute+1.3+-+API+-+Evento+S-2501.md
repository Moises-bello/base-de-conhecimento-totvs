---
content_hash: 0bb5af982af305cda3a8779b7256b22585920ded7447b9e8b569d48ea7cf82ab
fetched_at: '2026-06-29T00:11:56.546267+00:00'
page_id: '867144040'
product: rm
source: tdn-rm
title: DT - Processo Trabalhista - leiaute 1.3 - API - Evento S-2501
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Processo+Trabalhista+-+leiaute+1.3+-+API+-+Evento+S-2501
version: 2
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Gestão de Pessoas |
| Função: | Cadastro do S-2501 |
| País: | Brasil |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHHCM-13432](https://jiraproducao.totvs.com.br/browse/DRHHCM-13432) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2410

## **03.****SITUAÇÃO/REQUISITO**

Atender as implementações referentes ao novo leiaute do eSocial S-1.3, que tem previsão de implantação em ambiente de produção em**02/12/2024.**

## **04. SOLUÇÃO**

Adaptação da API:

| Propriedade | Descrição | Tipo | JSON |
| --- | --- | --- | --- |
| hasS2555 | Retorna se evento possui ou não evento S-2555 correspondente | Campo | has2555 |
| ideSeqProc | Número sequencial atribuído pela empresa | Campo | ideProc.ideSeqProc |
| vrCR13 | Valor relativo ao Imposto sobre a renda retido na fonte para o código de receita - 13º Salário | Campo | ideTrab.infoCRIRRF.vrCR13 |
| vrRendMoleGrave13 | Valor do rendimento isento por ser portador de moléstia grave atestada por laudo médico - 13º salário | Campo | ideTrab.infoCRIRRF.infoIR.vrRendMoleGrave13 |
| vrRendIsen65Dec | Valor de parcela isenta de aposentadoria para beneficiário de 65 anos ou mais - 13º salário | Campo | ideTrab.infoCRIRRF.infoIR.vrRendIsen65Dec |
| vrJurosMora13 | Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função - 13º salário | Campo | ideTrab.infoCRIRRF.infoIR.vrJurosMora13 |
| vrPrevOficial13 | Valor referente à previdência oficial - 13º salário | Campo | ideTrab.infoCRIRRF.infoIR.vrPrevOficial13 |
| rendIsen0561 | Rendimentos Isentos exclusivos do CR 0561 | Grupo | ideTrab.infoCRIRRF.infoIR.rendIsen0561 |
| vlrDiarias | Valor relativo a diárias | Campo | ideTrab.infoCRIRRF.infoIR.rendIsen0561.vlrDiarias |
| vlrAjudaCusto | Valor relativo a ajuda de custo | Campo | ideTrab.infoCRIRRF.infoIR.rendIsen0561.vlrAjudaCusto |
| vlrIndResContrato | Valor relativo a indenização e rescisão de contrato, inclusive a título de PDV e acidentes de trabalho | Campo | ideTrab.infoCRIRRF.infoIR.rendIsen0561.vlrIndResContrato |
| vlrAbonoPec | Valor relativo ao abono pecuniário | Campo | ideTrab.infoCRIRRF.infoIR.rendIsen0561.vlrAbonoPec |
| vlrAuxMoradia | Valor relativo ao auxílio moradia | Campo | ideTrab.infoCRIRRF.infoIR.rendIsen0561.vlrAuxMoradia |

## **05. DOCUMENTAÇÃO**

**[eSocial versão S-1.3 - Leiautes](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.3/index.html)**
