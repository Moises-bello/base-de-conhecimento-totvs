---
content_hash: 26fb03ed6274bd536801af700d872cbb6584cd055d733016f3caeae84bbced7a
fetched_at: '2026-06-29T00:12:01.569349+00:00'
page_id: '896372327'
product: rm
source: tdn-rm
title: PI - Proposta - VPL Zerar
type: documentation
url: https://tdn.totvs.com/display/LRM/PI+-+Proposta+-+VPL+Zerar
version: 5
---

Quando falamos em “zerar o VPL (Valor Presente Líquido)” de um plano de financiamento modificado, estamos essencialmente garantindo que as condições financeiras do plano, após as alterações, sejam equivalentes, em termos de valor no tempo, às condições originais.

**O que é o VPL?**  
O Valor Presente Líquido é uma métrica financeira que traz todos os fluxos de pagamentos futuros (entrada, parcelas mensais, anuais, etc.) para o presente, descontando-os a uma taxa de atratividade (taxa de juros ou custo de oportunidade). Ao fazer isso, podemos comparar fluxos de caixa que acontecem em diferentes momentos como se todos fossem “avaliados hoje”.

**Por que zerar o VPL ao alterar um plano?**  
Em um plano de financiamento imobiliário, o comprador e o vendedor combinam condições que geram um determinado valor presente. Esse valor presente reflete o “poder de compra” do montante acordado, considerando quando e como os pagamentos são feitos. Caso o plano seja modificado: por exemplo, diluindo parte do valor de entrada em mais parcelas, alterando valores mensais ou anuais, ou mudando o prazo. Essas alterações tendem a mudar o valor presente. Se pagamentos forem adiados para mais tarde sem ajuste no valor nominal, o VPL diminui; se pagamentos forem adiantados ou aumentados, o VPL tende a subir.

Zerar o VPL em relação ao plano original significa fazer ajustes nos valores das parcelas de modo que o valor presente do novo fluxo de pagamentos seja exatamente o mesmo do fluxo original. Em outras palavras, mesmo tendo alterado a forma, o prazo ou a distribuição dos pagamentos, você garante que o “valor econômico” do acordo, visto do presente, não se altere. Assim, nenhuma das partes sofre perda ou ganha vantagem indevida devido às mudanças no cronograma ou na estrutura de pagamentos.

**Em resumo:**

* O VPL mede o valor de todas as parcelas, trazidas ao presente.
* Zerar o VPL após uma modificação significa ajustar os novos pagamentos (seja aumentando algumas parcelas, inserindo outras, mudando seu valor) para manter o mesmo valor presente do plano original.
* Essa prática garante a neutralidade econômica da alteração, mantendo o mesmo poder de compra e a mesma atratividade financeira que havia antes da mudança.

**Exemplo:**

Abaixo descrevo o raciocínio completo e detalhado para chegar ao valor do ajuste necessário nas parcelas mensais de modo a manter o mesmo Valor Presente Líquido (VPL) original após a retirada de R$100.000 do fluxo anual, redistribuindo esta perda de valor presente para a parte mensal.

**Contexto Original:**

* Valor total do plano: R$1.100.000,00
* Estrutura de pagamentos original (datas tomando 06/12/2024 como data zero):
  1. Entrada à vista (t=0 meses): R$220.000,00 em 06/12/2024
  2. Pagamentos mensais: Total de R$440.000,00 divididos em 100 parcelas mensais (cada parcela mensal = R$440.000/100 = R$4.400,00).
     + Primeira parcela mensal: 06/01/2025 (t=1 mês)
     + Última parcela mensal: 100ª parcela em t=100 meses.
  3. Pagamentos anuais: Total de R$440.000,00 divididos em 6 parcelas anuais (cada parcela anual = R$440.000/6 ≈ R$73.333,33).
     + Primeira parcela anual: 06/01/2025 (t=1 mês)
     + Demais parcelas anuais a cada 12 meses: t=13, 25, 37, 49, 61 meses.

Com isso, a distribuição original é:

* Entrada: R$220.000,00 (t=0)
* Mensal: 100 parcelas de R$4.400,00 (t=1 a t=100)
* Anual: 6 parcelas de aproximadamente R$73.333,33 (t=1, 13, 25, 37, 49, 61)

Soma: 220.000 + 440.000 + 440.000 = 1.100.000

**Taxa de Desconto (TMA):** 1% ao mês

**Situação Nova:**

O cliente retira R$100.000 do montante anual, passando o total anual de R$440.000 para R$340.000, mantendo o mesmo número de parcelas anuais (6). Assim, cada parcela anual cai de ~R$73.333,33 para R$340.000/6 ≈ R$56.666,67. Portanto:

Novo plano desejado pelo cliente, sem ajuste:

* Entrada: R$220.000,00 (igual, t=0)
* Mensal: 100 parcelas de R$4.400,00 (igual)
* Anual: 6 parcelas de R$56.666,67 (ao invés de R$73.333,33)

Soma agora: 220.000 + 440.000 + 340.000 = 1.000.000. Ou seja, reduzimos o total em R$100.000. Isso, sem mexer nas parcelas mensais, reduzirá o VPL em relação ao plano original.

Nosso objetivo: manter o mesmo VPL do plano original. Para isso, precisamos compensar a perda de VPL causada pela redução das parcelas anuais, aumentando o valor das parcelas mensais. Vamos chamar o acréscimo em cada parcela mensal de "Δ".

**Cálculo do VPL Original:**

Para manter o mesmo VPL, precisamos comparar o VPL antes e depois.

**Notação:**

* i = 1% ao mês
* Fator de desconto para um fluxo em t meses: 1/(1+i)^t = 1/(1,01^t)

Séries de pagamentos:

1. Entrada (t=0): VPL\_Entrada = 220.000 (não há desconto)
2. Mensal (original): 100 parcelas de R$4.400,00 de t=1 a t=100. VPL da parte mensal original: R$277.932 (aproximado)
3. Anual (original): 6 parcelas de ~R$73.333,33 nos meses t={1,13,25,37,49,61}. VPL anual original: R$330.026 (aprox.)

**VPL Original Total:**

VPL Original=220.000+277.932+330.026≈827.958

**VPL do Novo Plano (antes do ajuste nas parcelas mensais):**

Agora, com parcelas anuais de 56.666,67. VPL anual original: R$255.022 (aprox.)

A parte mensal, antes do ajuste, continua a mesma (4.400 por mês), então seu VPL não muda: VPL Mensal = 277.932

Entrada = 220.000

VPL novo, sem ajuste=220.000+277.932+255.022=752.954 (aprox.)

Comparando:

* VPL original: ~827.958
* VPL novo (sem ajuste): ~752.954

Diferença de VPL: 827.958 - 752.954 = 75.004 (aprox.)

Perdemos cerca de 75.000 de valor presente ao reduzir as parcelas anuais (devido ao deslocamento no tempo e desconto).

**Ajuste Necessário (Δ) nas Parcelas Mensais:**

Queremos que o VPL após o ajuste volte a ser o VPL original (~827.958).

A nova estrutura após o ajuste será:

* Entrada: 220.000 (igual)
* Mensal: (4.400 + Δ) por 100 meses
* Anual: 56.666,67 por 6 anos

Vamos escrever a equação de equilíbrio do VPL:

**VPLoriginal=VPLnovo ajustado**

**Portanto, Δ ≈ R$1.190,00 por parcela mensal.**

---

**Conclusão:**

Para manter o mesmo VPL do plano original, após reduzir R$100.000 do fluxo anual (deixando o anual em R$340.000), é necessário aumentar cada parcela mensal em aproximadamente R$1.190,00.

Assim, a nova parcela mensal seria: 4.400 + 1.190 = R$5.590,00 (aproximadamente).

Esse ajuste compensa a perda de valor presente causada pela diminuição do valor das parcelas anuais, mantendo o mesmo VPL da proposta original.
