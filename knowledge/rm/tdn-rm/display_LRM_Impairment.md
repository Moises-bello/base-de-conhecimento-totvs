---
content_hash: 7d6d3d3761da678491ffcaa7bc02c9306e8f8ca587e428a2508125899cccfd8c
fetched_at: '2026-06-29T00:09:26.162248+00:00'
page_id: '423938285'
product: rm
source: tdn-rm
title: Impairment
type: documentation
url: https://tdn.totvs.com/display/LRM/Impairment
version: 13
---

O Teste de Impairment é o instrumento utilizado para adequar o ativo a sua real capacidade de retorno econômico, evitando que o mesmo esteja registrado por um valor maior que o valor recuperável.

Com o resultado da aplicação do teste de impairment (compatível com as práticas contábeis adotadas no Brasil e as normas internacionais), não será mais aceito a existência de qualquer ativo, em um balanço patrimonial, por valor superior ao que ele é capaz de produzir de caixa líquido para a entidade, pela sua venda ou pela sua utilização. Atualmente um ativo deverá ser apresentado pelo valor que ele será capaz de se transformar em dinheiro. O teste de Impairment irá diminuir o valor registrado de um ativo e não aumentá-lo, como era o caso do procedimento de reavaliação.

O Impairment estará disponível em Operações Patrimoniais | Impairment, ou pelo aplicativo em Movimentações | Assistentes | Ocorrências Automáticas | Impairment.

**Realizando o Teste de Impairment**

Na primeira etapa deverá ser selecionado um ou mais patrimônios que sofrerão o Teste de Impairment.

Ao avançar etapa, serão apresentados o(s) Código(s) do(s) Patrimônio(s), Descrição e Valor Base, deverá ser informado manualmente a qual Cenário de Cálculo o teste será aplicado. O sistema também irá carregar as informações abaixo:

Depreciação Acumulada ao Final do Mês Anterior: É a depreciação que o patrimônio sofreu até o final do mês de calculo anterior ao cálculo atual.

Valor Contábil: É o custo de aquisição do ativo menos a depreciação acumulada até o momento do teste de recuperação do ativo.

Valor Recuperável (O Valor deste campo pode ser editado):

Trata-se do maior valor entre o valor líquido de venda de um ativo e seu valor em uso.

Ao editar o valor recuperável a taxa de depreciação será automaticamente modificada.

Vida Útil Restante Meses (O Valor deste campo pode ser editado):

Nele será apresentado o tempo de vida restante para o patrimônio se tornar irreparável, seja no contexto operacional, técnico e\ou econômico.

Ao editar a vida útil restante, automaticamente a taxa de depreciação será alterada.

Taxa de Depreciação % Mensal (O Valor deste campo pode ser editado):

Nele será apresentada a taxa de depreciação ao mês do patrimônio. Ao editar esta taxa automaticamente a vida útil restante será modificada.

Nesta etapa deve ser informada a data que será realizada o teste de impairment, o responsável pela realização do mesmo, o número e a data do laudo onde foi constatada a necessidade do teste de recuperabilidade.

O usuário também poderá optar por contabilizar o processo e inserir valores absolutos de impairment, marcando esta última opção o valor de impairment será zerado, mas ainda assim poderá ser editado.

Exemplos:

Em uma base com duas moedas (1-R$ e 2-US$) possuímos um patrimônio onde na tabela de cálculos são apresentadas as seguintes faixas após 30 meses de depreciação:

R$ Normal:

-Valor Base: R$ 10.000,00

– Depreciação Acumulada R$ 5.000,00

– Valor Residual ao final da vida útil R$0,00

- Valor Contábil R$ 5.000,00

US$ Normal:

-Valor Base: US$ 5.000,00

– Depreciação Acumulada US$ 2.500,00

– Valor Residual ao final da vida útil US$ 0,00

– Valor Contábil US$ 2.500,00

Note que a taxa de depreciação deste patrimônio é 20% ao ano. No 31º mês, notamos que o valor de mercado do patrimônio é R$ R$ 4.000,00 e não R$5.000,00, como calculado pelo sistema, então se faz necessário o teste de Impairment somente informando o novo valor de R$ 4.000,00. Neste momento, podemos somente informar R$ 4.000,00 no processo de Impairment ou informar R$ 1.000,00 indicando este como valor absoluto da perda. Ao informar R$ 4.000,00, o sistema automaticamente indicará que R$ 1.000,00 são de perda por Impairment, fazendo com que, no final do mês, na tabela de cálculos, as faixas sejam representadas da seguinte forma:

R$:

-Valor Base: R$ 9.000,00

-Depreciação R$ 150,00

-Depreciação Acumulada R$ 5.150,00

- Impairment R$1.000,00

US$:

- Valor Base: US$ 4.000,00

– Depreciação US$ 66,66

– Depreciação Acumulada US$ 2.575,00

– Impairment US$ 500,00

Vale lembrar que ao realizar o teste de impairment, além de conseguir informar um novo valor para o patrimônio, poderá também informar a nova vida útil deste patrimônio. Se for informada a nova vida útil, o sistema automaticamente deverá recalcular a taxa de depreciação para TODAS as faixas de cálculo deste patrimônio. Caso não seja informado (exemplo acima), o sistema manterá a taxa de depreciação após o impairment resultando em uma diminuição da vida útil.

Observação: Neste exemplo, o impairment fez com que a vida útil do patrimônio diminuísse, pois agora o patrimônio depreciará somente até R$9.000,00 sendo que ele já depreciou R$5.000,00 com 30 meses. Como não foi informada a nova vida útil do patrimônio, o sistema continuará o depreciando com taxa de 20% ao ano.  
   
**Teste de Impairment com Nova Vida Útil**  
   
No exemplo anterior, o Teste de Impairment foi realizado somente alterando o valor do patrimônio e permanecendo a mesma taxa de depreciação, fazendo assim com a vida útil do patrimônio fosse reduzida.  
O sistema permite que seja realizado o Teste de Impairment possibilitando a informação de uma nova vida útil restante para o patrimônio, podendo reduzir, aumentar ou continuar a mesma.  
Ao informar o novo valor do patrimônio, ou o valor do próprio Impairment, o sistema calcula automaticamente a vida útil restante do bem, possibilitando a conferência e atualização da mesma pelo usuário no processo de Impairment.  
Abaixo segue uma simulação do exemplo acima com os mesmos valores, porém com a atualização da vida útil restante do bem para 30 meses, fazendo com que o sistema adeque a taxa de depreciação dos cenários para esta nova durabilidade do bem.

Exemplo: No 31º mês, notamos que o valor de mercado do patrimônio é R$ R$ 4.000,00 e não R$5.000,00, como calculado pelo sistema, então se faz necessário o Impairment somente informando o novo valor de R$ 4.000,00. Neste momento, é possível informar R$ 4.000,00 no processo de Impairment ou informar R$ 1.000,00 indicando este como valor absoluto da perda. Ao informar R$ 4.000,00, o sistema automaticamente indicará que R$ 1.000,00 são de perda por Impairment e que com esta perda, a vida útil restante do patrimônio diminuirá, para 27 meses com taxa de depreciação de 20% ao ano. Como este Impairment significa somente uma provisão de perda do valor do patrimônio em relação ao valor de mercado, na prática, sua vida útil restante teria que continuar a mesma, então informamos que a vida útil restante será de 30 meses. O sistema calculará a nova taxa de depreciação da seguinte forma:

(((9.000,00 – 5000) / 30) \* 100) / 9.000,00 = 1,4815% ao mês = 17,78% ao ano

Com esta nova taxa de depreciação, as faixas de cálculo deste patrimônio do mês ficam da seguinte forma:

R$:

- Vlr Base: R$ 9.000,00

– Depreciação Acumulada R$ 133,34

– Depreciação Acumulada R$ 5. 133, 34

– Impairment R$ 1.000,00

US$:

- Vlr Base: US$ 4.000,00

– Depreciação US$ 59,26

– Depreciação Acumulada US$ 2.566,67

– Impairment US$ 500, 00

**Informações Importantes sobre o cálculo da taxa de depreciação:**

- A taxa de depreciação é sempre aplicada no valor base corrigido e não no valor contábil do patrimônio.

Exemplo - Vamos supor que ao realizar o teste de Impairment para determinado bem seja apresentado os seguintes valores:

Valor Base de Depreciação: R$ 19.338,08  
Deprec. Acum. ao Final do Mês Anterior: R$ 4.189,92  
Valor Contábil: R$ 15.148,16  
Valor Recuperável: R$ 15.148,16  
Vida Útil Restante (meses): 47  
Taxa de Depreciação (%Mensal): 1,667

Se aplicarmos a taxa de depreciação no valor Base de Depreciação chegamos ao seguinte cálculo:  
19.338,08 \* 1,6667% = 322,3013 322,3013 \* 47 = 15.148,16

Ou seja, 15.148,16 é o valor restante que ainda falta para depreciar.

Cálculo realizado pelo sistema para chegar à taxa de depreciação

Vamos supor que o patrimônio apresentou os dados abaixo:

Valor Base de Depreciação: R$ 19.338,08  
Deprec. Acum. ao Final do Mês Anterior: R$ 4.189,92  
Valor Contábil: R$ 15.148,16  
Valor Recuperável: R$ 15.148,16  
Vida Útil Restante (meses): 47  
Taxa de Depreciação (%Mensal): 1,667

Então vamos informar um valor Recuperável de 14.148,16, ou seja, será gerado um Impairment no valor de 1.000,00.  
Se mantermos a vida útil restante em 47 meses a taxa de depreciação será 1,6415.

Como o sistema chega nesta taxa de depreciação:  
O novo Valor Base de Depreciação do bem será de 18.338,08, pois o Impairment no valor de 1.000,00 irá reduzir o Valor Base de Depreciação.

Então o sistema realiza:  
14.148,16(Valor Recuperável) / 18.338,08 (Valor Base de depreciação) \* 100 = 77,1518.  
Então 77,1518% corresponde ao percentual que o patrimônio ainda falta para depreciar. Se pegarmos 77,1518% / 47 (meses) = 1,6415 %  
Aplicando a taxa de depreciação de 1,6415% ao mês no valor base de 18.338,08 chegamos a um valor mensal de depreciação de 301,0247  
Multiplicando 301,02476 por 47 meses chegamos ao valor de 14.148,16, que corresponde ao valor contábil do bem ou o valor que ainda falta para depreciar todo o patrimônio.

Portanto, a taxa de depreciação no sistema Patrimonial sempre deverá ser aplicada no Valor Base de Depreciação.

**OBSERVAÇÕES:**

O impairment de patrimônios, que possuem avaliação deduz o valor da avaliação sem afetar a linha de cálculo não avaliada. Caso o valor do impairment seja maior que o valor da avaliação a diferença (valor do impairment - saldo residual da avaliação) será deduzida da linha de cálculo sem avaliação.

Exemplo:  
O patrimônio 01.01.0001 possui uma linha de avaliação com valor base de R$6000,00 e depreciação de R$60,00. Ele também possui uma linha de cálculo não avaliada com valor base R$25000,00 e depreciação de R$250,00.  
Após sofrer um impairment de R$7000,00 serão geradas duas ocorrências, uma de R$5940,00 para a linha de cálculo avaliada e outra de R$1060,00 para a linha de cálculo sem avaliação. O valor base da linha avaliada irá para R$60,00 e o valor base da linha não avaliada irá para R$23940,00.

Se o impairment for menor ou igual saldo residual da avaliação então será gerada uma ocorrência no valor do impairment para a linha de cálculo avaliada. Para a linha não avaliada será gerada uma ocorrência zerada, pois a vida útil do bem pode ser modificada. Nesse caso a ocorrência zerada precisa ser associada a nova taxa de depreciação, pois se a ocorrência for excluída a taxa também precisa ser eliminada.

**Taxa:**A nova taxa calculada ou informada pelo usuário no momento geração do Impairment, só começará a ser aplicada na próxima competência de cálculo, após impairment*.*

Veja Também

* Revisão de Vida Útil
* Reversão de Impairment
Recursos Adicionais

* [Lei nº 11.638 de 28.12.2007](http://www.normaslegais.com.br/legislacao/lei11638_2007.htm)
* [RESOLUÇÃO CFC Nº. 1.110/07](http://www.normaslegais.com.br/legislacao/resolucaocfc1110_2007.htm)
