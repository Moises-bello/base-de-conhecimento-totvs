---
article_id: 360059841373
category: Folha Mensal
content_hash: 0768efed8e8953bdfb85fb5338b2b5680e4c566def01271aa94592fe1c95a3c0
fetched_at: '2026-06-28T22:46:59.475322+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RM - FOP - Como calcular funcionário de múltiplos vínculos numa mesma coligada?
type: support-article
updated_at: '2022-04-05T15:52:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059841373-RM-FOP-Como-calcular-funcion%C3%A1rio-de-m%C3%BAltiplos-v%C3%ADnculos-numa-mesma-coligada
---

**Dúvida**

Como calcular funcionário de múltiplos vínculos numa mesma coligada?  
  
**Ambiente**

RM - Totvs Folha de Pagamento - A partir da 12.1.24  
  
**Solução**

Nesse exemplo, será demonstrado o cálculo de um funcionário que possui dois vínculos na mesma base de dados, ou seja, na mesma coligada.

Tabela de INSS considerada no exemplo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098360734/mceclip0.png)  
  
**Passo 1:**

Será realizado o lançamento da folha competência abril/2020 para as chapas 72547 (1) e 74547 (2), na coligada 1.  
Funcionário chapa 1 – Salario – 2.000,00  
Funcionário chapa 2 – Salario – 7.000,00  
  
**Passo 2:**

Foi realizado lançamento da folha para a segunda chapa 1, com a base de INSS de 2.000,00;

Conforme tabela progressiva, sistema calculou 1.045,00 na primeira faixa no evento código de calculo 428, com a dedução de 7,5% valor de 78,37;

Salario de 2.000,00 – 1.045,00 da primeira faixa, sobrando um valor de 955,00, onde será calculado o valor do INSS na segunda faixa, lançando a base no evento código de calculo 429:  
955,00 \* 9% = 85,95;

Valor do INSS descontado do funcionário chapa 1 – 78,37 + 85,95 = 164,32;

Veja que o sistema lançou os eventos Base INSS Tributária de Folha, primeira e segunda faixa, pois para calcular a segunda chapa, o sistema irá precisar dessas faixas e da base de INSS, para atender ao eSocial.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100599973/mceclip1.png)  
 **Passo 3:**

Foi realizado lançamento da folha para a segunda chapa 2, com a base de INSS de 7.000,00;

Conforme tabela progressiva, sistema irá somar a base de INSS da primeira chapa com a base da chapa 2.

Lembrando que a primeira faixa já foi descontada integralmente na chapa 1, restando um valor de 89,60 para ser calculado na segunda chapa, ou seja 89,60 \*9% = 8,06  / 7.000,00 – 89,60 = 6.910,40;

Calculando 3ª faixa da tabela de INSS: 3.134,40 (teto terceira faixa) – 2.089,60 (teto da segunda faixa) = 1.044,50 \* 12% = 125,34;

Calculando 4ª faixa da tabela de INSS: 6.101,06 (teto da tabela INSS) – 3.134,40 (teto da terceira faixa) = 415,33;

Valor a descontar INSS na chapa 2 – 8,06 + 125,34 + 415,33 = 548,73;

Soma do INSS descontado das duas chapas 72547 (1) e 74547 (2): 548,73 + 164,32 = 713,05;

Lembrando que a soma das duas bases, o desconto não pode ser superior ao teto do INSS: 713,05.

**OBS.:** Caso seja necessário alterar ou inserir qualquer evento no envelope de qualquer chapa, terá que cancelar toda a movimentação das duas chapas e refazer o processo para que o sistema reconheça os valores de acordo com as faixas tributadas.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100600893/mceclip2.png)
