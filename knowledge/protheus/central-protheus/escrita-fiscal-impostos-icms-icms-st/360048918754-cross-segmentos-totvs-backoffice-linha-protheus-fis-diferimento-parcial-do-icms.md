---
article_id: 360048918754
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: 37ee5382239fec30d38d5a21b009287682d5bf1947ce948d521f94baae76a1f2
fetched_at: '2026-06-28T22:39:20.483945+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Diferimento Parcial
  do ICMS e ICMS ST
type: support-article
updated_at: '2021-07-13T17:29:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048918754-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Diferimento-Parcial-do-ICMS-e-ICMS-ST
---

**Duvida:**

Quais os Procedimentos para o cálculo do Diferimento Parcial do ICMS e ICMS\_ST

**Solução:**

**Cálculo Diferimento - Alíquota Diferida**

A regra de cálculo do Diferimento do ICMS não prevê a geração de uma alíquota diferida, e sim da aplicação do % de Diferimento sobre o ICMS total calculado.

**Exemplo:**

1. Valor da Mercadoria R$ 1.000,00 (a)

2. Alíquota do ICMS 18% (b)

3. Valor do ICMS da operação (18% de R$ 1.000,00) R$ 180,00 (c) = (a) x (b)

4. Percentual do ICMS diferido 33,33% (Previsto na legislação do Estado ou no Regime                                Especial concedido) (d)

5. Valor do ICMS diferido (33,33% de R$ 180,00) R$ 60,00 (e) = (c) x (d)

6. Valor do ICMS devido (R$ 180,00 – R$ 60,00) R$ 120,00 (f) = (c) – (d).

Desta forma, quando da operação de Diferimento com Substituição Tributária, devido à necessidade do envio da Alíquota com diferimento, será alterada a regra de cálculo do Diferimento.

**Exemplo:**

Valor da Mercadoria R$ 1.000,00 (a)

2. Alíquota do ICMS 18% (b)

3. Valor do ICMS da operação (18% de R$ 1.000,00) R$ 180,00 (c) = (a) x (b)

4. Percentual do ICMS diferido 33,33% (Previsto na legislação do Estado ou no Regime Especial concedido) (d)

5. Alíquota com Diferimento (33,33% de 18) = 12%. (e) = (b) x (d). Valor inteiro arredondado.

6. Valor do ICMS devido (Base ICMS \* Alíquota com Diferimento) R$ 1000,00 \* 12% (f) = (a) \* (e)

7. Valor do ICMS diferido (Valor do ICMS da operação - Valor do ICMS devido) R$ 180,00 – R$ 120,00 (g) = (c) - (f)

Devido ao cálculo realizado de forma diferente quando ICMS-ST as operações poderão ter diferença do ICMS Diferido.

## Procedimento para Utilização

* Cadastrar exceção fiscal com alíquota interna do ICMS com valor da alíquota reduzida pelo Diferimento, e para calculo do ICMS ST informe alíquota do destinatário.

  **Exemplo de configuração da Exceção fiscal:**

  F7\_ALIQINT   = 12 - alíquota com Diferimento.

  F7\_ALIQDST  =18  - Alíquota do destinatário para cálculo do ICMS ST

  No cadastro de TES é necessário informar no campo **ICMS Diferido (F4\_ICMSDIF)** o conteúdo **5=Diferimento com ST.**

  Desta forma, o sistema irá calcular valor do ICMS com alíquota informada na exceção fiscal. Exemplo: **12%**, e não será reduzido o valor do diferimento de ICMS, pois esta redução já ocorreu    na alíquota.

  **Nos livros fiscais** **e tabela CD2**

  Serão gravados base e alíquota correspondente ao cálculo de ICMS da nota.

  No campo **FT\_ICMSDIF** e **Apuração de ICMS**, será impresso o valor correspondente ao diferimento do ICMS (alíquota cheia, sem aplicação do diferimento sobre alíquota.                  Exemplo: 18% multiplicada pelo percentual do diferimento informado no campo                    **F4\_PICMDIF = 33,33**.

Para mais detalhes, segue o link:

<https://tdn.totvs.com/display/public/PROT/FIS0010_Diferimento_Parcial_do_ICMS_e_ICMS_ST>

<https://tdn.totvs.com/display/public/PROT/FIS0069_DIFERIMENTO_ICMS>
