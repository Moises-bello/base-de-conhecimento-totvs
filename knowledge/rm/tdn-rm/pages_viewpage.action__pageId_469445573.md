---
content_hash: 4c4c312bb35dcdadd05ed8b536d2f028d033a4b0772ec2ee99731b62a80b50ac
fetched_at: '2026-06-29T00:10:16.429086+00:00'
page_id: '469445573'
product: rm
source: tdn-rm
title: Reajuste - Como realizar a validação do reajuste de contrato de venda
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=469445573
version: 5
---

Vamos fazer um exemplo simples para facilitar a validação.

Ex. 1: Peguei R$ 1000,00 emprestado, taxa de 1,5% a.m., por dois meses e gostaria de validar se a taxa aplicada foi realmente a definida em contrato.

Os valores calculados ficaram dessa forma.

|  |  |  |  |
| --- | --- | --- | --- |
| **Mês** | **Valor Base** | **Juros** | **Valor Atualizado** |
| 1º | R$ 1.000,00 | 1,50% | R$ 1.015,00 |
| 2º | R$ 1.015,00 | 1,50% | R$ 1.030,23 |

Vamos proporcionalizar a coluna de valor atualizado e achar a taxa calculada.

|  |  |  |
| --- | --- | --- |
| **Mês** | **Valor Atualizado** | **Mês Anterior/ Mês Atual** |
| 0º | R$  1.000,00 | 0,0000% |
| 1º | R$  1.015,00 | 1,4778% |
| 2º | R$  1.030,23 | 1,4783% |

Percebemos que a taxa teve uma pequena diferença da taxa do contrato, mas por quê?

Ao realizar a proporção devemos analisar qual valor é o valor base e qual valor é o valor reajustado. Seguindo essa definição, o último valor achado é o valor reajustado e o anterior é o valor base. Então, refazendo o cálculo teremos a taxa correta.

|  |  |  |
| --- | --- | --- |
| **Mês** | **Valor Atualizado** | **Mês Atual/ Mês Anterior** |
| 0º | R$  1.000,00 | 0,0000% |
| 1º | R$  1.015,00 | 1,5000% |
| 2º | R$  1.030,23 | 1,5005% |

Com o novo cálculo teremos, ainda, fração no valor da taxa, pois estamos utilizando valores arredondados (2 casas) na base de cálculo do valor atualizado.

Ex2: Agora pegaremos os valores calculados anteriormente, mês a mês, e somaremos R$100,00 a parcela, que é referente aos valores de seguro e taxa administrativa. Ao final do cálculo teremos a mesma taxa calculada em contrato?

|  |  |  |
| --- | --- | --- |
| **Mês** | **Valor Atualizado + R$ 100,00** | **Mês Atual /**  **Mês Anterior** |
| 0º | R$  1.100,00 | 0,0000% |
| 1º | R$  1.115,00 | 1,3636% |
| 2º | R$  1.130,23 | 1,3659% |

Com o acréscimo de R$ 100,00, a parcela ficou com base de cálculo diferente da base calculada, desta forma, o índice não representou a taxa do contrato. Então, para termos o valor correto da taxa deveremos retirar todos os valores que não foram utilizados na base de cálculo do reajuste.

Com por exemplo, taxa de administração, juros de atraso, multa, iptu, seguro ou qualquer outra taxa que interfira na base de cálculo do reajuste.

Ex.3: Agora iremos utilizar um caso real de reajuste de contrato e validar seus valores utilizando o relatório da ‘Ficha Financeira Analítica’. Não podemos utilizar a opção com deságio marcado na ficha, pois muda a base de cálculo do reajuste.

Ficha retirada no mês 01/2019

 Ficha retirada no mês 02/2019

Vamos preencher a planilha com as informações de reajuste para cada grupo e tipo parcela que tenham saldo devedor.

Devemos verificar somente as parcelas em aberto de cada grupo e caso o grupo do tipo parcela não reajusta parcelas vencidas utilizaremos somente os valores das parcelas a vencer.

Grupo 2 - Mensal

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Data Base | Grupos | Tipo Parc | Saldo Devedor | Parc Abertas | Reajusta Juros? | Qual é a base do Juros | Taxa % Juros | Reajusta CM? | Qual é a base da CM | Índice CM | Reajusta Parcela Vencida? |
| 31/01/2019 | 2 | Mensal | R$  106.763,90 | 163 | Não | Valor principal | 0,9489% | Sim | Principal + Juros Atual | -0,00210 | Sim |
| 28/02/2019 | 2 | Mensal | R$  106.942,36 | 163 | Não | Valor principal | 0,9489% | Sim | Principal + Juros Atual | 0,00150 | Sim |

Grupo 2 – Anual

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Data Base | Grupos | Tipo Parc | Saldo Devedor | Parc Abertas | Reajusta Juros? | Qual é a base do Juros | Taxa % Juros | Reajusta CM? | Qual é a base da CM | Índice CM | Reajusta Parcela Vencida? |
| 31/01/2019 | 2 | Anual | R$    28.457,90 | 13 | Não | Valor principal | 0,9489% | Sim | Principal + Juros Atual | -0,00210 | Sim |
| 28/02/2019 | 2 | Anual | R$    28.500,54 | 13 | Não | Valor principal | 0,9489% | Sim | Principal + Juros Atual | 0,00150 | Sim |

Seguindo as premissas dos exemplos acima teremos que retirar da coluna de saldo devedor, de cada grupo, os valores de taxa de administração, juros de atraso, multa, seguro, IPTU ou qualquer outra taxa que interfira na base de cálculo do reajuste.

Detalhes da Ficha em Jan/2019

Não temos valores a serem deduzidos no saldo devedor do grupo 2 anual e mensal

Detalhes da Ficha em Fev/2019

Temos um valor de R$ 19,22 a ser deduzido somente no grupo 2, tipo parcela mensal.

A nova planilha ficou com os valores assim:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Data Base** | **Grupos** | **Tipo Parcela** | **Novo Saldo Devedor** | **Número de Parc Abertas** |
| 31/01/2019 | 2 | Mensal | R$        106.763,90 | 163 |
| 28/02/2019 | 2 | Mensal | **R$    106.923,14** | 163 |
|  |  |  |  |  |
| **Data Base** | **Grupos** | **Tipo Parcela** | **Novo Saldo Devedor** | **Número de Parc. Abertas** |
| 31/01/2019 | 2 | Anual | R$          28.457,90 | 13 |
| 28/02/2019 | 2 | Anual | R$          28.500,54 | 13 |

Outro ponto importante a ser conferido é o número de parcelas de cada grupo/Tipo Parcela, pois não poderíamos validar os índices que não foram aplicados em todas as parcelas em todas as datas bases. A base de cálculo muda e o índice fica distorcido, então, caso o número de parcelas da data base anterior seja maior que a atual, teremos que igualar a proporção dos valores do saldo devedor para que as bases fiquem proporcionalmente iguais.

No caso acima não precisaria recalcular, mas vamos fazer um exemplo. Caso o número de parcelas da base de janeiro fosse 164 parcelas e de fevereiro fosse 163 teríamos que fazer o seguinte cálculo:

Para finalizar a validação iremos calcular os índices dos grupos e verificar se estão de acordo com as informações das regras.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Data Base** | **Grupos** | **Tipo Parcela** | **Novo Saldo Devedor** | **Mês Atual /** **Mês Anterior** |
| 31/01/2019 | 2 | Mensal | R$  106.763,90 | 0 |
| 28/02/2019 | 2 | Mensal | R$  106.923,14 | **0,0014915** |
|  |  |  |  |  |
| **Data Base** | **Grupos** | **Tipo Parcela** | **Novo Saldo Devedor** | **Mês Atual /** **Mês Anterior** |
| 31/01/2019 | 2 | Anual | R$    28.457,90 | 0 |
| 28/02/2019 | 2 | Anual | R$    28.500,54 | **0,0014984** |

Os valores ficaram bem próximos do índice utilizado que era **0,0015** para ambas as regras.
