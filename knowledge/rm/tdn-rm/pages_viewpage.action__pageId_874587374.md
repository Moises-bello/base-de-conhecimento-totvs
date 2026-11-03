---
content_hash: c09fda5e6790b46fedcb7dc204b587551f2011218c61b88a85e3fd0e5eb6a853
fetched_at: '2026-06-29T00:11:59.640391+00:00'
page_id: '874587374'
product: rm
source: tdn-rm
title: DT - S-2205 - Ajuste na Tag <depSF> Alteração no Artigo nº 363 da IN Pres/INSS
  nº 28/2022
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=874587374
version: 13
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | S-2205 - Ajuste na Tag <depSF> Alteração no Artigo nº 363 da IN Pres/INSS nº 28/2022 |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-11293](https://jiraproducao.totvs.com.br/browse/DRHROTRM-11293 "View this issue") |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2402.234
* 12.1.2406.163
* 12.1.2410.101 e superiores

## **03. SITUAÇÃO/REQUISITO**

Tratar a geração do evento "S-2205 - Alteração de Dados Cadastrais do Trabalhador"  para que a tag <depSF> seja gerada conforme alteração do Artigo nº 363 da Instrução Normativa Pres/INSS nº 28/2022.

## **04. SOLUÇÃO**

O produto foi ajustado para que, na geração do evento S-2205, a tag <depSF> passe a gerar o valor "S" quando o dependente válido tiver entre 4 e 14 anos de idade, e o campo "Entregou comprov. frequência escolar" no cadastro de Dependente estiver marcado, atendendo o artigo abaixo:

**Exemplo:**

Dependente com idade igual a 13 anos e com o campo "Entregou comprov. frequência escolar" marcado, conforme demonstração abaixo:

Geração do XML do evento S-2205:

## **05. DEMAIS INFORMAÇÕES**

[DT - Salário Família - Declaração de frequência escolar](https://tdn.totvs.com/pages/viewpage.action?pageId=860252085)
