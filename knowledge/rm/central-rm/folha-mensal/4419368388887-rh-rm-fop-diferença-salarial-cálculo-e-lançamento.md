---
article_id: 4419368388887
category: Folha Mensal
content_hash: 5b6f72112b33fafe1fce49a7f176d88361a51dbb462de9083bac0de5cde2e76a
fetched_at: '2026-06-28T22:46:59.257182+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Diferença Salarial  Cálculo e Lançamento
type: support-article
updated_at: '2024-08-01T17:23:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4419368388887-RH-RM-FOP-Diferen%C3%A7a-Salarial-C%C3%A1lculo-e-Lan%C3%A7amento
---

**Competência 04/2020**

* **Coligada 1**

           Salário : R$ 600,00

**Envelope :**

                    Horas Normais :   R$ 600,00

                     Base tributada de INSS Folha 1 faixa :  600,00  - 7,5 %

                     INSS : 45,00  - 7,5 %

* **Coligada 2**

 Salário : R$ 400,00       

**Envelope:**

                     Horas Normais :  400,00

                     Base tributada de INSS Folha 1 faixa :  400,00  - 7,5 %

                     INSS : 30,00  - 7,5 %

**Competência 05/2020**

* **Coligada 1**

**Reajuste Salarial**

                Novo Salário: R$ 1.000,00   - Diferença Salarial: R$ 400,00

**Calculando a diferença salarial retroativo a competência 4**

**Diferenças do período Mês/Ano: 4/2020 Período: 1**----------------------------------------------------------------------------  
Código    Descrição                                                    Ref.            Hora                  Valor  
0001  HORAS NORMAIS                                           220,00         220:00               400,00 P  
0003  INSS                                                                 9,00            000:00               35,32 D  
0238  BASE DE FGTS DIF SALARIAL 0,00                                      000:00               400,00 B  
s428  BASE TRIBUTADA DE INSS FOLHA 1º FAIXA    7,50             000:00              45,00 B  
S429  BASE TRIBUTADA DE INSS FOLHA 2º FAIXA    9,00            000:00               355,00 B

Ao calcular a diferença salarial, o sistema soma as bases de todos os vínculos do funcionário na competência do cálculo da diferença, 04/2020, verifica o que já foi tributado e em qual faixa o valor da diferença se enquadra. As faixas referentes reajuste salarial são armazenadas na tabela **PFVERBASDIS**.    
  
No exemplo, as bases de INSS foram somadas nas duas coligadas verificando-se que já havia sido tributado R$ 1.000,00 na 1ª faixa, restando o valor de R$ 45,00 para tributar nessa faixa. O valor restante R$ 355,00 foi tributado na segunda faixa, resultando em um desconto de INSS de R$ 35,32 sendo:

* 7,5% de R$ 45,00 = 3,37
* 9% de R$ 355,00 = 31,95

**Valor Armazenado na Ficha Financeira - Verbas Geradas por Diferença - PFVERBASDIS:**

* Horas normais      R$ 400,00
* INSS                      R$ 35,32 - 7,5% de R$ 45,00 + 9% de R$ 355,00
* Base tributada de INSS folha 1 faixa  -  R$ 45,00
* Base Tributada de INSS  folha 2 faixa -  R$ 355,00

**Envelope de diferença acumulada até o período Mês/Ano: 5/2020 Período: 1  
----------------------------------------------------------------------------**Código     Descrição                                   Ref.               Hora                    Valor  
0244  DIFERENCA SALARIAL - DISSÍDIO   220,00           220:00                 400,00 P  
0237  INSS DIFERENCA SALARIAL             9,00              000:00                 35,32 D  
0238  BASE DE FGTS DIF SALARIAL           0,00              000:00                 400,00 B

**Importante:** Caso haja a necessidade de refazer o processamento da Diferença Salarial, é necessário que seja realizado o processo de Cancelamento do Movimento para que as verbas de Diferença possam ser devidamente canceladas. Logo após, o processo de Diferença Salarial poderá ser executado novamente.

Para verificar o material referente ao Cancelamento das verbas, **[CLIQUE AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057701274-RH-RM-FOP-Cancelamento-do-Movimento).**
