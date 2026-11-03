---
content_hash: 5fc967d5c3f4c1d26716b32ded7603abf02d3f47fb2472cb19fb8a360950e3dc
fetched_at: '2026-06-29T00:11:36.719514+00:00'
page_id: '773502808'
product: rm
source: tdn-rm
title: 'DT - DIRF: Sempre habilitar "Usa Filtro de seleção ao gerar DIRF em arquivo"'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=773502808
version: 6
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | DIRF em arquivo |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-5941](https://jiraproducao.totvs.com.br/browse/DRHROTRM-5941) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2209.244
* 12.1.2302.169
* 12.1.2306.113

## **03. SITUAÇÃO/REQUISITO**

O parâmetro "Usa filtro de seleção ao gerar DIRF em arquivo" somente está sendo habilitado quando o parâmetro "Todos" é selecionado.

## **04. SOLUÇÃO**

Foi realizado um aprimoramento para garantir que o parâmetro "Usa filtro de seleção ao gerar DIRF em arquivo" esteja sempre habilitado, como ilustrado na demonstração a seguir:

I

**Observação:**

Ao selecionar qualquer uma das opções a seguir, o parâmetro "Usa filtro de seleção ao gerar DIRF em arquivo" não será mantido marcado no perfil, a fim de evitar erros no envio da DIRF:

* Apenas com IRRF
* Com IRRF ou rendimentos acima de R$6.000,00 ou com assalariado com rendimentos acima de R$28.559,70
