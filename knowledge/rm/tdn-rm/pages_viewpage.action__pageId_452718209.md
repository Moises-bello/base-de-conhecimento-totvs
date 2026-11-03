---
content_hash: 73e14d3d37a26f8d2b136ead5651a06250e4ffc7ded64fd5db9e17b4520fe357
fetched_at: '2026-06-29T00:09:58.843201+00:00'
page_id: '452718209'
product: rm
source: tdn-rm
title: Código de Cálculo 11 - INSS de 13º Salário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718209
version: 2
---

Desconto do tipo valor.

O sistema soma os eventos lançados no mês com código de cálculo '48-13º Salário', '66-Dif. 13º Salário' e '97-Dif. 13º Salário Rescisão' e acha o valor do total que incide INSS 13º salário (controle interno).

O sistema busca o total já descontado de INSS 13º salário em envelopes anteriores encontra o valor de 'JÁ DESCONTOU".

O calculo é feito da seguinte forma:

((INC. INSS 13o. SAL. \* TAXA) / 100) - JÁ DESCONTOU

O valor encontrado de INC. INSS 13o. SAL. (somatória de todos os eventos que incidem INSS 13º salário) é aplicada a tabela informada nas Tabelas de Cálculo e multiplicado pela taxa da faixa encontrada. Este valor é dividido por 100 e do resultado é subtraído o valor de 'JÁ DESCONTOU'.

Este evento é utilizado para o cálculo das rescisões e diferença de 13º salário.

Quando utiliza o Cálculo .Net

O sistema soma os eventos lançados no mês com incidência em 'INSS 13º Salário', com exceção do evento com código de  '102-2ª parcela 13º Salário', para este evento o INSS é descontado no evento com código de cálculo '103-I.N.S.S. 2ª parc. 13º Salário'.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
