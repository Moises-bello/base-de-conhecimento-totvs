---
content_hash: 885c09ad47bdfa770ce89a2913d33ec40607fe61273a308e127048f2fb00219d
fetched_at: '2026-06-29T00:11:55.822789+00:00'
page_id: '864340409'
product: rm
source: tdn-rm
title: DT - Processo Trabalhista - leiaute 1.3 - Banco de Dados - Evento S-2501
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Processo+Trabalhista+-+leiaute+1.3+-+Banco+de+Dados+-+Evento+S-2501
version: 4
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
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHHCM-13379](https://jiraproducao.totvs.com.br/browse/DRHHCM-13379) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2410

## **03.****SITUAÇÃO/REQUISITO**

Atender as implementações referentes ao novo leiaute do eSocial S-1.3, que tem previsão de implantação em ambiente de produção em**02/12/2024.**

## **04. SOLUÇÃO**

Adaptação do banco de dados:

| Propriedade | Descrição | Tipo | Tabela |
| --- | --- | --- | --- |
| ideSeqProc | Número sequencial atribuído pela empresa | Int | VPROCESSOTRIBUTOS.IDESEQPROC |
| vrCR13 | Valor relativo ao Imposto sobre a renda retido na fonte para o código de receita - 13º Salário | Numeric (14, 2) | VPROCTRIBIRRF.VRCR13 |
| vrRendMoleGrave13 | Valor do rendimento isento por ser portador de moléstia grave atestada por laudo médico - 13º salário | Numeric (14, 2) | VPROCTRIBIRRF.VRRENDMOLEGRAVE13 |
| vrRendIsen65Dec | Valor de parcela isenta de aposentadoria para beneficiário de 65 anos ou mais - 13º salário | Numeric (14, 2) | VPROCTRIBIRRF.VRRENDISEN65DEC |
| vrJurosMora13 | Juros de mora recebidos, devidos pelo atraso no pagamento de remuneração por exercício de emprego, cargo ou função - 13º salário | Numeric (14, 2) | VPROCTRIBIRRF.VRJUROSMORA13 |
| vrPrevOficial13 | Valor referente à previdência oficial - 13º salário | Numeric (14, 2) | VPROCTRIBIRRF.VRPREVOFICIAL13 |
| vlrDiarias | Valor relativo a diárias | Numeric (14, 2) | VPROCTRIBIRRF.VLRDIARIAS |
| vlrAjudaCusto | Valor relativo a ajuda de custo | Numeric (14, 2) | VPROCTRIBIRRF.VLRAJUDACUSTO |
| vlrIndResContrato | Valor relativo a indenização e rescisão de contrato, inclusive a título de PDV e acidentes de trabalho | Numeric (14, 2) | VPROCTRIBIRRF.VLRINDRESCONTRATO |
| vlrAbonoPec | Valor relativo ao abono pecuniário | Numeric (14, 2) | VPROCTRIBIRRF.VLRABONOPEC |
| vlrAuxMoradia | Valor relativo ao auxílio moradia | Numeric (14, 2) | VPROCTRIBIRRF.VLRAUXMORADIA |

## **05. DOCUMENTAÇÃO**

**[eSocial versão S-1.3 - Leiautes](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.3/index.html)**
