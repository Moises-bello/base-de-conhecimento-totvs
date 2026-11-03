---
content_hash: 5507f51f31e5d38f55ef7735f5b7d96f4bb0f4110a0818a262e7fdf3edd3a40b
fetched_at: '2026-06-29T00:09:28.536434+00:00'
page_id: '423938701'
product: rm
source: tdn-rm
title: Exemplo 3 - Transferência de Grupos Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938701
version: 4
---

**Exemplos de Transferência de rateios gerenciais:**

No caso de se desejar transferir os rateios gerenciais, as contas gerenciais podem não ter seus saldos zerados nas seguintes situações:

a) Existe saldo anterior gerencial em conta contábil que não exige rateio (a conta contábil foi alterada: antes ela tinha rateio e depois deixou de ter). Para evitar este tipo de problema, pode-se executar o processo Zerar Saldo Anterior para contas gerenciais.  
Para o caso da conta contábil que não tinha rateio mas passou a ter, e que possui saldo anterior sem este rateio, o lançamento de transferência para zerar seu saldo anterior, utilizará a conta gerencial de ajuste informada na entrada de dados.

b) A conta gerencial está sendo usada em outras contas contábeis que não participaram da transferência. (Para evitar este tipo de problema, deve-se usar rateio apenas nos grupos que participam da transferência).Ex: Vamos supor que a conta gerencia 5.01 é utilizada nos grupos de Despesas/Custos e Receitas, porém por algum motivo esta conta está sendo utilizada também em um grupo de Compensação. Ao realizar a transferência, os grupos de origem informados são Despesas/Custos e Receitas, desta maneira existirá saldo na conta 5.01 para o grupo de Compensação e como este não participa da transferência, a conta gerencial 5.01 não será zerada.

c) Existem inconsistências na base de dados, como por exemplo registros de rateios sem relacionamento com  lançamento correspondente, etc. O relatório de Consistência de Lançamentos detecta esses erros e em alguns casos os acerta.

d) O saldo em 2º. valor das contas gerenciais não será zerado. O 2º. valor das gerenciais não existe gravado nos lançamentos. Ele é calculado baseando na porcentagem do primeiro valor e, por isso, matematicamente, não é sempre que estes valores são zerados após a transferência.

**Exemplo**

Conta contábil: 3.1.1.1.004

Dois Lançamentos:

1) 1º valor = 2000   
    2º valor = 0  
    Conta gerencial 5.01 = 0 (100%)

2) 1º valor = 1000  
    2º valor = 300  
    Conta gerencial 5.02  (100%)  
   
Lançamento  gerado na Transferência:

1º valor = 3000 (2000+1000)   
2º valor = 300 (0+300)  
Conta gerencial 5.01 – rateio no valor de 2000 (66%)  
Conta gerencial 5.02 – rateio no valor de 1000 (34%)

No exemplo acima se após a transferência de grupos contábeis emitirmos um relatório em segundo valor para a conta 5.01, será apresentado um saldo de 300,00, pois o lançamento de origem da conta 3.1.1.1.004 no valor de 2000,00 possui o segundo valor zerado. Já a conta 5.02 apresentará após a transferência um saldo em segundo valor zerado, pois o lançamento de origem apresenta o segundo valor corretamente.  Para evitar este tipo de situação pode ser executado o processo de 'Recálculo de segundo valor'  marcando a opção 'Recalcula inclusive quando o segundo valor for igual a zero'. Este processo pode ser executado apenas para os lançamentos que estão nestas condições utilizando-se os filtros de data e referência. Caso tenha dúvidas sobre o processo de 'Recálculo de segundo valor' consulte o help.

e) Existem dois lançamentos com valores idênticos, porém em um lançamento a conta que está sofrendo a transferência  está a débito e no outro está a crédito. As contas gerenciais destes dois lançamentos são diferentes. Neste caso o processo de transferência não irá gerar nenhum lançamento, pois o sistema verifica primeiramente se existe saldo para a conta contábil de origem. Caso não exista não é realizado nenhum procedimento.  
   
**Exemplo**

Conta contábil: 3.1.1.1.004

Dois Lançamentos:

1) Data: 01/01/2010  
    Filial: 1 - Centro de Custo: 01 - Depto: 00 - Valor: 100,00  
    Débito:  3.1.1.1.004  
    Crédito: 2.1.1.1.001  
    Rateio Débito: 5.01 = 100,00

2) Data: 01/01/2001  
    Filial: 1 - Centro de Custo: 01 - Depto: 00 - Valor: 100,00  
    Débito:  1.1.1.1.001  
    Crédito: 3.1.1.1.004  
    Rateio Crédito: 5.02 = 100,00

Verificação feita pelo sistema na  Transferência:  
Na Filial: 1 -  Centro de Custo: 01 - Depto: 00 e Conta: 3.1.1.1.004 temos:

100,00 a Débito  
100,00 a Crédito

Saldo Contábil será igual a 0,00

Se o sistema verificar que o saldo contábil é igual a zero não será gerado lançamento de transferência para esta conta contábil, portanto a conta gerencial 5.01 permanecerá com o saldo de 100,00 a débito e a conta gerencial 5.02 permanecerá com o saldo de 100,00 a crédito, ou seja, não serão zeradas na transferência.
