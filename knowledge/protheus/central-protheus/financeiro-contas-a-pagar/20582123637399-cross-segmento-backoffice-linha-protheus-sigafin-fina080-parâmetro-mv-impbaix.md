---
article_id: 20582123637399
category: Financeiro - Contas a Pagar
content_hash: 2968fb4b855027d6152d4545bc726b43b87b7c4d197d627e4810d5e46779c983
fetched_at: '2026-06-28T22:38:08.256727+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA080 - Parâmetro
  MV_IMPBAIX
type: support-article
updated_at: '2024-01-16T21:16:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20582123637399-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA080-Par%C3%A2metro-MV-IMPBAIX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20582123624983) Tempo aproximado para leitura: **02:00 min** **Dúvida**  
Ao baixar um título com multas e juros que os valores dos impostos estão sendo acrescidos com o valor da multa. Como excluir o valor acrescido para os impostos?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões  
  
**Solução**

O parâmetro **MV\_IMPBAIX**  considera os juros, multa ou desconto na base do imposto, sendo:

1 = Considera valores de juros, multa ou desconto.

2 = Não considera valores de juros, multa ou desconto.  
  
Cenário: Quando utilizada a parametrização para abater os impostos no momento da baixa:

**PIS/COFINS/CSLL**

**MV\_BR10925 = 1**

**IRPJ**

Tipo **(A1\_PESSOA)** = Jurídica.

Tp.Entidade **(A1\_ENTID)**= Informe um tipo de entidade diferente de 00, 02 e 10

IRPJ baixa **(A1\_IRBAX)**= 1 - SIM

Aplicação:

**Se o conteúdo do parâmetro MV\_IMPBAIX for igual a 1 – Considera valores**

**Exemplo 1: Baixa Total**

* Incluir um título de R$ 10.000,00 o Sistema gera um registro na tabela SE1.
* 1º Registro com o TIPO: NF com valor de R$ 10.000,00, em aberto com saldo de R$ 10.000,00.
* Efetuar a baixa total, informando um desconto de R$ 1.000,00, a base de cálculo dos impostos será de: R$10.000,00 - R$1.000,00 = R$9.000,00.

|  |  |
| --- | --- |
| **Baixa Total** |  |
|  | **NF** |
| Base de Cálculo | R$9.000,00 |
| PIS | R$58,50 |
| COFINS | R$270,00 |
| CSLL | R$90,00 |
| IRRF | R$135,00 |
| **Valor Recebido** | **R$8.446,50** |

**Exemplo 2: Baixa Parcial**

* Incluir um título de R$ 10.000,00 o Sistema gera um registro na tabela SE1.
* 1º Registro com o TIPO: NF com valor de R$ 10.000,00, em aberto com saldo de R$ 10.000,00.
* Ao efetuar a baixa parcial, informando um desconto de R$ 1.000,00 e valor recebido R$ 7.000,00, ou seja, do título será deduzido do saldo, a base de calculo dos impostos será de R$ 7.000,00 - R$ 1.000,00 = R$ 6.000,00:

|  |  |
| --- | --- |
| **Baixa Total** |  |
|  | **NF** |
| Base de Cálculo | R$6.000,00 |
| PIS | R$39,00 |
| COFINS | R$180,00 |
| CSLL | R$60,00 |
| IRRF | R$90,00 |
| **Valor Recebido** | **R$7.000,00** |

**Se o conteúdo do parâmetro MV\_IMPBAIX for igual a 2 – Não Considera valores**

**Exemplo 3: Baixa Total**

* Incluir um título de R$ 10.000,00 o Sistema gera 1 registro na tabela SE1.
* 1º Registro com o TIPO: NF com valor de R$ 10.000,00, em aberto com saldo de R$ 10.000,00.
* Ao efetuar a baixa total, informando um desconto de R$ 1.000,00, a base de cálculo dos impostos será de: R$ 10.000,00.

|  |  |
| --- | --- |
| **Baixa Total** |  |
|  | **NF** |
| Base de Cálculo | R$10.000,00 |
| PIS | R$65,00 |
| COFINS | R$300,00 |
| CSLL | R$100,00 |
| IRRF | R$150,00 |
| **Valor Recebido** | **R$9.385,00** |

**Exemplo 4: Baixa Parcial**

* Incluir um título de R$ 10.000,00 o Sistema gera 1 registro na tabela SE1.
* 1º Registro com o TIPO: NF com valor de R$ 10.000,00, em aberto com saldo de R$ 10.000,00.
* Ao efetuar a baixa parcial, informando um desconto de R$ 1.000,00 e valor recebido de R$ 7.000,00, ou seja, do título será deduzido do saldo.
* A base de cálculo dos impostos será de R$ 7.000,00 + R$ 1.000,00 = R$ 8.000,00, pois o valor recebido seria de R$ 8.000,00 se não houvesse o desconto.

|  |  |
| --- | --- |
| **Baixa Total** |  |
|  | **NF** |
| Base de Cálculo | R$8.000,00 |
| PIS | R$52,00 |
| COFINS | R$240,00 |
| CSLL | R$80,00 |
| IRRF | R$120,00 |
| **Valor Recebido** | **R$7.000,00** |

**IMPORTANTE:**

Na próxima baixa efetuada para este cliente no mesmo mês o valor do desconto será abatido da base de calculo, pois o valor do desconto deverá ser desconsiderado conforme definido no parâmetro, situação que não pode ocorrer no momento da baixa parcial.

Na baixa parcial o cálculo será sobre o valor recebido do título, Movimento bancário + Desconto – Multas – Juros, pois este valor será deduzido do **E1\_SALDO**, na próxima baixa para o mesmo cliente dentro do mês a diferença desse valor será abatido da base de cálculo.

**Saiba Mais**

[Conceito parâmetro MV\_IMPBAIX](https://tdn.totvs.com/pages/releaseview.action?pageId=73084336)
