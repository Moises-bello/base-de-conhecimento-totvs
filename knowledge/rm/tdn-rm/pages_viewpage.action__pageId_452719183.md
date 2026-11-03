---
content_hash: 0e6f9b0076d1fad3db31be2d085cd4cde29ce3986adee2b2e9964abe55e6fcff
fetched_at: '2026-06-29T00:10:04.002078+00:00'
page_id: '452719183'
product: rm
source: tdn-rm
title: Tipo de Cálculo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719183
version: 25
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplos de utilização**
3. **Tela Tipo de Cálculo**

1. **Principais Campos e Parâmetros**

4. **Tabelas utilizadas**

## **01.** **VISÃO GERAL**

**Tipo de Cálculo, Corrige Valores, Habitualidade e Parâmetros relacionados à afastamento**   
Os parâmetros **Tipo de Cálculo**, **Corrige Valores, Habitualidade** e **Parâmetros relacionados à afastamento** estão disponíveis em todas as abas de Média, e as definições destes campos seguem abaixo:

Tipo de cálculo

**Tipo de cálculo**  
Selecione o tipo de cálculo dos eventos para média de 13º salário na Rescisão.  
São três as opções:   
**0 - sem média** (não considerará média)  
**1 - média por valor** (considerará valores dos eventos)  
**2 - média por hora** (considerará número de horas dos eventos)

Número de meses

**Número de meses**  
   
**Selecionando o Tipo de Cálculo = HORA ou VALOR**  
**Meses p/ evento Valor**  
Informe o(s) número(s) de meses (até três períodos) para o cálculo da(s) média(s) dos eventos do tipo valor.  
**Meses p/ evento Hora**  
Informe o(s) número(s) de meses (até três períodos) para o cálculo da(s) média(s) dos eventos do tipo hora.  
**Meses p/ evento. Ref**  
Informe o(s) número(s) de meses (até três períodos) para o cálculo da(s) média(s) dos eventos do tipo referência.

Observação:

Na primeira coluna, informando o número de meses igual a **"0" (zero),** o sistema calculará a média de 13º salário sobre o Período Aquisitivo. Se o usuário informar um determinado número de meses, o sistema irá considerar esse número para cálculo da média.  
A segunda e terceira colunas, caso estejam preenchidas com **"0" (zero)**, serão desconsideradas pelo sistema. Se o usuário lançar quaisquer números de meses em uma dessas colunas ou em ambas, esses números serão considerados para cálculos das médias.  
O maior valor encontrado (considerando os três períodos informados), é que será assumido pelo sistema.

Maiores Valores

**Maiores Valores**  
Informe o número de meses para que o sistema busque os maiores valores, dentro dos meses indicados para o cálculo da média, dos eventos do tipo valor.   
**Exemplo:**  
O número de meses indicado para a média foi 3 (três). O sistema buscará nos últimos 3 (três) meses da Ficha Financeira os eventos que participarão do cálculo da média de férias (incidem férias).  
No campo "Maiores Valores" foi informado 2 (dois) meses. Neste caso, o sistema irá verificar quais os 2 (dois) meses, dentre os 3 (três) informados para a média, que possuem os eventos com maiores valores, para utilizá-los no cálculo da média.

Observação:

O sistema tratará da seguinte forma as informações dos campos Nro. Meses p/ análise, Nro. Meses para habitualidade, Meses p/ ev. Valor, Meses p/ ev. Hora e Maiores Valores:  
Antes de mais nada, será necessário verificar se determinado evento é habitual ou não. Para isso, o sistema irá verificar nos N meses anteriores ao atual (onde N é o número de meses para análise) quantas ocorrências existem.   
Se existir pelo menos o número especificado como mínimo para se considerar habitual, o evento entrará para a média.  
O sistema irá, então, procurar os eventos selecionados nos últimos N meses anteriores ao atual (onde N, agora, é o número de Meses p/ Ev. Valor e Meses/ Ev. Hora), selecionando e somando os Maiores Valores.  
O resultado será dividido pelo número de Meses p/ Ev. Valor e Meses p/ ev. Hora (conforme o tipo do evento)

Últimos Meses Per Aquisitivo

## **VERSÃO**

false

**A partir do release:**

* 12.1.2402.164
* 12.1.2406 e Superiores

**Últimos Meses Per Aquisitivo**

Quando o cálculo for verificar uma quantidade de meses específica para o cálculo das médias baseando no período aquisitivo. Nesse caso será considerado a quantidade de meses parametrizados nesses campos. 

Atenção:

Esses campos servem para cálculos de médias, caso seja parametrizado em Férias e Férias na Rescisão, na comparação de valores dentro do período aquisitivo, então somente serão habilitados se os campos anteriores estiverem parametrizados para média por período aquisitivo, ou seja, em "Meses p/ evento Valor", "Meses p/ evento Hora" e/ou "Meses p/ evento Referência" na primeira coluna informado o número de meses igual a "0" (zero) e nas outras 99.

Parâmetros de Maiores Valores

**Considera maiores valores para soma**

Este parâmetro configura o sistema, de modo que, durante o cálculo de média, o usuário pode escolher dentre os valores obtidos para média de valor e hora, os maiores de cada tipo. Sendo comparado de acordo com o mês das médias.

**Compara maior média por grupo**

Este parâmetro configura o sistema, de modo que, durante o cálculo de média, o usuário pode escolher dentre os valores obtidos para média de valor e hora, os maiores de cada tipo. Sendo comparado de acordo com o grupo a que o evento de média pertence.

Habitualidade

**Habitualidade**  
   
**Número de meses para análise:**  
Informe o número de meses que deverão ser considerados pelo sistema para verificar a Habitualidade (frequência), do evento, isto é, o número de vezes em que o evento foi habitual. Este campo está diretamente associado ao seguinte:  
   
**Número de Meses para habitualidade**  
Informe um número mínimo de meses que os eventos, que entrarão para o cálculo das médias, deverão constar na ficha financeira do funcionário para ser considerado pelo sistema para o cálculo da média.  
Essa habitualidade será verificada dentro do período (número de meses para análise) informado no campo anterior.   
Caso o usuário não deseje que esta consistência seja feita, deverá informar 0 (zero).  
Informando um número de meses de habitualidade diferente de 0 (zero), o sistema irá proceder da seguinte maneira:  
   
**Exemplo:**  
No cálculo da média de férias foram consideradas as informações:  
Meses para ev. Valor: 6  
Meses para ev. Hora: 6  
Número. Meses para análise: 12  
Número. Meses para Habitualidade: 5  
   
Os eventos "Comissão" e "Hora Extra" incidem férias e serão pesquisados para o cálculo da média de férias.   
O sistema pesquisará nos últimos 12 (doze) meses a habitualidade desses eventos.  
Como o número de meses informado para o cálculo da média foi 0 (zero), serão considerados os eventos constantes em todo o período aquisitivo do funcionário.  
O evento "Comissão" somente consta em 2 (dois) meses do período aquisitivo, logo não será considerado para o cálculo da média, mesmo estando incidindo férias, pois o número de meses de habitualidade ("Nr. Meses Hab.") é 5 (cinco).  
O evento "Hora Extra 50%" está presente em 7 (sete) meses do período aquisitivo, logo será considerado para o cálculo da média.  
Embora o evento "Hora Extra 50%" tenha ocorrido 7 (sete) vezes, não serão considerados 7 (sete) meses para cálculo da média, uma vez que, no campo Meses p/ ev. Hora, foi informado 6 (seis meses).

Atenção:

O sistema não irá considerar os eventos para média, caso o número de meses da habitualidade seja superior ao número de meses para o cálculo da média (Meses p/ ev. Valor,Meses p/ ev. Hora).  
Informando um número de meses (valor) diferente de 0 (zero), o usuário deverá também preencher o campo "Maiores Valores".

Correção de Valores

**Correção de Valores**  
   
**Corrige valores pelo salário da época**  
Marque este parâmetro caso deseje que os eventos do Tipo Valor, os eventos do Tipo hora e os eventos do Dipo dia sejam corrigidos de acordo com o histórico salarial do funcionário para o cálculo da média.   
   
**Corrige valores por tabela de correção**  
Confirmando este campo, o sistema atualizará os valores dos eventos que participarão da média de férias, de acordo com a "Tabela de Correção".

Atenção:

**Média por Hora**  
O sistema corrigirá somente os valores dos eventos tipo "valor" que participarão da média. Os eventos tipo "hora" terão seus valores atualizados de acordo com o valor hora do salário atual.   
**Média por Valor**   
O sistema corrigirá os valores dos tipo "valor" e dos eventos tipo "hora".

**Tabela de Correção**  
Através deste campo o usuário poderá atualizar a unidade monetária. Selecione a tabela de correção de valores (índice, moeda, etc.) a ser considerada.

Observação:

**01:** O cálculo da correção do valor é feito pela divisão do índice na data do pagamento do evento (ou data imediatamente anterior) multiplicado pelo índice na data do último dia do mês da competência atual (ou data imediatamente anterior).  
**02:** Sugerimos a impressão do debug do cálculo e das médias com tipo da fonte Courier New e Tamanho 8.

Parâmetros relacionados à afastamentos

**Parâmetros relacionados à afastamentos**

Marque os afastamentos que os meses não serão contados para cálculo de médias.

**Exemplo:** Marcando o afastamento Af.Ac.Trabalho, durante o período de afastamento os meses não serão considerados para cálculo de média  
   
   
**Desconsidera o mês em que o funcionário ficar 'XX' dias ou mais afastado para contagem de meses** Cadastre no campo o número de dias para que o mês não seja considerado para contagem de tempo para cálculo de médias  
**Exemplo:**  
Se for cadastrado o número 31, o mês em que o funcionário estiver afastado por período inferior a 31 dias será considerado para cálculo das médias e no mês em que o funcionário estiver afastado por período superior ou igual a 31 dias não será considerado.  
   
   
**Desconsidera também p/soma dos valores** Marque este parâmetro caso queira desconsiderar também os valores dos meses de afastamentos parametrizados acima.

**Substitui período de afastamento por meses anteriores**  
Com este parâmetro marcado, o período a ser desconsiderado para o cálculo de média é substituído por meses respectivamente anteriores em quantidade referente ao período do afastamento.

Atenção:

Este parâmetro não é válido para empresas que realizam o cálculo da média de acordo com o Período Aquisitivo, somente para últimos 'N' meses.

**Exemplo:**  
Considere que a apuração de média do funcionário é realizada nos últimos 6 meses, e que dentro deste período o funcionário ficou 2 meses afastados:  
   
Meses para a apuração de média: 01/2010 a 06/2010  
Período do afastamento: de 01/04/2010 a 01/06/2010  
   
Caso o parâmetro **'Substitui período de afastamento por meses anteriores'** esteja marcado, o sistema automaticamente aumenta o número de meses em igual quantidade do afastamento. No caso do exemplo o sistema considera os meses de Nov/09 e Dez/09 para o cálculo das médias. Caso nestes meses também existam afastamentos o sistema desconsidera, trazendo sempre o anterior.

## **03****. EXEMPLOS DE UTILIZAÇÃO**

Comparação de Média em até 3 períodos distintos

Utilizando dados fictícios.

Dica

Esse exemplo serve para os demais cálculos e médias caso seja parametrizado em 13º salário, Aviso Prévio e Licença Maternidade para comparar valores.

Os valores podem ser conferidos na discriminação do log de cálculo de médias após calcular as férias do funcionário.

Parametrização do sindicato:

Calculando Média de Férias para o funcionário 00005 - TESTE MÉDIA SINDICATO

Salário Nominal: 2.423,30  
Data de Admissão: 10/06/2012  
Data de Vencimento das Férias: 09/06/2022

**PRIMEIRO CÁLCULO DAS MÉDIAS**

Média de Férias dos **últimos 12 meses** para eventos tipo Valor  
  Período a ser considerado: 01/2022 a 12/2022

Média de Férias dos últimos 12 meses para eventos tipo Hora  
  Período a ser considerado: 01/2022 a 12/2022

Média de Férias dos últimos 12 meses para eventos tipo Referência  
  Período a ser considerado: 01/2022 a 12/2022

**Grupo 1**

Total da Média do Grupo 1: 463,127205  
Valor arredondado do Grupo 1: **463,13**

**Grupo 2**

Total da Média do Grupo 2: 447,670000  
Valor arredondado do Grupo 2: **447,67**

**Total da Média de Férias: 910,800000**

**SEGUNDO CÁLCULO DAS MÉDIAS**

Média de Férias dos **últimos 6 meses** para eventos tipo Valor  
  Período a ser considerado: 07/2022 a 12/2022

Média de Férias dos últimos 6 meses para eventos tipo Hora  
  Período a ser considerado: 07/2022 a 12/2022

Média de Férias dos últimos 6 meses para eventos tipo Referência  
  Período a ser considerado: 07/2022 a 12/2022

**Grupo 1**

Total da Média do Grupo 1: 479,718549  
Valor arredondado do Grupo 1: **479,72**

**Grupo 2**

Total da Média do Grupo 2: 460,973333  
Valor arredondado do Grupo 2: **460,97**

**Total da Média de Férias: 940,690000**

**TERCEIRO CÁLCULO DAS MÉDIAS**

Média de Férias dos **últimos 3 meses** para eventos tipo Valor  
  Período a ser considerado: 10/2022 a 12/2022

Média de Férias dos últimos 3 meses para eventos tipo Hora  
  Período a ser considerado: 10/2022 a 12/2022

Média de Férias dos últimos 3 meses para eventos tipo Referência  
  Período a ser considerado: 10/2022 a 12/2022

**Grupo 1**

Total da Média do Grupo 1: 575,564347  
Valor arredondado do Grupo 1: **575,56**

**Grupo 2**

Total da Média do Grupo 2: 481,350000  
Valor arredondado do Grupo 2: **481,35**

**Total da Média de Férias: 1.056,910000**

**RESULTADO FINAL APÓS COMPARAÇÃO DAS MÉDIAS**

Será considerada a média dos últimos 3 meses.  
Média do Grupo 1: 575,56  
Média do Grupo 2: 481,35  
**Valor total da média: 1.056,91**

Corrige valores11Corrige valores pelo salário da época

Utilizando dados fictícios.

Parametrização do sindicato:

Para comparação dos cálculos veja abaixo com o parâmetro desmarcado:

Mesmo cálculo após marcar o parâmetro

Veja abaixo os salários utilizados para o cálculo da correção de valores pelo salário da época

2Corrige valores por tabela de correção

Utilizando dados fictícios.

Parametrização do sindicato:

Para comparação dos cálculos veja abaixo com o parâmetro desmarcado:

Mesmo cálculo após marcar o parâmetro e selecionar a tabela

Veja abaixo os valores utilizados para o cálculo que foram cadastrados como índice em Cadastro de Moedas e Índices, sendo os valores cadastrados no anexo Cotações

Últimos Meses Per Aquisitivo

Utilizando dados fictícios.

Dica

Esse exemplo serve somente para cálculos de médias caso seja parametrizado em Férias e Férias na Rescisão para comparar valores dentro do período aquisitivo.

Os valores podem ser conferidos na discriminação do log de cálculo de médias após calcular as férias do funcionário.

Parametrização do sindicato:

Calculando Média de Férias para o funcionário 00005 - TESTE MÉDIA SINDICATO

Salário Nominal: 2.423,30  
Data de Admissão: 10/06/2012  
Data de Vencimento das Férias: 09/06/2022

**PRIMEIRO CÁLCULO DAS MÉDIAS**

**Média de Férias dos meses do período aquisitivo** para eventos tipo Valor  
 Serão considerados os **últimos 12 meses do período aquisitivo**  
  Período a ser considerado: 06/2021 a 05/2022

Média de Férias dos meses do período aquisitivo para eventos tipo Hora  
 Serão considerados os últimos 12 meses do período aquisitivo  
  Período a ser considerado: 06/2021 a 05/2022

Média de Férias dos meses do período aquisitivo para eventos tipo Referência  
 Serão considerados os últimos 12 meses do período aquisitivo  
  Período a ser considerado: 06/2021 a 05/2022

**Grupo 1**

Discriminação dos valores do grupo

  Calculando média do evento tipo H: 0082 - HORA EXTRA 50%  
    Mês 06/2021: 6,233333 \* 1,50 (%inc.) \* 11,015000 = 102,990250  
    Mês 07/2021: 6,233333 \* 1,50 (%inc.) \* 11,015000 = 102,990250  
    Mês 08/2021: 6,233333 \* 1,50 (%inc.) \* 11,015000 = 102,990250  
    Mês 09/2021: 6,233333 \* 1,50 (%inc.) \* 11,015000 = 102,990250  
    Mês 10/2021: 6,233333 \* 1,50 (%inc.) \* 11,015000 = 102,990250  
    Mês 11/2021: 6,233333 \* 1,50 (%inc.) \* 11,015000 = 102,990250  
    Mês 12/2021: 18,350000 \* 1,50 (%inc.) \* 11,015000 = 303,187875  
    Mês 01/2022: 4,200000 \* 1,50 (%inc.) \* 11,015000 = 69,394500  
    TOTAL       = 990,52

  Calculando média do evento tipo H: 0083 - HORA EXTRA 100%  
    Mês 06/2021: 4,083333 \* 2,00 (%inc.) \* 11,015000 = 89,955833  
    Mês 07/2021: 4,083333 \* 2,00 (%inc.) \* 11,015000 = 89,955833  
    Mês 08/2021: 4,083333 \* 2,00 (%inc.) \* 11,015000 = 89,955833  
    Mês 09/2021: 4,083333 \* 2,00 (%inc.) \* 11,015000 = 89,955833  
    Mês 10/2021: 4,083333 \* 2,00 (%inc.) \* 11,015000 = 89,955833  
    Mês 11/2021: 4,083333 \* 2,00 (%inc.) \* 11,015000 = 89,955833  
    Mês 12/2021: 6,633333 \* 2,00 (%inc.) \* 11,015000 = 146,132333  
    Mês 01/2022: 4,150000 \* 2,00 (%inc.) \* 11,015000 = 91,424500  
    Mês 02/2022: 3,866667 \* 2,00 (%inc.) \* 11,015000 = 85,182667  
    TOTAL       = 862,47

  Calculando média do evento tipo H: 0159 - DSR EM HORAS (RM Chronus)  
    Mês 08/2021: 40,000000 \* 1,00 (%inc.) \* 11,015000 = 440,600000  
    Mês 09/2021: 32,000000 \* 1,00 (%inc.) \* 11,015000 = 352,480000  
    Mês 10/2021: 40,000000 \* 1,00 (%inc.) \* 11,015000 = 440,600000  
    Mês 11/2021: 32,000000 \* 1,00 (%inc.) \* 11,015000 = 352,480000  
    Mês 12/2021: 32,000000 \* 1,00 (%inc.) \* 11,015000 = 352,480000  
    Mês 01/2022: 40,000000 \* 1,00 (%inc.) \* 11,015000 = 440,600000  
    Mês 02/2022: 32,000000 \* 1,00 (%inc.) \* 11,015000 = 352,480000  
    Mês 03/2022: 32,000000 \* 1,00 (%inc.) \* 11,015000 = 352,480000  
    Mês 04/2022: 32,000000 \* 1,00 (%inc.) \* 11,015000 = 352,480000  
    Mês 05/2022: 40,000000 \* 1,00 (%inc.) \* 11,015000 = 440,600000  
    TOTAL       = 3.877,28

Total dos eventos tipo Hora: 5.730,278375

Média de eventos tipo Hora: 5.730,278375 **/ 12** = 477,523198

Total da Média do Grupo 1: 477,523198  
Valor arredondado do Grupo 1: **477,52**

**Grupo 2**

Discriminação dos valores do grupo

  Calculando média do evento tipo V: 0084 - COMISSAO  
    Mês 02/2022 = 254,18  
    TOTAL       = 254,18

  Calculando média do evento tipo V: 0104 - PRODUTIVIDADE  
    Mês 06/2021 = 346,93  
    Mês 07/2021 = 346,93  
    Mês 08/2021 = 346,93  
    Mês 09/2021 = 346,93  
    Mês 10/2021 = 346,93  
    Mês 11/2021 = 384,02  
    Mês 12/2021 = 384,02  
    Mês 01/2022 = 384,02  
    Mês 02/2022 = 393,60  
    Mês 03/2022 = 393,60  
    Mês 04/2022 = 393,60  
    Mês 05/2022 = 393,60  
    TOTAL       = 4.461,11

Total dos eventos tipo Valor: 4.715,290000

Média de eventos tipo Valor: 4.715,290000 **/ 12** = 392,940833

Total da Média do Grupo 2: 392,940833  
Valor arredondado do Grupo 2: **392,94**

**Total da Média de Férias: 870,460000**

**SEGUNDO CÁLCULO DAS MÉDIAS**

**Média de Férias dos meses do período aquisitivo** para eventos tipo Valor  
 Serão considerados os **últimos 6 meses do período aquisitivo**  
  Período a ser considerado: 12/2021 a 05/2022

Média de Férias dos meses do período aquisitivo para eventos tipo Hora  
 Serão considerados os últimos 6 meses do período aquisitivo  
  Período a ser considerado: 12/2021 a 05/2022

Média de Férias dos meses do período aquisitivo para eventos tipo Referência  
 Serão considerados os últimos 6 meses do período aquisitivo  
  Período a ser considerado: 12/2021 a 05/2022

**Grupo 1**

Discriminação dos valores do grupo

  Calculando média do evento tipo H: 0082 - HORA EXTRA 50%  
    Mês 12/2021: 18,350000 \* 1,50 (%inc.) \* 11,015000 = 303,187875  
    Mês 01/2022: 4,200000 \* 1,50 (%inc.) \* 11,015000 = 69,394500  
    TOTAL       = 372,58

  Calculando média do evento tipo H: 0083 - HORA EXTRA 100%  
    Mês 12/2021: 6,633333 \* 2,00 (%inc.) \* 11,015000 = 146,132333  
    Mês 01/2022: 4,150000 \* 2,00 (%inc.) \* 11,015000 = 91,424500  
    Mês 02/2022: 3,866667 \* 2,00 (%inc.) \* 11,015000 = 85,182667  
    TOTAL       = 322,74

  Calculando média do evento tipo H: 0159 - DSR EM HORAS (RM Chronus)  
    Mês 12/2021: 32,000000 \* 1,00 (%inc.) \* 11,015000 = 352,480000  
    Mês 01/2022: 40,000000 \* 1,00 (%inc.) \* 11,015000 = 440,600000  
    Mês 02/2022: 32,000000 \* 1,00 (%inc.) \* 11,015000 = 352,480000  
    Mês 03/2022: 32,000000 \* 1,00 (%inc.) \* 11,015000 = 352,480000  
    Mês 04/2022: 32,000000 \* 1,00 (%inc.) \* 11,015000 = 352,480000  
    Mês 05/2022: 40,000000 \* 1,00 (%inc.) \* 11,015000 = 440,600000  
    TOTAL       = 2.291,12

Total dos eventos tipo Hora: 2.986,441875

Média de eventos tipo Hora: 2.986,441875 **/ 6** = 497,740313

Total da Média do Grupo 1: 497,740313  
Valor arredondado do Grupo 1: **497,74**

**Grupo 2**

Discriminação dos valores do grupo

  Calculando média do evento tipo V: 0084 - COMISSAO  
    Mês 02/2022 = 254,18  
    TOTAL       = 254,18

  Calculando média do evento tipo V: 0104 - PRODUTIVIDADE  
    Mês 12/2021 = 384,02  
    Mês 01/2022 = 384,02  
    Mês 02/2022 = 393,60  
    Mês 03/2022 = 393,60  
    Mês 04/2022 = 393,60  
    Mês 05/2022 = 393,60  
    TOTAL       = 2.342,44

 Total dos eventos tipo Valor: 2.596,620000

Média de eventos tipo Valor: 2.596,620000 **/ 6** = 432,770000T

Total da Média do Grupo 2: 432,770000  
Valor arredondado do Grupo 2: **432,77**

**Total da Média de Férias: 930,510000**

**TERCEIRO CÁLCULO DAS MÉDIAS**

**Média de Férias dos meses do período aquisitivo** para eventos tipo Valor  
 Serão considerados os **últimos 3 meses do período aquisitivo**  
  Período a ser considerado: 03/2022 a 05/2022

Média de Férias dos meses do período aquisitivo para eventos tipo Hora  
 Serão considerados os últimos 3 meses do período aquisitivo  
  Período a ser considerado: 03/2022 a 05/2022

Média de Férias dos meses do período aquisitivo para eventos tipo Referência  
 Serão considerados os últimos 3 meses do período aquisitivo  
  Período a ser considerado: 03/2022 a 05/2022

**Grupo 1**

Discriminação dos valores do grupo

  Calculando média do evento tipo H: 0159 - DSR EM HORAS (RM Chronus)  
    Mês 03/2022: 32,000000 \* 1,00 (%inc.) \* 11,015000 = 352,480000  
    Mês 04/2022: 32,000000 \* 1,00 (%inc.) \* 11,015000 = 352,480000  
    Mês 05/2022: 40,000000 \* 1,00 (%inc.) \* 11,015000 = 440,600000  
    TOTAL       = 1.145,56

Total dos eventos tipo Hora: 1.145,560000

Média de eventos tipo Hora: 1.145,560000 **/ 3** = 381,853333

Total da Média do Grupo 1: 381,853333  
Valor arredondado do Grupo 1: **381,85**

**Grupo 2**

Discriminação dos valores do grupo

  Calculando média do evento tipo V: 0104 - PRODUTIVIDADE  
    Mês 03/2022 = 393,60  
    Mês 04/2022 = 393,60  
    Mês 05/2022 = 393,60  
    TOTAL       = 1.180,80

Total dos eventos tipo Valor: 1.180,800000

Média de eventos tipo Valor: 1.180,800000 **/ 3** = 393,600000

Total da Média do Grupo 2: 393,600000  
Valor arredondado do Grupo 2: **393,60**

**Total da Média de Férias: 775,450000**

**RESULTADO FINAL APÓS COMPARAÇÃO DAS MÉDIAS**

Será considerada a média do período aquisitivo.  
Média do Grupo 1: 497,74  
Média do Grupo 2: 432,77  
**Valor total da média: 930,51 - Nesse caso o valor do SEGUNDO CÁLCULO DAS MÉDIAS**

## **04****. TELA Tipo de Cálculo**

**Principais Campos e Parâmetros**

|  |  |
| --- | --- |
| **Campo** | **Descrição** |
| Tipo de Cálculo | Selecionar o tipo de cálculo do sindicato |
| Número de meses | Informar os números de meses a serem considerados para eventos Valor, Hora, Referência |
| Maiores Valores | Informar o número de meses para que o sistema busque os maiores valores, dentro dos meses indicados para o cálculo da média, dos eventos do tipo valor |
| Últimos meses Per. Aquisitivo | Informar o número de meses para verificar uma quantidade de meses específica no cálculo das médias baseando no período aquisitivo |
| Considera soma total da competência ao buscar maiores valores | Marcar para selecionar dentre os valores obtidos para média de valor e hora, os maiores de cada tipo. Sendo comparado de acordo com o mês das médias |
| Compara maior média por grupo | Marcar para selecionar dentre os valores obtidos para média de valor e hora, os maiores de cada tipo. Sendo comparado de acordo com o grupo a que o evento de média pertence |
| Correção de Valores | Selecionar se será feita a correção pelo salário da época ou por tabela de correção. Selecionando o parâmetro de tabela de correção deverá informar qual tabela será utilizada |
| Habitualidade | Informar o nº de meses para análise e o nº de meses para habitualidade |
| Parâmetros relacionados à afastamentos | Parametrizar de acordo com as necessidades para influenciar ou não no cálculo das médias |

## **05****. TABELAS UTILIZADAS**

* PSINDIC
* PESINDMED

---

Retornar [Sindicatos](http://tdn.totvs.com.br/display/LRM/Sindicatos)
