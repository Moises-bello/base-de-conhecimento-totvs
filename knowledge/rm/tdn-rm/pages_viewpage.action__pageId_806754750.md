---
content_hash: 2804efe165c6ba8fb10928824a291c0e665f4f3fcb3e47f8ac45880fe7b76010
fetched_at: '2026-06-29T00:11:43.413572+00:00'
page_id: '806754750'
product: rm
source: tdn-rm
title: DT - S-1010 - Adequação das tags <codIncCP> e <codIncIRRF> para os eventos
  INSS de Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=806754750
version: 12
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | S-1010: Adequação dsa tags <codIncCP> e <codIncIRRF> para os eventos de INSS de Férias. |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado): | [DRHROTRM-6906](https://jiraproducao.totvs.com.br/browse/DRHROTRM-6906) |

## **01. VERSÕES**

**A partir das Versões:**

* 12.1.2302.240
* 12.1.2306.187
* 12.1.2310.121

## **02. SITUAÇÃO/REQUISITO**

Ajuste dos valores gerados nas tags <codIncCP> e <codIncIRRF> nos eventos de INSS de férias, visando a conformidade com os requisitos do eSocial.

## **03. SOLUÇÃO**

Com a inclusão do IRRF no eSocial, foram efetuados ajustes nos valores de incidência de INSS (tag <codIncCP>) e IRRF (tag <codIncIRRF>) no evento S-1010.

Essa adaptação visa prevenir qualquer discrepância entre a folha de pagamento e os valores reportados ao governo.

**O QUE FOI AJUSTADO?**

1) Criados os campos 'Evento INSS Férias envelope' e 'Evento INSS Férias Próximo Mês envelope' nos [parâmetros do eSocial.](https://tdn.totvs.com/pages/viewpage.action?pageId=540899121)

2) Adequação da geração das tags <codIncCP> e <codIncIRRF> para a verba informada no campo "Evento INSS Antecipação de Férias(Desconto)' existente nos [parâmetros do eSocial.](https://tdn.totvs.com/pages/viewpage.action?pageId=645896860)

3) Após a inserção das verbas especificadas nos parâmetros do eSocial mencionadas nos campos acima (1 e 2), torna-se imprescindível gerar e enviar o XML S-1010 correspondente a essas verbas.

Veja como proceder para realizar essa adequação acessando o link: [S-1010: Como ajustar os valores das tags <codIncCP> e <codIncIRRF>](https://tdn.totvs.com/pages/viewpage.action?pageId=770941181).

Essa etapa é fundamental para garantir a correta geração das tags **<codIncCP>** e **<codIncIRRF>**, conforme demonstrado abaixo:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **CAMPOS PARAMETRIZADOR** | **CODINCCP ANTES DO AJUSTE** | **CODINCCP DEPOIS DO AJUSTE** | **CODINCIRRF ANTES DO AJUSTE** | **CODINCIRRF DEPOIS DO AJUSTE** |
| Evento INSS Férias envelope |  | 31 |  | 9 |
| Evento INSS Férias Próximo Mês envelope |  | 00 |  | 9 |
| Evento INSS Antecipação de Férias (Desconto) | 00 | 00 | 9 | 43 |

4) Nos patches acima mencionados, os valores enviados no XML do evento S-1010 para os códigos de cálculos abaixo sofrerão as seguintes alterações:

|  |  |  |
| --- | --- | --- |
| CÓDIGO DE CÁCULO | **CODINCIRRF ANTES DO AJUSTE** | **CODINCIRRF DEPOIS DO AJUSTE** |
|  | 9 | 43 |
|  | 43 | 9 |
|  | 9 | 43 |

## **04. ASSUNTOS RELACIONADOS**
