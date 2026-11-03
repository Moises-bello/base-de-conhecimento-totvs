---
content_hash: 321b2c813bbe201e77f872960ffa8ade4711df9888a23ad3e55f4b75142dbe72
fetched_at: '2026-06-29T00:12:13.985449+00:00'
page_id: '962613095'
product: rm
source: tdn-rm
title: DT - Lançamento Financeiro - Tipo "24-Total Guia FGTS Digital" - Respeitar
  o período informado na geração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=962613095
version: 20
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Lançamento Financeiro - Tipo "24-Total Guia FGTS Digital" - Respeitar o período informado na geração |
| País: | Brasil |
| Issue: | [DRHROTRM-12516](https://jiraproducao.totvs.com.br/browse/DRHROTRM-12516) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2410.266
* 12.1.2502.168
* 12.1.2506.113 e superiores

## **03. SITUAÇÃO/REQUISITO**

Adequar a geração do lançamento financeiro do tipo **"24 ‑ Total Guia FGTS Digital"** para respeitar o período informado no momento da geração. Atualmente, o processo gera o lançamento com base em todas as movimentações do mês, independentemente do intervalo definido pelo usuário.

## **04. SOLUÇÃO**

Implementamos de forma que, ao gerar o lançamento financeiro do tipo **"24 – Total Guia FGTS Digital"**, o sistema agora respeita o período selecionado pelo usuário. Isso significa que poderá escolher separadamente o período referente ao **décimo terceiro salário** e ao **mês da folha mensal**, conforme desejado.

Com essa funcionalidade, os lançamentos financeiros serão gerados dentro do período especificado, atendendo às exigências referentes à folha mensal e ao décimo terceiro, que devem ser transmitidas separadamente.

Importante!

O lançamento financeiro do tipo **"24 – Total Guia FGTS Digital"** deve ser gerado por competência **somente na competência 12 (dezembro)**, a fim de separar a movimentação do décimo terceiro salário da movimentação da folha de pagamento mensal. Nos meses restantes, recomenda-se gerar o lançamento com o parâmetro **"TODOS"**, para que os valores fiquem consistentes com os valores apurados pelo FGTS Digital.

## **05. DEMAIS INFORMAÇÕES**

[Lançamento Financeiro - Cadastro](https://tdn.totvs.com.br/display/public/LRM/Cadastros+Financeiros)
