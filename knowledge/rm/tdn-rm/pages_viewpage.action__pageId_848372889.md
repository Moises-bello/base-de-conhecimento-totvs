---
content_hash: dfbe3cd9d02127bace67091be400f1a131a732d5e735efb5f218704282b75110
fetched_at: '2026-06-29T00:11:51.451707+00:00'
page_id: '848372889'
product: rm
source: tdn-rm
title: DT - Folha Analítica e Relatório Conferência FGTS - Bases de FGTS do eSocial
  conforme Guia FGTS Digital
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=848372889
version: 24
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento - eSocial |
| Função: | Folha Analítica e Relatório Conferência FGTS - Bases de FGTS do eSocial conforme Guia FGTS Digital |
| País: | Brasil |
| Issue: | [DRHROTRM-10360](https://jiraproducao.totvs.com.br/browse/DRHROTRM-10360) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2310.221
* 12.1.2402.165
* 12.1.2406.101 e superiores

## **03.****SITUAÇÃO/REQUISITO**

Adaptar o produto TOTVS Folha de Pagamento para incluir campos de FGTS com valores compatíveis com a guia de FGTS Digital, nos processos de Folha Analítica e Relatório de Conferência de FGTS.

[Manual de Orientação FGTS Digital página 22](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-do-orientacao-do-fgts-digital-versao-1-1-01-03-2024.pdf)

**OBSERVAÇÃO:**

Na opção b), também estão incluídas as rescisões realizadas entre os dias 01 e 09 do mês, em que o lançamento financeiro é exclusivamente rescisório + mensal. A guia gerada no Portal do FGTS Digital será a guia parametrizada.

## **04. SOLUÇÃO**

Com a implementação do FGTS Digital, foram realizadas alterações na demonstração das bases de FGTS para separar o FGTS mensal do FGTS rescisório.

Para realizar essa tratativa, foi necessário alterar os seguintes campos para considerar a parte mensal do FGTS:

* **Base FGTS eSocial**(eventos que incidem FGTS - eventos que estornam FGTS) desconsiderando os códigos de cálculos: 62, 99, 219  para funcionários ativos e demitidos sem direito a saque.
* **Base FGTS 13o. Sal.** **eSocial**(eventos que incidem FGTS 13 - eventos que estornam FGTS 13) desconsiderando os códigos de cálculos 71, 98 e 220 para funcionários ativos e demitidos sem direito a saque.
* **Base FGTS Indeniz.** **eSocial**considerando somente os códigos de cálculos: 62, 99, 219 e 71, 98 e 220 para funcionários ativos e demitidos sem direito a saque.

Além disso, foi necessária a criação de novos campos para considerar a parte rescisória do FGTS:

* **Base FGTS Resc. eSocial** (eventos que incidem FGTS - eventos que estornam FGTS) desconsiderando os códigos de cálculos: 62, 99, 219 para demitidos com direito a saque.
* **Base FGTS 13º Resc.** **eSocial**(eventos que incidem FGTS 13 - eventos que estornam FGTS 13) desconsiderando os códigos de cálculos 71, 98 e 220 para demitidos com direito a saque.
* **Base FGTS Ind Resc. eSocial** considerando somente os códigos de cálculos: 62, 99, 219, 71, 98 e 220 para demitidos com direito a saque.
* **FGTS Rescisório eSocial**
* **FGTS 13º Rescisório eSocial**
* **FGTS Indeniz. Resc.** **eSocial**

**ATENÇÃO: As demais bases de FGTS não sofreram alterações.**

| Código de Cálculo | Descrição Código de Cálculo |
| --- | --- |
| 62 | [Aviso Prévio](https://tdn.totvs.com/pages/viewpage.action?pageId=452719687) |
| 99 | [Dif. Aviso Prévio](https://tdn.totvs.com/pages/viewpage.action?pageId=452718356) |
| 219 | [Aviso Prévio Calculado Pelo Usuário](https://tdn.totvs.com/pages/viewpage.action?pageId=452719689) |
| 71 | [13º Salário indenizado](https://tdn.totvs.com/pages/viewpage.action?pageId=452718484) |
| 98 | [Dif 13º Salário indeniz. Rescisão](https://tdn.totvs.com/pages/viewpage.action?pageId=452718367) |
| 220 | [13º Calculado Pelo Usuário](https://tdn.totvs.com/pages/viewpage.action?pageId=452719649) |

Os processos abaixo foram adequados utilizando os novos campos:

* Folha Analítica: Inclusão dos campos acima
* Relatório Conferência de FGTS: Tratativa para considerar os novos campos

Aba 1true1Folha AnaliticaFGTS Digital

No exemplo abaixo o funcionário ativo possui pagamento de dissidio. As bases foram impressas nos campos para o FGTS mensal.

Retorno eSocial

No exemplo abaixo o funcionário foi demitido com direito a saque. As bases foram impressas nos novos campos para o FGTS rescisório.

Retorno eSocial

No exemplo abaixo o funcionário foi demitido com direito a saque em 11/04/2024 que acrescida de10 dias é posterior à data de vencimento do FGTS (20/04). As bases foram impressas nos novos campos para o FGTS rescisório.

Retorno eSocial

4Relatório de Conferencia FGTSRelatório de Conferencia FGTS

No exemplo abaixo o funcionário ativo possui pagamento de dissidio. Os valores de FGTS foram impressos no campo Mensal.

Retorno eSocial

No exemplo abaixo o funcionário foi demitido com direito a saque. Os valores de FGTS foram impressos no campo Rescisório.

Retorno eSocial

No exemplo abaixo o funcionário foi demitido com direito a saque em 11/04/2024 que acrescida de10 dias é posterior à data de vencimento do FGTS (20/04). Os valores de FGTS foram impressos no campo Rescisório.

Retorno eSocial

## **5. DEMAIS INFORMAÇÕES**

* [Folha Analítica](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719339)
* [Manual de Orientação FGTS Digital](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-do-orientacao-do-fgts-digital-versao-1-1-01-03-2024.pdf)
* [Código De Cálculo 492 - Base Excedente FGTS 13º a Compensar no FGTS Folha](https://tdn.totvs.com.br/pages/releaseview.action?pageId=1043712337)
