---
content_hash: cec01a568dd8647c88b7159731c28f011d16197e1865eff2b771e0273100f562
fetched_at: '2026-06-29T00:11:49.488231+00:00'
page_id: '834266469'
product: rm
source: tdn-rm
title: DT - DIRF 2023/2024 - Utilização dos campos "Desconto Simplificado Caixa" da
  ficha financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=834266469
version: 22
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | DIRF - Utilização dos campos "Desconto Simplificado Caixa" da ficha financeira |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-9415](https://jiraproducao.totvs.com.br/browse/DRHROTRM-9415 "View this issue") |

## **ATENÇÃO: ESSE TDN FOI DESCONTINUADO. ACESSE O NOVO LINK:**

## **02.****LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2306.244
* 12.1.2310.185
* 12.1.2402.120 e Superiores.

## **03.****SITUAÇÃO/REQUISITO**

Adequar a geração da DIRF para gerar o campo "Desconto Simplificado", utilizando os valores retornados no período corrente. 

**04.****SOLUÇÃO**

A partir de agora, a DIRF irá considerar os novos campos 'DESCONTO SIMPLIFICADO CAIXA' criados na ficha financeira, conforme descrito abaixo, para preenchimento do campo 'Desconto Simplificado' na DIRF:

* **PFPERFF.IRRFSIMPLIFICADOCAIXA**
* **PFPERFF.IRRFFERSIMPLIFICADOCAIXA:** quando no mesmo caixa houver férias, férias na rescisão ou mais de um recibo de férias, o campo será preenchido com o último cálculo realizado.
* **PFPERFF.IRR13SIMPLIFICADOCAIXA:** quando no mesmo caixa houver 13º, rescisão e 2ª parcela, o campo será preenchido com o último cálculo realizado.

Para garantir essa atualização, estamos conduzindo uma verificação e atualização nos campos que atualmente se encontram como NULL no momento da geração da DIRF, a fim de evitar quaisquer inconsistências ou falhas na geração.

É importante observar que pode haver uma demora significativa na primeira vez, caso o volume de dados seja grande.

Não será necessário qualquer ação por parte do usuário, pois o produto irá acionar a rotina "**Atualiza campo Desconto Simplificado**" automaticamente, quando encontrar o campo NULL.

No log, serão registradas as informações dos funcionários e períodos que sofrerem alterações nos campos:

* **PFPERFF.IRRFSIMPLIFICADOCAIXA**
* **PFPERFF.IRRFFERSIMPLIFICADOCAIXA**
* **PFPERFF.IRR13SIMPLIFICADOCAIXA**

**Exemplo 1:**

Segue abaixo um exemplo de envelope referente ao mês de dezembro de 2023, no qual o valor do IRRF é zero. É importante observar que não há informação sobre o regime simplificado, pois o valor não alcançou o limite que permitiria sua aplicação. Após a conclusão do processo, o novo campo "IRRF Simplificado Caixa" será marcado como zero, indicando que o cálculo realizado para o caixa não foi simplificado.

**Importante:** O novo campo sempre considerará o caixa e manterá a mesma informação em todos os períodos.

Veja que no mês de dezembro não foi apresentado o valor no calculo simplificado.

**Exemplo 2:**

Abaixo estão dois envelopes demonstrados no mês de agosto de 2023: um com o cálculo simplificado e outro sem o cálculo simplificado. Após a execução do processo, o novo campo 'IRRF Simplificado Caixa' será marcado como zero. Isso ocorre porque o cálculo do caixa não foi simplificado; após o segundo lançamento, a base de IRRF do caixa não utilizou o cálculo simplificado para a retenção do IRRF.

**Importante:** O novo campo sempre considerará o caixa e manterá a mesma informação em todos os períodos.

Veja que no mês de agosto não foi apresentado o valor utilizado no calculo simplificado.

**Exemplo 3:**

Abaixo temos dois envelopes demonstrados no mês de agosto de 2023, ambos com o cálculo simplificado. Após a execução do processo, o novo campo 'IRRF Simplificado Caixa' será marcado como um, indicando que o cálculo do caixa foi simplificado.

**Importante:** O novo campo sempre considerará o caixa e manterá a mesma informação em todos os períodos.

Veja que no mês de agosto foi apresentado o valor utilizado no calculo simplificado.

**Exemplo 4:**

Abaixo temos um envelope demonstrado no mês de agosto de 2023, no qual o cálculo da folha e das férias apresenta um valor simplificado:

**Importante:** O novo campo sempre considerará o caixa e manterá a mesma informação em todos os períodos.

Veja que no mês de agosto foi apresentado o valor utilizado no calculo simplificado, tanto no caixa da folha como no caixa de férias.

**ATENÇÃO**

1. Devido à vigência da legislação do "Desconto Simplificado" a partir do caixa 05/2023, a validação será realizada a partir dessa competência, ou seja, se o ano de geração da DIRF for 2023, apenas os meses a partir de maio de 2023 serão considerados. No entanto, se o ano for posterior a 2023, o produto irá contemplar todos os meses do ano selecionado.
2. Ao concluir a atualização do campo, a flag "Desconto Simplificado Alterado Manualmente" na ficha financeira (PFPERFF) será marcada.

## **05. DEMAIS INFORMAÇÕES**

[DIRF/Informe de Rendimentos](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719351)
