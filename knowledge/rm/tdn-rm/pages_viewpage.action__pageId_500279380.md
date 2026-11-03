---
content_hash: 3342fa561843244d80db86f02b8136fdf9aa131151fbf351cefdf25e26c7eb08
fetched_at: '2026-06-29T00:10:23.156647+00:00'
page_id: '500279380'
product: rm
source: tdn-rm
title: Método de Calculo de Fundos de Renda Fixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=500279380
version: 3
---

**MODELO DE CÁLCULO DE FUNDOS DE CURTO E MÉDIO PRAZO**

Ao avaliar um extrato mensal de um fundo de investimento de curto ou médio prazo, apesar do layout variar um pouco de uma instituição financeira para outra, são disponibilizadas algumas informações essenciais ao cotista: saldo inicial do período, os diversos valores que foram aplicados e resgatados no período, os respectivos efeitos tributários, e um saldo final do período.

Entretanto para entender o cálculo executado no fundo é necessário avaliar cada operação de aplicação e resgate com uma “lupa”. Ao executar uma operação de aplicação, o que está ocorrendo na essência é a aquisição de determinada quantidade de cotas do fundo pelo preço da cota do dia. A quantidade de cotas é facilmente identificada pela razão direta do montante investido em função da cotação do fundo. Cada operação de aplicação devemos tratar como a abertura de uma subconta no fundo, com o respectivo saldo de cotas.

***COTAS ADQUIRIDAS = VALOR APLICADO / VALOR DA COTA NO DIA***

No momento do resgate ocorre o efeito de estorno de cotas da respectiva subconta, porém o cálculo exige alguns cuidados. Ao executar um resgate, se o cotista não for beneficiário de isenção de impostos, ocorrerá o recolhimento de impostos (IR e IOF). O efeito nas cotas do fundo ocorrerá pelo respectivo valor bruto.

***VALOR BRUTO = VALOR RESGATADO + IR + IOF***

***COTAS PARA ESTORNO = VALOR BRUTO / VALOR DA COTA NO DIA***

Para efeito de cálculo, o estorno de cotas nas subcontas deve ocorrer sempre da subconta mais antiga para a mais nova. Não havendo saldo suficiente na subconta mais antiga, o efeito do estorno incide sobre esta até o seu limite de cotas, levando a zero. O restante de cotas a ser estornadas incide então na segunda subconta mais antiga conforme o mesmo critério, e assim por diante.

Para efeito do cálculo do saldo disponível pelo sistema, dada uma data de referência, devemos considerar como saldo inicial o valor correspondente ao encerramento de período do mês anterior. Ou seja, se desejo calcular o saldo disponível em 05/07/2019, devo considerar como saldo inicial o valor registrado no encerramento de período no dia 30/06/2019.

O sistema registra esta informação na forma de uma linha para cada subconta na tabela *FAPLFINMOV*. O valor é gravado na forma de cotas, que por necessidade de precisão, obriga a utilização de dois campos da tabela: o campo *COTASINTEIRO* registra a parte inteira, e o campo *COTASFRACAO* registra a parte fracionária. Para chegar ao número de cotas correspondente para a subconta é necessária uma operação matemática, que depende do número de decimais que foi informado na definição da aplicação financeira.

***NÚMERO DE COTAS = COTASINTEIRO + (COTASFRACAO / 10 ^ NÚMERO DE DECIMAIS)***

***SALDO DA SUBCONTA = NÚMERO DE COTAS \* VALOR DA COTA NO DIA***

***SALDO INICIAL DO PERÍODO = ∑ (SALDOS DAS SUBCONTAS)***

Baseado na movimentação do período, o sistema calcula a rentabilidade diária para cada uma das subcontas (aplicações). O cálculo se inicia com o saldo inicial da subconta no período, e para cada dia é executado um processamento em sequência que calcula o rendimento diário, e determina o saldo do dia seguinte.

* Calcular o rendimento diário
* Calcular o efeito de resgates
* Aplicar efeito de ajustes
* Calcular o saldo do próximo dia

O cálculo do rendimento diário utiliza a cotação do dia, a cotação anterior (destacando que finais de semana e feriados não tem cotação), e o saldo inicial do dia.

***RENDIMENTO[d0] = (COTACAO[d0] – COTACAO[d0-n]) \* SALDO[d0] / COTACAO[d0-n]***

***SALDO[d0+1] = SALDO[d0] + RENDIMENTO[d0] – RESGATE[d0] + AJUSTE[d0]***

Legenda:

* (d0) = dia corente
* (n) = dias

Neste documento somente iremos detalhar o cálculo do IR e do IOF sobre o valor do último saldo calculado no processo incremental, mas é importante destacar que estes valores são calculados em cada operação de resgate. Nestes casos o processo utilizado é calcular os impostos pelo saldo parcial (como se fosse um resgate total), e então aplicar uma proporção pela razão do valor do resgate e o saldo parcial.

***IOF RESGATE = IOF TOTAL \* VALOR DO RESGATE / SALDO PARCIAL***

***IR RESGATE = IR TOTAL \* VALOR DO RESGATE / SALDO PARCIAL***

***VALOR BRUTO DO RESGATE = VALOR DO RESGATE + IOF DO RESGATE + IR DO RESGATE***

***COTAS DO RESGATE = VALOR BRUTO DO RESGATE / VALOR DA COTA NO DIA***

**CÁLCULO DO IOF**

O IOF é calculado a partir da rentabilidade da aplicação financeira em determinado período, e sobre este é aplicada uma alíquota com um redutor diário, de modo que o imposto não tenha nenhum efeito após 30 dias após a aplicação.

A base de cálculo é calculada pela soma dos rendimentos, a partir da data da aplicação:

***BASE DE CALCULO = ∑ (RENDIMENTO)***

***IOF = BASE DE CÁLCULO \* ALÍQUOTA / 100***

A alíquota é determinada conforme a tabela abaixo:

|  |  |
| --- | --- |
| Número de dias de investimento | Alíquota de IOF |
| 01 | 96% |
| 02 | 93% |
| 03 | 90% |
| 04 | 86% |
| 05 | 83% |
| 06 | 80% |
| 07 | 76% |
| 08 | 73% |
| 09 | 70% |
| 10 | 66% |
| 11 | 63% |
| 12 | 60% |
| 13 | 56% |
| 14 | 53% |
| 15 | 50% |
| 16 | 46% |
| 17 | 43% |
| 18 | 40% |
| 19 | 36% |
| 20 | 33% |
| 21 | 30% |
| 22 | 26% |
| 23 | 23% |
| 24 | 20% |
| 25 | 16% |
| 26 | 13% |
| 27 | 10% |
| 28 | 6% |
| 29 | 3% |
| 30 | 0% |

**CÁLCULO DE IR**

O IR é calculado em função da rentabilidade da aplicação financeira em determinado período, e sobre esta é aplicada uma alíquota baseada em uma tabela progressiva.

A base de cálculo é calculada pela soma dos rendimentos, reduzidos do IOF recolhido, a partir da data da aplicação:

***BASE DE CALCULO = ∑ (RENDIMENTO) - IOF***

***IR = BASE DE CÁLCULO \* ALIQUOTA / 100***

Tabela progressiva de IR para aplicações de Curto Prazo:

|  |  |
| --- | --- |
|  | Alíquota de IR |
| Até 180 dias | 22,5% |
| Após | 20% |

Tabela progressiva de IR para aplicações de Médio/Longo Prazo:

|  |  |
| --- | --- |
|  | Alíquota de IR |
| Até 180 dias | 22,5% |
| De 181 até 360 dias | 20% |
| De 361 até 720 dias | 17,5% |
| Após | 15% |

Nos meses de maio e novembro, no momento do encerramento mensal, ocorre para cada subconta o cálculo da rentabilidade total do período do come-cotas (6 meses), calculando então o valor do IR considerando a menor alíquota do IR, ou seja, 20% para fundos de curto prazo, e 15% para fundos de médio/longo prazo, e então quantidade de cotas correspondente ao imposto calculado é estornado da subconta como recolhimento de IR Come-Cotas.

Após a incidência de um come-cotas, o cálculo do IR restante passa a se comportar de forma diferente. Para o período entre a data da aplicação até a data que ocorreu o come-cotas, a alíquota a ser aplicada é a diferença entre aquela definida na tabela progressiva e a alíquota utilizada no cálculo do come-cotas. Por exemplo, se a aplicação em um fundo de médio prazo foi feita no dia 20/05/2019, no encerramento do mesmo mês deve ocorrer a retenção do IR por uma alíquota de 15%. Ao fazer um resgate que incida sobre esta mesma subconta no dia 10/06/2019, a rentabilidade do período entre o dia 20/05 e 30/05 deve ser submetida a uma alíquota de 7,5% (22,5% - 15%), e a rentabilidade do período restante (entre 01/06 e 10/06) deve ser submetido a uma alíquota de 22,5%.

**CÁLCULO DO IOF VIRTUAL**

Por ocasião do cálculo do IR Come-Cotas, como qualquer cálculo de IR, exige que primeiro seja calculado o valor do IOF sobre o valor resgatável da subconta, mas não ocorre a retenção, razão porque este valor é denominado IOF Virtual. Entretanto, se porventura a subconta for submetida a um resgate, com prazo não maior que 30 dias após a aplicação, o IOF Virtual é compensado na operação. No mesmo exemplo da aplicação efetuada no dia 20/05/2019 e resgatada no dia 10/06/2019, o cálculo do IR poderá compensar o IOF Virtual:

***BASE DE CALCULO = ∑ (RENDIMENTO) – IOF + IOFVIRTUAL***

**Observação:**

Existe divergência de comportamento entre algumas instituições financeiras. Diversas consideram que, uma vez que o IOF foi tratado no cálculo do IR Come-Cotas, o efeito finaliza neste ponto, outras não. Visando tratar os dois modelos, foi implementado o campo IOFVIRTUAL na tabela FAPLFIN, visando capturar o modelo de cálculo. No caso de marcada a opção “IOF Virtual Integral”, o cálculo se modifica para:

***BASE DE CALCULO = ∑ (RENDIMENTO) + IOFVIRTUAL***
