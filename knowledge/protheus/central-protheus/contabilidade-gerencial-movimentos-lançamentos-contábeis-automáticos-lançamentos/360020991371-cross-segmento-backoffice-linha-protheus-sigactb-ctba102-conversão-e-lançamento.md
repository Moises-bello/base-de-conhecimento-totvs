---
article_id: 360020991371
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: 5fe7fc8718638f7ef0eb83d1fd2c5e460475cc0de2abce209a77832ae089e0cc
fetched_at: '2026-06-28T22:40:32.582023+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus- SIGACTB - CTBA102 - Conversão e
  lançamento por conta
type: support-article
updated_at: '2025-09-03T20:28:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020991371-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Convers%C3%A3o-e-lan%C3%A7amento-por-conta
---

**Dúvida**Como realizar a conversão e gerar um lançamento por conta?  
  
**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 12  
  
**Solução**Para realizar a conversão e gerar um lançamento por conta, deve-se utilizar a rotina de laçamento contábil (CTBA101 ou CTBA102) parametrizando as contas com o critério de conversão para a moeda desejada assim com a taxa de conversão.

A seguir veremos os critérios para conversão da Contabilidade Gerencial

**1 – Diária**ou**9 – Vencimento**

Mesmo que tipo **1**

Apesar da nomenclatura **Vencimento**, o critério **9** e o **1** realizam o mesmo cálculo com a taxa do dia da inclusão do lançamento.

Efetua a conversão para a outra moeda pela taxa do dia da inclusão do lançamento.

**2 – Média**ou**8 – Média Histórica**

Mesmo que o tipo **2**

Converte o valor para a outra moeda pela média das taxas do período em que o lançamento é efetuado.

Exemplo: lançamento no dia 20/05/2014 que está no período cinco;

Período 05 -> de 01/05/2014 a 31/05/2014

A taxa de conversão será a soma de todas as taxas do período 05 dividido por 31.

**3 – Mensal**ou**7 – Mensal Histórica**

Mesmo que o tipo **3**

Converte pela taxa do último dia do período.

Exemplo: lançamento no dia 20/05/2014 que está contida no período cinco;

Período 05 ->  de 01/05/2014 a 31/05/2014

o valor será convertido pela taxa do dia 31/05/2014.

**4 – Informada**ou**A – Não Ajusta**

Permite informar e mantém informado, pelo usuário, para a outra moeda. Caso o valor em outra moeda informada seja diferente de zero é gravado **A** no critério de conversão na tabela CT2. Caso o valor for igual a zero é gravado **5** no critério de conversão CT2.

**5 – Não tem Conversão ou 6 – Fixo**

É apresentado mantendo zerado. Não permite digitação de valores para outra moeda, somente zero, mostrando mensagem do critério de conversão.

**Exemplos de contabilização de contas  com diferentes critérios de conversão.**

Critérios de conversão das contas (Com M2 Deb)

1. Lançamento Padrão sem valor informado em outra moeda (moeda 02)  
   ![](https://tdn.totvs.com/download/attachments/155584149/figura01.png?version=1&modificationDate=1409922929000&api=v2)  
     
   ![](https://tdn.totvs.com/download/attachments/155584149/figura02.png?version=1&modificationDate=1409922974000&api=v2)  

   Contabilização de Aquisição de ativos.(Tela de Contabilização)

   ![](https://tdn.totvs.com/download/attachments/155584149/figura03.png?version=1&modificationDate=1409923054000&api=v2)

   Gravação no CT2  
   ![](https://tdn.totvs.com/download/attachments/155584149/figura04.png?version=1&modificationDate=1409923154000&api=v2)
2. Com campo valor em outra moeda (moeda 2) preenchida no lançamento padrão com SN3->N3\_VORIG2.  
   Tela de contabilização de aquisição de ativos:  
   ![](https://tdn.totvs.com/download/attachments/155584149/figura05.png?version=1&modificationDate=1409923207000&api=v2)  

   Gravação no CT2

   ![](https://tdn.totvs.com/download/attachments/155584149/figura06.png?version=1&modificationDate=1409923288000&api=v2)

**Saiba mais**

**[Critérios de conversão](https://tdn.totvs.com/pages/viewpage.action?pageId=155584149)**

**[Utilizando Mais de 5 Moedas](https://tdn.totvs.com/pages/viewpage.action?pageId=312160924)**

[Lançamentos em outras moedas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007149771-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Lan%C3%A7amentos-em-outras-moedas)
