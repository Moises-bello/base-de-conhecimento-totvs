---
article_id: 6066289794327
category: Escrita Fiscal - Impostos - ICMS
content_hash: 93e9598cb7ad029c22bbd1bed4d915fa0fefc4182aab61a1636c1158cffbc666
fetched_at: '2026-06-28T22:39:24.067551+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal -
  Como calcular O Difal  pela Diferença de aliquotas em Vendas fora do estado ?
type: support-article
updated_at: '2022-05-13T18:32:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6066289794327-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Gest%C3%A3o-Fiscal-Como-calcular-O-Difal-pela-Diferen%C3%A7a-de-aliquotas-em-Vendas-fora-do-estado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **HH:MM:SS min** **Dúvida**Como calcular Difal  pela Diferença de alíquotas em Vendas?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Foi efetuada a implementação do parâmetro **MV\_UFALCMP**, para permitir o cálculo do DIFAL de duas maneiras distintas: pelo ICMS calculado ou pela diferença de alíquotas (Interna e Interestadual).

Por padrão o cálculo é efetuado pela diferença entre o ICMS calculado. Para configurar o cálculo pela diferença de alíquotas, basta informar os estados (de destino) para os quais esta configuração se aplica, conforme os exemplos abaixo:

 

**Exemplos:**

Base de cálculo: 137,96

Alíquota Interna: 12%

Alíquota Interestadual: 6%

ICMS origem: 16,56

% de Redução Base DIFAL: 41,18%

Base de cálculo reduzida: 137,96 \* 41,18% = 56,81

CST = 20

**Cenário 1** - Cálculo do DIFAL não considerado pelo o ICMS calculado

MV\_UFALCMP = **em branco**

                  Considerando o DIFAL da seguinte forma de cálculo:

           ICMS DIFAL = [BC x ALQ interestadual] - ICMS origem;

           ICMS DIFAL = [56,81 x  6%] - 16,56;

           ICMS DIFAL = [3,41] - 16,56;

                   ICMS DIFAL = - 13,15;

   Neste exemplo, será considerado o valor 0,00 no DIFAL.

**Cenário 2** - Cálculo do DIFAL pela diferença entre alíquota interna e alíquota interestadual

MV\_UFALCMP = **MG/**

                  Considerando o DIFAL da seguinte forma de cálculo:

           ICMS DIFAL = BC x [ALQ interna - ALQ interestadual];

           ICMS DIFAL = 56,81 x [12% - 6%];

           ICMS DIFAL = 56,81 x [6%];

           ICMS DIFAL = 3,41

| **É necessário efetuar o cadastro do novo parâmetro MV\_UFALCMP manualmente, em:**  **SIGACFG → Banco de Dados → Dicionários → Banco de Dados → Parâmetros → Incluir**  **Considerar as informações:**  **Nome de Var.: MV\_UFALCMP**  **Tipo: 1 - Carácter**  **Cont. Port: MG/**  **Descrição: Informe os Estados que calculam DIFAL considerando a diferença entre alíquota interestadual e interna** |
| --- |

## 

Boletim

* [http://tdn.totvs.com/display/public/PROT/FIS0012\_Emenda\_Constitucional\_87\_2015](https://tdn.totvs.com/display/public/PROT/FIS0012_Emenda_Constitucional_87_2015) - Emenda Constitucional 87 2015
