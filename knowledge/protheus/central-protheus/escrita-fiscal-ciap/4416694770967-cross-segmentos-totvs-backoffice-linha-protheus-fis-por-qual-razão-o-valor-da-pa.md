---
article_id: 4416694770967
category: Escrita Fiscal - CIAP
content_hash: 51c951a2e9f3a55d04a99a54a15e507cfe4c136f59e2bedd5725fa468bd65a01
fetched_at: '2026-06-28T22:39:33.942300+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Por qual razão o
  valor da parcela do CIAP varia mensalmente? 
type: support-article
updated_at: '2021-12-21T20:07:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416694770967-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Por-qual-raz%C3%A3o-o-valor-da-parcela-do-CIAP-varia-mensalmente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Por qual razão o valor da parcela do CIAP varia mensalmente?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

O Sistema efetua o cálculo mês a mês, internamente, e o grava no campo **FA\_VALOR,** demonstrado no **Livro CIAP (MATR995):**

**Valor do ICMS / 48 = Valor máximo de Crédito por Parcela \* Fator  = Valor a ser apropriado**  
  
Para aproveitamento do crédito, divida o ICMS constante na Nota de Aquisição pelo fator igual à base 1/48 da relação entre o valor das Operações de Saídas e Prestações Tributadas e o Total das Operações de Saídas e Prestações do Período.  
  
Tendo o valor do ICMS dividido em 48 parcelas, o teto máximo de aproveitamento de crédito por período, sendo aplicado o fator que altera a cada mês, recalcula-se o valor da parcela e é por isso que os valores creditados não são os mesmos.  
  
O sistema faz o cálculo de acordo com a legislação:  
  
**LEI COMPLEMENTAR Nº 87, DE 13 DE SETEMBRO DE 1996**  
  
"..*. I – a apropriação será feita à razão de um quarenta e oito avos por mês, devendo a primeira fração ser apropriada no mês em que ocorrer a entrada no estabelecimento;  (Inciso Incluído pela LCP nº 102, de 11.7.2000)*  
  
*II – em cada período de apuração do imposto, não será admitido o creditamento de que trata o inciso I, em relação à proporção das operações de saídas ou prestações isentas ou não tributadas sobre o total das operações de saídas ou prestações efetuadas no mesmo período;  (Inciso Incluído pela LCP nº 102, de 11.7.2000)*  
  
*III – para aplicação do disposto nos incisos I e II deste parágrafo, o montante do crédito a ser apropriado será obtido multiplicando-se o valor total do respectivo crédito pelo fator igual a 1/48 (um quarenta e oito avos) da relação entre o valor das operações de saídas e prestações tributadas e o total das operações de saídas e prestações do período, equiparando-se às tributadas, para fins deste inciso, as saídas e prestações com destino ao exterior ou as saídas de papel destinado à impressão de livros, jornais e periódicos; (Redação dada pela Lei Complementar nº 120, de 2005)."*

**Observações:**

```
Em caso de dúvidas relacionadas com o cálculo do fator, disponibilizamos este material para consulta:
```

```
https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022837272-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Composi%C3%A7%C3%A3o-do-valor-total-de-sa%C3%ADdas-tributadas-FA-TOTTRIB-e-de-todas-as-sa%C3%ADdas-FA-TOTSAI-no-CIAP
```
