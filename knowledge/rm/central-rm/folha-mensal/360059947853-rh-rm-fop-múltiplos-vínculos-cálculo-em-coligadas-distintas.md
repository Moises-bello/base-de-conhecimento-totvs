---
article_id: 360059947853
category: Folha Mensal
content_hash: 0999ad454275f7ea8ba64b4bb28fef61a326788fd6641d343cd2d19e7d7846cc
fetched_at: '2026-06-28T22:46:59.468382+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Múltiplos Vínculos: cálculo em coligadas distintas'
type: support-article
updated_at: '2022-04-05T15:49:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059947853-RH-RM-FOP-M%C3%BAltiplos-V%C3%ADnculos-c%C3%A1lculo-em-coligadas-distintas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:05 min  
  
Dúvida**Como calcular funcionário de múltiplos vínculos em coligadas distintas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Nesse exemplo, será demonstrado o cálculo de um funcionário que possui dois vínculos em coligadas distintas, ou seja, uma chapa na coligada 1 e outra chapa na coligada 2.  
  
Tabela de INSS considerada no exemplo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098360734/mceclip0.png)

* **Lançamento da coligada 1**

--> Funcionário coligada 1, chapa xxx, com o salário de 3.000,00.  
--> Foram lançados 30 dias salário.  
  
**Cálculo:** Nesse exemplo, o sistema irá calcular a primeira faixa no evento código de calculo 428: 1.045,00 \* 7,5% = 78,37. Logo, R$3.000,00 – 1.045,00 = 1.955,00. Feito isso, será lançada a segunda faixa no evento código de calculo 429 no valor de 1.044,60 \* 9% = 94,01. Ficando um saldo de 910,40 para a terceira faixa, que será lançado no evento código de calculo 430: 910,40 \* 12% = 109,24. Assim, totalizando um desconto de INSS para o funcionário na coligada 1, no valor de 78,37 + 94,01 + 109,24 = 281,62.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098481874/mceclip0.png)

* **Lançamento da coligada 2**

--> Funcionário coligada 2, chapa yyy, com o salário de 3.500,00  
--> Foram lançados 30 dias salário.  
  
**Cálculo:** Nesse exemplo, o sistema irá calcular a partir da 3ª faixa, pois a primeira, segunda e um pouco do valor da terceira faixa já foram calculadas na Chapa xxx da coligada 1, onde o sistema irá somar a base do INSS do funcionário da coligada 1 com o valor da base do funcionário da coligada 2 e refazer os cálculos a partir da 3 faixa.  
  
Conforme tabela progressiva do INSS, a base de INSS na terceira faixa é no valor de 1.044,80. Como já foi utilizado uma base de 910,40 na coligada 1 para a chapa xxx, onde 1.044,80 – 910,40 = 134,40, será utilizado uma base de 134,40 para a chapa yyy para coligada 2. Portanto, 134,40 \* 12% = 16,12. Como a base do funcionário ultrapassa o teto do INSS, então será calculada a 4ª faixa, onde o teto do INSS é 6.101,06 – o valor da 3ª faixa 3.134,40 = 2.966,66 \* 14% = 415,33. Assim, totalizando o desconto do INSS entre as duas chapas no valor de 78,37 + 94,01 + 109,24 + 16,12 + 415,33 = 713,07.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100731133/mceclip1.png)  
  
**Importante**  
Os valores acima são ilustrativos. A empresa deverá validar a tabela e seus valores.   
  
**Saiba Mais**  
[Novo Cálculo de INSS múltiplos vínculos conforme o eSocial](https://tdn.totvs.com/pages/releaseview.action?pageId=546683921)  
[Cálculo de INSS múltiplos vínculos conforme o eSocial](https://tdn.totvs.com/pages/releaseview.action?pageId=440829559)  
[Configurações Gerais - FOP](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719263)  
[Múltiplos Vínculos que necessitam de Recálculo](https://tdn.totvs.com.br/pages/releaseview.action?pageId=465386747)
