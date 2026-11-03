---
content_hash: 6975795367c0f39e0ec96ee47b0f2a7fb38729a1cc0e5829d387757e733c44fa
fetched_at: '2026-06-29T00:09:24.830500+00:00'
page_id: '423938034'
product: rm
source: tdn-rm
title: Reversão de Impairment
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938034
version: 4
---

Da mesma forma como  teste de impairment é evitar que um ativo esteja registrado por um valor maior que o valor recuperável. A reversão será utilizada em casos que houver alteração nesse valor, desta forma a redução por perdas poderá ser reduzida ou eliminada. Ajustando assim, o valor contábil do patrimônio.

Portanto, o processo de reversão de impairment será utilizado em casos onde for necessário recuperar/desfazer perdas por impairment.  Ou seja, o patrimônio utilizado no processo precisa ter sofrido impairment em **período anterior** (Ou seja, para fazer a Reversão o período em que o Impairment foi realizado deverá estar liberado).

**Realizando a Reversão de Impairment:**

Em uma base possuímos um patrimônio onde na tabela de cálculos são apresentadas as seguintes faixas após 30 meses de depreciação:

R$:

* Valor Base: R$ 10.000,00
* Depreciação Acumulada R$ 5.000,00
* Valor Residual ao final da vida útil R$0,00
* Valor Contábil R$ 5.000,00

Notamos que o valor de mercado do patrimônio é R$ R$ 4.000,00 e não R$5.000,00, como calculado pelo sistema, então se fez necessário o teste de Impairment somente informando o novo valor de R$ 4.000,00. Neste momento, podemos somente informar R$ 4.000,00 no processo de Impairment ou informar R$ 1.000,00 indicando este como valor absoluto da perda. Ao informar R$ 4.000,00, o sistema automaticamente indicará que R$ 1.000,00 são de perda por Impairment, fazendo com que, no final do mês, na tabela de cálculos, as faixas sejam representadas da seguinte forma:

R$:

* Valor Base: R$ 9.000,00
* Depreciação R$ 150,00
* Depreciação Acumulada R$ 5.150,00
* Impairment R$1.000,00

Após 3 meses realizado o impairment verificou- se que a perda não foi de R$1.000,00 e sim de R$400,00. Para que esse processo fosse revertido, foi necessário usar o processo de reversão.

Ao selecionar previamente este patrimônio o sistema irá apresentar na coluna "valor de impairment" R$ 1.000,00, o usuário irá informar manualmente no campo "valor de reversão" R$ 600,00. O sistema irá gerar uma ocorrência de reversão de impairment, a partir deste momento a redução por perdas deste patrimônio será R$ 400,00 e não mais R$ 1000,00.

Contabilização:  
O sistema permite que a reversão seja contabilizada e integrada a Totvs Gestão Contábil.  
   
**Para calcular a taxa de depreciação na Reversão de Impairment o sistema procede da seguinte forma:**

* 1º- Soma o "Valor Contábil" com o "Valor de Reversão": será o novo valor contábil;
* 2º- Soma o "Valor Base de Depreciação" com o "Valor de Reversão": será o novo valor base;
* 3º- Divide o valor contábil calculado no item 1 com o valor base de depreciação calculado no item 2;
* 4º- O resultado encontrado no divisão de valores realizada no item 3 é multiplicada por 100;
* 5º- O valor encontrado no item 4 será dividido pela vida útil restante (meses), sendo o resultado a taxa de depreciação.

Ou seja, como é uma reversão, deve-se considerar o valor da reversão em relação ao valor contábil e o valor base de depreciação.  
   
**Abaixo as regras do sistema para que a reversão seja realizada com sucesso:**

1. Patrimônios Inativos ou totalmente baixados não poderão sofrer a reversão de Impairment.
2. O valor da reversão não pode ser maior do que o valor de impairment realizado anteriormente para os patrimônios envolvidos no processo.
3. Valor de Reversão não pode ser negativo.
4. Data da reversão deve estar dentro do período de cálculo e maior que a data de aquisição do patrimônio.
5. Patrimônios remetidos ou integrados a objetos de manutenção não podem sofrer ocorrência de impairment ou reversão.

Recursos Adicionais

* [Lei nº 11.638 de 28.12.2007](http://www.normaslegais.com.br/legislacao/lei11638_2007.htm)
* [RESOLUÇÃO CFC Nº. 1.110/07](http://www.normaslegais.com.br/legislacao/resolucaocfc1110_2007.htm)
Veja Também
