---
content_hash: cca17625ca678fb0fca6bd7b55c4e3719bae6b8233f83abc020899c729fa69e2
fetched_at: '2026-06-29T00:09:26.569427+00:00'
page_id: '423938322'
product: rm
source: tdn-rm
title: Máquina de Cálculo do Patrimônio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938322
version: 2
---

**Cálculo da Correção Monetária**

Até 1994, no Brasil os Balanços eram demonstrados com os ajustes denominados de "Correção Monetária de Balanços" (Lei 6.404/76). Para fins de contabilidade tributária, os itens permanentes do Balanço (basicamente Ativo Permanente e Patrimônio Líquido) eram ajustados em função de um coeficiente fornecido pelo governo (com base em algum índice de inflação).

**Parametrização**

Antes da execução do cálculo devem-se definir informações como o tipo de depreciação (cota integral ou proporcional) e a periodicidade – cadastro de cálculo e o .

**Formulas utilizadas para realização do Cálculo da Correção**

Índices

O sistema possui a seguinte regra para utilização do índice no cálculo:

* Índice Médio = após 94 a UFIR média é a do último dia do mês;
* Índice Correção = UFIR do primeiro dia do mês corrente;
* Índice Final = após 94 a UFIR utilizada é a do primeiro dia do mês seguinte.

Exemplo:

O cálculo para o mês de janeiro/2011 considerará como índice final o índice do primeiro dia de fevereiro/2011

**Cálculos da Correção do Valor do Patrimônio**

A Correção Monetária será o valor base em índice multiplicado pela diferença entre o índice final e o índice de correção:

Correção Monetária = Valor base em índice \* (índice final – índice de correção) que que  que contenham Vídeos, Imagens, Áudios, Apresentações e Documentos.

O valor corrigido em moeda será a soma da correção monetária com o valor base em moeda do mês corrente:

Valor Corrigido em Moeda = Correção Monetária + Valor base em moeda

A Correção da Depreciação Acumulada será calculada da seguinte forma:

Correção da Depreciação Acumulada = valor da depreciação acumulada em índice \* (índice final – índice de correção) + depreciação do mês em índice \* (índice final – índice médio)

A Depreciação Acumulada Corrigida do patrimônio será a soma entre a depreciação acumulada do mês corrente com a correção da depreciação acumulada:

Depreciação Acumulada Corrigida = depreciação acumulada + correção da depreciação acumulada

Para o mês que possui 28 dias a depreciação acumulada corrigida do mês será a soma da correção da depreciação acumulada do mês anterior, a depreciação do mês corrente e a correção da depreciação:

Depreciação acumulada corrigida = correção da depreciação acumulada (mês anterior) + depreciação do mês + correção da depreciação

Veja também

* Execução do Cálculo de Depreciação
