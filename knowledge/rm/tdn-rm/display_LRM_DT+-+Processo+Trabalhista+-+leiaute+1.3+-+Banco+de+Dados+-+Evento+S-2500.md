---
content_hash: fd7544890a81f21a75995b10183dc4b4812a63202c102b0712e17a47fb1f83a5
fetched_at: '2026-06-29T00:11:55.815937+00:00'
page_id: '864340360'
product: rm
source: tdn-rm
title: DT - Processo Trabalhista - leiaute 1.3 - Banco de Dados - Evento S-2500
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Processo+Trabalhista+-+leiaute+1.3+-+Banco+de+Dados+-+Evento+S-2500
version: 6
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
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHHCM-13378](https://jiraproducao.totvs.com.br/browse/DRHHCM-13378) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2410

## **03.****SITUAÇÃO/REQUISITO**

Atender as implementações referentes ao novo leiaute do eSocial S-1.3, que tem previsão de implantação em ambiente de produção em**02/12/2024.**

## **04. SOLUÇÃO**

Adaptação do banco de dados:

| Propriedade | Descrição | Tipo | Tabela |
| --- | --- | --- | --- |
| dtAdmRespDir | Data de admissão do trabalhador no empregador de origem | Datetime | VPROCESSOTRABALHISTA.DTADMRESPDIR |
| matRespDir | Matrícula no empregador de origem | String | VPROCESSOTRABALHISTA.MATRESPDIR |
| idInfoInterm | Primary key | Int | VPROCTRABINFOINTERM.IDINFOINTERM |
| dia | Dia do mês efetivamente trabalhado pelo empregado com contrato de trabalho intermitente | Int | VPROCTRABINFOINTERM.DIA |
| hrsTrab | Horas trabalhadas no dia pelo empregado com contrato de trabalho intermitente, no formato HHMM | String | VPROCTRABINFOINTERM.HRSTRAB |
| idPeriodo | Foreing key - Período das bases de cálculo (VPROCTRABPERIODO) | Int | VPROCTRABINFOINTERM.IDPERIODO |

## **05. DOCUMENTAÇÃO**

**[eSocial versão S-1.3 - Leiautes](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.3/index.html)**
