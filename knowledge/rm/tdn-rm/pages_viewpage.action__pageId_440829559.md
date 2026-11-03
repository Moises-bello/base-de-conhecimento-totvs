---
content_hash: c2e42bbb947b2ddf546d5b96df49162d364a9de052fd440c3ff6197b5da544ff
fetched_at: '2026-06-29T00:09:53.049533+00:00'
page_id: '440829559'
product: rm
source: tdn-rm
title: Cálculo de INSS múltiplos vínculos conforme o eSocial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=440829559
version: 45
---

# Objetivo:

---

       O objetivo deste documento é orientar como calcular o INSS para que os valores retornados pelo TOTVS Folha de Pagamento sejam os mesmos retornados pelo Governo.

---

01Parâmetro - Calcula INSS conforme eSocial

Para calcular o INSS conforme o eSocial será necessário marcar o parâmetro “Calcula INSS conforme eSocial” e informar a partir de quando o sistema iniciará a calcular desta forma, em Parametrizador | Folha Normal | Geral.

**Atenção:** Marcando esse parâmetro em uma coligada todas deverão estar marcadas.

**Observações:**

* Marcando este parâmetro o sistema sempre irá verificar se existe outras chapas/vínculos do mesmo funcionário para **encontrar a alíquota de** INSS, independente se o outro vinculo for na coligada corrente ou em outra coligada.
* Este parâmetro ficará habilitado quando o parâmetro “Calcula IRRF/INSS de múltiplos vínculos sem chapa centralizadora” estiver marcado. E deve ser marcado em **todas** as coligadas que existirem o vínculo relacionado aos múltiplos vínculos.
* Foram criados novos códigos de cálculo para controle do cálculo dos múltiplos vínculos:

+ [428 - Base Tributada De Inss Folha Primeira Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857540)
+ [429 - Base Tributada De Inss Folha Segunda Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857547)
+ [430 - Base Tributada De Inss Folha Terceira Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857555)
+ [431 - Base Tributada De Inss Folha Quarta Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857562)
+ [432 - Base Tributada De Inss 13º Primeira Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857570)
+ [433 - Base Tributada De Inss 13º Segunda Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857577)
+ [434 - Base Tributada De Inss 13º Terceira Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857583)
+ [435 - Base Tributada De Inss 13º Quarta Faixa](https://tdn.totvs.com.br/pages/viewpage.action?pageId=535857591)

* Os códigos de cálculo abaixo deixam de ser utilizados nesse processo:

+ [387 - Base Tributada de INSS Folha Múltiplos Vínculos](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452719615)
+ [388 - Base Tributada de INSS 13º Múltiplos Vínculos](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452718955)

* Os códigos de cálculos serão criados na base de dados após qualquer cálculo no produto (folha, provisão, etc).
* O usuário deverá criar eventos com esses códigos de cálculo, sendo do tipo base de cálculo e valor.
* Ao final do lançamento de todos os vínculos o usuário deve recalcular a base de todos os vínculos novamente. O ideal é que seja processado um vínculo por vez e após o seu cálculo não sejam feitas alterações no vínculo anterior. Caso seja necessário alterações, indicamos que seja cancelada a movimentação dos vínculos seguintes e lançada novamente.
* Atualmente o cálculo das férias não verifica a base de INSS outro vínculo.

**Atenção:**

Os usuários que já estão utilizando as versões abaixo:

**12.1.28.103 ,12.1.27.167, 12.1.26.212 e** **12.1.25.267** ou superiores, devem seguir as parametrizações do documento ,que contém as mudanças no calculo passando a considerar ordem de calculo conforme orientação do eSocial.

2Exemplo - Folha Normal

Calculo na coligada 1 antes de lançar na coligada 8

Calculo na coligada 8 após de lançar na coligada 1

Recalculando geral para todas as coligadas

Após recálculo o lançamento da coligada 1 foi alterado acrescentando o CC387 - BASE TRIBUTADA DE INSS FOLHA MÚLTIPLOS VÍNCULOS

E na coligada 8 ficará:

CONCLUSÃO:

Evento INSS = 76,56 + 544,47 = 621,03 – Teto do desconto de INSS

Evento CC387 - BASE TRIBUTADA DE INSS FOLHA MÚLTIPLOS VÍNCULOS

696,00 + 4949,80 = 5645,8 – Teto da base de desconto de INSS

3Exemplo - Férias

Supondo que tem dois vínculos em coligadas 1 e 8.

Quando calcula as férias destes vínculos o recibo de férias:

No envelope de férias lança o evento de INSS férias coligada 1

Ao lançar para o envelope na coligada 1 sem ainda não lançar na coligada 8

No envelope de férias lança o evento de INSS férias coligada 8

Ao lançar para o envelope na coligada 8 já tendo lançado na coligada 1 – Com isso o valor pago já havia atingido o teto, portanto o lançamento será conforme o log abaixo:

Recalculando geral para todas as coligadas

Coligada 1 recebe o evento CC387 - BASE TRIBUTADA DE INSS FOLHA MÚLTIPLOS VÍNCULOS com a base teto do INSS e os dois eventos de INSS lançados anteriormente somando o teto de desconto do INSS

Coligada 8 continua com o CC387 - BASE TRIBUTADA DE INSS FOLHA MÚLTIPLOS VÍNCULOS com a base teto do INSS zerado, o evento de restituição do valor descontado no recibo de férias e o desconto do recibo de férias

CONCLUSÃO:

Evento INSS (todo calculado na coligada 1) = 414,02 + 207,01 = 621,03 – Teto do desconto de INSS

Evento CC387 - BASE TRIBUTADA DE INSS FOLHA MÚLTIPLOS VÍNCULOS

(toda a base na coligada 1) = 5645,8 – Teto da base de desconto de INSS

4Exemplo - Rescisão com folha em outra coligada

Cálculo da demissão na coligada 1

Lançamento de folha na coligada 8 – lança o evento de CC387 - BASE TRIBUTADA DE INSS FOLHA MÚLTIPLOS VÍNCULOS

Recálculo da rescisão na coligada 1 e 8

CONCLUSÃO:

Evento INSS (todo calculado na coligada 1) = 190,81 + 385,00 = 575,81 – ALIQUOTA 11%

Evento CC387 - BASE TRIBUTADA DE INSS FOLHA MÚLTIPLOS VÍNCULOS

1734,66 (valor base INSS rescisão) + 3500,00 (valor base INSS folha) = 5234,66 \* 11% = 575,81

5Exemplo - Rescisão em duas coligadas

Cálculo da demissão na coligada 1

Lançamento de folha na coligada 8 – lança o evento de CC387 - BASE TRIBUTADA DE INSS FOLHA MÚLTIPLOS VÍNCULOS

Recálculo da rescisão na coligada 1 e 8

CONCLUSÃO:

Evento INSS = 190,81 + 385,00 =  575,81 – ALIQUOTA 11%

Evento CC387 - BASE TRIBUTADA DE INSS FOLHA MÚLTIPLOS VÍNCULOS

1734,66  + 3500,00  = 5234,66 \* 11% = 575,81

Evento INSS13 = 104,08 + 23,33 = 127,41 ALIQUOTA 8%

Evento CC388 - BASE TRIBUTADA DE INSS13 MÚLTIPLOS VÍNCULOS

1301,00  + 291,67  = 1592,67 \* 8% = 127,41

6Exemplo - 2ª parcela de 13º salário

Cálculo da 2ª parcela na coligada 1

Cálculo da 2ª parcela na coligada 8 – lança o evento de CC388 - BASE TRIBUTADA DE INSS13 MÚLTIPLOS VÍNCULOS

Recálculo do 13º salário nas coligada 1 e 8

CONCLUSÃO:

Evento INSS13 = 150,08 + 224,21 = 374,29 ALIQUOTA 11%

Evento CC388 - BASE TRIBUTADA DE INSS13 MÚLTIPLOS VÍNCULOS

1364,38  + 2038,35  = 3402,73 \* 11% = 374,29

7Exemplos de INDMVExemplos de INDMV

**Exemplo I de INDMV:**

Coligada 1

Lançamento de folha

Base de INSS outro Emprego Complementar CC 181

INSS Outro emprego - CC29

Lançando folha na coligada 2

Foi feito o lançamento de folha mensal.

Depois do lançamento na coligada 2 o sistema gerou uma pendência de recalculo na coligada 1.

O usuário deverá fazer o recalculo da coligada 1 para o correto calculo do INSS.

Após o recalculo da coligada 1 a pendencia de recalculo será excluída do relatório.

Gerando o XML S-1200 .

Coligada 1

O sistema retorna **2** quando o INSS atingiu o teto .

Coligada 2

Atingiu o teto

**Exemplo II de INDMV:**

Coligada 1 : Atigindo o teto do INSS

O indMV =2

Coligada 2: Não atingiu o teto

O indMV =1

Coligada 3 - Ultrapassando o teto de INSS

O indMV =3

falsefalse

**Produto:** Folha de Pagamento

false

**Rotina:** eSocial

false

**Versões:**

|  |
| --- |
| 12.1.21.241 |
| 12.1.22.233 |
| 12.1.23.158 |
| 12.1.24.102 |

falsefalse

**Status: Concluido**

false

**Data:**

false

**Autor:**
