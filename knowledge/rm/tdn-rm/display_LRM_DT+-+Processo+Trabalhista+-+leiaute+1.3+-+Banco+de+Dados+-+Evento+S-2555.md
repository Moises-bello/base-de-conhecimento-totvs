---
content_hash: b74d87b86a9cc35c2a8a0df8a2c924ee05b7339895cf4f5b50d4fa5563448a0a
fetched_at: '2026-06-29T00:11:55.829261+00:00'
page_id: '864340429'
product: rm
source: tdn-rm
title: DT - Processo Trabalhista - leiaute 1.3 - Banco de Dados - Evento S-2555
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Processo+Trabalhista+-+leiaute+1.3+-+Banco+de+Dados+-+Evento+S-2555
version: 3
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Gestão de Pessoas |
| Função: | Cadastro do S-2555 |
| País: | Brasil |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHHCM-13411](https://jiraproducao.totvs.com.br/browse/DRHHCM-13411) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2410

## **03.****SITUAÇÃO/REQUISITO**

Atender as implementações referentes ao novo leiaute do eSocial S-1.3, que tem previsão de implantação em ambiente de produção em**02/12/2024.**

## **04. SOLUÇÃO**

Adaptação do banco de dados:

| Propriedade | Descrição | Tipo | Tabela |
| --- | --- | --- | --- |
| idConsolidacao | Primary key | Int | VPROCTRIBCONSOLIDACAO.IDCONSOLIDACAO |
| codColigada | Código da coligada | DCODCOLIGADA | VPROCTRIBCONSOLIDACAO.CODCOLIGADA |
| nrProcTrab | Número do processo trabalhista, da ata ou número de identificação da conciliação | String | VPROCTRIBCONSOLIDACAO.NRPROCTRAB |
| perApurPgto | Mês/ano em que é devida a obrigação de pagar a parcela prevista no acordo/sentença | String | VPROCTRIBCONSOLIDACAO.PERAPURPGTO |

## **05. DOCUMENTAÇÃO**

**[eSocial versão S-1.3 - Leiautes](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.3/index.html)**
