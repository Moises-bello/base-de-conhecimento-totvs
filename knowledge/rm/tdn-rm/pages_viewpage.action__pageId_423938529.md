---
content_hash: 5f1e35352b9414f31d9eb85a0e56e1bb1370645318f1fade5cf9eea63645565b
fetched_at: '2026-06-29T00:09:27.507016+00:00'
page_id: '423938529'
product: rm
source: tdn-rm
title: Criação de Moldes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938529
version: 2
---

Cada molde criado corresponderá a uma partida no lançamento a ser gerado por esta estrutura e seguirá as mesmas regras e validações existentes no cadastro de partidas dos lançamentos. Crie quantos moldes desejar.

Em cada molde deverão ser preenchidas as informações que serão fixas nas partidas dos lançamentos, bem como definidas quais informações poderão ser preenchidas no momento da geração automática dos lançamentos correspondendo à parte flexível, utilizando para isto as variáveis criadas anteriormente.

Ao lado de cada campo existe uma caixa que deverá ser marcada no caso de se desejar utilizar neste campo uma variável ao invés de um valor fixo, em seguida informe a variável correspondente.

**Expressão de Valor**

Ao criar um molde, os campos *Valor* e/ou *Valor 2ª Moeda* podem ser preenchidos com valores fixos ou utilizar variáveis que receberão os valores no momento da geração dos lançamentos ou ainda utilizar expressões para calcular os respectivos valores.

Para fazer uso deste recurso deve-se primeiro cadastrar uma variável do tipo *valor*, marcar a utilização de uma variável no campo Valor e em seguida acessar a função de expressão clicando no ícone que será apresentado logo a seguir. Veja que para usar uma expressão, não é necessário indicar uma variável no campo Valor e sim, montar uma expressão utilizando a variável criada.

**Exemplo de utilização da função Expressão de Valor:**

Suponhamos que você esteja criando uma estrutura de lançamentos para recolhimento de uma dívida parcelada. E que cada parcela da dívida corresponda a 5% do total, mais juros de 2% ao mês.   
Crie uma estrutura de Lançamentos Periódicos. Em seguida crie a variável VALOR (do tipo Valor), crie também um molde colocando os dados nos campos necessários, como Conta, Filial etc. Indique a utilização de variável no campo Valor, e clique no ícone que será apresentado logo à frente para criar uma expressão. Será aberta uma área para a criação da expressão. Em Parâmetros selecione a variável criada e monte a expressão como no exemplo:  (VALOR\*5/100) + ( (VALOR\*5/100)\*2/100)

Esta expressão lhe dará o valor da parcela a ser paga. Na hora de gerar o lançamento, na variável VALOR, você deverá informar o valor total da dívida, para que o sistema calcule corretamente.  
Você poderá optar por não criar uma variável para VALOR, caso este valor seja fixo até o restante da dívida, e no lugar de VALOR, que é sua variável, informar o valor real da dívida.  
Assim:  (100000\*5/100) + ((100000\*5/100)\*2/100)  
Neste caso, a variável para o campo VALOR nem precisa ser criada.  
Para o campo *Valor 2ª Moeda* o mesmo procedimento acima pode ser utilizado.  
Você poderá utilizar além de variáveis, as funções disponíveis assim como números e operadores lógicos (+, /, -, \*.^).

**Observações**

* O cadastro de variáveis não é obrigatório na inclusão de uma estrutura.
* As variáveis só poderão ser utilizadas nas estruturas em que foram criadas.
* Uma estrutura pode ter um ou vários moldes que podem utilizar a mesma variável ou variáveis distintas. No caso de se utilizar a mesma variável em mais de um molde da estrutura, todas as partidas geradas que utilizarem a mesma variável receberão o mesmo valor no campo correspondente. Caso em mais de um molde seja necessário utilizar variáveis para o mesmo campo, mas estas necessitem receber valores distintos, crie uma variável para ser utilizada em cada molde, informando para todas elas o mesmo tipo. Crie, por exemplo na estrutura **X**, a variável **CONTACRED1** para ser utilizada no molde 1 e também a variável **CONTACRED2** para ser utilizada no molde 2.
