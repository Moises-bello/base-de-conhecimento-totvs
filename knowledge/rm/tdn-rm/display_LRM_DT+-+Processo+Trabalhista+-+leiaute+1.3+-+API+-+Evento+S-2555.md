---
content_hash: 063d26e696ae30898f12f9170c8b146c685b1c5f46cc2b0dda64d7c2ea8fcdc0
fetched_at: '2026-06-29T00:11:56.552139+00:00'
page_id: '867144297'
product: rm
source: tdn-rm
title: DT - Processo Trabalhista - leiaute 1.3 - API - Evento S-2555
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Processo+Trabalhista+-+leiaute+1.3+-+API+-+Evento+S-2555
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
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHHCM-13433](https://jiraproducao.totvs.com.br/browse/DRHHCM-13433) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2410

## **03.****SITUAÇÃO/REQUISITO**

Atender as implementações referentes ao novo leiaute do eSocial S-1.3, que tem previsão de implantação em ambiente de produção em**02/12/2024.**

## **04. SOLUÇÃO**

Adaptação da API:

| Propriedade | Descrição | Tipo | JSON |
| --- | --- | --- | --- |
| codColigada | Código da coligada | Campo | companyId |
| branchId | Código da filial | Campo | branchId |
| excluidoERP | Retorna se processo foi excluído ou não | Campo | excluidoERP |
| nrProcTrab | Número do processo trabalhista, da ata ou número de identificação da conciliação | Campo | nrProcTrab |
| perApurPgto | Mês/ano em que é devida a obrigação de pagar a parcela prevista no acordo/sentença | Campo | perApurPgto |

## **05. DOCUMENTAÇÃO**

**[eSocial versão S-1.3 - Leiautes](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.3/index.html)**
