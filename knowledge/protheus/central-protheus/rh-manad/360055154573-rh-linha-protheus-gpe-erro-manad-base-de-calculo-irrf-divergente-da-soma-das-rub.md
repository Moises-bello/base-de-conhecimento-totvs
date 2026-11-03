---
article_id: 360055154573
category: RH - MANAD
content_hash: ba3cfd0ecb4dadcb4ff8065d2d29cdc0a904e99f7cce0cdef807ae1839e480f7
fetched_at: '2026-06-28T22:43:33.806530+00:00'
product: protheus
section_id: 360008157193
source: central-protheus
title: 'RH - Linha Protheus - GPE -  Erro MANAD: Base de calculo IRRF divergente da
  soma das rubricas classificadas como 1 e 2 (GPEM110A)'
type: support-article
updated_at: '2021-04-06T20:21:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055154573-RH-Linha-Protheus-GPE-Erro-MANAD-Base-de-calculo-IRRF-divergente-da-soma-das-rubricas-classificadas-como-1-e-2-GPEM110A
---

**Dúvida**Erro MANAD: Base de calculo IRRF divergente da soma das rubricas classificadas como 1 e 2 (GPEM110A).  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17.  
  
**Solução**O sistema apresenta erro em uma determinada matricula, e o próprio validador do MANAD indica o funcionário:

![](https://tdn.totvs.com/download/attachments/283397092/image2017-6-30%2010%3A32%3A11.png?version=1&modificationDate=1498830765000&api=v2)

1) Localize o funcionário dentro do arquivo texto gerado, nos registros K250 e K300:

![](https://tdn.totvs.com/download/attachments/283397092/image2017-6-30%2010%3A33%3A3.png?version=1&modificationDate=1498830765000&api=v2)

Cada pipe ("I") separa um registro do outro, para que seja possível identificar ao que se refere. Abaixo detalhes do que cada um, representa:

* Texto fixo
* CNPJ
* Indicador do tipo de folha

1 - folha normal  
2 - folha de 13º salário  
3 - folha de férias  
4 - folha complementar à normal  
5 - folha complementar ao 13º  
6 - outras folhas

* Código lotação (cc)
* Filial / matricula
* Período
* Código da verba
* Valor da verba
* Indicador PROVENTO (P) ou DESCONTO (D)
* Indicador de base de calculo IRRF:

1 - base de cálculo salário mensal  
2 - base de cálculo - 13º Salário  
3 - Não é base de cálculo  
9 - outras bases de cálculo

* Indicador de Base de Cálculo para a Previdência Social:

1 - base de calculo do Salário de Contribuição mensal  
2 - base de cálculo do 13º salário  
3 - refere-se a valor descontado do segurado  
4 - refere-se a valor pago de Salário Família  
5 - base de cálculo do Salário-Maternidade  
6 - base de cálculo exclusiva do FGTS  
7 - Deduções da base de cálculo  
8 - não é base de cálculo  
9 - outras bases de cálculo  
  
Print de tela , apresentando os registros de acordo com a descrição acima:

![](https://tdn.totvs.com/download/attachments/283397092/image2017-6-30%2010%3A33%3A53.png?version=1&modificationDate=1498830765000&api=v2)

2) O ideal é utilizar a ferramenta de excel, para separação e visualização das informações

* Texto fixo
* CNPJ
* Indicador do tipo de folha

1 - folha normal  
2 - folha de 13º salário  
3 - folha de férias  
4 - folha complementar à normal  
5 - folha complementar ao 13º  
6 - outras folhas

* Código lotação (cc)
* Filial / matricula
* Período
* Data de pagamento
* CBO
* Cargo
* Qtd dependentes IRRF
* Qtd dependentes salário família
* Valor base IRRF
* Valor base previdência social (INSS)

3 ) Após a separação destes dados é possível efetuar a conferencia de forma prática, conforme tabela abaixo.

O bloco K300 (mostra de forma analítica as verbas pagas):

| Texto fixo | CNPJ | Indicador do tipo de folha | Código lotação (cc) | Filial / matricula | Período | Cod da verba (rubrica) | Valor | Indicador (P ou D) | Indicador BS de calculo IRRF | Indicador BS de calculo INSS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| K300 | 3873484000171 | 1 | 12030017870007800000 | 101001091 | 32017 | 20 | R$            1.397,50 | P | 1 | 1 |
| K300 | 3873484000171 | 1 | 12030017870007800000 | 101001091 | 32017 | 29 | R$                  33,88 | P | 1 | 1 |
| K300 | 3873484000171 | 1 | 12030017870007800000 | 101001091 | 32017 | 111 | R$               228,68 | P | 1 | 1 |
| K300 | 3873484000171 | 1 | 12030017870007800000 | 101001091 | 32017 | 132 | R$               106,68 | P | 3 | 8 |
| K300 | 3873484000171 | 1 | 12030017870007800000 | 101001091 | 32017 | 133 | R$                  35,56 | P | 1 | 8 |
| K300 | 3873484000171 | 1 | 12030017870007800000 | 101001091 | 32017 | 401 | R$               149,40 | D | 3 | 3 |
| K300 | 3873484000171 | 1 | 12030017870007800000 | 101001091 | 32017 | 471 | R$               142,24 | D | 1 | 8 |
| K300 | 3873484000171 | 1 | 12030017870007800000 | 101001091 | 32017 | 552 | R$                  46,58 | D | 3 | 8 |
| K300 | 3873484000171 | 1 | 12030017870007800000 | 101001091 | 32017 | 561 | R$                  83,85 | D | 3 | 8 |
| K300 | 3873484000171 | 1 | 12030017870007800000 | 101001091 | 32017 | 563 | R$                  72,97 | D | 3 | 8 |
| K300 | 3873484000171 | 1 | 12030017870007800000 | 101001091 | 32017 | 564 | R$                    2,30 | D | 3 | 8 |
| K300 | 3873484000171 | 1 | 12030017870007800000 | 101001091 | 32017 | 566 | R$                  12,53 | D | 3 | 8 |
| K300 | 3873484000171 | 1 | 12030017870007800000 | 101001091 | 32017 | 568 | R$                  86,12 | D | 3 | 8 |
| K300 | 3873484000171 | 1 | 12030017870007800000 | 101001091 | 32017 | 701 | R$            1.660,06 | O | 3 | 8 |
| K300 | 3873484000171 | 1 | 12030017870007800000 | 101001091 | 32017 | 725 | R$            1.510,66 | O | 3 | 8 |
| K300 | 3873484000171 | 1 | 12030017870007800000 | 101001091 | 32017 | 745 | R$            1.660,06 | O | 3 | 8 |
| K300 | 3873484000171 | 1 | 12030017870007800000 | 101001091 | 32017 | 755 | R$               132,80 | O | 3 | 8 |
| K300 | 3873484000171 | 1 | 12030017870007800000 | 101001091 | 32017 | 786 | R$            1.397,50 | O | 3 | 8 |
| K300 | 3873484000171 | 1 | 12030017870007800000 | 101001091 | 32017 | 787 | R$               486,45 | O | 3 | 8 |
| K300 | 3873484000171 | 1 | 12030017870007800000 | 101001091 | 32017 | 796 | R$               349,60 | O | 3 | 8 |
| K300 | 3873484000171 | 1 | 12030017870007800000 | 101001091 | 32017 | 801 | R$                    9,00 | O | 3 | 8 |
| K300 | 3873484000171 | 1 | 12030017870007800000 | 101001091 | 32017 | 815 | R$               332,01 | O | 3 | 8 |
| K300 | 3873484000171 | 1 | 12030017870007800000 | 101001091 | 32017 | 816 | R$                  96,28 | O | 3 | 8 |
| K300 | 3873484000171 | 1 | 12030017870007800000 | 101001091 | 32017 | 817 | R$                  51,71 | O | 3 | 8 |
| K300 | 3873484000171 | 1 | 12030017870007800000 | 101001091 | 32017 | 930 | R$               149,40 | O | 9 | 8 |
| K300 | 3873484000171 | 1 | 12030017870007800000 | 101001091 | 32017 | 933 | R$               758,36 | O | 3 | 8 |
| K300 | 3873484000171 | 1 | 12030017870007800000 | 101001091 | 32017 | 999 | R$            1.206,31 | O | 3 | 8 |

O Bloco K250 mostra de forma sintética apenas as bases de calculo

| Texto fixo | CNPJ | Indicador do tipo de folha | Código lotação (cc) | Filial / matricula | Período | Data de pagamento | CBO | Cargo | Qtd dependentes IRRF | Qtd dependentes salário família | Valor base IRRF | Valor base previdência social (INSS) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| K250 | 3873484000171 | 1 | 12030017870007800000 | 101001091 | 32017 | 6042017 | 410105,00 | 0 | ANALISTA DE PROCESSO | 4 | 1660,06 | 1660,06 |

4) Vamos conferir as verbas que entram para base de calculo do IRRF de acordo com o bloco K300:

| Código da verba | Valor | P OU D? |
| --- | --- | --- |
| 20 | R$                   1.397,50 | P |
| 29 | R$                         33,88 | P |
| 111 | R$                      228,68 | P |
| 133 | R$                         35,56 | P |
| 471 | R$                      142,24 | D |
|  |  |  |
| TOTAL | R$                   1.553,38 | (TOTAL DE PROVENTOS - DESCONTOS COM INCIDÊNCIA PARA IRRF) |

5) Comparando a base de IRRF gerada no registro K250 que é de $1660,06 com os valores analíticos do bloco K300 que é de $1553,38 conforme quadro acima, a diferença é de $106,68 .

Analisando as verbas do acumulado, verificamos que o valor corresponde à verba de abono pecuniário.

![](https://tdn.totvs.com/download/attachments/283397092/image2017-6-30%2010%3A47%3A10.png?version=1&modificationDate=1498830765000&api=v2)

Isso acontece porque a verba de ABONO (132) esta com NÃO para IRRF no acumulado, porém esta com SIM para IRRF na tabela SRV (cadastro de verbas) atual:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088902974/mceclip0.png)

São enviados para o MANAD, os pagamentos feitos ao funcionário e também a tabela de verbas. O validador faz uma comparação das incidências da época e das incidências atuais, se estiverem divergentes ele apresenta erro. Por isso não orientamos a mudança das incidências no decorrer  das competências.

Para essas situações , será necessário analisar o que é devido, ou seja, se o calculo da época estava correto ou a incidência atual é que está errada.  
  
**Saiba Mais**[Artigos sobre Manad](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360008157193-RH-MANAD)
