---
content_hash: 160894cf45d0bce548edfa3565173a8eae78c6af2808c4a27c80a303b5776c75
fetched_at: '2026-06-29T00:10:05.065238+00:00'
page_id: '452719272'
product: rm
source: tdn-rm
title: Fórmulas / Funções – M
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719272
version: 10
---

**Função Max**  
Retorna o maior valor entre dois valores informados.  
MAX (VALOR, VALOR)  
   
   
**Função MEDCOMIS**  
Retorna o valor da Média de Comissão referente ao campo "Número de Meses" em Administração de Pessoal | Sindicato para funcionários tipos O - Comissionista, F - Temporário/Comissionista e M - Misto.  
Quando o valor do mínimo garantido pelo Sindicato for maior que o valor da média calculada, o sistema tem a opção para que retorne o valor da média calculada. Para isto é necessário adicionar na formula o parâmetro 'PARAMS: S', para ignorar o mínimo do sindicato.  
A formula ficaria assim: MEDCOMIS ("STRING PARAMS:S'), onde:  
   
STRING seria de acordo com os tipos de média abaixo:   
**1** para Férias·   
**2** para13º Salário·  
**3** para Aviso Prévio·  
**4** para Licença maternidade  
**5** para Avos Totais de Férias (entre vencidas e proporcionais)   
   
PARAMS é uma variável fixa que indica se irá ignorar ou não o mínimo garantido. Se informar S, o mínimo será ignorado. Se for N, será considerado o mínimo do sindicato.  
   
**Observação**  
   
Mesmo informando N para a variável PARAMS e o mínimo do sindicato seja menor que o valor da média encontrado, deverá retornar o de maior valor, que neste caso, é a médica calculada.  
A utilização do Parâmetro PARAMS na fórmula é opcional. Caso use somente a variável STRING, sempre irá retornar o de maior valor encontrado entre média calculada ou mínimo garantido. Neste caso a Fórmula ficaria assim: MEDCOMIS (STRING).  
Os eventos de comissão devem estar com o campo "Compõe Comissão" marcado.  
   
   
**Função MEDCOMISDATA.**  
Retorna o valor da Média de Comissão de acordo com o sindicato e com a data informada para funcionários tipos O - Comissionista, F - Temporário/Comissionista e M - Misto.  
MEDCOMISDATA (VALOR, VALOR, DATA)  
Onde:  
**VALOR1**:  
Informar o tipo de média que será calculado.  
**VALOR2**:   
Informar o tipo de processo (férias, cálculo da folha ou rescisão) que será calculado.  
**DATA:**  
Informar a data que será realizado o cálculo da Média.  
   
**Observações:**  
De acordo com a sintaxe **MEDCOMISDATA (VALOR1, VALOR2, DATA):**  
**VALOR1 -** Neste campo poderão ser usados os seguintes valores de retorno**:**  
**1** para Férias  
**2** para13º Salário  
**3** para Aviso Prévio  
**5** para férias proporcionais  
   
**VALOR2 -** Neste campo poderão ser usados os seguintes valores de retorno:  
**1** para Férias  
**2** para13º Salário  
**3** para Rescisão  
**5** para férias proporcionais  
   
**DATA -** Informar a data que será realizado o cálculo da Média de Comissão, exemplo: TABFUNC ('DATADEMISSAO'), TABFUNC ('INICPROGFERIAS1' ou **0(ZERO)** para que o cálculo seja realizado na competência atual.

**Exemplos:**

**MEDCOMISDATA (1, 1, TABFUNC ('INICPROGFERIAS1', 'D'))**  
Retorna as médias de Comissão de férias(**1**) no cálculo das Férias(**1**) observando o início de gozo do funcionário.   
   
**MEDCOMISDATA (1 ,3, TABFUNC ('DATADEMISSAO', 'D'))**  
Retorna as média de Comissão de Férias(**1**) na rescisão(**3**), verificando a data de demissão do funcionário.  
   
**MEDCOMISDATA (2 ,3, 0)**  
Retorna as médias de Comissão de 13º Salário (**2**) na Rescisão (**3**), verificando a data da competência atual.  
   
**MEDCOMISDATA (3 ,3, TABFUNC ('DATADEMISSAO', 'D'))**  
Retorna as médias de Comissão de Aviso Prévio (**3**) na Rescisão (**3**), verificando a data de demissão do funcionário.

**Função MEDREMBASE**

Média de Remuneração por Base que será calculada de acordo com a parametrização da pasta Remuneração Base habilitada quando marca o parâmetro 'Utiliza cálculo de média de remuneração base para professor' na pasta Média do cadastro de sindicatos.

MEDREMBASE( VALOR , VALOR )

Onde os valores utilizados para o retorno dos tipos de médias pela MEDREMBASE são:

Primeiro VALOR:  
1 para Férias  
2 para Férias Rescisão  
3 para 13º Salário  
4 para 13º Rescisão  
5 para Aviso Prévio  
6 para Licença maternidade

Segundo VALOR:  
1 - Período de Férias Vencido  
2 - Período de Férias Proporcionais

**Observação:** O Segundo VALOR só será considerado, quando o Primeiro VALOR for 1 - Férias ou 2 – Férias Rescisão. Esse valor só terá efeito quando no Cadastro do Sindicato estiver configurado para considerar o período aquisitivo na apuração da média, ou seja, “Quantidade de meses” igual a zero nas subpastas Férias e Férias Rescisão da pasta Remuneração Base.

**Atenção:** Para os outros cálculos o segundo Valor deve ser passados como (0) Zero.

**Exemplos:**

MEDREMBASE(1, 1) - Retornará o valor da média de Férias no Período de Férias Vencido

MEDREMBASE(1, 2) - Retornará o valor da média de Férias no Período de Férias Proporcionais

MEDREMBASE(2, 1) - Retornará o valor da média de Férias Rescisão no Período de Férias Vencido

MEDREMBASE(2, 2) - Retornará o valor da média de Férias Rescisão no Período de Férias Proporcionais

MEDREMBASE(3, 0) - Retornará o valor da média de 13º Salário

MEDREMBASE(4, 0) - Retornará o valor da média de 13º Rescisão

MEDREMBASE(5, 0) - Retornará o valor da média de Aviso Prévio

MEDREMBASE(6, 0) - Retornará o valor da média de Licença maternidade

**Função MEDREMBASEDATA**

Média de Remuneração por Base por data que será calculada de acordo com a parametrização da pasta Remuneração Base habilitada quando marca o parâmetro 'Utiliza cálculo de média de remuneração base para professor' na pasta Média do cadastro de sindicatos.

MEDREMBASEDATA ( VALOR, VALOR, DATA )

Primeiro VALOR:  
1 para Férias  
2 para Férias Rescisão  
3 para 13º Salário  
4 para 13º Rescisão  
5 para Aviso Prévio  
6 para Licença maternidade

Segundo VALOR:  
1 - Período de Férias Vencido  
2 - Período de Férias Proporcionais

**Observação:** O Segundo VALOR só será considerado, quando o Primeiro VALOR for 1 - Férias ou 2 – Férias Rescisão. Esse valor só terá efeito quando no Cadastro do Sindicato estiver configurado para considerar o período aquisitivo na apuração da média, ou seja, “Quantidade de meses” igual a zero nas subpastas Férias e Férias Rescisão da pasta Remuneração Base.

**Atenção:** Para os outros cálculos o segundo Valor deve ser passados como (0) Zero.

**DATA -** Informar a data que será realizado o cálculo da Média, exemplo: TABFUNC ('DATADEMISSAO'), TABFUNC ('INICPROGFERIAS1'.

Modelos:

MEDREMBASEDATA (1, 1, DATA) - Retornará o valor da média de Férias no Período de Férias Vencido e na data selecionada

MEDREMBASEDATA (1, 2, DATA) - Retornará o valor da média de Férias no Período de Férias Proporcionais e na data selecionada

MEDREMBASEDATA (2, 1, DATA) - Retornará o valor da média de Férias Rescisão no Período de Férias Vencido e na data selecionada

MEDREMBASEDATA (2, 2, DATA) - Retornará o valor da média de Férias Rescisão no Período de Férias Proporcionais e na data selecionada

MEDREMBASEDATA (3, 0, DATA) - Retornará o valor da média de 13º Salário na data selecionada

MEDREMBASEDATA (4, 0, DATA) - Retornará o valor da média de 13º Rescisão na data selecionada

MEDREMBASEDATA (5, 0, DATA) - Retornará o valor da média de Aviso Prévio na data selecionada

MEDREMBASEDATA (6, 0, DATA) - Retornará o valor da média de Licença maternidade na data selecionada

**Exemplos:**  
MEDREMBASEDATA (1 1,,TABFUNC ('INICPROGFERIAS1', 'D'))

Retorna as médias da remuneração base de férias (1) de acordo com o período aquisitivo vencido, observando o início de gozo do funcionário. Como essa data é a data de marcação das férias o parâmetro “Considera mês atual”, na subpasta Férias da pasta Remuneração Base no cadastro de sindicato, deve estar marcado para considerar até o mês atual.

MEDREMBASEDATA (3, 0, TABFUNC ('DATADEMISSAO', 'D'))

Retorna as médias da remuneração base de Aviso Prévio (3) verificando a data de demissão do funcionário. Caso essa data de demissão seja na competência atual o parâmetro “Considera mês atual”, na subpasta Aviso Prévio da pasta Remuneração Base no cadastro de sindicato, deve estar marcado para considerar até o mês atual.

**Observação:**

**01 -** Para a função de fórmula MEDREMBASEDATA, sempre que utilizar data que envolva a competência atual o parâmetro “Considera mês atual” deve estar marcado dentro de cada subpasta da pasta Remuneração Base no cadastro de sindicato, para que seja considerado.

**02 –** Quando está utilizando a função MEDREMBASEDATA com o parâmetro do Segundo VALOR igual a 1 - Período de Férias Vencido e a data selecionada for menor que o período aquisitivo será retornado 0 (zero) porque passa a ser férias proporcionais. Por exemplo:

Na MEDREMBASEDATA (1, 1, 01/07/2021), se insere a data 01/07/2021 e maior que isso informa cálculo, se inserir a data 01/06/2021 apresentará valor zero. Sendo que o período aquisitivo é 01/08/2020 a 31/07/2021. Com a data do mês 6 o período passa a ser proporcional por isso retorna zero, pois no segundo parâmetro está férias vencidas e deveria ser férias proporcionais.

   
**Função MEDSUBST**  
Retorna o valor da média de substituição do funcionário, tendo como base o intervalo de datas de substituição informado como parâmetro.  
MEDSUBST ('DATA DE INICIO DO INTERVALO', 'DATA DE FIM DO INTERVALO', 'NUMERO DE MESES PARA MEDIA ')  
   
**Observação:**  
O número de horas utilizado no cálculo é o número de horas calculado e não mais o informado pelo usuário. Teoricamente, este valor já deve estar na tabela de substituições na hora do cálculo da fórmula. O mesmo é preenchido durante o cálculo da movimentação do funcionário.  
   
   
**Exemplo:**  
Em Administração de Pessoal l Funcionários l ícone visualizar ficha financeira | pasta substituição.  
Suponhamos que o Funcionário substitui dois funcionários:  
1) No mês 10/2013, 10 dias (73:20 horas) na função do funcionário 00203.   
2) No mês 11/2013, 30 dias (220:00 horas) na função do funcionário 00202.  
   
**Cadastrar a formula abaixo:**  
MEDIASUBST('01/01/2013', '30/11/2013', 11)  
   
**Demonstração do Cálculo da Fórmula:**  
Salário hora dos Funcionários Substituídos:  
Funcionário 00203: 361,00 / 220 = 1,64  
Funcionário 00202: 585,26 / 220 = 2,66  
Salário hora do Funcionário Substituido:  
185,26 / 220 = 0,84  
Transformar o número de horas substituídas em minutos:  
73:20 horas = 4400 minutos  
220:00 horas = 13200 minutos  
Diferença entre o salário hora do substituído e do Substituido:  
1,64 - 0,84 = 0,80  
2,66 - 0,84 = 1,82  
Cálculo da Média:  
(4400 / 60) / 11 \* 0,80 = 5,33  
(13200/ 60) / 11 \* 1,82 = 36,36  
5,33 + 36,36 = **41,69** (Resultado da fórmula).  
   
   
   
   
**Função Memoria**   
Retorna um valor armazenado em memória  
MEMORIA (INDEFINIDO)  
   
**Observações:**  
-Tipo de retorno: indefinido (de acordo com conteúdo da memória)  
-Para atribuir valor a uma memória, deve-se usar a função **Atribui.**  
   
   
**Função Mês**  
Retorna mês de competência.  
Mês  
   
**Função MESCX**  
Retorna mês-caixa.  
MESCX  
   
**Função MESDT**  
Retorna o mês de uma data.  
MESDT (DATA)  
   
   
**Exemplo**

MESDT (22/08/1997)  
Retornará '8'.  
   
   
**Função MH**  
Retorna os minutos de um evento da ficha financeira.  
MH (MÊS, ANO, 'CÓD. DO EVENTO)  
   
   
**Observação:**  
O parâmetro **MÊS** da variável acima é o seguinte **Meses para Pesquisa**  
**0 - do ano informado**  
MH (0,2013,'0001')  
Esta fórmula retorna o total de minutos do evento 0001 do ano informado (segundo parâmetro) na ficha financeira.  
   
**15 - do ano corrente**  
MH (15,0,'0082')  
Esta fórmula retorna o total de minutos do evento 0082 na ficha financeira do ano corrente.   
   
**16 - do período aquisitivo**   
MH (16,0,'0082')  
Esta fórmula retorna o total de horas do evento 0082 conforme o último período Aquisitivo no Histórico de Férias do funcionário.   
   
**Observação:**   
**1 -** Para férias o parâmetro de ano não será considerado, ou seja, retorno referente a férias será considerado o primeiro período aquisitivo em aberto encontrado para o funcionário.   
**2 -** Os eventos serão contabilizados no final do período aquisitivo quando o mês for partido.  
**Exemplo:** Período aquisitivo de 16/10/2015 a 15/10/2016 e 16/10/2016 a 15/10/2017, se houver evento de faltas a serem considerados em 10/2016, este evento será considerado para o período 16/10/2015 a 15/10/2016 que termina em 10/2016.  
   
Para os meses 17, 18, 19 e 20, os cálculo serão verificados em Administração de Pessoal | sindicatos | pasta médias nos campos "Número de Meses"  
   
**17 - do período da média de férias;(Tipo de média)**  
**MH (17,0,'0082')**  
Esta fórmula retorna o total de horas do evento 0082 conforme o período da Média de Férias do sindicato do funcionário. Se no sindicato estiver parametrizado com média do período aquisitivo o sistema retornará o total de horas do evento dentro do período aquisitivo de férias do funcionário.   
   
**18 - do período da média de 13º; (Tipo de Média)**  
**MH (18,2013,'0082')**  
Esta fórmula retorna o total de minutos do evento 0082 conforme o período da Média de 13o Salário do sindicato do funcionário.   
19 - do período da média de aviso prévio e;(Tipo Média)  
   
**MH (19,2013,'0082')**  
Esta fórmula retorna o total de minutos do evento 0082 conforme o período da Média de Aviso do sindicato do funcionário.  
20 - do período da média de licença maternidade. (Tipo Média)  
   
**MH (20,2013,'0084')**  
Esta fórmula retorna o total de minutos do evento 0082 conforme o período da Média de Licença Maternidade do sindicato do funcionário  
   
   
   
**Função MIM**  
Retorna o menor valor entre dois valores informados.  
MIN (VALOR, VALOR)  
   
   
**Função Minga**  
Retorna mínimo garantido pelo sindicato.  
MINGA  
   
**Função MINGADATA**  
Retorna mínimo garantido pelo sindicato em uma determinada data  
MINGADATA (DATA)  
   
**Exemplo:**  
MINGADATA(01/10/2013),   
Retornará o valor do mínimo garantido estipulado a partir de 01/10/2013  
   
**Função MN**  
Retorna o número de ocorrências de um evento na ficha financeira.  
MN (MÊS, ANO, 'CÓD. DO EVENTO)  
   
**Observação:**  
O parâmetro **MÊS** da variável acima é o seguinte **Meses para Pesquisa.**  
**0 - do ano informado**  
**MN (0,2013,'0001')**  
Esta fórmula retorna o total de ocorrência do evento 0001 do ano informado (segundo parâmetro) na ficha financeira.  
   
**15 - do ano corrente**  
**MN (15,0,'0082')**  
Esta fórmula retorna o total de ocorrências do evento 0082 na ficha financeira do ano corrente.   
   
**16 - do período aquisitivo**   
**MN (16,0,'0082')**  
Esta fórmula retorna o total de ocorrências do evento 0082 conforme o último período Aquisitivo no Histórico de Férias do funcionário.   
Para os meses 17, 18, 19 e 20, os cálculo serão verificados em Administração de Pessoal | sindicatos | pasta médias nos campos "Número de Meses"  
   
**17 - do período da média de férias;(Tipo de média)**  
**MN (17,0,'0082')**  
Esta fórmula retorna o total de ocorrências do evento 0082 conforme o período da Média de Férias do sindicato do funcionário. Se no sindicato estiver parametrizado com média do período aquisitivo o sistema retornará o total de horas do evento dentro do período aquisitivo de férias do funcionário.   
   
**18 - do período da média de 13º; (Tipo de Média)**  
**MN (18,2013,'0082')**  
Esta fórmula retorna o total de ocorrências do evento 0082 conforme o período da Média de 13o Salário do sindicato do funcionário.   
19 - do período da média de aviso prévio e;(Tipo Média)  
   
**19 - do período da média de aviso prévio; (Tipo de Média)**  
**MN (19,2013,'0082')**  
Esta fórmula retorna o total de ocorrências do evento 0082 conforme o período da Média de Aviso do sindicato do funcionário.  
20 - do período da média de licença maternidade. (Tipo Média)  
   
**20 - do período da média de Licença Maternidade; (Tipo de Média)**  
**MN (20,2013,'0084')**  
Esta fórmula retorna o total de ocorrências do evento 0082 conforme o período da Média de Licença Maternidade do sindicato do funcionário  
   
**Função MR**  
Retorna o valor da referência de um evento da ficha financeira.  
MR (MÊS, ANO, 'CÓDIGO DO EVENTO')  
   
**Observação:**  
O parâmetro **MÊS** da variável acima é o seguinte **Meses para Pesquisa.**  
**0 - do ano informado**  
MH (0,2013,'0001')  
Esta fórmula retorna o total de minutos do evento 0001 do ano informado (segundo parâmetro) na ficha financeira.  
   
**15 - do ano corrente**  
MH (15,0,'0082')  
Esta fórmula retorna o total de minutos do evento 0082 na ficha financeira do ano corrente.   
   
**16 - do período aquisitivo**   
MH (16,0,'0082')  
Esta fórmula retorna o total de horas do evento 0082 conforme o último período Aquisitivo no Histórico de Férias do funcionário.   
Para os meses 17, 18, 19 e 20, os cálculo serão verificados em Administração de Pessoal | sindicatos | pasta médias nos campos "Número de Meses"  
   
 **17 - do período da média de férias;(Tipo de média)**  
**MH (17,0,'0082')**  
Esta fórmula retorna o total de horas do evento 0082 conforme o período da Média de Férias do sindicato do funcionário. Se no sindicato estiver parametrizado com média do período aquisitivo o sistema retornará o total de horas do evento dentro do período aquisitivo de férias do funcionário.   
   
**18 - do período da média de 13º; (Tipo de Média)**  
**MH (18,2013,'0082')**  
Esta fórmula retorna o total de minutos do evento 0082 conforme o período da Média de 13o Salário do sindicato do funcionário.   
19 - do período da média de aviso prévio e;(Tipo Média)  
   
**MH (19,2013,'0082')**  
Esta fórmula retorna o total de minutos do evento 0082 conforme o período da Média de Aviso do sindicato do funcionário.  
20 - do período da média de licença maternidade. (Tipo Média)  
   
**MH (20,2013,'0084')**  
Esta fórmula retorna o total de minutos do evento 0082 conforme o período da Média de Licença Maternidade do sindicato do funcionário  
   
   
   
   
**Função MTDATA**  
Monta uma data a partir de um dia, um mês e um ano informados.  
MTDATA (DIA, MES, ANO)  
   
**Exemplo:**  
MTDATA(1,9,2013) = 01/09/2013.  
   
   
**Função MUDOUCCUSTOMES**  
Retorna 1 (um) quando o funcionário estava, no fim da competência anterior, em centros de custos diferente do atual. Em caso contrário, a função retorna 0 (zero).  
MUDOUCCUSTOMES  
   
   
   
   
**Observações:**

* A variável de fórmula MUDOUCCUSTOMES - "Mudou de Centro de Custos no Mês" será utilizada na operação de estorno da contabilização de encargos para os funcionários transferidos entre seções de um mesmo CGC e com centros de custos distintos.
* A variável de fórmula MUDOUCCUSTOMES para efeitos de comparação, considera os centros de custos associados às seções onde o funcionário estava lotado no fim das competências atual e anterior. Se o funcionário mudou para uma seção diferente no início da competência atual e retornou para a mesma seção em que estava lotado no fim da competência anterior, o resultado da função retornará Falso (zero).
* Os centros de custos considerados são centros de custos do Folha de Pagamento. A variável MUDOUCCUSTOMES não compara mudanças de centros de custos de Globais.
* Quando a variável MUDOUCCUSTOMES for utilizada na Folha Analítica ou Contabilização o sistema irá verificar o mês e ano informado na geração dos relatórios invés do mês e ano da competência da base.  
    
  **Exemplos:**  
  -**Funcionário chapa 00002:**  
   Centro de Custos 01.05 - associado à Seção atual: 01.02  
   Centro de Custos 01.01 - associado à Seção anterior: 01.03.  
   Retorna 1, pois de acordo o centro de custos associado à seção 01.02 é diferente do o centro    de custos associado à seção 01.03.  
  + Funcionário chapa 00005:\*  
    Centro de Custos 01.01 - associado à Seção atual: 01.07  
    Centro de Custos 01.01 - associado à Seção anterior: 01.08  
    Retorna 0, pois apesar das seções serem diferentes, o centro de custos associado a ambas é o mesmo.  
      
      
    **Função MUDOUSECMES**  
    Retorna se 1 (um) se o funcionário estava no final da competência anterior, em seção diferente da seção atual, caso contrário retorna 0.  
                MUDOUSECMES(STRING)   
    Onde STRING é o código de quebra que será analisado.   
      
      
    **Exemplo:**  
    Seção atual =01.12  
    Seção anterior =01.03  
      
    **1) MUDOUSECMES ('?????'),** neste caso a fórmula retornará =1 (verdade), pois houve mudança de seção na quebra informada na fórmula, 5(cinco) interrogações.  
      
    **2) MUDOUSECMES ('??'),** neste caso a fórmula retornará=0 (falso), pois não houve alteração de seção na quebra informada na fórmula, 2(duas) interrogações.  
      
    **MVRUBRICA**  
    Retorna o somatório dos valores de eventos de CC 480 que contenham o código da rúbrica 9253 em seu cadastro.  
    MVRUBRICA (MÊS COMP, ANO ACOMP, '9253')     
      
    **Observação:**  
    Esta formula **MVRUBRICA,**foi criada especialmente para os lançamentos financeiros do crédito do trabalhador, onde o '9253' é correspondente ao código da rúbrica utilizado nos eventos de CC 480.  
      
    **Função MV**  
    Retorna o somatório dos valores de um evento na ficha financeira num determinado intervalo.  
    MV (MÊS, ANO, 'EVENTO')  
      
    **Observação:**  
    O parâmetro **MÊS** da variável acima é o seguinte **Meses para Pesquisa.**  
    **0 - do ano informado**  
    MH (0,2013,'0001')  
    Esta fórmula retorna o total de minutos do evento 0001 do ano informado (segundo parâmetro) na ficha financeira.  
      
    **15 - do ano corrente**  
    MH (15,0,'0082')  
    Esta fórmula retorna o total de minutos do evento 0082 na ficha financeira do ano corrente.   
      
    **16 - do período aquisitivo**  
    MH (16,0,'0082')  
    Esta fórmula retorna o total de horas do evento 0082 conforme o último período Aquisitivo no Histórico de Férias do funcionário.   
    Para os meses 17, 18, 19 e 20, os cálculo serão verificados em Administração de Pessoal | sindicatos | pasta médias nos campos "Número de Meses"  
      
    **17 - do período da média de férias;(Tipo de média)**  
    **MH (17,0,'0082')**  
    Esta fórmula retorna o total de horas do evento 0082 conforme o período da Média de Férias do sindicato do funcionário. Se no sindicato estiver parametrizado com média do período aquisitivo o sistema retornará o total de horas do evento dentro do período aquisitivo de férias do funcionário.   
      
    **18 - do período da média de 13º; (Tipo de Média)**  
    **MH (18,2013,'0082')**  
    Esta fórmula retorna o total de minutos do evento 0082 conforme o período da Média de 13o Salário do sindicato do funcionário.   
    19 - do período da média de aviso prévio e;(Tipo Média)  
      
    **MH (19,2013,'0082')**  
    Esta fórmula retorna o total de minutos do evento 0082 conforme o período da Média de Aviso do sindicato do funcionário.  
    20 - do período da média de licença maternidade. (Tipo Média)  
      
    **MH (20,2013,'0084')**  
    Esta fórmula retorna o total de minutos do evento 0082 conforme o período da Média de Licença Maternidade do sindicato do funcionário  
      
      
    **Função Max**  
    Retorna o maior valor entre dois valores informados.  
    MAX (VALOR, VALOR)  
      
      
    **Função MEDCOMIS**  
    Retorna o valor da Média de Comissão referente ao campo "Número de Meses" em Administração de Pessoal | Sindicato.   
    MEDCOMIS (STRING)  
      
    **Observações:**  
     Onde os valores utilizados para o retorno dos tipos de médias pela MEDCOMIS são:  
    **1** para Férias·   
    **2** para13º Salário·  
    **3** para Aviso Prévio·  
    **4** para Licença maternidade  
    **5** para Avos Totais de Férias (entre vencidas e proporcionais) ·

* Não deve ser lançado os eventos de comissão para média no grupo zero, porque não será calculado na variável MEDCOMIS, ou seja, as médias deverão sempre ser discriminadas em grupos distintos, sendo do tipo valor, e os eventos de comissão devem estar com o campo "Compõe Comissão" marcado.
* Para o Salário Maternidade a variável MEDCOMIS trará o valor de média de comissão apenas   após o lançamento da movimentação da funcionária afastada.  
    
  **Função MEDCOMISDATA**  
  Retorna o valor da Média de Comissão de acordo com o sindicato e com a data informada.  
  MEDCOMISDATA (VALOR, VALOR, DATA)  
  Onde:  
  **VALOR1**:  
  Informar o tipo de média que será calculado.  
  **VALOR2**:   
  Informar o tipo de processo (férias, cálculo da folha ou rescisão) que será calculado.  
  **DATA:**  
  Informar a data que será realizado o cálculo da Média.  
    
  **Observações:**  
  De acordo com a sintaxe **MEDCOMISDATA (VALOR1, VALOR2, DATA):**  
  **VALOR1 -** Neste campo poderão ser usados os seguintes valores de retorno**:**  
  **1** para Férias  
  **2** para13º Salário  
  **3** para Aviso Prévio  
  **5** para férias proporcionais  
    
  **VALOR2 -** Neste campo poderão ser usados os seguintes valores de retorno:  
  **1** para Férias  
  **2** para13º Salário  
  **3** para Rescisão  
  **5** para férias proporcionais  
    
  **DATA -** Informar a data que será realizado o cálculo da Média de Comissão, exemplo: TABFUNC ('DATADEMISSAO'), TABFUNC ('INICPROGFERIAS1' ou **0(ZERO)** para que o cálculo seja realizado na competência atual.  
    
  **Exemplos:**  
  **MEDCOMISDATA (1, 1, TABFUNC ('INICPROGFERIAS1', 'D'))**  
  Retorna as médias de Comissão de férias(**1**) no cálculo das Férias(**1**) observando o início de gozo do funcionário.   
    
  **MEDCOMISDATA (1 ,3, TABFUNC ('DATADEMISSAO', 'D'))**  
  Retorna as média de Comissão de Férias(**1**) na rescisão(**3**), verificando a data de demissão do funcionário.  
    
  **MEDCOMISDATA (2 ,3, 0)**  
  Retorna as médias de Comissão de 13º Salário (**2**) na Rescisão (**3**), verificando a data da competência atual.  
    
  **MEDCOMISDATA (3 ,3, TABFUNC ('DATADEMISSAO', 'D'))**  
  Retorna as médias de Comissão de Aviso Prévio (**3**) na Rescisão (**3**), verificando a data de demissão do funcionário.  
    
    
  **Função MEDSUBST**  
  Retorna o valor da média de substituição do funcionário, tendo como base o intervalo de datas de substituição informado como parâmetro.  
  MEDSUBST ('DATA DE INICIO DO INTERVALO', 'DATA DE FIM DO INTERVALO', 'NUMERO DE MESES PARA MEDIA ')  
    
  **Observação**  
  O número de horas utilizado no cálculo é o número de horas calculado e não mais o informado pelo usuário. Teoricamente, este valor já deve estar na tabela de substituições na hora do cálculo da fórmula. O mesmo é preenchido durante o cálculo da movimentação do funcionário.  
    
    
  **Exemplo:**  
  Em Administração de Pessoal l Funcionários l ícone visualizar ficha financeira | pasta substituição.  
  Suponhamos que o Funcionário substitui dois funcionários:  
  1) No mês 10/2013, 10 dias (73:20 horas) na função do funcionário 00203.   
  2) No mês 11/2013, 30 dias (220:00 horas) na função do funcionário 00202.  
    
  **Cadastrar a formula abaixo:**  
  MEDIASUBST('01/01/2013', '30/11/2013', 11)  
    
  **Demonstração do Cálculo da Fórmula:**  
  Salário hora dos Funcionários Substituídos:  
  Funcionário 00203: 361,00 / 220 = 1,64  
  Funcionário 00202: 585,26 / 220 = 2,66  
  Salário hora do Funcionário Substituido:  
  185,26 / 220 = 0,84  
  Transformar o número de horas substituídas em minutos:  
  73:20 horas = 4400 minutos  
  220:00 horas = 13200 minutos  
  Diferença entre o salário hora do substituído e do Substituido:  
  1,64 - 0,84 = 0,80  
  2,66 - 0,84 = 1,82  
  Cálculo da Média:  
  (4400 / 60) / 11 \* 0,80 = 5,33  
  (13200/ 60) / 11 \* 1,82 = 36,36  
  5,33 + 36,36 = **41,69** (Resultado da fórmula).  
    
    
    
    
  **Função Memoria**  
  Retorna um valor armazenado em memória  
  MEMORIA (INDEFINIDO)  
    
  **Observações:**  
  -Tipo de retorno: indefinido (de acordo com conteúdo da memória)  
  -Para atribuir valor a uma memória, deve-se usar a função **Atribui.**  
    
    
  **Função Mês**  
  Retorna mês de competência.  
  Mês  
    
  **Função MESCX**  
  Retorna mês-caixa.  
  MESCX  
    
  **Função MESDT**  
  Retorna o mês de uma data.  
  MESDT (DATA)  
    
    
  **Exemplo**  
   MESDT (22/08/1997)  
  Retornará '8'.  
    
    
  **Função MH**  
  Retorna os minutos de um evento da ficha financeira.  
  MH (MÊS, ANO, 'CÓD. DO EVENTO)  
    
    
  **Observação:**  
  O parâmetro **MÊS** da variável acima é o seguinte **Meses para Pesquisa**  
  **0 - do ano informado**  
  MH (0,2013,'0001')  
  Esta fórmula retorna o total de minutos do evento 0001 do ano informado (segundo parâmetro) na ficha financeira.  
    
  **15 - do ano corrente**  
  MH (15,0,'0082')  
  Esta fórmula retorna o total de minutos do evento 0082 na ficha financeira do ano corrente.   
    
  **16 - do período aquisitivo**  
  MH (16,0,'0082')  
  Esta fórmula retorna o total de horas do evento 0082 conforme o último período Aquisitivo no Histórico de Férias do funcionário.   
  Para os meses 17, 18, 19 e 20, os cálculo serão verificados em Administração de Pessoal | sindicatos | pasta médias nos campos "Número de Meses"  
    
  **17 - do período da média de férias;(Tipo de média)**  
  **MH (17,0,'0082')**  
  Esta fórmula retorna o total de horas do evento 0082 conforme o período da Média de Férias do sindicato do funcionário. Se no sindicato estiver parametrizado com média do período aquisitivo o sistema retornará o total de horas do evento dentro do período aquisitivo de férias do funcionário.   
    
  **18 - do período da média de 13º; (Tipo de Média)**  
  **MH (18,2013,'0082')**  
  Esta fórmula retorna o total de minutos do evento 0082 conforme o período da Média de 13o Salário do sindicato do funcionário.   
  19 - do período da média de aviso prévio e;(Tipo Média)  
    
  **MH (19,2013,'0082')**  
  Esta fórmula retorna o total de minutos do evento 0082 conforme o período da Média de Aviso do sindicato do funcionário.  
  20 - do período da média de licença maternidade. (Tipo Média)  
    
  **MH (20,2013,'0084')**  
  Esta fórmula retorna o total de minutos do evento 0082 conforme o período da Média de Licença Maternidade do sindicato do funcionário  
    
    
    
  **Função MIM**  
  Retorna o menor valor entre dois valores informados.  
  MIN (VALOR, VALOR)  
    
    
  **Função Minga**  
  Retorna mínimo garantido pelo sindicato.  
  MINGA  
    
  **Função MINGADATA**  
  Retorna mínimo garantido pelo sindicato em uma determinada data.  
  MINGADATA (DATA)  
    
  **Exemplo:**  
  MINGADATA(01/10/2013),   
  Retornará o valor do mínimo garantido estipulado a partir de 01/10/2013.  
    
    
  **Função MN**  
  Retorna o número de ocorrências de um evento na ficha financeira.  
  MN (MÊS, ANO, 'CÓD. DO EVENTO)  
    
  **Observação:**  
  O parâmetro **MÊS** da variável acima é o seguinte **Meses para Pesquisa.**  
  **0 - do ano informado**  
  MH (0,2013,'0001')  
  Esta fórmula retorna o total de minutos do evento 0001 do ano informado (segundo parâmetro) na ficha financeira.  
    
  **15 - do ano corrente**  
  MH (15,0,'0082')  
  Esta fórmula retorna o total de minutos do evento 0082 na ficha financeira do ano corrente.   
    
  **16 - do período aquisitivo**  
  MH (16,0,'0082')  
  Esta fórmula retorna o total de horas do evento 0082 conforme o último período Aquisitivo no Histórico de Férias do funcionário.   
  Para os meses 17, 18, 19 e 20, os cálculo serão verificados em Administração de Pessoal | sindicatos | pasta médias nos campos "Número de Meses"  
    
  **17 - do período da média de férias;(Tipo de média)**  
  **MH (17,0,'0082')**  
  Esta fórmula retorna o total de horas do evento 0082 conforme o período da Média de Férias do sindicato do funcionário. Se no sindicato estiver parametrizado com média do período aquisitivo o sistema retornará o total de horas do evento dentro do período aquisitivo de férias do funcionário.   
    
  **18 - do período da média de 13º; (Tipo de Média)**  
  **MH (18,2013,'0082')**  
  Esta fórmula retorna o total de minutos do evento 0082 conforme o período da Média de 13o Salário do sindicato do funcionário.   
  19 - do período da média de aviso prévio e;(Tipo Média)  
    
  **MH (19,2013,'0082')**  
  Esta fórmula retorna o total de minutos do evento 0082 conforme o período da Média de Aviso do sindicato do funcionário.  
  20 - do período da média de licença maternidade. (Tipo Média)  
    
  **MH (20,2013,'0084')**  
  Esta fórmula retorna o total de minutos do evento 0082 conforme o período da Média de Licença Maternidade do sindicato do funcionário  
    
    
    
  **Função MR**  
  Retorna o valor da referência de um evento da ficha financeira.  
  MR (MÊS, ANO, 'CÓDIGO DO EVENTO')  
    
  **Observação:**  
  O parâmetro **MÊS** da variável acima é o seguinte **Meses para Pesquisa.**  
  **0 - do ano informado**  
  MH (0,2013,'0001')  
  Esta fórmula retorna o total de minutos do evento 0001 do ano informado (segundo parâmetro) na ficha financeira.  
    
  **15 - do ano corrente**  
  MH (15,0,'0082')  
  Esta fórmula retorna o total de minutos do evento 0082 na ficha financeira do ano corrente.   
    
  **16 - do período aquisitivo**  
  MH (16,0,'0082')  
  Esta fórmula retorna o total de horas do evento 0082 conforme o último período Aquisitivo no Histórico de Férias do funcionário.   
  Para os meses 17, 18, 19 e 20, os cálculo serão verificados em Administração de Pessoal | sindicatos | pasta médias nos campos "Número de Meses"  
    
  **17 - do período da média de férias;(Tipo de média)**  
  **MH (17,0,'0082')**  
  Esta fórmula retorna o total de horas do evento 0082 conforme o período da Média de Férias do sindicato do funcionário. Se no sindicato estiver parametrizado com média do período aquisitivo o sistema retornará o total de horas do evento dentro do período aquisitivo de férias do funcionário.   
    
  **18 - do período da média de 13º; (Tipo de Média)**  
  **MH (18,2013,'0082')**  
  Esta fórmula retorna o total de minutos do evento 0082 conforme o período da Média de 13o Salário do sindicato do funcionário.   
  19 - do período da média de aviso prévio e;(Tipo Média)  
    
  **MH (19,2013,'0082')**  
  Esta fórmula retorna o total de minutos do evento 0082 conforme o período da Média de Aviso do sindicato do funcionário.  
  20 - do período da média de licença maternidade. (Tipo Média)  
    
  **MH (20,2013,'0084')**  
  Esta fórmula retorna o total de minutos do evento 0082 conforme o período da Média de Licença Maternidade do sindicato do funcionário  
    
    
    
  **Função MTDATA**  
  Monta uma data a partir de um dia, um mês e um ano informados.  
  MTDATA (DIA, MES, ANO)  
    
  **Exemplo:**  
  MTDATA(1,9,2013) = 01/09/2013.  
    
    
  **Função MUDOUCCUSTOMES**  
  Retorna 1 (um) quando o funcionário estava, no fim da competência anterior, em centros de custos diferente do atual. Em caso contrário, a função retorna 0 (zero).  
  MUDOUCCUSTOMES  
    
    
    
  **Observações:**

* A variável de fórmula MUDOUCCUSTOMES - "Mudou de Centro de Custos no Mês" será utilizada na operação de estorno da contabilização de encargos para os funcionários transferidos entre seções de um mesmo CGC e com centros de custos distintos.
* A variável de fórmula MUDOUCCUSTOMES para efeitos de comparação, considera os centros de custos associados às seções onde o funcionário estava lotado no fim das competências atual e anterior. Se o funcionário mudou para uma seção diferente no início da competência atual e retornou para a mesma seção em que estava lotado no fim da competência anterior, o resultado da função retornará Falso (zero).
* Os centros de custos considerados são centros de custos do Folha de Pagamento. A variável MUDOUCCUSTOMES não compara mudanças de centros de custos de Globais.
* Quando a variável MUDOUCCUSTOMES for utilizada na Folha Analítica ou Contabilização o sistema irá verificar o mês e ano informado na geração dos relatórios invés do mês e ano da competência da base.

**Exemplos:**  
-**Funcionário chapa 00002:**  
 Centro de Custos 01.05 - associado à Seção atual: 01.02  
 Centro de Custos 01.01 - associado à Seção anterior: 01.03.  
 Retorna 1, pois de acordo o centro de custos associado à seção 01.02 é diferente do o centro    de custos associado à seção 01.03.

* + Funcionário chapa 00005:\*  
    Centro de Custos 01.01 - associado à Seção atual: 01.07  
    Centro de Custos 01.01 - associado à Seção anterior: 01.08  
    Retorna 0, pois apesar das seções serem diferentes, o centro de custos associado a ambas é o mesmo.  
      
      
    **Função MUDOUSECMES**  
    Retorna se 1 (um) se o funcionário estava no final da competência anterior, em seção diferente da seção atual, caso contrário retorna 0.  
                MUDOUSECMES(STRING)   
    Onde STRING é o código de quebra que será analisado.   
      
      
    **Exemplo:**  
    Seção atual =01.12  
    Seção anterior =01.03  
      
    **1) MUDOUSECMES ('?????'),** neste caso a fórmula retornará =1 (verdade), pois houve mudança de seção na quebra informada na fórmula, 5(cinco) interrogações.  
      
    **2) MUDOUSECMES ('??'),** neste caso a fórmula retornará=0 (falso), pois não houve alteração de seção na quebra informada na fórmula, 2(duas) interrogações.  
      
      
      
    **Função MV**  
    Retorna o somatório dos valores de um evento na ficha financeira num determinado intervalo.  
    MV (MÊS, ANO, 'EVENTO')  
      
    **Observação:**  
    O parâmetro **MÊS** da variável acima é o seguinte **Meses para Pesquisa.**  
    **0 - do ano informado**  
    MH (0,2013,'0001')  
    Esta fórmula retorna o total de minutos do evento 0001 do ano informado (segundo parâmetro) na ficha financeira.  
      
    **15 - do ano corrente**  
    MH (15,0,'0082')  
    Esta fórmula retorna o total de minutos do evento 0082 na ficha financeira do ano corrente.   
      
    **16 - do período aquisitivo**  
    MH (16,0,'0082')  
    Esta fórmula retorna o total de horas do evento 0082 conforme o último período Aquisitivo no Histórico de Férias do funcionário.   
    Para os meses 17, 18, 19 e 20, os cálculo serão verificados em Administração de Pessoal | sindicatos | pasta médias nos campos "Número de Meses"  
      
    **17 - do período da média de férias;(Tipo de média)**  
    **MH (17,0,'0082')**  
    Esta fórmula retorna o total de horas do evento 0082 conforme o período da Média de Férias do sindicato do funcionário. Se no sindicato estiver parametrizado com média do período aquisitivo o sistema retornará o total de horas do evento dentro do período aquisitivo de férias do funcionário.   
      
    **18 - do período da média de 13º; (Tipo de Média)**  
    **MH (18,2013,'0082')**  
    Esta fórmula retorna o total de minutos do evento 0082 conforme o período da Média de 13o Salário do sindicato do funcionário.   
    19 - do período da média de aviso prévio e;(Tipo Média)  
      
    **MH (19,2013,'0082')**  
    Esta fórmula retorna o total de minutos do evento 0082 conforme o período da Média de Aviso do sindicato do funcionário.  
    20 - do período da média de licença maternidade. (Tipo Média)  
      
    **MH (20,2013,'0084')**  
    Esta fórmula retorna o total de minutos do evento 0082 conforme o período da Média de Licença Maternidade do sindicato do funcionário
