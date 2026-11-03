---
content_hash: 3a73941cb116128b33a815b73739b6b2490d98411521b8d029e8377a9e544202
fetched_at: '2026-06-29T00:11:36.003304+00:00'
page_id: '770940423'
product: rm
source: tdn-rm
title: DT - S-1010 - Adequação da tag <codIncIRRF>
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=770940423
version: 21
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | S-1010: Adequação da tag <codIncIRRF> |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-6343](https://jiraproducao.totvs.com.br/browse/DRHROTRM-6343 "View this issue") |

## **01. VERSÕES**

**A partir das Versões:**

* 12.1.2209.235
* 12.1.2302.158
* 12.1.2306.103

## **02. SITUAÇÃO/REQUISITO**

Adequação dos valores gerados nas tag's <codIncCP> e <codIncIRRF> dos eventos de INSS para atender ao eSocial.

## **03. SOLUÇÃO**

Com a inclusão do IRRF no eSocial, foi necessário realizar ajustes nos valores de incidência de INSS (tag <codIncCP>) e IRRF (tag <codIncIRRF>)no evento S-1010.

Essa adequação tem como objetivo evitar qualquer discrepância entre a folha de pagamento e os valores retornados pelo governo.

**O que foi ajustado?**

Nos patches acima mencionados, os valores enviados no XML do evento S-1010 para os códigos de cálculos abaixo sofrerão as seguintes alterações:

|  |  |  |
| --- | --- | --- |
| CÓDIGO DE CÁCULO | **CODINCIRRF ANTES DO AJUSTE** | **CODINCIRRF DEPOIS DO AJUSTE** |
| [3 - I.N.S.S.](https://tdn.totvs.com/pages/viewpage.action?pageId=452718215) | 9 | 41 |
| [11 - I.N.S.S. de 13º Salário](https://tdn.totvs.com/pages/viewpage.action?pageId=452718209) | 9 | 42 |
| [68 - INSS DE DIFERENÇA SALARIAL](https://tdn.totvs.com/pages/viewpage.action?pageId=452718219) | 9 | 41 |
| [82 - I.N.S.S. Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=452718205) | 9 | 43 |
| [85 - I.N.S.S. calculado pelo usuário](https://tdn.totvs.com/pages/viewpage.action?pageId=452718201) | 9 | 41 |
| [92 - Restituição de I.N.S.S.](https://tdn.totvs.com/pages/viewpage.action?pageId=452719626) | 0 | 41 |
| [103 - I.N.S.S. 2ª parc. 13º Salário](https://tdn.totvs.com/pages/viewpage.action?pageId=452718233) | 9 | 42 |
| [108 - INSS DE DIF SALARIAL DE 13º](https://tdn.totvs.com/pages/viewpage.action?pageId=452718958) | 9 | 42 |
| [110 - INSS DE DIF SALARIAL DE FÉRIAS](https://tdn.totvs.com/pages/viewpage.action?pageId=452718218) | 9 | 43 |
| [131 - I.N.S.S. Férias desc. mês ant.](https://tdn.totvs.com/pages/viewpage.action?pageId=452718225) | 9 | 43 |
| [141 - INSS Férias no mês (informado)](https://tdn.totvs.com/pages/viewpage.action?pageId=452718223) | 9 | 43 |
| [153 - Restituição de I.N.S.S. 13º](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718762) | 9 | 42 |
| [159 - INSS de férias outro emprego](https://tdn.totvs.com/pages/viewpage.action?pageId=452718222) | 43 | 9 |
| [171 - INSS 13º Sal descontado p/ previd ref lic maternide](https://tdn.totvs.com/pages/viewpage.action?pageId=452718206) | 9 | 42 |
| [185 - INSS DE FÉRIAS PROXIMO MÊS OUTRO EMPREGO](https://tdn.totvs.com/pages/viewpage.action?pageId=452719942) | 43 | 9 |
| [193 - INSS DE FÉRIAS MÊS ANTERIOR OUTRO EMPREGO](https://tdn.totvs.com/pages/viewpage.action?pageId=452719896) | 9 | 9 |
| [205 - INSS Descontado RRA](https://tdn.totvs.com/pages/viewpage.action?pageId=452718220) | 41 | 9 |
| [209 - INSS Descontado RRA Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=452719900) | 43 | 9 |
| [213 - INSS Descontado RRA 13º Salário](https://tdn.totvs.com/pages/viewpage.action?pageId=452719681) | 42 | 9 |
| [89 - I.N.S.S. com alíquota normal](https://tdn.totvs.com/pages/viewpage.action?pageId=452718204) | 41 | 9 |
| [90 - I.N.S.S. Férias com alíquota normal](https://tdn.totvs.com/pages/viewpage.action?pageId=452718959) | 43 | 9 |
| [91 - I.N.S.S. 13º c/ alíquota normal](https://tdn.totvs.com/pages/viewpage.action?pageId=452718212) | 42 | 9 |
| [137 - I.N.S.S. Fér. Próx. mês c/ alíq. normal](https://tdn.totvs.com/pages/viewpage.action?pageId=452718228) | 43 | 9 |
|  |  |  |
| CÓDIGO DE CÁCULO | **CODINCP ANTES DO AJUSTE** | **CODINCP DEPOIS DO AJUSTE** |
| [142 - INSS Férias próx. mês (informado)](https://tdn.totvs.com/pages/viewpage.action?pageId=452718227) | 31 | 0 |
| [153 - Restituição de I.N.S.S. 13º](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718762) | 0 | 32 |

**Como devo proceder no produto para realizar esse ajuste no eSocial?**

Verifique o passo a posso descrito no link: [S-1010: Como ajustar os valores das tags <codIncCP> e <codIncIRRF>](https://tdn.totvs.com/pages/viewpage.action?pageId=770941181)

## **04. ASSUNTOS RELACIONADOS**
