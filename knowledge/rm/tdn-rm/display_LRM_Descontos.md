---
content_hash: c3d827f10b83a2c86bf69940c386ec55f9434ed0d4ea0b684b67f1240bf50304
fetched_at: '2026-06-29T00:10:06.567426+00:00'
page_id: '452719316'
product: rm
source: tdn-rm
title: Descontos
type: documentation
url: https://tdn.totvs.com/display/LRM/Descontos
version: 4
---

Nesta etapa será definido como será feito o desconto de INSS no pagamento das férias.  
   
**Parâmetros**  
Sempre desconta no recibo  
Com este parâmetro marcado, no recibo de férias será calculado o INSS de férias com o código de cálculo 82, independentemente do número de dias de férias no mês.  
Com o parâmetro desmarcado, o sistema irá calcular o INSS de férias conforme a regra abaixo:

* Se o funcionário tiver mais de 22 dias de férias no mês, será lançado o código de cálculo 82 no recibo de férias.
* Se o funcionário tiver menos de 22 dias de férias no mês, o INSS de férias não será descontado no recibo de férias, porém o valor deste será abatido da base de IRRF Férias (através do evento com código de cálculo 90 - INSS FERIAS ALÍQUOTA NORMAL e 137 - INSS FERIAS DO PROXIMO MES ALIQUOTA NORMAL).
  + No lançamento das férias, o sistema tributará os valores de férias juntamente com os demais valores do envelope, e lançará o correspondente desconto de INSS no evento de código de cálculo 3 - INSS.
  + Não haverá o lançamento do código de cálculo 82 - INSS FÉRIAS.
  + O valor do INSS a ser abatido do IRRF será o valor do evento de código de cálculo 89 - INSS ALÍQUOTA NORMAL, que será calculado a partir da subtração do evento com código de cálculo 3 - INSS menos o evento com código de cálculo 90 - INSS FERIAS ALÍQUOTA NORMAL.
  + Observando-se a alíquota normal, ou seja, poderá haver uma diferença entre no valor pelo motivo do código de cálculo 3 - INSS estar com a alíquota reduzida.

**Atenção**  
A regra acima somente funciona com o parâmetro desmarcado.

Deduz integral (inclui mês seguinte)  
Marcando este parâmetro, o INSS de Férias será descontado integralmente nas férias (incluindo dedução correspondente ao mês seguinte).   
Com este parâmetro desmarcado, o desconto de INSS de férias proporcional, ou seja, apenas o valor referente ao mês corrente. O valor do INSS a ser deduzido da base de IRRF será o mesmo valor a ser descontado.

**Observação**  
Este parâmetro só é considerado no cálculo de férias partidas e a quantidade de dias de férias no mês for maior ou igual a 22 dias.  
Discrimina INSS no recibo de férias  
Marcando este parâmetro, o evento com o código de cálculo 103 - I.N.S.S. Férias próx. mês será discriminado no Recibo de Férias.   
Exemplo

* Férias de 20/01 a 20/01 – Como as férias estão no próprio mês da competência, o evento com o código de cálculo 82 - I.N.S.S. Férias será descontado integralmente
* Férias 20/01 a 05/02 – Como as férias são partidas, no mês da competência não será descontado o evento de código de cálculo 82 – INSS Férias, mas será descriminado e descontado o evento de código de cálculo 130 - I.N.S.S. Férias próx. Mês. No lançamento das férias para o envelope, não será descontado o evento com o CC82.
* Férias 06/02 a 02/03 – Como no mês das férias os dias de gozo são maior que 22, será descontado o evento de CC 82 e o evento de CC 130.

**Observações**

* Este parâmetro só é considerado no cálculo de férias partidas
* Mesmo não fazendo o desconto no recibo do evento de CC 82, o mesmo é considerado para dedução de IRRF de Férias (evento de CC 30)

**Atenção**  
Este parâmetro só fica habilitado quando o parâmetro 'Deduz INSS Integral' estiver marcado.

Limita desconto do INSS ao teto (férias em meses partidos)  
Com este parâmetro marcado, o desconto do INSS no recibo de férias será limitado ao teto, mesmo que a soma do desconto de INSS de férias no mês  e do próximo mês possa ultrapassar o teto.

**Exemplo**  
Salário: R$ 3500,00  
Período de gozo: 20/03 a 08/04  
Teto desconto INSS: R$ 171,77  
Tabela INSS em vigor:

* Até R$ 468,47 - 8%
* Até R$ 780,78 - 11%
* Até R$ 1561, 56 - 11%

Como  a base de Férias atingiu o teto, o sistema realiza os seguintes cálculos:  
   
Férias: R$ 2333,33 (20 dias)  
1/3 Férias: R$ 777,78  
Base de Férias: R$ 3111,11  
INSS férias no mês: Teto do desconto de INSS (R$ 171,77 / 30) \* 12 dias =   R$ 103,07   
INSS Férias Prox. mês: Teto do desconto de INSS R$ 171,77 - INSS Férias no mês = R$ 68, 70  
   
**Observação**  
Este parâmetro só é considerado no cálculo de férias partidas.  
Para cálculos de múltiplos vínculos o parâmetro “Limita desconto do INSS ao teto (férias em meses partidos) ” será considerado no cálculo por vinculo, ou seja, de acordo com a coligada onde o vínculo está cadastrado será verificado o parâmetro marcado.

Cada competência tem um teto separado, podendo inclusive ter tabelas de INSS diferentes, por exemplo quando existe troca de tabela no segundo mês de férias, cada competência tem um teto diferente.

**Atenção**  
Este parâmetro só fica habilitado quando o parâmetro 'Deduz INSS Integral' estiver marcado.

Desconta integral quando a base de férias atingir o teto (férias durante o mês)  
Este parâmetro só é considerado para cálculo de férias integrais em um único mês. Selecione este parâmetro se pretender que o desconto de INSS seja feito integralmente nas férias (sobre o valor integral do teto) e quando não houver nenhum desconto de INSS no lançamento de folha de pagamento.

**Observação**  
Quando as férias de um funcionário são menores que 30 dias e não são partidas (todos os dias ocorrem em um mesmo mês) e a base de INSS destes dias de férias atingir o teto de INSS, o sistema proporcionaliza o desconto de INSS de acordo com o número de dias de férias para que o restante de desconto de INSS seja efetuado durante o lançamento de folha no mês.   
   
**Exemplo**  
Salário: R$ 2000,00  
Texto do INSS: R$ 132,00  
Período de gozo: 01/11 a 20/11 (20 dias) e 10 dias a abono.  
   
*Com parâmetro 'Desconta integral quando a base de férias atingir o teto' marcado:*  
Dias trabalhados: R$ 666,67  
Férias no mês: 1333,33  
1/3 de Férias:  444,44  
Abono: R$ 666,67  
1/3 de Abono: R$ 222,22  
INSS de Férias: R$ 132,00  
IRRF de Férias: 395,00  
Adiantamento: R$ 2008,00  
Proventos: R$ 3333,84  
Descontos: 2535,34  
Líquido: R$ 798,50  
   
*Com parâmetro 'Desconta integral quando a base de férias atingir o teto' desmarcado:*  
Dias Trabalhados: R$ 666,67  
Arredondamento: R$ 0,17  
Férias no Mês: R$ 1333,33   
1/3 de Férias: R$ 444,44  
Abono: R$ 666,67  
1/3 de Abono: R$ 222,22  
**INSS:** R$ **44,00** (R$132,00/30\*10 dias trabalhados)  
**INSS nas Férias:** R$ **88,00** (R$132,00/30\*20 dias de férias)  
IRRF de férias: R$ 407,00  
Adiantamento: R$ 2084,00  
Proventos   R$ 3333,84  
Descontos   R$ 2623,34  
Líquido     R$ 710,50

Desconsidera projeção dias trabalhados no cálculo alíquota INSS de férias  
Com este parâmetro marcado, o sistema irá calcular a alíquota do INSS para processar os cálculos do INSS de Férias. Com o parâmetro desmarcado, o sistema irá projetar os dias trabalhados e considerará para cálculo a alíquota do INSS de Férias. Caso contrário, o sistema terá como base somente a verbas de férias para o cálculo da alíquota do INSS de férias.

**Exemplo**  
Salário do funcionário: R$ 500,00  
Período de gozo de férias: 15/09/200 a 14/10/2000 (30 dias)  
Tabela de INSS em vigor: Até R$ 398,48 - 8%  
Até R$ 664,13 - 9%  
Até R$ 1328,25 - 11%  
   
**Parâmetro Marcado**  
*Cálculo do Recibo de Férias:*  
Dias Trabalhados: R$ 233,33 (14 dias trabalhados)  
Férias no Mês: R$ 266,67(16 dias)  
Férias Próx. Mês: R$ 233,33 (14dias)  
1/3 Férias no Mês: R$ 88,89  
1/3 Férias Próx. Mês: R$ 77,78  
Arred. Férias: R$ 0,03  
INSS: R$ 24,56 (9%)  
INSS Férias no Mês: R$ 28,44 (8%)  
INSS Férias Prox. Mês: R$ 24,89 (8%)  
Adiant. Conforme Recibo: R$ 613,35   
   
*Cálculo do INSS de Férias no mês:*  
16 dias de Férias no mês (R$ 266,67) + 1/3 de Férias no mês (R$ 88,89) = R$ 355,56 \* 8% = R$ 28,44  
   
*Cálculo do INSS:*  
Remuneração total do mês = R$ 588,89 \* 9% = R$ 53,00  
Subtrai o INSS de Férias no mês = R$ 53,00 - R$ 28,44 = R$ 24,56  
   
*Cálculo do INSS de Férias próx. mês:*  
14 dias de Férias próx. mês (R$ 233,33) + 1/3 de Férias próx. mês (R$ 77,78) = R$ 311,11 \* 8% = R$ 24,89  
   
**Parâmetro desmarcado**  
*Cálculo do Recibo de Férias:*  
Dias Trabalhados: R$ 233,33 (14 dias trabalhados)  
Férias no Mês: R$ 266,67 (16 dias)  
Férias Próx. Mês: R$ 233,33 (14dias)  
1/3 Férias no Mês: R$ 88,89  
1/3 Férias Próx. Mês: R$ 77,78  
Arred. Férias: R$ 0,03  
INSS: R$ 21,00 (9%)  
INSS Férias no Mês: R$ 32,00 (9%)  
INSS Férias Prox. Mês: R$ 28,00 (9%)  
Adiant. Conforme Recibo: R$ 606,70  
    
*Cálculo do INSS de Férias no mês:*  
16 dias de Férias no mês (R$ 266,67) + 1/3 de Férias no mês (R$ 88,89) = R$ 355,56 \* 9% = R$ 32,00   
   
*Cálculo do INSS:*  
Remuneração total do mês = R$ 588,89 \* 9% = R$ 53,00  
Subtrai o INSS de Férias no mês = R$ 53,00 - R$ 32,00 = R$ 21,00  
   
*Cálculo do INSS de Férias próx. Mês:*  
14 dias de Férias próx. Mês (R$ 233,33) + 1/3 de Férias próx. Mês (R$ 77,78) = R$ 311,11 \* 9% = R$ 28,00  
   
**Atenção**  
Com o parâmetro marcado, o sistema não projetou os dias trabalhados do mês da competência para o cálculo da alíquota do INSS.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

<< Retornar para **Férias**
