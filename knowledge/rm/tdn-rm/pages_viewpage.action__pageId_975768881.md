---
content_hash: 4a5e97f8e9e235e946c98e8572a45562af34c6a2a4154fd850d3019773bf2bbe
fetched_at: '2026-06-29T00:12:15.281763+00:00'
page_id: '975768881'
product: rm
source: tdn-rm
title: DT - eSocial - Adequação da tabela dinâmica "PCLATRAEST - Classificação do
  Trabalhador Estrangeiro"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=975768881
version: 7
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento - eSocial |
| Função: | Adequação da tabela dinâmica "PCLATRAEST - Classificação do Trabalhador Estrangeiro" |
| País: | Brasil |
| Ticket: |  |
| Issue: | [DRHROTRM-14314](https://jiraproducao.totvs.com.br/browse/DRHROTRM-14314) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2410.284
* 12.1.2502.186
* 12.1.2506.127 e superiores

## **03.****SITUAÇÃO/REQUISITO**

Adequação da tabela dinâmica  "PCLATRAEST - Classificação do Trabalhador Estrangeiro" para atender ao [Leiaute S-1.3 do eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.3/index.html#evtAdmissao), no que se refere a descrição do item "3" da tag <condIng> "Condição de ingresso do trabalhador migrante”.

Essa tag é gerada nos eventos do eSocial S-2200 (Cadastramento Inicial do Vínculo) e S-2300 (Trabalhador Sem Vínculo), conforme regras estabelecidas no leiaute.

## **04. SOLUÇÃO**

Realizar a adequação do produto TOTVS Folha de Pagamento para contemplar a correta descrição do item "3"  da tag <condIng> "Condição de ingresso do trabalhador migrante”, conforme definido no Leiaute S-1.3 do eSocial.

1) Alterada descrição da classificação 09 da Tabela Dinâmica "**PCLATRAEST - Classificação do Trabalhador Estrangeiro**", conforme abaixo:

| De | Para |
| --- | --- |
| Permanência no Brasil em razão de filhos ou cônjuge brasileiros | Permanência no Brasil em razão de reunião familiar |

2) Na geração do XML do eSocial, o valor **"09"** da tabela dinâmica "**PCLATRAEST - Classificação do Trabalhador Estrangeiro**" será convertido e gerado como **"3"** na tag `<condIng>`, conforme estabelecido no leiaute do eSocial.

**Leiaute**

Ao gerar a tag `<condIng>`, o sistema realiza internamente um mapeamento **De/Para** entre os códigos da tabela dinâmica e os códigos exigidos pelo leiaute do eSocial, conforme exemplificado abaixo:

| De (tabela dinâmica "**PCLATRAEST - Classificação do Trabalhador Estrangeiro**") | | Para (tag <condIng> "Condição de ingresso do trabalhador migrante”) | |
| --- | --- | --- | --- |
| 01 | Visto permanente | 7 | Outra Condição |
| 02 | Visto temporário | 7 | Outra Condição |
| 03 | Asilado | 7 | Outra Condição |
| 04 | Refugiado | 1 | Refugiado |
| 05 | Solicitante de Refúgio | 2 | Solicitante de Refúgio |
| 06 | Residente fora do Brasil | 7 | Outra Condição |
| 07 | Deficiente físico e com mais de 51 anos | 7 | Outra Condição |
| 08 | Com residência provisória e anistiado, em situação irregular | 7 | Outra Condição |
| 09 | Permanência no Brasil em razão de reunião familiar | 3 | Permanência no Brasil em razão de reunião familiar |
| 10 | Beneficiado pelo acordo entre países do Mercosul | 4 | Beneficiado pelo acordo entre países do Mercosul |
| 11 | Dependente de agente diplomático e/ou consular | 5 | Dependente de agente diplomático e/ou consular |
| 12 | Benefici. pelo Tratado de Amizade, entre a Repúb. do Brasil e Repúb. Portuguesa | 6 | Benefici. pelo Tratado de Amizade, entre a Repúb. do Brasil e Repúb. Portuguesa |

**Exemplo:**

Cadastro do Funcionário

Geração do XML

## **05. DOCUMENTAÇÃO**
