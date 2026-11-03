---
content_hash: 82ed045464497a0697986b9be81b354520b8f9f0308ed1827078350f3b9fe401
fetched_at: '2026-06-29T00:12:06.905131+00:00'
page_id: '917133365'
product: rm
source: tdn-rm
title: DT - AEJ Portaria 671/2021 - Marcação Pré-Assinalada no dia Feriado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=917133365
version: 12
---

## **01. DADOS GERAIS**

| **Produto:** | **RM** |
| --- | --- |
| **Linha de Produto:** | **Linha RM** |
| **Segmento:** | **RH** |
| **Módulo:** | **TOTVS Automação de Ponto** |
| **Função:** | **AEJ Portaria 671/2021** |
| **País:** | **Brasil** |
| **Requisito/Story/Issue:** | **[DRHJORNRM-7421](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-7421)** |

## **02. VERSÕES**

* A partir dos patches:

  + 12.1.2406.241
  + 12.1.2410.178
  + 12.1.2502.105  e superiores.

## **03. SITUAÇÃO/REQUISITO**

O arquivo AEJ não está trazendo as informações de marcações pré assinaladas, do horário de intervalo no dia de feriado.

## **04. SOLUÇÃO**

Ajustado o relatório AEJ para a emissão das batidas pré-assinaladas no dia de feriado.

## **05.** **EXEMPLO DE UTILIZAÇÃO**

11Geração do Relatório AEJ - Sindicato parâmetro Marcado - "Considera intervalo de Refeição em Feriados"

Funcionário possui horário planejado 07:00-11:00-13:00-17:00.No dia 15/11/2024  efetuou as batidas 07:00-17:00.

Gerando o relatório AEJ, será demonstrada as batidas pré-assinaladas .

1Geração do Relatório AEJ - Sindicato parâmetro Desmarcado - "Considera intervalo de Refeição em Feriados"

Funcionário possui horário planejado 07:00-11:00-13:00-17:00.No dia 15/11/2024  efetuou as batidas 07:00-17:00.

Emitindo o relatório AEJ, não será demonstrada as batidas pré-assinaladas .

## **06. ASSUNTOS RELACIONADOS**

* [DT - AEJ Portaria 671/2021 - Adequação do número sequencial dos pares das batidas de acordo com a jornada realizada](https://tdn.totvs.com/pages/viewpage.action?pageId=845421464)

* [DT - AEJ Portaria 671/2021 - Adequação para que as batidas desconsideradas 'D' não tenham o número sequencial de pares preenchido](https://tdn.totvs.com/pages/viewpage.action?pageId=856916971)
* [DT - AEJ Portaria 671/2021 - Adequação do Relatório no formato ASCII ISO 8859-1](https://tdn.totvs.com/pages/viewpage.action?pageId=862097001)
